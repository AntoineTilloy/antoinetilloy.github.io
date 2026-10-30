---
title: Bien plus qu’il n’en faut sur le cycle du combustible nucléaire et le taux de recyclage associé
date: '2020-01-14T18:56:39'
slug: bien-plus-quil-nen-faut-sur-le-cycle-du-combustible-nucleaire-et-le-taux-de-recyclage-associe-soon-online
french: true
---

*Les combustibles nucléaires usés issus des réacteurs électrogènes français sont recyclés. D'aucuns arguent que ce recyclage permet de récupérer 96% du combustible, l'industrie est très vertueuse et exemplaire ! D'autres disent au contraire que le recyclage ne permet qu'1% de réutilisation, le recyclage c'est du bullshit ! Qui a raison ?*

*Je trouve que cette controverse est un bon prétexte pour expliquer la physique associée, qui est intéressante. Mon objectif est d'expliquer en détails l'aval du cycle du combustible pour son intérêt propre, la résolution de la controverse étant ensuite un corollaire trivial. Au passage, c'est l'occasion d'apprendre un peu plus sur l'histoire civile et militaire du nucléaire, le principe d'un réacteur nucléaire, et les subtilités des différents isotopes de l'uranium et du plutonium.*

## La fission nucléaire et la réaction en chaîne

### La base

Les réacteurs à eau (légère), qui sont ultra majoritaires dans le monde, produisent de la chaleur par fission d'uranium enrichi. D'abord pourquoi de l'eau, et pourquoi enrichi ?

Dans la nature, l'uranium contient environ 0.7 % d'uranium 235 et 99.3% d'uranium 238. Seul le premier, le 235 est fissile, c'est à dire qu'il se casse en produisant de l'énergie lorsqu'il est soumis à un flux de neutrons.

Lorsqu'un noyau d'uranium 235 fissionne, il produit 2 ou 3 neutrons qui peuvent eux mêmes faire fissionner un atome d'uranium 235, c'est la réaction en chaîne, qui permet de se passer d'une source externe de neutrons. Pour que la réaction en chaîne se maintienne, il faut qu'au moins un neutron en moyenne issu d'une fission engendre une autre fission.

![1000px-Fission_chain_reaction.svg](/wp-content/uploads/2020/01/1000px-fission_chain_reaction.svg_.png)

Qu'est-ce qui peut arriver d'autre au neutron ? Essentiellement, être capturé par un atome de 238 ou simplement sortir du bloc d'uranium. Plus le bloc est gros, moins on perd de neutrons, et donc plus on s'approche de la masse critique, c'est à dire le point où la réaction en chaîne se maintient. Le problème c'est que même pour un bloc de taille infinie, c'est à dire avec aucune perte de neutrons à l'extérieur, il faut au moins environ 10% d'uranium 235 pour atteindre la masse critique, sans quoi l'uranium 238 capture trop de neutrons. Bref on peut rassembler autant d'uranium naturel qu'on veut, on n'atteindra jamais la masse critique tout seul.

Face à ce problème, les physiciens ont trouvé deux solutions : l'*enrichissement* et la *modération*.

### 

### Atteindre la masse critique

L'enrichissement est la solution la plus évidente : augmenter la concentration d'uranium 235 pour réduire le taux de capture par 238. C'est une procédure pas évidente car 235 et 238 sont chimiquement indistinguables et donc il faut ruser en exploitant leur légère différence de masse. Aujourd'hui, on fait cela par centrifugation et avant ça, on le faisait par diffusion gazeuse. C'était très cher et très énergivore, ça l'est un peu moins maintenant, mais ça reste une opération non triviale.

Une autre solution est de modérer (c'est à dire ralentir) les neutrons. Là on touche à de la physique franchement pas évidente. Il se trouve que lorsque les neutrons vont vite l'uranium 235 leur apparaît petit et 238 gros. Mais si les neutrons vont moins vite alors l'uranium 235 apparaît de plus en plus gros et 238 proportionnellement plus petit, et donc la probabilité de collision avec 235 augmente.

Pourquoi ? En général à ce moment on invoque la mécanique quantique, et la théorie quantique des champs, en faisant des grands gestes avec les mains. Je dois dire que ça reste peu évident pour moi, je sais que c'est un effet qu'on mesure mais je ne sais pas jusqu'à quel point on sait le dériver des équations fondamentales de la physique. On a probablement des modèles assez phénoménologiques sur la structure des noyaux pour l'expliquer, mais je n'en sais pas plus.

Pour ralentir les neutrons, il suffit de les faire passer dans un milieu qui les laisse rebondir pour qu'ils perdent progressivement leur énergie mais ne les capture pas trop. L'eau du robinet est un bon modérateur, et le graphite (des mines de crayon) et l'eau lourde (de l'eau où l'hydrogène est remplacé par son isotope lourd, le deuterium) en sont d'encore meilleurs.

### Retour sur l'histoire du nucléaire

Aux tous débuts du nucléaire, dans les années 40, les physiciens ont commencé par modérer, parce que c'était le plus simple. Les américains autour d'Enrico Fermi ont utilisé du graphite, et les allemands, principalement autour d'Heisenberg, ont utilisé l'eau lourde. Dans les deux cas avec un combustible d'uranium naturel.

{{< figure src=`/wp-content/uploads/2020/01/pile-e1579014368980.jpg` alt=`scanned: May 2001 by Image Delivery Systems LLC` caption=`Une des piles de graphite du projet Manhattan` width="346" >}}

Le réacteur de Fermi, modéré au graphite, a donné naissance à la première génération de réacteurs nucléaires exploités à travers le monde, et notamment les réacteurs à uranium naturel graphite gaz (UNGG) français (aujourd'hui tous en démantèlement), et les tristement célèbres *Reaktor Bolshoy Moshchnosti Kanalnyi* (RBMK) \[qui fonctionnent en fait à l'uranium légèrement enrichi\] dont ceux qui ont vu la série *Chernobyl* connaissent désormais tout.

{{< figure src=`/wp-content/uploads/2020/01/saint_laurent.jpg` alt=`saint_laurent` caption=`Réacteurs A1 et A1 à l'uranium naturel (UNGG) de la centrale de Saint Laurent` width="414" >}}

Si les nazis ne sont pas parvenus à fabriquer la bombe nucléaire, les réacteurs à eau lourde qu'ils exploraient ont plus tard été industrialisés et sont utilisés aujourd'hui par le Canada et l'Inde.

Aujourd'hui la France, comme la plupart des pays produisant de l'énergie nucléaire, exploite des réacteurs utilisant de l'eau comme modérateur et de l'uranium enrichi à environ 4% comme combustible. La masse critique est ainsi obtenue en combinant enrichissement et modération. Cette combinaison est celle des réacteurs de deuxième génération (comme les 58 réacteurs actuellement exploités en France) et de troisième génération (comme l'EPR).

En fait, du point de vue physique, cette combinaison correspond aussi à la génération 0 de réacteurs. Il y a environ 2 milliards d'années, l'uranium naturel avait une concentration plus forte en 235 (3.6%) qu'aujourd'hui (0.7%). Le 235 a une demi vie plus courte que le 238, et donc la concentration en 235 diminue au cours du temps. Par rapport à l'uranium actuel, l'uranium naturel d'il y a 2 milliards d'années était enrichi, à peu près autant que celui des centrales françaises. À Oklo au Gabon, des infiltrations d'eau (faisant office de modérateur) dans un gisement d'uranium ont ainsi permis de maintenir une réaction en chaîne pendant plusieurs centaines de milliers d'années.

En résumé, que ce soit dans la nature ou dans un réacteur, pour obtenir une réaction nucléaire auto-entretenue, il faut modérer, enrichir, ou les deux.

Avant de passer à la suite, et regarder ce qui sort d'un réacteur, on peut noter qu'on a déjà un sous produit de la fabrication de combustible à l'uranium enrichi : l'uranium appauvri. On part d'un uranium naturel à 0.7%, et après enrichissement environ un dixième devient de l'uranium enrichi à 4% et le reste de l'uranium appauvri à 0.3% (le taux est variable). Donc on produit beaucoup d'uranium appauvri, a priori inutile.

![uapp](/wp-content/uploads/2020/01/uapp.png)

### Le combustible usé

Maintenant qu'est ce qui sort du réacteur après environ 3 ans de réactions ? Naïvement, à quoi peut-on s'attendre ? On a dû consommer une fraction de l'uranium 235 présent, et donc, en démarrant avec 100% d'uranium (lui même à 4%) de 235, on a dû passer typiquement à 97% d'uranium (à environ 1% de 235) et 3% de produits de fission, c'est à dire de fragments issus de la fission d'uranium.

{{< figure src=`/wp-content/uploads/2020/01/naive_composition.png` alt=`naive_composition` caption=`Composition naïve du combustible usé` width="344" >}}

En fait, ça n'est pas ce qu'on obtient. La concentration de l'uranium est effectivement tombée à 1% de 235 environ mais au lieu d'avoir 97% d'uranium au total on en a 95%. On a en plus 4% de produits de fission (au lieu des 3% attendus), 1% environ de plutonium et environ 0.1% de d'autres atomes lourds (les actinides mineurs). Que s'est il passé ?

{{< figure src=`/wp-content/uploads/2020/01/realcomposition.png` alt=`realcomposition` caption=`Composition réelle du combustible usé` width="408" >}}

## Transmutation de l'uranium 238

### Principe

Pour comprendre il faut revenir au tout début et les captures parasites de neutrons par l'uranium 238. L'idée de la modération était de les réduire pour favoriser les fissions de 235 et atteindre la masse critique. Mais il en reste malgré tout un certain nombre. Il faut maintenant suivre cet uranium 238. Lorsqu'il capture un neutron, l'uranium 238 devient uranium 239. C'est un noyau très instable qui se désintègre rapidement en neptunium 239 (désintégration beta -, essentiellement un neutron du noyau se transforme en proton). Le neptunium 239 est toujours instable et se désintègre ensuite en plutonium 239 qui est stable (au moins pour quelques dizaines de milliers d'années). Ainsi, à cause de ces captures, une partie de l'uranium 238, a priori spectateur, est *transmutée* en plutonium 239.

{{< figure src=`/wp-content/uploads/2020/01/generation_pu239.jpg` alt=`generation_pu239` caption=`Génération du plutonium 239 par capture ([IN2P3](http://www.laradioactivite.com/site/pages/laformationduplutonium239.htm))` width="500" >}}

Le plutonium 239 possède, en première approximation, les mêmes propriétés que l'uranium 235 du point de vue de la fission nucléaire. Les captures permettent ainsi de "régénérer" partiellement le combustible : à mesure que de l'uranium 235 est consommé, on produit du plutonium 239 essentiellement substituable, qui vient en partie compenser la perte de 235. L'uranium 238 n'est pas fissile, mais il est *fertile*, c'est à dire qu'il peut produire de la matière fissile.

On peut ainsi expliquer la composition du combustible usé en sortie de réacteur : au total 2% du total d'uranium 238 a été transmuté en plutonium. 1% de ce plutonium a fissionné et ajoute 1% aux produits de fission, et 1% reste intact dans le combustible usé. Les 0.1% d'actinides mineurs correspondent à des atomes lourds produits par de multiples captures de neutrons, on reviendra sur eux plus tard.

### Applications militaires du plutonium

Dès les débuts du projet Manhattan, les américains ont compris l'intérêt militaire du plutonium. L'uranium est très difficile à enrichir pour atteindre de hauts pourcentages (+ de 95%) d'uranium 235 fissile. Les deux isotopes de l'uranium sont quasi indistinguables (ils réagissent pareil, fondent pareil, etc.) et seule leur petite différente de masse peut permettre de les séparer. C'est cher, lent et compliqué.

Le plutonium est produit en petite quantité dans les réacteurs, mais il est facilement séparable du reste par des réactions chimiques. Ainsi, si l'on souhaite produire une bombe, et pour peu que l'on possède un réacteur adapté, il peut être beaucoup plus simple de le faire à partir de plutonium extrait de combustibles préalablement irradiés qu'à partir d'uranium coûteusement enrichi.

C'est ce qui s'est produit historiquement. Les américains, après un énorme effort de guerre, ont péniblement réussi à enrichir 64 kg d'uranium pour produire la bombe Little Boy qui explosa sur Hiroshima.

Mais c'est leur programme de production de plutonium qui permit de faire la première bombe atomique de l'essai Trinity, puis Fat man qui explosa sur Nagazaki et ensuite le gros de leur arsenal.

{{< figure src=`/wp-content/uploads/2020/01/trinity-e1579016571135.jpg` alt=`trinity.jpg` caption=`Bombe au plutonium (6kg) de l'essai Trinity` width="5554" >}}

En France, la première série de réacteurs du CEA (G1 G2 G3), uranium naturel graphite gaz (UNGG) avait aussi pour objectif la production de plutonium pour la force de dissuasion. Plus généralement, posséder un réacteur donne accès au plutonium comme sous produit, qui donne potentiellement accès à une production industrielle d'armes nucléaires.

C'est le risque de prolifération lié aux activités nucléaires même a priori civiles qui explique que l'on soit modérément serein quand un pays instable démarre un réacteur nucléaire, sauf à pouvoir contrôler précisément ce qui entre et sort de ses réacteurs. On va voir plus tard que ce point est à nuancer pour les réacteurs actuels, qui ne permettent pas facilement un détournement militaire, à cause de la faible qualité du plutonium qui en sort.

### Le retraitement des combustibles nucléaires usés et recyclage

Après cette digression, revenons sur le combustible usé en sortie de réacteur

Le combustible usé contient 4% de produits de fission et actinides mineurs. Ils sont très radioactifs et pas simplement fissiles, bref non seulement inutiles mais aussi pénibles à gérer. Le combustible usé contient aussi 1% de plutonium fissile, et 95% d'uranium lui même à 1% environ d'uranium 235 fissile.![acu](/wp-content/uploads/2020/01/acu.png)

L'idée du retraitement est de séparer ce qui est potentiellement réutilisable de ce qui ne l'est pas. Les produits de fission et les actinides mineurs sont dangereux et inutiles, ils sont donc séparés et vitrifiés (c'est à dire mélangés à un verre spécial et coulés dans des fûts en inox). Le plutonium et l'uranium sont extraits.

Le plutonium est mélangé à de l'uranium appauvri en substitut de l'uranium 235 pour produire un nouveau combustible, le MOX (pour mixed oxydes). Ce dernier contient aujourd'hui environ 9% de plutonium (on verra pourquoi c'est beaucoup plus que les 4% d'uranium 235 du combustible standard plus tard). On produit environ 1 MOX pour 10 combustibles UNE retraités.

L'uranium extrait est appelé uranium de retraitement (URT). Aujourd'hui il est simplement entreposé en attente de réutilisation. Mais jusqu'en 2013 (et probablement de nouveau à partir de 2023) il était réenrichi pour donner de l'uranium de retraitement réenrichi (URE) à grosso modo 6% de 235 contre 1% pour l'URT avant réenrichissement (on verra aussi plus tard pourquoi c'est plus que 4%). On produisait (et produira) environ 1.5 combustible URE pour 10 UNE retraités.

Les réacteurs doivent être adaptés pour utiliser ces combustibles dont la réactivité est un peu différente de celle des UNE, mais la technologie reste celle des réacteurs actuels. En France ce sont les réacteurs 900MW, donc les plus anciens réacteurs à eau (dont Fessenheim) qui ont été adaptés pour brûler du MOX ("moxés" pour faire fancy). L'URE était quant à lui brûlé dans les réacteurs de la centrale de Cruas (900MW aussi) jusqu'en 2013 (mais je ne sais pas où EDF prévoit de le faire ensuite).

En sortie de réacteur, les MOX et URE usés contiennent toujours de l'uranium et du plutonium qu'on pourrait être tenté de réutiliser.

Mais aujourd'hui ça n'est pas le cas et la France se contente de "monorecycler" ses combustibles usés. MOX et URE usés sont donc entreposés en l'état dans les piscines de la Hague. En résumé on a donc quelque chose comme ça :

![summary](/wp-content/uploads/2020/01/summary.png)

## Le multirecyclage

### Tous les plutonium ne se valent pas

Le MOX usé contient toujours environ 5% de plutonium, bien plus que les UNE usés, et une ressource a priori énorme. Pourquoi ne s'en sert-on pas ? Plus suspect encore le MOX était chargé à 9% de plutonium alors qu'on a dit que le plutonium 239 avait grosso modo les mêmes propriétés que l'uranium 235 (et on n'a besoin que de 4% de ce dernier). Pourquoi ça ne nous pète pas à la figure ?

En fait on a trop simplifié la situation. Les captures de neutrons ne s'arrêtent pas au plutonium 239. Lui même peut capturer un neutron sans fissionner pour donner du plutonium 240. Ce dernier peut encore capturer un neutron pour produire du plutonium 241, qui se désintègre ou, s'il capture encore un neutron, donner du plutonium 242. Les isotopes impairs du plutonium sont fissiles, mais les isotopes pairs ne le sont pas dans les réacteurs actuels. La proportion d'isotopes impairs détermine la "qualité" du plutonium. Tous les plutoniums ne se valent pas.

{{< figure src=`/wp-content/uploads/2020/01/formationplutonium.jpg` alt=`FormationPlutonium` caption=`Différents isotopes du plutonium ([IN2P3](http://www.laradioactivite.com/site/pages/lesisotopesduplutonium.htm))` width="464" >}}

Le plutonium du combustible UNE usé ne contient que 60% de plutonium 239 fissile, et environ 30% de 240 qui est au contraire un poison neutronique (il capture beaucoup les neutrons et réduit la réactivité). C'est pour ça qu'il fallait monter à 9% pour faire un MOX réactif. Maintenant en sortie le MOX usé contient certes 5% de plutonium, mais ce dernier a encore moins de 239 (moins de 40%) car les captures se sont multipliées pendant que les isotopes fissiles étaient consommés (augmentant mécaniquement la fraction d'isotopes pairs non fissiles).

Maintenant, pourquoi ne pas faire du "super MOX" à 15% de plutonium pour compenser la dégradation de sa qualité ? Pour comprendre le problème, il faut remonter au tout début et la question de la modération. On l'a vu la présence d'eau comme modérateur (et caloporteur) dans les réacteurs actuels favorise la réaction en ralentissant les neutrons, et en facilitant les fissions d'uranium 235 (ou plutonium impair) par rapport aux captures. Les isotopes pairs du plutonium, on l'a dit, ne sont pas fissiles pour des neutrons modérés, mais ils le deviennent pour des neutrons rapides, non ralentis.

Ainsi, si on réduit la modération, on réduit la réactivité en augmentant les captures, mais on l'augmente en rendant fissile les isotopes pairs du plutonium. Tant qu'il n'y a pas trop de plutonium, le premier effet domine et la perte d'eau réduit la réactivité. Mais passé environ 12%, l'augmentation de réactivité des isotopes pairs du plutonium domine, l'effet d'une réduction de modération est une augmentation de la réactivité. Un réacteur chargé avec un tel combustible serait donc instable en cas de perte de l'eau dans le circuit primaire, ce qui est inacceptable.

Pourquoi ne pas enrichir le plutonium comme on enrichit l'uranium, par centrifugation ? L'uranium est peu radioactif, c'est un émetteur beta de longue période. On peut le passer dans des centrifugeuses et plus généralement des usines sans protection massive. À l'inverse le plutonium possède une durée de vie plus courte et est un puissant émetteur alpha, rayonnement fortement énergétique. Il ainsi beaucoup plus compliqué à manipuler ce qui rend son enrichissement difficile.

On est ainsi limité à environ 9% pour la concentration en plutonium dans du combustible. Le plutonium du MOX usé est ainsi de qualité trop faible pour fabriquer un combustible capable d'alimenter une réaction en chaîne car il faudrait monter à des pourcentages supérieurs. On va voir qu'il y a malgré tout des solutions.

### Retour sur l'utilisation militaire du plutonium et risque de prolifération

Comme on a parlé de la question de la qualité isotopique du plutonium on peut revenir sur les applications militaires et le risque de prolifération. Aujourd'hui, on ne sait pas faire de bombe avec du plutonium contenant moins de 90% de plutonium 239.

Comment l'obtenir ?

Pour obtenir du plutonium ultra pur en 239 il faut éviter les captures additionnelles, et donc irradier un très court moment, typiquement seulement quelques jours au lieu de 3 ans. Pour ça il faut avoir un réacteur qui permet de faire des irradiations très courtes d'assemblages de combustible sans tout perturber.

Les réacteurs au graphite le permettaient très facilement, les réacteurs à eau pressurisée actuels rendent ça très compliqué car il faut arrêter le réacteur à chaque déplacement d'un assemblage. De surcroît, ces arrêts sont visibles dans la production électrique : un pays qui tenterait malgré tout de produire du plutonium militaire avec un réacteur à eau civil n'est pas trop difficile à démasquer.

Le fait que les réacteurs à eau produisent un plutonium très dégradé en conditions normales et qu'il soit difficile de faire des irradiations courtes avec est ainsi un gros avantage du point de vue de la prolifération.

### Multirecyclage du plutonium dans les réacteurs actuels

Donc on résume, le plutonium qui sort d'un réacteur à eau possède un mélange d'isotopes dont seule une fraction est fissile.

Après un second passage en réacteur, ce plutonium contient tellement d'isotopes non fissiles qu'on ne peut plus en faire du combustible sans dépasser un taux limite qui rendrait le réacteur instable. Peut-on passer outre ?

Oui, a priori on peut. Pour ça on peut imaginer ajouter de l'uranium 235 issu de l'enrichissement pour donner un coup de boost au plutonium dégradé. Là où le plutonium 239 permettait de remplacer l'uranium 235, on peut remplacer une partie du plutonium de mauvaise qualité par de l'uranium 235 pour augmenter sa réactivité.

Naturellement, l'intérêt est moindre car il faut ajouter de l'uranium enrichi pour brûler le plutonium. Comme cela conduit à mettre des isotopes plus lourds du plutonium plus longtemps en réacteur, ça conduit aussi à produire plus d'actinides mineurs.

Le plutonium se dégrade aussi de plus en plus pour arriver à une valeur d'équilibre autour de 30% en plutonium 239, on a donc asymptotiquement un plutonium de très basse qualité (même si la qualité ne tend pas vers 0).

Ce multirecyclage du plutonium sur base uranium enrichi, aujourd'hui, n'est pas fait, mais c'est dans les tiroirs en France pour l'après 2030. Je me garderai bien de dire si c'est positif ou pas, il y a des avantages et des défauts et le bilan n'est pas évident.

### Pollution isotopique de l'uranium

Maintenant on pourrait imaginer réutiliser l'uranium contenu dans les URE usés. La difficulté est similaire à celle que l'on rencontre pour le plutonium. Souvenons nous que pour le combustible à l'uranium réenrichi, on montait à 6% de 235 au lieu de 4% dans des combustibles non-recyclés. La raison, c'est que l'uranium qui est déjà passé en réacteur contient un peu d'uranium 236, qui vient de l'uranium 235 qui n'a pas fissionné et a capturé un neutron.

Cet uranium 236 est un puissant poison neutronique, c'est à dire qu'il capte des neutrons sans rien faire, et donc réduit fortement la réactivité.

Après un deuxième passage en réacteur, l'uranium de l'URE usé contient beaucoup d'uranium 236 et il est donc plus difficile d'en faire un combustible recyclé. Ici l'obstacle est je crois davantage économique que technique : comme il y a peu d'URE usé, qu'il faudrait réenrichir beaucoup pour produire peu de nouveau combustibles, ça ne vaut pas le coup.

### Multirecyclage croisé ??

Maintenant on pourrait être encore plus vicieux et réutiliser l'uranium du MOX usé et le plutonium de l'URE usé.

La réutilisation de l'uranium du MOX usé est impossible sans multirecyclage de son plutonium pour des raisons réglementaires. La France a signé des traités de non-prolifération qui lui interdisent d'accumuler trop de plutonium séparé, c'est à dire hors d'un assemblage de combustible prêt à être utilisé. A priori ce plutonium de faible qualité n'est pas proliférant, mais j'imagine que les traités ne mentionnent pas l'isotopie.

Pour le recyclage du plutonium de l'URE usé a priori pas de problème de physique évident, mais probablement un obstacle économique qui est qu'aujourd'hui il y a très peu d'URE usé. Peut-être que cela changera quand le réenrichissement de l'uranium de retraitement sera repris.

## Multirecyclage en réacteurs à neutrons rapides

Jusqu'à maintenant on parle de recyclage à petite échelle et il faut maintenant mentionner une option qui changerait complètement les ordres de grandeur. Pour ça il faut revenir au concept de modération.

On l'a vu la modération, en augmentant la réactivité, permet de faire fonctionner des réacteurs avec des concentrations "faibles" de matière fissile. La contrepartie, c'est que les neutrons modérés font fissionner uniquement les isotopes impairs du plutonium et que ce dernier accumule ainsi les isotopes pairs.

L'idée des réacteurs à neutrons rapides est simplement de ne pas modérer en utilisant un combustible très concentré en matières fissiles, c'est à dire à l'uranium très enrichi, ou fortement concentré en plutonium.

Dans un tel réacteur il se passe plusieurs choses intéressantes. D'abord, l'intégralité des isotopes du plutonium sont fissiles, ce qui permet de stabiliser sa qualité à une valeur plus élevée que le multirecyclage en réacteurs modérés (à eau légère).

Mais ça n'est pas le plus intéressant...

### Régénération et surgénération

On l'a vu, un réacteur à eau légère produit du plutonium mais ce dernier ne compense pas la quantité d'uranium consommée. Il y a trop de pertes de neutrons. Maintenant, la fission d'un noyau de plutonium 239 produit environ 3 neutrons en moyenne. Ainsi, pour peu que l'on ne perde pas trop de neutrons à droit à gauche, on doit pouvoir en utiliser 1 pour faire de nouvelles fissions et 1 (voire plus) pour régénérer la matière fissile à partir de l'uranium 238.

C'est précisément ce qu'on peut faire dans un réacteur à neutrons rapide. En imaginant que ce dernier est démarré avec un mélange uranium 238 / plutonium 239, on peut faire fissionner tout le 239 tout en le régénérant intégralement par transmutation de l'uranium 238. En fait on peut même en théorie surgénérer, et produire plus de plutonium qu'on n'en consomme pour alimenter d'autres réacteurs plus standards. Ainsi, au lieu de consommer environ 0.5% de l'uranium naturel, on pourrait en théorie monter à 100%, c'est à dire gagner un facteur 200 dans l'utilisation de la ressource naturelle.

Ça c'est en théorie. En pratique, les réacteurs à neutrons rapides sont aujourd'hui un peu plus compliqués à faire. Il y a des questions de sûreté et de prolifération potentiellement moins simples que pour les réacteurs à eau et donc il y en a beaucoup moins en service.

En France il y avait Superphénix, arrêté dans les années 1990 pour des raisons à la fois techniques et politiques, Phénix (plus petit, démarré avant et arrêté après) et il devait y avoir Astrid, projet dont la réalisation pratique a récemment été repoussée à l'après 2050.

{{< figure src=`/wp-content/uploads/2020/01/superphenix_reactor_south.jpg` alt=`Superphenix_reactor_south` caption=`Superphénix (© [Yann Forget](https://commons.wikimedia.org/wiki/User:Yann "User:Yann") / <a href="https://commons.wikimedia.org/" class="external text">Wikimedia Commons</a> / <span class="plainlinks noprint"><a href="https://creativecommons.org/licenses/by-sa/3.0/" class="external text" rel="nofollow">CC-BY-SA</a>)</span>` width="407" >}}

Les russes ont divers prototypes de taille quasi industrielle comme le BN800 à Beloyarsk. Les réacteurs à neutrons rapides sont donc faisables, ça n'est pas de la science fiction ni quelque chose d'incertain comme la fusion nucléaire, mais le fait est qu'il y en a peu.

## Taux de recyclage et économie de ressources

Maintenant qu'on a dit tout ça, on peut se demander combien ces diverses réutilisations de matière permettent comme économies ou recyclage suivant ce qu'on choisit comme stratégie.

Commençons par le chiffre généralement mis en avant par les partisans du recyclage:

### 96% du combustible est recyclable - trompeur

*Techniquement c'est vrai*, effectivement on sort du combustible usé l'uranium de retraitement et le plutonium. Restent 4% qu'on vitrifie. Donc on a bien 96% de recyclable. Mais c'est franchement trompeur : déjà, ces 96% ne sont pas uniformes et énergétiquement et il y a autant dans les 95% d'uranium faiblement enrichi que dans le 1% de plutonium. Il ne reste plus grand chose à essorer de ce dernier, et une fois essoré on ne sait pas bien quoi faire du reliquat appauvri (à moins de le fertiliser en réacteur à neutrons rapides...).

De plus, si on passait à une régénération intégrale du plutonium en réacteur à neutrons rapide, c'est à dire si on gagnait un facteur 200 d'efficacité énergétique, ce chiffre de 96% ne changerait pas, il pourrait même devenir moins bon ! En effet, si on régénère le plutonium à un meilleur taux et en imaginant que les gaines tiennent le coup, on pourrait faire tourner le réacteur plus longtemps, et augmenter mécaniquement le pourcentage de produits de fission et d'actinides mineurs en sortie. On aurait donc un taux de recyclage inférieur alors que la situation est clairement meilleure.

À l'inverse, imaginons qu'on réduise artificiellement le temps passé en réacteur des combustibles (le burnup) et qu'on ne produise ainsi qu'1% de produits de fission. Alors 99% du combustible serait recyclable.

Bref, ce chiffre n'est pas incorrect mais il ne permet pas de comparaison raisonnable, et induit au moins superficiellement une opinion fausse. C'est une mauvaise métrique.

### 1% du combustible est effectivement recyclé - trompeur aussi

Ce chiffre est en général donné par les opposants au recyclage dans l'hypothèse que l'on ne fait que du MOx et donc que seul le plutonium est réutilisé et une unique fois (mais c'est légitime, c'est effectivement ce qu'on fait aujourd'hui).

Savoir ce qu' "*effectivement recyclé*" veut dire n'est pas tout à fait clair, mais on comprend bien l'idée : on ne réutilise que le plutonium, et il représente 1% du combustible en masse.

Ça n'est pas totalement faux mais c'est aussi franchement trompeur : ce plutonium possède une énorme densité énergétique. De plus, quand EDF réutilisera de nouveau l'uranium de retraitement, est-ce qu'on passera d'un coup à 96% avec ce calcul ? Ou est-ce qu'on ne compte que l'uranium 235 contenu dans l'uranium de retraitement ? Mais alors comment prendre en compte la portion de plutonium régénérée en réacteur ? Le problème d'un réacteur nucléaire c'et qu'il brûle typiquement plus de matière fissile que ce qu'on met dedans en entrée...

Le pourcentage effectivement recyclé est trop ambigu pour être défini de manière univoque. C'est aussi une mauvaise métrique.

### Qu'est ce qu'une bonne mesure ?

En physique, on réfléchit souvent à la question de "la bonne mesure". Et il y a quelques principes simples qu'on peut utiliser pour trouver une bonne mesure.

Le principal, c'est qu'il faut que la valeur ne change pas par un simple *relabelling* ou redéfinition des objets.

Par exemple imaginons que je rajoute un bloc de bois qui ne sert à rien à côté du combustible et que je déclare qu'il fait aussi partie du combustible. Ou que je me mette à compter les gaines dans le combustible, ou les murs de la centrale. Ça ne doit rien changer en termes de recyclage, c'est la même situation. Or pour les deux valeurs précédemment mentionnées, ça change tout !

Après avoir pas mal réfléchi à la question, je pense (je ne dis pas que c'est original) que la seule manière raisonnable d'estimer ce qui est recyclé est de regarder combien on économise de ressources naturelles à service identique (ici la production d'électrique).

On imagine un cycle ouvert, c'est à dire une configuration où le combustible usé n'est pas réutilisé. Et on le compare aux alternatives et on regarde l'économie de ressources obtenue, c'est à dire combien on a dû miner d'uranium dans les deux configurations. On obtient alors :

1.  Réutilisation du plutonium 1 fois avec du MOX (monorecyclage) **10% d'économie** \[pour 10 UNE, on produit 1 MOX\]
2.  Réutilisation du plutonium avec le MOx et de l'uranium avec l'URE **25% d'économie** \[pour 10 UNE, on produit 1 MOX et 1.5 URE\]
3.  Monorecyclage de l'URE + multirecyclage du plutonium en réacteurs à eau légère **30% d'économie** \[là la comptabilité est plus compliquée...\]
4.  Multirecyclage en réacteur à neutrons rapide en théorie jusqu'à **99.5% d'économie**

Je pense que ce sont les chiffres pertinents à avoir en tête et probablement les seuls cohérents. Quitte à passer pour un scientiste, je prends le risque de dire que ce n'est pas une question de point de vue. Les autres chiffres sont non seulement trompeurs mais incohérents (soit à cause de leur périmètre ambigu, soit à cause de la régénération des matières fissiles).

On voit qu'en poussant comme un fou les réacteurs actuels on monte à 30% et il paraît difficile, même en principe, de dépasser 40%. En revanche, si on s'autorise des réacteurs à neutrons rapides, alors on change complètement de ligue.

### Quel type de recyclage choisir ?

Est-ce qu'il est toujours mieux de recycler plus ? C'est une question bien plus large que ce qu'on aborde ici, et je voudrais être clair sur le fait que je n'ai pas cherché à y répondre. Ce recyclage a plein d'impacts secondaires : quand on recycle, on fait davantage d'opérations sur des matières radioactives (négatif), ce qui reste est au total moins radiotoxique (positif), le volume de déchets finaux est réduit (positif, même si l'ampleur est discutée), le conditionnement des déchets est meilleur (positif), on dispose d'une technologie de séparation du plutonium qui pourrait être utilisée à d'autres fins (négatif). Et il y a encore plein d'autres critères...

Par ailleurs, tant que l'on monorecycle ou multirecycle dans les réacteurs actuels, c'est à dire qu'on est autour de 10 - 30% d'économie, alors l'économie d'énergie n'est pas de manière évidente le critère dominant permettant de choisir parmi les précédentes nuances. C'est le saut vers le multirecyclage en réacteurs à neutrons rapides qui change réellement la donne.

Ce qui est sûr c'est qu'à très long terme, si le nucléaire se maintient et se développe, notamment via la Chine et que l'on reste sur un cycle  uranium/plutonium (pas de thorium) alors la limitation des ressources naturelles forcera le multirecyclage en réacteurs à neutrons rapides. En attendant, la ressource naturelle est peu chère dans le coût total de l'énergie nucléaire, notamment parce que des progrès importants ont été réalisés sur l'extraction et l'enrichissement de l'uranium, et donc il n'y a pas une très forte pression ce qui explique (je me garde de dire si ça justifie) le fait que la puissance publique ait repoussé récemment l'horizon de développement du multirecyclage en réacteurs à neutrons rapides.

### Retour sur le contexte et le débat public

La question de savoir s'il fallait recycler ou non le combustible usé (et le point incroyablement plus précis et restreint de savoir quelle économie de ressources le recyclage permet) était posée dans le débat public de 2019 sur la gestion des matières et déchets radioactifs. J'étais membre de la commission qui organisait ce débat. On avait organisé un exercice de [clarification des controverses techniques](https://pngmdr.debatpublic.fr/approfondir/clarification-des-controverses-techniques) avec des experts de tous horizons pour se mettre d'accord sur les conséquences du recyclage des combustibles usés (à défaut de trancher sur sa pertinence).

La question du taux de recyclage avait fait débat, mais on avait convenu dans la synthèse, non sans mal, que l'économie de ressources naturelles était la manière pertinente de mesurer la chose. Ensuite, durant le débat lui même, on avait pu voir que le débat était très actif sur le choix d'une stratégie plutôt qu'une autre, avec une situation qui peut sembler à front renversé pour le béotien. Les "pro-nucléaire" sont quasi uniformément favorables à la stratégie la plus ambitieuse possible de recyclage, les "anti-nucléaire", dont un certain nombre d'associations environnementales, souhaitant à l'inverse son arrêt immédiat. C'est que derrière tous les aspects positifs ou négatifs du recyclage, il y a surtout la question de la poursuite du nucléaire, le recyclage ancrant son utilisation dans la durée. Mais c'est une autre histoire...

*Il est difficile d'écrire un blogpost pareil sans faire d'erreurs, n'hésitez pas à les corriger dans les commentaires.*
