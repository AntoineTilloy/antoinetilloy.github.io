#!/usr/bin/env python3
"""One-off conversion of the WordPress.com export (WXR) into Hugo content.

Usage: python3 tools/wp2hugo.py _wordpress/export.xml

Writes:
  content/posts/YYYY-MM-DD-slug.md    published posts
  content/pages/<slug>.md             published pages (with their old URL)
  archive/comments/YYYY-MM-DD-slug.yaml   approved comments (no emails/IPs)
  _wordpress/drafts/*.md              unpublished drafts (not in the repo)
"""
import html
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

NS = {
    "wp": "http://wordpress.org/export/1.2/",
    "content": "http://purl.org/rss/1.0/modules/content/",
}
ROOT = Path(__file__).resolve().parent.parent
OLD_HOSTS = r"(?:https?:)?//(?:www\.)?(?:tilloy\.wordpress\.com|atilloy\.com|tilloy\.files\.wordpress\.com)"

# Pages keep their old WordPress URL (parent/child structure).
PAGE_URLS = {
    "about": "/about/",
    "research": "/research/",
    "list-of-publications": "/research/list-of-publications/",
    "talks": "/research/talks/",
    "teaching": "/teaching/",
    "physique-pour-tous": "/teaching/physique-pour-tous/",
    "working-with-me-2": "/working-with-me-2/",
}
MENU_WEIGHT = {"about": 2, "research": 3, "teaching": 4, "working-with-me-2": 5}


def text(item, tag):
    el = item.find(tag, NS)
    return el.text if el is not None and el.text is not None else ""


class Converter:
    def __init__(self, attachments):
        self.attachments = attachments  # attachment id -> url
        self.ph = {}

    def keep(self, s):
        key = f"XPHX{len(self.ph)}X"
        self.ph[key] = s
        return key

    # --- URL helpers -----------------------------------------------------
    @staticmethod
    def local_url(url):
        url = html.unescape(url.strip())
        url = re.sub(OLD_HOSTS + r"/(?:wp-content/uploads/)?(\d{4}/\d{2}/[^?#\s\"']+\.(?:png|jpe?g|gif|pdf|svg))(?:\?[^\s\"']*)?",
                      r"/wp-content/uploads/\1", url, flags=re.I)
        url = re.sub(OLD_HOSTS + r"(/[^\s\"']*)?", lambda m: m.group(1) or "/", url)
        return url

    @staticmethod
    def attr(tag, name):
        m = re.search(rf'\b{name}\s*=\s*"([^"]*)"', tag) or re.search(rf"\b{name}\s*=\s*'([^']*)'", tag)
        return html.unescape(m.group(1)) if m else ""

    def md(self, fragment):
        """HTML fragment -> Markdown (placeholders pass through untouched)."""
        out = subprocess.run(["pandoc", "-f", "html", "-t", "gfm", "--wrap=none"],
                             input=fragment, capture_output=True, text=True, check=True).stdout
        return out.strip()

    @staticmethod
    def sc_arg(s):
        s = s.strip()
        return f"`{s}`" if "`" not in s else '"' + s.replace('"', "&quot;") + '"'

    def figure(self, img_tag, caption_html="", align=""):
        src = self.local_url(self.attr(img_tag, "src"))
        src = re.sub(r"-\d+x\d+(\.\w+)$", r"\1", src)
        alt = self.attr(img_tag, "alt")
        width = self.attr(img_tag, "width")
        if not width:  # block editor stores the size as an inline style
            w = re.search(r"width:\s*(\d+)px", self.attr(img_tag, "style"))
            width = w.group(1) if w else ""
        args = [f"src={self.sc_arg(src)}"]
        if alt:
            args.append(f"alt={self.sc_arg(alt)}")
        cap = self.md(caption_html) if caption_html.strip() else ""
        if cap:
            args.append(f"caption={self.sc_arg(cap)}")
        if width:
            args.append(f'width="{width}"')
        if "right" in align:
            args.append('class="right"')
        elif "left" in align:
            args.append('class="left"')
        return self.keep("\n\n{{< figure " + " ".join(args) + " >}}\n\n")

    # --- main ------------------------------------------------------------
    def convert(self, body):
        self.ph = {}
        gutenberg = "<!-- wp:" in body

        # math: $latex ...$ (WordPress.com syntax) and the odd bare $...$
        def latex(m):
            tex = re.sub(r"(?:&(?:amp;)?[a-z]+=[\w#-]*)+\s*$", "", m.group(1))
            tex = html.unescape(tex).replace("\xa0", " ").strip()
            return self.keep(f"${tex}$")
        body = re.sub(r"\$latex\s+(.*?)\$", latex, body, flags=re.I | re.S)
        body = re.sub(r"(?<![\w$])\$(?=\S)([^$<>\n]{1,80}?(?<=\S))\$(?![\w$])", latex, body)

        # [caption]...[/caption]
        def caption(m):
            attrs, inner = m.group(1), m.group(2)
            img = re.search(r"<img[^>]*>", inner)
            if not img:
                return inner
            cap = re.sub(r"<a[^>]*>\s*<img[^>]*>\s*</a>|<img[^>]*>", "", inner, count=1)
            return self.figure(img.group(0), cap, self.attr(attrs, "align"))
        body = re.sub(r"\[caption([^\]]*)\](.*?)\[/caption\]", caption, body, flags=re.S)

        # Gutenberg image blocks with optional caption
        def gfigure(m):
            block = m.group(0)
            img = re.search(r"<img[^>]*>", block)
            cap = re.search(r"<figcaption[^>]*>(.*?)</figcaption>", block, re.S)
            cls = self.attr(block, "class")
            return self.figure(img.group(0), cap.group(1) if cap else "", cls) if img else block
        body = re.sub(r'<div class="wp-block-image[^"]*">\s*<figure.*?</figure>\s*</div>'  # older block editor
                      r'|<figure class="wp-block-image[^"]*"[^>]*>.*?</figure>', gfigure, body, flags=re.S)

        # galleries: [gallery ids=...] and Jetpack slideshows
        def gallery(ids):
            srcs = [self.local_url(self.attachments[i]) for i in ids if i in self.attachments]
            return self.keep("\n\n{{< gallery >}}\n" + "\n".join(srcs) + "\n{{< /gallery >}}\n\n")
        body = re.sub(r'\[gallery[^\]]*ids="([\d,]+)"[^\]]*\]', lambda m: gallery(m.group(1).split(",")), body)
        body = re.sub(r"<!-- wp:jetpack/slideshow (\{.*?\}) -->.*?<!-- /wp:jetpack/slideshow -->",
                      lambda m: gallery([str(i) for i in yaml.safe_load(m.group(1))["ids"]]), body, flags=re.S)

        # embeds, videos, files
        def youtube(url):
            vid = re.search(r"(?:v=|youtu\.be/)([\w-]{11})", url)
            return self.keep("\n\n{{< youtube " + vid.group(1) + " >}}\n\n") if vid else url
        body = re.sub(r"<!-- wp:embed (\{.*?\}) -->.*?<!-- /wp:embed -->",
                      lambda m: youtube(yaml.safe_load(m.group(1))["url"]), body, flags=re.S)
        body = re.sub(r"^\s*(https?://(?:www\.)?(?:youtube\.com/watch\S+|youtu\.be/\S+))\s*$",
                      lambda m: youtube(m.group(1)), body, flags=re.M)
        body = re.sub(r"<!-- wp:video .*?<video[^>]*src=\"([^\"]+)\".*?<!-- /wp:video -->",
                      lambda m: self.keep('\n\n{{< video src="' + self.local_url(m.group(1)) + '" >}}\n\n'), body, flags=re.S)

        def wpfile(m):
            opts = yaml.safe_load(m.group(1))
            name = re.search(r'<a id="wp-block-file[^>]*>(.*?)</a>', m.group(2), re.S)
            name = html.unescape(name.group(1)) if name else Path(opts["href"]).stem
            embed = "true" if "<object" in m.group(2) else "false"
            return self.keep('\n\n{{< pdf src="' + self.local_url(opts["href"]) + f'" title={self.sc_arg(name)} embed={embed} >}}}}\n\n')
        body = re.sub(r"<!-- wp:file (\{.*?\}) -->(.*?)<!-- /wp:file -->", wpfile, body, flags=re.S)
        body = body.replace(">}}}}", ">}}")

        # clean HTML
        body = re.sub(r"<!-- /?wp:.*?-->", "", body, flags=re.S)
        body = re.sub(r"<a[^>]*>\s*(<img[^>]*>)\s*</a>", r"\1", body)
        body = re.sub(r'\s(?:style|class|id|width|height|srcset|sizes|data-[\w-]+|target|rel|title)="[^"]*"', "", body)
        body = re.sub(r"</?span[^>]*>", "", body)
        body = re.sub(r"<img[^>]*src=\"[^\"]*\.pdf\"[^>]*>", "", body)  # broken image in Talks
        for _ in range(2):  # whitespace just inside <em>, <a>... breaks Markdown emphasis
            body = re.sub(r"(\s|&nbsp;)+(</(?:em|strong|i|b|a)>)", r"\2 ", body)
            body = re.sub(r"(<(?:em|strong|i|b)>)(\s|&nbsp;)+", r" \1", body)
        body = re.sub(r'(href|src)="([^"]*)"', lambda m: f'{m.group(1)}="{html.escape(self.local_url(m.group(2)))}"', body)
        if not gutenberg:
            body = wpautop(body)

        out = self.md(body)

        # placeholders back; a math placeholder alone on its line becomes display math
        def restore(m):
            return self.ph[m.group(0)]
        out = re.sub(r"^(XPHX\d+X)([.,;:]?)$",
                     lambda m: "$$\n" + self.ph[m.group(1)][1:-1] + m.group(2) + "\n$$"
                     if self.ph[m.group(1)].startswith("$") else m.group(0), out, flags=re.M)
        for _ in range(3):
            out = re.sub(r"XPHX\d+X", restore, out)
        out = re.sub(r" {2,}\n(?=\n|$)", "\n", out)   # line break at paragraph end
        out = re.sub(r" {2,}\n", "\\\\\n", out)      # visible hard line break: trailing backslash
        out = out.replace("-\\>", "->")
        out = re.sub("\u00a0(?![:;!?»])(?<!«\u00a0)", " ", out)  # stray non-breaking spaces
        out = re.sub(r"\n{3,}", "\n\n", out)
        return out.strip() + "\n"


BLOCK = r"(?:table|thead|tfoot|caption|col|colgroup|tbody|tr|td|th|div|dl|dd|dt|ul|ol|li|pre|form|map|area|blockquote|address|math|style|p|h[1-6]|hr|fieldset|legend|section|article|aside|hgroup|header|footer|nav|figure|figcaption|details|menu|summary|object|iframe|video)"


def wpautop(s):
    """Minimal port of WordPress' wpautop for classic-editor content."""
    s = re.sub(rf"(<{BLOCK}[\s/>])", r"\n\n\1", s)
    s = re.sub(rf"(</{BLOCK}>)", r"\1\n\n", s)
    paras = [p.strip() for p in re.split(r"\n\s*\n", s) if p.strip()]
    out = []
    for p in paras:
        if re.match(rf"</?{BLOCK}[\s/>]", p) or p.startswith("XPHX") and re.fullmatch(r"(XPHX\d+X\s*)+", p):
            out.append(p)
        else:
            out.append("<p>" + p.replace("\n", "<br>\n") + "</p>")
    return "\n\n".join(out)


def front_matter(d):
    return "---\n" + yaml.safe_dump(d, allow_unicode=True, sort_keys=False, width=1000) + "---\n\n"


def main(xml_path):
    items = list(ET.parse(xml_path).getroot().iter("item"))
    attachments = {text(i, "wp:post_id"): text(i, "wp:attachment_url")
                   for i in items if text(i, "wp:post_type") == "attachment"}
    conv = Converter(attachments)
    dirs = {k: ROOT / v for k, v in [("posts", "content/posts"), ("pages", "content/pages"),
                                     ("comments", "archive/comments"), ("drafts", "_wordpress/drafts")]}
    for d in dirs.values():
        d.mkdir(parents=True, exist_ok=True)

    for it in items:
        kind, status = text(it, "wp:post_type"), text(it, "wp:status")
        if kind not in ("post", "page"):
            continue
        title = html.unescape(it.find("title").text or "").strip()
        date = text(it, "wp:post_date").replace(" ", "T")
        slug = text(it, "wp:post_name") or re.sub(r"\W+", "-", title.lower()).strip("-")
        fm = {"title": title, "date": date}
        if status != "publish":
            fm["draft"] = True
            path = dirs["drafts"] / f"{kind}-{date[:10]}-{slug}.md"
        elif kind == "post":
            fm["slug"] = slug
            path = dirs["posts"] / f"{date[:10]}-{slug}.md"
        else:
            fm["url"] = PAGE_URLS[slug]
            if slug in MENU_WEIGHT:
                fm["menu"] = {"main": {"weight": MENU_WEIGHT[slug]}}
            path = dirs["pages"] / f"{slug.removesuffix('-2')}.md"
        path.write_text(front_matter(fm) + conv.convert(text(it, "content:encoded")))

        comments = []
        for c in it.findall("wp:comment", NS):
            if text(c, "wp:comment_approved") != "1" or text(c, "wp:comment_type") == "pingback":
                continue
            comments.append({
                "id": int(text(c, "wp:comment_id")),
                "parent": int(text(c, "wp:comment_parent") or 0),
                "author": html.unescape(text(c, "wp:comment_author")),
                "author_url": text(c, "wp:comment_author_url") or None,
                "date": text(c, "wp:comment_date"),
                "content": conv.md(wpautop(text(c, "wp:comment_content"))) + "\n",
            })
        if comments and status == "publish":
            meta = {"post": title, "url": fm.get("url") or f"/{date[:4]}/{date[5:7]}/{date[8:10]}/{slug}/",
                    "comments": comments}
            (dirs["comments"] / f"{date[:10]}-{slug}.yaml").write_text(
                yaml.safe_dump(meta, allow_unicode=True, sort_keys=False, width=1000))


if __name__ == "__main__":
    main(sys.argv[1])
