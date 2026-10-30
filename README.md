# atilloy.com

Source of [atilloy.com](https://atilloy.com), built with [Hugo](https://gohugo.io).
Every push to `main` rebuilds and publishes the site (see `.github/workflows/hugo.yml`).

## Everyday use

Preview locally (opens at http://localhost:1313, refreshes as you save):

    hugo server

Then publish:

    git add -A && git commit -m "New post" && git push

## Where things are

| What | Where |
|---|---|
| Blog posts | `content/posts/YYYY-MM-DD-slug.md` |
| Pages (About, Research, Talks...) | `content/pages/*.md` |
| Images and PDFs | `static/...` (served as-is: `static/x/y.pdf` → `/x/y.pdf`) |
| Old WordPress uploads | `static/wp-content/uploads/` (kept at their old URLs) |
| Site title, menu, settings | `hugo.toml` |
| Look and layout | `layouts/`, `assets/css/main.css` |
| Old WordPress comments (not shown) | `archive/comments/` |

## Writing a post

Create `content/posts/2026-11-02-my-new-post.md`:

    ---
    title: My new post
    date: 2026-11-02T10:00:00
    slug: my-new-post
    ---

    Text in Markdown. Inline math $\rho_t$, display math:

    $$
    \partial_t \rho = \mathcal{L}(\rho)
    $$

It will appear at `/2026/11/02/my-new-post/`. Add `draft: true` to the front
matter to keep a post unpublished (`hugo server -D` shows drafts locally).

Put new files in e.g. `static/files/2026/` and link them as `/files/2026/name.pdf`.

## Extras available in posts

    {{< figure src="/files/img.png" caption="A caption, *Markdown* allowed" >}}
    {{< figure src="/files/img.png" class="right" width="250" >}}   (floated right)
    {{< youtube VIDEO_ID >}}
    {{< pdf src="/files/notes.pdf" title="Lecture notes" embed=true >}}
    {{< gallery >}}
    /files/a.jpg
    /files/b.jpg
    {{< /gallery >}}

## Upgrading Hugo

Math is rendered at build time with the KaTeX version bundled in Hugo. When
changing `HUGO_VERSION` in the workflow, also update the KaTeX stylesheet
version in `layouts/baseof.html` to match.
