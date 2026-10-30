---
title: Potpourri of articles II
date: '2017-06-08T12:29:01'
slug: potpourri-of-articles-ii
---

This time, two very recent preprints about the black hole information paradox and a neat mathematical problem.

--***(Information) Paradox Lost*** by Tim Maudlin, [arXiv:1705.03541](https://arxiv.org/abs/1705.03541)

What if the reason the black hole (BH) information paradox has been discussed for so long is that there is actually no paradox to solve? What if people are just providing conjectural answers in "*need for a question*"? Tim makes a *very* convincing case that the paradox vanishes once things are properly defined and understood. This is an archetypal example of a situation where the clarity of mind of a serious philosopher of science should be stimulating for the physics community.

A lot has been written on the BH information paradox already. To be honest, I have never really understood the fascination of the community for this problem. I have tried to understand many times why the problem was so pressing, but the arguments I found were rarely if at all convincing. Trying to genuinely understand the paradox is annoyingly complicated by the fact that a large fraction of the folklore in the field is not supported by the literature: some options are dismissed as "provably" inadequate, but the proof cannot ever be found anywhere.

Tim's preprint is welcome as it states the (alleged) problem in very clear terms and does so in a slightly provocative style that is very pleasant to read. The diffusing of the paradox is surprisingly simple: we see a spurious tension between (orthodox) quantum theory and relativity in the context of BHs because we are not applying the former theory properly. More precisely, the loss of unitarity in quantum mechanical dynamics in the presence of an evaporating BH can be traced back to the fact that we do not consider Cauchy surfaces as we should. The final hypersurface considered "after" the evaporation is typically not a Cauchy surface. Had we considered Cauchy-to-Cauchy maps, there would be no reason to expect any kind of problem.

{{< figure src=`/wp-content/uploads/2017/05/penrose_maudlin.png` alt=`penrose_maudlin` caption=`Penrose diagram of an evaporating black hole. $\Sigma_1$ is a Cauchy surface, but $\Sigma_2$ is not --from Tim's preprint` width="296" >}}

Tim provides successive refinements of his point and relates it with two theorems by Robert Geroch on the causal structure of Lorentzian manifolds. As Tim's solution is quite simple, he needs to explain why the paradox has been so deeply misunderstood. He identifies, the problem, I think quite acutely, in a sloppy use of concepts that are intuitively clear but break down in the context of BHs. The section "*But it no longer exists!*" is excellent in this respect and refutes an objection based on a naive argument that I would have almost surely made (and that is, I believe, widely used in the literature). Along the way, Tim clarifies many important subtleties hidden in concepts such as information and observer ("from the point of view of observer A" may have many meanings).

Even if you doubt that a philosopher could bring something to a 40 year old physics problem, even if Tim's point turns out to not hold for some subtle reason, his article is certainly a mandatory read for anyone interested in the BH information paradox.

-- ***The grasshopper problem***\
by Olga Goulko and Adrian Kent, [arXiv:1705.07621](https://arxiv.org/abs/1705.07621)

Consider a given patch of grass of unit area but so far unspecified shape $S$. A grasshopper lands at a random point uniformly distributed on this patch. Then the grasshopper makes a jumps of length $d$ in a random direction (with a uniformly distributed angle). Your objective is to maximize the probability $P_S(d)$ that the grasshopper is still on the patch of grass after the jump. What is the optimal shape $S$ for the patch of grass that gives the highest probability?

The problem came to the authors because it is related in some subtle way to Bell inequalities but they realized the question was interesting in itself, because the optimal shapes are quite counter intuitive. Indeed, the naive disc shape can easily be shown to not be optimal, even for short jump distances $d\ll 1$ (for $d\gg 1$, the disc is trivially suboptimal as $P_{disc}(d)=0$). The optimal shapes are weird, have interesting discrete rotational symmetry and there seems to be a phase transition at a well defined value of $d$.

{{< figure src=`/wp-content/uploads/2017/06/grasshopper.png` alt=`grasshopper` caption=`Phase diagram of the optimal grass patch as a function of the grasshopper jump size` width="2459" >}}

The paper is a really nice as analytical estimations are mixed with thorough numerical explorations. I would not be surprised if it becomes a classic a bit like the [sofa problem](https://en.wikipedia.org/wiki/Moving_sofa_problem).
