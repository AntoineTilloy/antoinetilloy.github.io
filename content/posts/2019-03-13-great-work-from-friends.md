---
title: Great work from friends
date: '2019-03-13T10:30:15'
slug: great-work-from-friends
---

My smart friends have been doing great work recently and I think it deserves attention.

## I Understanding deep neural networks theoretically

[Jonathan Donier](https://fr.linkedin.com/in/jonathan-donier-b1151461), who now works for *Spotify* in London after a PhD in applied maths in Paris, has put a series of 3 fundamental articles on theoretical machine learning:

1\) **Capacity allocation analysis of neural networks: A tool for principled architecture design** -- [arXiv:1902.04485](http://arxiv.org/abs/1902.04485)\
2) **Capacity allocation through neural network layers** -- [arXiv:1902.08572](http://arxiv.org/abs/1902.08572)\
3) **Scaling up deep neural networks: a capacity allocation perspective** -- [arXiv:1903.04455](http://arxiv.org/abs/1903.04455)

In these papers, Jonathan defines and explores the notion of *capacity* *allocation* of a neural network, which formalizes the intuitive idea that some parts of a network encode more information about certain parts of the input space. The objective is to understand how a given architecture of network manages to capture the structure of correlations in the input. Ultimately, this should allow one to go beyond fuzzily grounded heuristics and expensive trial and error in order to design networks with a topology adapted to the problem right from the start.

{{< figure src=`/wp-content/uploads/2019/03/image.png` >}}

Jonathan very progressively builds up the theory from basic definitions to non-trivial scaling prescriptions for deep networks. The first paper defines the *capacity* rigorously in the simplest settings and deals mostly with the linear case. The second one considers special non-linear settings where the capacity analysis can still be carried out exactly and where one gets insights about the decoupling role of non-linearity. The final one puts all the pieces together and, among other things, allows to rigorously recover many initialization prescriptions for deep networks that where known only from heuristics. This super quick summary does not do justice to the content: this series of papers is, in my opinion, a major advance in the theoretical understanding of deep neural networks.

## II Making measurements crystal clear in Bohmian mechanics

[Dustin Lazarovici](https://dustinlazarovici.com/), who is now a philosopher of physics in Lausanne after a PhD in mathematical physics in Munich, has put online a very clear paper explaining how position measurements work in Bohmian mechanics and what their relation with particle positions is.

**Position Measurements and the Empirical Status of Particles in Bohmian Mechanics** -- [arXiv:1903.04555](https://arxiv.org/abs/1903.04555)

{{< figure src=`/wp-content/uploads/2019/03/image-1.png` >}}

Dustin is perhaps one of the people who has the clearest mind on foundations and Bohmian mechanics in particular. The notion of measurement in Bohmian mechanics is usually so deeply misunderstood that Dustin's concise explanation is a great reference for anyone interested in these questions. I particularly enjoyed the very end, where the link (or lack of link) with consciousness is precisely discussed. I think it exemplifies what useful work by philosophers of physics can be like: not muddling the water (as physicists usually think philosophers do) but sharpening the reasoning to save physicists from their own confusion.

## III Popularizing tricky mathematical notions

[Antoine Bourget](http://www.antoinebourget.org/blog/), who is now a postdoc at *Imperial College* in London, after a postdoc in Oviedo and a PhD at ENS in Paris (in the same office as me), has put a series of pedagogical videos on Youtube, through his account [*Scientia Egregia*](https://www.youtube.com/user/antoinebrgt).

{{< figure src=`/wp-content/uploads/2019/03/image-2.png` >}}

The videos are in French, and I recommend in particular the *[dictionnaire entre algèbre et géométrie](https://www.youtube.com/watch?v=SU6TsD3TM4k)*. Antoine starts with many simple examples to show the subtleties and motivate the definitions. He explains very well how one constructs mathematical notions to fit a certain intuition, a certain purpose, and thereby manages to make "obvious" really non-trivial concepts. Go check his [videos](https://www.youtube.com/user/antoinebrgt) so that he gets pressure to make more.
