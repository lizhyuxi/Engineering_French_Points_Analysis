750

**18**: Algèbre linéaire Alain Chillès ( ) , , , Valentin Vinoles , Adrien Joseph Remerciements Nous tenons à ***remercier*** chaudement tous les professeurs qui nous ont aidés à écrire ce livre , notamment en corrigeant les inévitables fautes

**28**: Algèbre linéaire Alain Chillès ( ) , , , Valentin Vinoles , Adrien Joseph Remerciements Nous tenons à remercier chaudement tous les professeurs qui nous ont aidés à ***écrire*** ce livre , notamment en corrigeant les inévitables fautes

**73**: Préambule à la première version Je tiens avant toutes choses à ***remercier*** ici le professeur pour son aide précieuse lors de la relecture de ce polycopié

**93**: Je tiens aussi à ***remercier*** mon ami Franz Ridde , professeur en MPSI au lycée du Parc de Lyon , qui m' a fourni un grand nombre d' exercices

**146**: Il servira de support au cours , de guide et permettra , à ceux qui le souhaitent , d' ***approfondir*** quelques sujets

**158**: Il ne s' agit en aucun cas d' ***apprendre*** par cur son contenu

**289**: Signalons aussi l' outil de géométrie plane Geogebra et l' excellent Ipe qui permet d' ***annoter*** en LATEX 2 les dessins produits directement ou à l' aide d' un autre outil

**999**: Signifie x E , y E L' écriture x , y E ne est pas correcte ! Opérations Signification Multiplication externe Multiplication des matrices Notations de définitions Introduit une nouvelle notation Introduit une nouvelle définition Espaces vectoriels dim E ou dim(E ) ou dimK E ou Ensemble des fonctions définies sur l' ensemble X à valeurs dans l' ensemble Y Ensemble des fonctions continues définies sur l' intervalle I R à valeurs dans Ensemble des fonctions continues par morceaux définies sur l' intervalle I R à valeurs dans K R ou C Ensemble des fonctions de classe C k où k N , définies sur l' intervalle I R à valeurs dans K R ou C Droite vectorielle engendrée par x Sous-espace vectoriel de l' espace vectoriel E engendré par la partie A Somme des sous-espaces vectoriels E1 et E2 d' un même espace vectoriel E Somme des Ei , où ( Ei ) iI est une famille de sous-espaces vectoriels d' un même espace vectoriel E et où I est un ensemble quelconque Somme directe des sous-espaces vectoriels E1 et E2 d' un même espace vectoriel Somme directe des Ei , où ( Ei ) iI est une famille de sous-espaces vectoriels d' un même espace vectoriel E et où I est un ensemble quelconque La dimension du K - espace vectoriel E Ensemble des applications linéaires de l' espace vectoriel E dans l' espace vectoriel L ( E , E ) , ensemble des endomorphismes de l' espace vectoriel E Ensemble des automorphismes de l' espace vectoriel E L ( E , K ) , où E est un K - espace vectoriel c' est l' ensemble des formes linéaires sur l' espace vectoriel E ( ***noter*** le ? et non pas ) Noyau d' une application linéaire f L ( E , F ) Image d' une application linéaire f L ( E , F ) Application linéaire identité de l' espace vectoriel E Restriction d' une application linéaire f L ( E , F ) à un sous-espace vectoriel Co-restriction d' une application linéaire f L ( E , F ) à un sous-espace vectoriel F 0 de F contenant Im(f ) Projection sur F parallèlement à G , où E F G Symétrie par rapport à F parallèlement à G Rang de l' application linéaire f Famille duale de la base ( ei ) iI d' un espace vectoriel E Dimension d' un supplémentaire de F Ensemble des solutions du système linéaire S Matrice n p dont les coefficients sont les ( ai , j ) ( i , j)1,n1,p Im(A ) , Ker(A ) , rang(A ) Déterminants Signification Nous utiliserons systématiquement les crochets pour noter les matrices ! Ensemble des matrices à coefficients dans l' ensemble A ayant n lignes et p colonnes Matrice identité de Mp ( K ) Matrice nulle de Mn , p ( K ) Matrice du vecteur x E dans la base E de l' espace vectoriel E Matrice de l' application linéaire f L ( E , E 0 ) dans les bases E de E et E 0 de Matrice de l' endomorphisme f L ( E ) dans la base E de E ( correspond à Matrice ne contenant que des 0 sauf sur la k - ième ligne et la l - ième colonne où il y a un 1 ( Attention : les dimensions de ces matrices ne sont pas précisées ... ) Transposée de A , où A Mn , p ( K ) Ensemble des matrices symétriques de Mp ( K ) Ensemble des matrices antisymétriques de Mp ( K ) Matrice diagonale Ensemble des matrices diagonales de Mp ( K ) Matrice du système de vecteurs X ( x1 ,

**1162**: Signifie x E , y E L' écriture x , y E ne est pas correcte ! Opérations Signification Multiplication externe Multiplication des matrices Notations de définitions Introduit une nouvelle notation Introduit une nouvelle définition Espaces vectoriels dim E ou dim(E ) ou dimK E ou Ensemble des fonctions définies sur l' ensemble X à valeurs dans l' ensemble Y Ensemble des fonctions continues définies sur l' intervalle I R à valeurs dans Ensemble des fonctions continues par morceaux définies sur l' intervalle I R à valeurs dans K R ou C Ensemble des fonctions de classe C k où k N , définies sur l' intervalle I R à valeurs dans K R ou C Droite vectorielle engendrée par x Sous-espace vectoriel de l' espace vectoriel E engendré par la partie A Somme des sous-espaces vectoriels E1 et E2 d' un même espace vectoriel E Somme des Ei , où ( Ei ) iI est une famille de sous-espaces vectoriels d' un même espace vectoriel E et où I est un ensemble quelconque Somme directe des sous-espaces vectoriels E1 et E2 d' un même espace vectoriel Somme directe des Ei , où ( Ei ) iI est une famille de sous-espaces vectoriels d' un même espace vectoriel E et où I est un ensemble quelconque La dimension du K - espace vectoriel E Ensemble des applications linéaires de l' espace vectoriel E dans l' espace vectoriel L ( E , E ) , ensemble des endomorphismes de l' espace vectoriel E Ensemble des automorphismes de l' espace vectoriel E L ( E , K ) , où E est un K - espace vectoriel c' est l' ensemble des formes linéaires sur l' espace vectoriel E ( noter le ? et non pas ) Noyau d' une application linéaire f L ( E , F ) Image d' une application linéaire f L ( E , F ) Application linéaire identité de l' espace vectoriel E Restriction d' une application linéaire f L ( E , F ) à un sous-espace vectoriel Co-restriction d' une application linéaire f L ( E , F ) à un sous-espace vectoriel F 0 de F contenant Im(f ) Projection sur F parallèlement à G , où E F G Symétrie par rapport à F parallèlement à G Rang de l' application linéaire f Famille duale de la base ( ei ) iI d' un espace vectoriel E Dimension d' un supplémentaire de F Ensemble des solutions du système linéaire S Matrice n p dont les coefficients sont les ( ai , j ) ( i , j)1,n1,p Im(A ) , Ker(A ) , rang(A ) Déterminants Signification Nous utiliserons systématiquement les crochets pour ***noter*** les matrices ! Ensemble des matrices à coefficients dans l' ensemble A ayant n lignes et p colonnes Matrice identité de Mp ( K ) Matrice nulle de Mn , p ( K ) Matrice du vecteur x E dans la base E de l' espace vectoriel E Matrice de l' application linéaire f L ( E , E 0 ) dans les bases E de E et E 0 de Matrice de l' endomorphisme f L ( E ) dans la base E de E ( correspond à Matrice ne contenant que des 0 sauf sur la k - ième ligne et la l - ième colonne où il y a un 1 ( Attention : les dimensions de ces matrices ne sont pas précisées ... ) Transposée de A , où A Mn , p ( K ) Ensemble des matrices symétriques de Mp ( K ) Ensemble des matrices antisymétriques de Mp ( K ) Matrice diagonale Ensemble des matrices diagonales de Mp ( K ) Matrice du système de vecteurs X ( x1 ,

**1994**: a. Cela signifie que si x et y sont dans E , alors x y est dans E. b. Cela signifie que si est un scalaire ( il est dans K ) et si x est dans E , alors .x est dans E. Que veut -on ***faire*** ? Garder l' essentiel , et éliminer les coordonnées

**1996**: a. Cela signifie que si x et y sont dans E , alors x y est dans E. b. Cela signifie que si est un scalaire ( il est dans K ) et si x est dans E , alors .x est dans E. Que veut -on faire ? ***Garder*** l' essentiel , et éliminer les coordonnées

**2001**: a. Cela signifie que si x et y sont dans E , alors x y est dans E. b. Cela signifie que si est un scalaire ( il est dans K ) et si x est dans E , alors .x est dans E. Que veut -on faire ? Garder l' essentiel , et ***éliminer*** les coordonnées

**2012**: Pour la somme de deux vecteurs , ***voir*** la figure 1.1 , de la présente page

**2032**: Pour le produit d' un vecteur par un scalaire , ***voir*** la figure 1.2 , page suivante

**2388**: Dans le K - espace vectoriel des fonctions polynomiales , toute fonction polynomiale est combinaison linéaire de la famille : On ne sait ***faire*** que des sommes finies de vecteurs ! D' où la présence du n. Lorsque n 0 , on obtient ( par convention ) 0E

**2547**: 1.1.1 ***Démontrer*** que , dans tout K - espace vectoriel , les relations suivantes sont vérifiées : 1.1.2 Parmi les ensembles suivants , lesquels , munis des opérations usuelles , sont des R - espaces vectoriels ? Sous-espaces vectoriels Soit E un K - espace vectoriel et F E , on dit que F est un sous-espace vectoriel de E si : F est stable par ( c' est - à - dire que pour tout ( x , y ) F 2 , x y F ) F est stable par

**2618**: 1.1.1 Démontrer que , dans tout K - espace vectoriel , les relations suivantes sont vérifiées : 1.1.2 Parmi les ensembles suivants , lesquels , munis des opérations usuelles , sont des R - espaces vectoriels ? Sous-espaces vectoriels Soit E un K - espace vectoriel et F E , on dit que F est un sous-espace vectoriel de E si : F est stable par ( c' est - à - ***dire*** que pour tout ( x , y ) F 2 , x y F ) F est stable par

**2645**: ( c' est - à - ***dire*** que pour tout x F et tout K , .x F )

**3062**: Pour ***démontrer*** qu' un ensemble est un K - espace vectoriel , il est très souvent plus simple et plus rapide de démontrer que c' est un sous-espace vectoriel d' un K - espace vectoriel déjà connu

**3083**: Pour démontrer qu' un ensemble est un K - espace vectoriel , il est très souvent plus simple et plus rapide de ***démontrer*** que c' est un sous-espace vectoriel d' un K - espace vectoriel déjà connu

**3723**: Si E 6 0E et si x E , x 6 0E , alors Vect(x ) est la droite vectorielle engendrée par x : Proposition 1.1 Si E est un K - espace vectoriel et si A E , A 6 , alors Vect(A ) est l' ensemble des combinaisons linéaires construites à ***partir*** des vecteurs de A : Vect(A ) A Vect(A ) A Démonstration ( ) L' ensemble des combinaisons linéaires de vecteurs de A est un sous-espace vectoriel de E qui contient A , il contient donc Vect(A )

**3892**: Partie génératrice Soit A E , on dit que A est une partie génératrice de E si Vect(A ) E Famille génératrice Soit ( ai ) iI E I une famille de vecteurs de E , on dit que c' est une famille génératrice de E si Quelle différence y a -t -il entre la famille ( ai ) iI et ai , i I ? Dans un ensemble , les termes ne apparaissent qu' une seule fois , alors que dans une famille , il est possible de les ***répéter***

**3910**: C' est la même différence qu' entre une liste et un ensemble en informatique ! a ***Voir*** le code 1.1 , de la présente a. L' ensemble ai , i I associé à la famille ( ai ) iI s' appelle le support de la famille

**4079**: Plus généralement , si ( ei ) iI est une famille génératrice d' un K - espace vectoriel E et si ( fj ) jJ est une famille génératrice d' un K - espace vectoriel F , alors la partie ( ei , 0F ) , i I ( 0E , fj ) , j J est une partie génératrice de E F 1.2.1 ***Démontrer*** que est une partie génératrice de K3

**4089**: 1.2.2 ***Déterminer*** une partie génératrice simple du plan de K3 d' équation 1.2.3 Déterminer une famille génératrice simple du plan vectoriel de K4 , d' équations : 1.2.4 Soit a R , démontrer que la famille ( x 7 ( x a)n ) nN est une famille génératrice du R - espace vectoriel des fonctions polynomiales

**4101**: 1.2.2 Déterminer une partie génératrice simple du plan de K3 d' équation 1.2.3 ***Déterminer*** une famille génératrice simple du plan vectoriel de K4 , d' équations : 1.2.4 Soit a R , démontrer que la famille ( x 7 ( x a)n ) nN est une famille génératrice du R - espace vectoriel des fonctions polynomiales

**4120**: 1.2.2 Déterminer une partie génératrice simple du plan de K3 d' équation 1.2.3 Déterminer une famille génératrice simple du plan vectoriel de K4 , d' équations : 1.2.4 Soit a R , ***démontrer*** que la famille ( x 7 ( x a)n ) nN est une famille génératrice du R - espace vectoriel des fonctions polynomiales

**4160**: 1.2.6 Soit F un sous-espace vectoriel d' un K - espace vectoriel E , que ***dire*** de 1.2.7 Soit E un K - espace vectoriel , soit E1 , E2 et E3 trois sous-espaces vectoriels de E tels que : Que peut -on en conclure ? 1.2.8 Soit E un K - espace vectoriel , A et B deux parties de E , comparer : Vect(A B ) et Vect(A ) Vect(B ) Vect(A B ) et Vect(A ) Vect(B ) 1.2.9 Soit E un K - espace vectoriel tel que E 6 0E et soit ( Ei ) i1,n des sous-espaces vectoriels de E , tous distincts de E. Démontrer que : À quelle condition est -il un sous-espace vectoriel de E ? 1.2.10 Reprendre l' exercice précédent lorsque l' on considère une famille dénombrable de sous-espaces vectoriels ( En ) nN

**4189**: 1.2.6 Soit F un sous-espace vectoriel d' un K - espace vectoriel E , que dire de 1.2.7 Soit E un K - espace vectoriel , soit E1 , E2 et E3 trois sous-espaces vectoriels de E tels que : Que peut -on en ***conclure*** ? 1.2.8 Soit E un K - espace vectoriel , A et B deux parties de E , comparer : Vect(A B ) et Vect(A ) Vect(B ) Vect(A B ) et Vect(A ) Vect(B ) 1.2.9 Soit E un K - espace vectoriel tel que E 6 0E et soit ( Ei ) i1,n des sous-espaces vectoriels de E , tous distincts de E. Démontrer que : À quelle condition est -il un sous-espace vectoriel de E ? 1.2.10 Reprendre l' exercice précédent lorsque l' on considère une famille dénombrable de sous-espaces vectoriels ( En ) nN

**4208**: 1.2.6 Soit F un sous-espace vectoriel d' un K - espace vectoriel E , que dire de 1.2.7 Soit E un K - espace vectoriel , soit E1 , E2 et E3 trois sous-espaces vectoriels de E tels que : Que peut -on en conclure ? 1.2.8 Soit E un K - espace vectoriel , A et B deux parties de E , ***comparer*** : Vect(A B ) et Vect(A ) Vect(B ) Vect(A B ) et Vect(A ) Vect(B ) 1.2.9 Soit E un K - espace vectoriel tel que E 6 0E et soit ( Ei ) i1,n des sous-espaces vectoriels de E , tous distincts de E. Démontrer que : À quelle condition est -il un sous-espace vectoriel de E ? 1.2.10 Reprendre l' exercice précédent lorsque l' on considère une famille dénombrable de sous-espaces vectoriels ( En ) nN

**4255**: 1.2.6 Soit F un sous-espace vectoriel d' un K - espace vectoriel E , que dire de 1.2.7 Soit E un K - espace vectoriel , soit E1 , E2 et E3 trois sous-espaces vectoriels de E tels que : Que peut -on en conclure ? 1.2.8 Soit E un K - espace vectoriel , A et B deux parties de E , comparer : Vect(A B ) et Vect(A ) Vect(B ) Vect(A B ) et Vect(A ) Vect(B ) 1.2.9 Soit E un K - espace vectoriel tel que E 6 0E et soit ( Ei ) i1,n des sous-espaces vectoriels de E , tous distincts de E. ***Démontrer*** que : À quelle condition est -il un sous-espace vectoriel de E ? 1.2.10 Reprendre l' exercice précédent lorsque l' on considère une famille dénombrable de sous-espaces vectoriels ( En ) nN

**4270**: 1.2.6 Soit F un sous-espace vectoriel d' un K - espace vectoriel E , que dire de 1.2.7 Soit E un K - espace vectoriel , soit E1 , E2 et E3 trois sous-espaces vectoriels de E tels que : Que peut -on en conclure ? 1.2.8 Soit E un K - espace vectoriel , A et B deux parties de E , comparer : Vect(A B ) et Vect(A ) Vect(B ) Vect(A B ) et Vect(A ) Vect(B ) 1.2.9 Soit E un K - espace vectoriel tel que E 6 0E et soit ( Ei ) i1,n des sous-espaces vectoriels de E , tous distincts de E. Démontrer que : À quelle condition est -il un sous-espace vectoriel de E ? 1.2.10 ***Reprendre*** l' exercice précédent lorsque l' on considère une famille dénombrable de sous-espaces vectoriels ( En ) nN

**4298**: Plus précisément , pour E Rp , on pourra ***démontrer*** que le résultat est toujours vrai , mais qu' il devient faux pour l' espace vectoriel des fonctions polynomiales

**4320**: 1.2.11 ***Donner*** un exemple d' une famille de sous-espaces ( Ei ) iI de Rp , distincts de Rp , tels que Sommes de sous-espaces vectoriels Soit E un K - espace vectoriel

**4415**: Somme finie Soit E1 et E2 deux sous-espaces vectoriels de E , on appelle somme de E1 et E2 et on note E1 E2 le sous-espace vectoriel : Somme quelconque Plus généralement , si ( Ei ) iI est une famille de sous-espaces vectoriels de E , on appelle somme des Ei et Ei le sous-espace vectoriel : Il est faux de ***penser*** : 1

**4622**: Il est équivalent de ***dire*** : 1

**4641**: ( ei ) iI est une famille génératrice de E Vect(ei ) Démonstration Immédiat à ***partir*** des définitions

**4668**: Soit E1 , E2 et E3 trois sous-espaces vectoriels de E. ( a ) ***Comparer*** pour l' inclusion les sous-espaces : ( b ) Comparer pour l' inclusion les sous-espaces : ( c ) Comparer pour l' inclusion les sous-espaces : 1.3.2 Soit E un K - espace vectoriel

**4678**: Soit E1 , E2 et E3 trois sous-espaces vectoriels de E. ( a ) Comparer pour l' inclusion les sous-espaces : ( b ) ***Comparer*** pour l' inclusion les sous-espaces : ( c ) Comparer pour l' inclusion les sous-espaces : 1.3.2 Soit E un K - espace vectoriel

**4688**: Soit E1 , E2 et E3 trois sous-espaces vectoriels de E. ( a ) Comparer pour l' inclusion les sous-espaces : ( b ) Comparer pour l' inclusion les sous-espaces : ( c ) ***Comparer*** pour l' inclusion les sous-espaces : 1.3.2 Soit E un K - espace vectoriel

**4715**: Soit E1 , E2 et E3 trois sous-espaces vectoriels de E. ***Démontrer*** que : Démontrer que ce ne est plus vrai , si l' on enlève une des hypothèses à gauche

**4718**: Soit E1 , E2 et E3 trois sous-espaces vectoriels de E. Démontrer que : ***Démontrer*** que ce ne est plus vrai , si l' on enlève une des hypothèses à gauche

**4960**: Deux sous-espaces vectoriels E1 et E2 de E sont en somme directe si , et seulement si , il y a écriture unique de 0E , c' est - à - ***dire*** : Démonstration Supposons que E1 et E2 soient en somme directe

**5086**: On en déduit que E1 et E2 sont en somme Soit E un K - espace vectoriel , soit ( Ei ) iI une famille de sous-espaces vectoriels de E , on dit qu' ils sont en somme directe , si on a écriture unique de 0E , soit : distincts 2 à 2 On écrit alors Ei à la place de Ne pas ***oublier*** que l' on ne sait faire que des sommes finies de vecteurs ! ! Si I contient strictement plus de deux éléments , la condition iI Ei 0E ne suffit pas pour assurer que les Ei sont en somme directe , de même que les conditions Ei Ej 0E pour tout Pour s' en convaincre , on peut considérer les sous-espaces vectoriels E1 R.(1 , 0 ) , E2 R.(0 , 1 ) et 1

**5092**: On en déduit que E1 et E2 sont en somme Soit E un K - espace vectoriel , soit ( Ei ) iI une famille de sous-espaces vectoriels de E , on dit qu' ils sont en somme directe , si on a écriture unique de 0E , soit : distincts 2 à 2 On écrit alors Ei à la place de Ne pas oublier que l' on ne sait ***faire*** que des sommes finies de vecteurs ! ! Si I contient strictement plus de deux éléments , la condition iI Ei 0E ne suffit pas pour assurer que les Ei sont en somme directe , de même que les conditions Ei Ej 0E pour tout Pour s' en convaincre , on peut considérer les sous-espaces vectoriels E1 R.(1 , 0 ) , E2 R.(0 , 1 ) et 1

**5119**: On en déduit que E1 et E2 sont en somme Soit E un K - espace vectoriel , soit ( Ei ) iI une famille de sous-espaces vectoriels de E , on dit qu' ils sont en somme directe , si on a écriture unique de 0E , soit : distincts 2 à 2 On écrit alors Ei à la place de Ne pas oublier que l' on ne sait faire que des sommes finies de vecteurs ! ! Si I contient strictement plus de deux éléments , la condition iI Ei 0E ne suffit pas pour ***assurer*** que les Ei sont en somme directe , de même que les conditions Ei Ej 0E pour tout Pour s' en convaincre , on peut considérer les sous-espaces vectoriels E1 R.(1 , 0 ) , E2 R.(0 , 1 ) et 1

**5141**: On en déduit que E1 et E2 sont en somme Soit E un K - espace vectoriel , soit ( Ei ) iI une famille de sous-espaces vectoriels de E , on dit qu' ils sont en somme directe , si on a écriture unique de 0E , soit : distincts 2 à 2 On écrit alors Ei à la place de Ne pas oublier que l' on ne sait faire que des sommes finies de vecteurs ! ! Si I contient strictement plus de deux éléments , la condition iI Ei 0E ne suffit pas pour assurer que les Ei sont en somme directe , de même que les conditions Ei Ej 0E pour tout Pour s' en ***convaincre*** , on peut considérer les sous-espaces vectoriels E1 R.(1 , 0 ) , E2 R.(0 , 1 ) et 1

**5145**: On en déduit que E1 et E2 sont en somme Soit E un K - espace vectoriel , soit ( Ei ) iI une famille de sous-espaces vectoriels de E , on dit qu' ils sont en somme directe , si on a écriture unique de 0E , soit : distincts 2 à 2 On écrit alors Ei à la place de Ne pas oublier que l' on ne sait faire que des sommes finies de vecteurs ! ! Si I contient strictement plus de deux éléments , la condition iI Ei 0E ne suffit pas pour assurer que les Ei sont en somme directe , de même que les conditions Ei Ej 0E pour tout Pour s' en convaincre , on peut ***considérer*** les sous-espaces vectoriels E1 R.(1 , 0 ) , E2 R.(0 , 1 ) et 1

**5239**: 1.4.1 Soit E C 0 ( R , R ) , ***démontrer*** que le sous-espace vectoriel des fonctions paires et celui des fonctions impaires sont en somme directe

**5288**: Quelle est leur somme ? 1.4.2 Soit E un K - espace vectoriel , soit E1 , E2 et E3 trois sous-espaces vectoriels de E. On suppose que ( a ) ***Démontrer*** que si E2 E3 , alors ( b ) Démontrer que le résultat devient faux lorsque E2 6 E3 et E1 6 E3

**5298**: Quelle est leur somme ? 1.4.2 Soit E un K - espace vectoriel , soit E1 , E2 et E3 trois sous-espaces vectoriels de E. On suppose que ( a ) Démontrer que si E2 E3 , alors ( b ) ***Démontrer*** que le résultat devient faux lorsque E2 6 E3 et E1 6 E3

**5340**: 1.4.3 Soit E un K - espace vectoriel , ( Ei ) iI et ( Ei0 ) iI deux familles de sous-espaces vectoriels de E , telles ***Démontrer*** que : 1.4.4 Soit E un K - espace vectoriel , soit E1 , E2 et E3 trois sous-espaces vectoriels de E. Démontrer que : Supplémentaires Soit E un K - espace vectoriel

**5363**: 1.4.3 Soit E un K - espace vectoriel , ( Ei ) iI et ( Ei0 ) iI deux familles de sous-espaces vectoriels de E , telles Démontrer que : 1.4.4 Soit E un K - espace vectoriel , soit E1 , E2 et E3 trois sous-espaces vectoriels de E. ***Démontrer*** que : Supplémentaires Soit E un K - espace vectoriel

**5597**: Deux sous-espaces vectoriels E1 et E2 de E sont supplémentaires dans E si , et seulement si : double inclusion Si E1 6 E et E 6 0E , il y a une infinité de supplémentaires de E1 ( cela peut ***être*** faux sur d' autres corps K que R ou C )

**5629**: 1.5.1 Dans R3 , ***trouver*** un supplémentaire du plan d' équation x y z 0

**5641**: ***Recommencer*** dans C3 ( en tant que C - espace vectoriel )

**5658**: 1.5.2 Dans R3 , ***trouver*** un supplémentaire de la droite d' équations : 1.5.3 Dans E C 0 ( R , R ) , trouver des supplémentaires de : Vect(x 7 x ) 1.5.4 Soit E C ( R , R ) , soit n N , trouver un supplémentaire de 1.5.5 On considère ici R comme un Q - espace vectoriel ( on a ici K Q )

**5678**: 1.5.2 Dans R3 , trouver un supplémentaire de la droite d' équations : 1.5.3 Dans E C 0 ( R , R ) , ***trouver*** des supplémentaires de : Vect(x 7 x ) 1.5.4 Soit E C ( R , R ) , soit n N , trouver un supplémentaire de 1.5.5 On considère ici R comme un Q - espace vectoriel ( on a ici K Q )

**5701**: 1.5.2 Dans R3 , trouver un supplémentaire de la droite d' équations : 1.5.3 Dans E C 0 ( R , R ) , trouver des supplémentaires de : Vect(x 7 x ) 1.5.4 Soit E C ( R , R ) , soit n N , ***trouver*** un supplémentaire de 1.5.5 On considère ici R comme un Q - espace vectoriel ( on a ici K Q )

**5918**: Proposition 1.2 Soit E un K - espace vectoriel et soit ( xi ) iI une famille de vecteurs de E. Il est équivalent de ***dire*** : 1

**5967**: autre formulation : a. Nous utiliserons parfois l' expression non tous nuls , pour ***parler*** de coefficients qui ne sont pas tous nuls

**6378**: Si il existe une écriture de 0E non trivial à ***partir*** des ( xi ) iJ , c' est encore une écriture de 0E non trivial à partir des vecteurs de X , car ( xi ) iJ est une sous-famille de X

**6395**: Si il existe une écriture de 0E non trivial à partir des ( xi ) iJ , c' est encore une écriture de 0E non trivial à ***partir*** des vecteurs de X , car ( xi ) iJ est une sous-famille de X

**6635**: Il est équivalent de ***dire*** : 1

**6747**: , en ) est une famille de vecteurs de E , ***démontrer*** que : ( a ) Dans tous les cas : 1.6.2 Dans R4 , on considère les sous-espaces vectoriels suivants : ( a ) Démontrer que ( c ) Exprimer les coordonnées d' un vecteur quelconque de R4 dans cette base

**6772**: , en ) est une famille de vecteurs de E , démontrer que : ( a ) Dans tous les cas : 1.6.2 Dans R4 , on considère les sous-espaces vectoriels suivants : ( a ) ***Démontrer*** que ( c ) Exprimer les coordonnées d' un vecteur quelconque de R4 dans cette base

**6777**: , en ) est une famille de vecteurs de E , démontrer que : ( a ) Dans tous les cas : 1.6.2 Dans R4 , on considère les sous-espaces vectoriels suivants : ( a ) Démontrer que ( c ) ***Exprimer*** les coordonnées d' un vecteur quelconque de R4 dans cette base

**6815**: 1.6.3 Dans R5 , on considère les vecteurs : F Vect(a , b , c ) et G Vect(d , e ) ( a ) ***Trouver*** des bases de F , G , F G et F G. ( b ) Trouver des équations de ces sous-espaces vectoriels

**6831**: 1.6.3 Dans R5 , on considère les vecteurs : F Vect(a , b , c ) et G Vect(d , e ) ( a ) Trouver des bases de F , G , F G et F G. ( b ) ***Trouver*** des équations de ces sous-espaces vectoriels

**6849**: 1.6.4 On considère dans R4 les cinq vecteurs suivants : ***Donner*** une équation du sous-espace vectoriel engendré par ces cinq vecteurs

**6882**: 1.6.5 Soit E F ( R , R ) et F le sous-espace vectoriel de E engendré par les fonctions : ***Déterminer*** une base de F

**6888**: ***Démontrer*** que : ( f ) R est une famille libre de F ( R , R ) 1.6.7 Soit A un ensemble , f une application de A dans R , telle que f ( A ) est infini

**6929**: ***Démontrer*** que la famille ( f ) R est libre dans F ( A , R )

**7007**: ***Démontrer*** que E est un R - espace vectoriel et en donner une base

**7018**: Démontrer que E est un R - espace vectoriel et en ***donner*** une base

**7023**: 1.6.9 ***Démontrer*** que dans Rn , il existe une famille infinie F de vecteurs tels que chaque sous famille de cardinal n est libre

**7190**: On peut ***échanger*** certains vecteurs de la famille génératrice avec des vecteurs de la famille libre tout en gardant la propriété d' être génératrice , soit : Démonstration Puisque ( g1 ,

**7210**: On peut échanger certains vecteurs de la famille génératrice avec des vecteurs de la famille libre tout en gardant la propriété d' ***être*** génératrice , soit : Démonstration Puisque ( g1 ,

**7261**: De plus , 1 6 0E ( car ( 1 ) est libre ) , on peut ***supposer*** que les coefficients ne sont pas tous nuls , par exemple le premier : avec 1 6 0

**7301**: Supposons qu' on ait formé une famille génératrice de la forme donc on peut ***écrire*** liées )

**7320**: Par le même argument qui ci - dessus , on a donc Il reste à ***démontrer*** que p n. Si p n , en prenant k n 1 dans la construction ci - dessus , on obtient que ( 1 ,

**7410**: On a donc p n. On peut aussi ***énoncer*** ce résultat avec une famille génératrice de cardinal quelconque ( peut-être infini ) , où l' on pourra échanger p vecteurs de cette famille tout en la gardant génératrice

**7429**: On a donc p n. On peut aussi énoncer ce résultat avec une famille génératrice de cardinal quelconque ( peut-être infini ) , où l' on pourra ***échanger*** p vecteurs de cette famille tout en la gardant génératrice

**7493**: Ce cardinal commun est appelé dimension de E et est notée a : dimK E ou dim E si il ne y a pas ambiguïté sur le corps K a. On ***utiliser*** aussi parfois la notation dim(E ) ou dimK ( E )

**7714**: On peut ***compléter*** la famille libre en une base , soit : Démonstration C' est une application immédiate du théorème de l' échange , en prenant comme famille génératrice une base de E ( qui a n éléments )

**7766**: Si on veut ***trouver*** une base d' un K - espace vectoriel E de dimension finie , on procède par itération : 1

**7952**: Pour cela , il suffit d' ***imposer*** z t 0 et ( x , y ) 6 ( 0 , 0 ) , car Par exemple , on peut prendre : Remarquons que nous avons utilisé une partie génératrice bien connue : la base canonique de R4

**7975**: Pour cela , il suffit d' imposer z t 0 et ( x , y ) 6 ( 0 , 0 ) , car Par exemple , on peut ***prendre*** : Remarquons que nous avons utilisé une partie génératrice bien connue : la base canonique de R4

**8085**: Si une famille de plus de n 1 éléments est libre , on pourrait la ***compléter*** en une base qui contiendrait au moins n 1 éléments , ce qui contredit dim E n. 2

**8149**: On utilise le théorème de l' échange pour ***extraire*** une base B G de E ( en partant d' une une sous-famille libre de G )

**8213**: On utilise le théorème de la base incomplète pour ***obtenir*** une base L0 L de E. Mais L0 a n dim E élément car c' est une base , donc on a L L0 , c' est donc une base

**8281**: Démonstration Si E 0E , il ne y a rien à ***démontrer***

**8323**: Tous les vecteurs ( en nombre fini ) de B peuvent s' ***écrire*** comme une combinaison linéaire d' éléments de G donc E est en fait engendré par une sous-famille finie G 0 de G. Comme E 6 0E , G 0 contient un vecteur x 6 0E

**8369**: Le théorème de la base incomplète permet alors de ***construire*** une base de E en complétant la famille ( x ) par des éléments de G. Soit E un K - espace vectoriel

**8480**: Alors E est de dimension infinie si , et seulement si , il existe des parties libres de cardinal quelconque n N. Démonstration Cela revient à ***démontrer*** que E est de dimension finie si , et seulement si , il existe n N tel que toute famille de E à n éléments soit liée

**8511**: On peut ***prendre*** n dim E 1

**8569**: Si E est de dimension finie , alors tout sous-espace vectoriel F de E est de dimension finie et , de plus : dim F dim E E F dim E dim F Démonstration Si F 0E , il ne y a rien à ***démontrer***

**8585**: Notons p le nombre maximal d' éléments que peut ***avoir*** une famille libre L de F

**8740**: La proposition précédente est très pratique pour ***démontrer*** l' égalité de deux espaces vectoriels : au lieu de démontrer le résultat par double inclusion , on peut se limiter à démontrer une inclusion et conclure par une égalité de dimension

**8751**: La proposition précédente est très pratique pour démontrer l' égalité de deux espaces vectoriels : au lieu de ***démontrer*** le résultat par double inclusion , on peut se limiter à démontrer une inclusion et conclure par une égalité de dimension

**8761**: La proposition précédente est très pratique pour démontrer l' égalité de deux espaces vectoriels : au lieu de démontrer le résultat par double inclusion , on peut se ***limiter*** à démontrer une inclusion et conclure par une égalité de dimension

**8763**: La proposition précédente est très pratique pour démontrer l' égalité de deux espaces vectoriels : au lieu de démontrer le résultat par double inclusion , on peut se limiter à ***démontrer*** une inclusion et conclure par une égalité de dimension

**8767**: La proposition précédente est très pratique pour démontrer l' égalité de deux espaces vectoriels : au lieu de démontrer le résultat par double inclusion , on peut se limiter à démontrer une inclusion et ***conclure*** par une égalité de dimension

**8864**: Base adaptée à une somme directe de deux sous-espaces vectoriels On suppose que E F G , on peut alors ***construire*** une base ( e1 ,

**8917**: Base adaptée à une somme directe finie De même , lorsque l' on a une décomposition en somme directe de E , on peut toujours ***construire*** une base adaptée à cette somme directe

**9208**: Dans le cas général , on procède par récurrence sur p. Proposition 1.3 Formule de Grassman Si E est un K - espace vectoriel de dimension finie , si F et G sont deux sous-espaces vectoriels de E , alors : Démonstration Soit F1 un supplémentaire de F G dans F et soit G1 un supplémentaire de F G dans G : On a alors Pour ***conclure*** , il suffit de prendre une base adaptée à cette décomposition en somme directe

**9213**: Dans le cas général , on procède par récurrence sur p. Proposition 1.3 Formule de Grassman Si E est un K - espace vectoriel de dimension finie , si F et G sont deux sous-espaces vectoriels de E , alors : Démonstration Soit F1 un supplémentaire de F G dans F et soit G1 un supplémentaire de F G dans G : On a alors Pour conclure , il suffit de ***prendre*** une base adaptée à cette décomposition en somme directe

**9349**: C' est une famille libre de E qu' on peut ***compléter*** en une base ( e1 ,

**9379**: , en ) de E. Alors d' après ce qui précède , ***Démontrer*** que F1 F2

**9434**: Soit G un sous-espace vectoriel de E tel que : ***Démontrer*** que F2 G. 1.7.4 Soit E un K - espace vectoriel de dimension finie , soit F et G deux sous-espaces vectoriels de E tels que F G 0E

**9465**: ***Démontrer*** qu' il existe un supplémentaire de F contenant G. 1.7.5 Soit E un K - espace vectoriel de dimension finie et F un sous-espace vectoriel strict de E ( F 6 E )

**9500**: ***Démontrer*** que F admet une infinité de supplémentaires

**9540**: , Vk des sous-espaces vectoriels de V tels que ***Démontrer*** que 1.7.7 Soit E un K - espace vectoriel de dimension finie n , soit F1 et F2 deux sous-espaces vectoriels de dimension p n. ( a ) Démontrer que l' on peut alors trouver un supplémentaire commun à F1 et F2

**9569**: , Vk des sous-espaces vectoriels de V tels que Démontrer que 1.7.7 Soit E un K - espace vectoriel de dimension finie n , soit F1 et F2 deux sous-espaces vectoriels de dimension p n. ( a ) ***Démontrer*** que l' on peut alors trouver un supplémentaire commun à F1 et F2

**9575**: , Vk des sous-espaces vectoriels de V tels que Démontrer que 1.7.7 Soit E un K - espace vectoriel de dimension finie n , soit F1 et F2 deux sous-espaces vectoriels de dimension p n. ( a ) Démontrer que l' on peut alors ***trouver*** un supplémentaire commun à F1 et F2

**9587**: ( b ) ***Généraliser*** lorsque le corps est R à un nombre fini de sous-espaces vectoriels de dimension p. ( c ) Puis , à une infinité dénombrable de tels sous-espaces vectoriels

**10190**: Si F est un sous-espace vectoriel de E , alors : f ( F ) f ( x ) , x F est un sous-espace vectoriel de E 0 De même , si F 0 est un sous-espace vectoriel de E 0 , alors : f 1 ( F 0 ) x E , f ( x ) F 0 est un sous-espace vectoriel de E Démonstration On a vu ( ***voir*** la remarque 1.17 , de la présente page ) que 0E 0 f ( 0E ) f ( F ) ( avec 0E F )

**10340**: On peut donc ***définir*** pour un endomorphisme f de E , la notion d' itéré de la manière suivante : On a alors les formules suivantes , si f et g sont deux endomorphismes de E tels que f g g f : ( a ) ( Formule du binôme ) : ( b ) ( Identité remarquable ) : 3

**10440**: Si f est un automorphisme de E , alors f 1 est aussi un automorphisme de E ( en particulier c' est un endomorphisme de E ) et on définit de même : 1.8.1 Soit f un endomorphisme de E , ***calculer*** 1.8.2 Soit f L ( E ) tel qu' il existe n N tel que f n 0L ( E ) ( on dit que f est nilpotent )

**10471**: ***Démontrer*** que idE f est inversible

**10574**: On peut ***utiliser*** les images et noyaux pour démontrer que des ensembles sont des sous-espaces vectoriels : ( a ) ( Image peu fréquent ) : est un sous-espace vectoriel de C 0 ( a , b , R ) en considérant l' endomorphisme de C 0 ( a , b , R ) : ( b ) ( Noyau très fréquent ) : est un sous-espace vectoriel de C 1 ( a , b , R ) en considérant la forme linéaire de C 1 ( a , b , R ) : Proposition 1.4 Soit E et E 0 deux K - espaces vectoriels , f L ( E , E 0 ) , alors : f est injective si , et seulement si , Ker(f ) 0E f est surjective si , et seulement si , Im(f ) E 0 Démonstration La caractérisation de la surjectivité est immédiate

**10580**: On peut utiliser les images et noyaux pour ***démontrer*** que des ensembles sont des sous-espaces vectoriels : ( a ) ( Image peu fréquent ) : est un sous-espace vectoriel de C 0 ( a , b , R ) en considérant l' endomorphisme de C 0 ( a , b , R ) : ( b ) ( Noyau très fréquent ) : est un sous-espace vectoriel de C 1 ( a , b , R ) en considérant la forme linéaire de C 1 ( a , b , R ) : Proposition 1.4 Soit E et E 0 deux K - espaces vectoriels , f L ( E , E 0 ) , alors : f est injective si , et seulement si , Ker(f ) 0E f est surjective si , et seulement si , Im(f ) E 0 Démonstration La caractérisation de la surjectivité est immédiate

**10754**: Pour l' injectivité , on utilise le fait que : Si E est un K - espace vectoriel et ( ei ) iI une base de E , alors pour ***connaître*** une application linéaire f L ( E , E 0 ) , il faut et il suffit de connaître la famille des images ( f ( ei ) ) iI

**10773**: Pour l' injectivité , on utilise le fait que : Si E est un K - espace vectoriel et ( ei ) iI une base de E , alors pour connaître une application linéaire f L ( E , E 0 ) , il faut et il suffit de ***connaître*** la famille des images ( f ( ei ) ) iI

**10798**: Plus formellement : est un isomorphisme C' est pourquoi il suffit de ***donner*** uniquement les images des vecteurs d' une base pour décrire une application linéaire

**10808**: Plus formellement : est un isomorphisme C' est pourquoi il suffit de donner uniquement les images des vecteurs d' une base pour ***décrire*** une application linéaire

**11111**: On applique les points 1 et 2 pour ***démontrer*** que ( f ( xi ) ) iI est à la fois libre et génératrice

**11377**: On a : Démonstration Soit f et g deux endomorphismes d' un K - espace vectoriel E. Si f g g f , alors : Démonstration Si f est un endomorphisme d' un K - espace vectoriel E , alors : Démonstration On utilise les deux premiers points de la propriété 1.26 , de la présente page avec f n à la place de f et f à la place de g. Soit E un K - espace vectoriel et f L ( E ) , soit F un sous-espace vectoriel de E , on dit que F est f -stable ou stable par f si : f ( F ) F , c' est - à - ***dire*** que , pour tout x F , f ( x ) F 1

**11456**: Si f est un automorphisme et F de dimension finie , alors F est stable par f F est stable par f 1 1.9.1 Soit f , g et h trois endomorphismes d' un K - espace vectoriel E tels que : ***Démontrer*** que ces trois endomorphismes ont même image et même noyau

**11481**: 1.9.2 Soit f un endomorphisme d' un K - espace vectoriel E , ***démontrer*** que : 1.9.3 Soit f et g deux endomorphismes d' un K - espace vectoriel E , démontrer que : Projecteurs et symétries Soit E un K - espace vectoriel , F et G deux sous-espaces vectoriels de E tels que E F G. On appelle projection de E sur F parallèlement à G l' endomorphisme de E défini par : x 7 xF où x xF xG avec xF F et xG G Puisque E F G , xF et xG sont uniques donc pF kG est bien définie

**11499**: 1.9.2 Soit f un endomorphisme d' un K - espace vectoriel E , démontrer que : 1.9.3 Soit f et g deux endomorphismes d' un K - espace vectoriel E , ***démontrer*** que : Projecteurs et symétries Soit E un K - espace vectoriel , F et G deux sous-espaces vectoriels de E tels que E F G. On appelle projection de E sur F parallèlement à G l' endomorphisme de E défini par : x 7 xF où x xF xG avec xF F et xG G Puisque E F G , xF et xG sont uniques donc pF kG est bien définie

**11919**: Si p est un projecteur , on a alors : E Im p Ker p d' après l' exemple 1.18 , page 49 , donc p est la projection de E sur son image Im p parallèlement à son noyau Ker p. Soit E un K - espace vectoriel , F et G deux sous-espaces vectoriels de E tels que E F G. On peut ***définir*** de même la notion de symétrie de E par rapport à F , parallèlement à G. C' est l' automorphisme de E défini x xF xG 7 xF xG , où x xF xG avec xF F et xG G Soit E un K - espace vectoriel , F et G deux sous-espaces vectoriels de E tels que E F G. On a alors : sF kG sF kG idE De plus , on a sF kG 2.pF kG idE et pF kG

**12033**: On peut ***définir*** plus généralement la notion de symétrie de E , ce sont les endomorphismes s de E tels que s s idE

**12059**: On peut alors ***démontrer*** ( à l' aide de la propriété 1.30 , de la présente page ) que si sF kG est la symétrie de E par rapport à F , parallèlement à G , alors sF kG sF kG idE

**12223**: ***Démontrer*** que p

**12231**: ***Démontrer*** que est une projection ( sur quoi ? parallèlement à quoi ? )

**12251**: 1.10.3 Soit l' application : ***Démontrer*** que est une symétrie ( par rapport à quoi ? parallèlement à quoi ? )

**12282**: 1.10.4 Soit p et q deux projecteurs d' un K - espace vectoriel E. ***Démontrer*** l' équivalence des trois propriétés suivantes : ( a ) p q est un projecteur

**12325**: 1.10.5 Si p et q sont deux projecteurs d' un K - espace vectoriel E tels que p q q p 0L ( E ) , ***démontrer*** que p q est un projecteur et en calculer son image et son noyau

**12334**: 1.10.5 Si p et q sont deux projecteurs d' un K - espace vectoriel E tels que p q q p 0L ( E ) , démontrer que p q est un projecteur et en ***calculer*** son image et son noyau

**12365**: 1.10.6 Si p et q sont deux projecteurs d' un K - espace vectoriel E tels que p q 0L ( E ) , ***démontrer*** que p q q p est un projecteur et en calculer son image et son noyau

**12376**: 1.10.6 Si p et q sont deux projecteurs d' un K - espace vectoriel E tels que p q 0L ( E ) , démontrer que p q q p est un projecteur et en ***calculer*** son image et son noyau

**12402**: 1.10.7 Soit f un endomorphisme d' un K - espace vectoriel E et p un projecteur de E , ***démontrer*** que : Cas particulier de la dimension finie Soit E et E 0 deux K - espaces vectoriels

**12880**: Démonstration Si n p , on peut ***définir*** l' application linéaire f L ( E , E 0 ) telle que f ( ei ) e0i pour tout i 1 , n. elle est donc libre , ce qui démontre que f est injective ( voir la remarque 1.19 , page 51 )

**12918**: Démonstration Si n p , on peut définir l' application linéaire f L ( E , E 0 ) telle que f ( ei ) e0i pour tout i 1 , n. elle est donc libre , ce qui démontre que f est injective ( ***voir*** la remarque 1.19 , page 51 )

**12981**: , f ( en ) ) est une famille libre à n éléments dans un espace de dimension p , donc n p. Si n p , on peut ***définir*** l' application linéaire f L ( E , E 0 ) telle que f ( ei ) e0i pour tout i 1 , p et E 0 , donc est génératrice

**13075**: , f ( en ) ) est une famille génératrice à n éléments dans un espace de dimension p , donc n p. Si n p , on peut ***définir*** l' application linéaire f L ( E , E 0 ) telle que f ( ei ) e0i pour tout i 1 , n 1 , p. D' après ce qui précède , f est injective et surjective donc bijective

**13151**: Réciproquement , si il existe f L ( E , E 0 ) bijective , alors d' après ce qui précède n p et p n , donc Ces propriétés sont très importantes pour ***démontrer*** des égalités ou des inégalités de dimensions ! Proposition 1.6 Rang d' une composition Soit E , E 0 et E 00 trois K - espaces vectoriels de dimensions finies , u L ( E , E 0 ) et v L ( E 0 , E 00 ) , alors : rang(v u ) dim E 0 rang(v ) rang(u ) Démonstration On peut déjà remarquer que : donc , en introduisant des supplémentaires : l' inégalité demandée devient : Or , il existe une application naturelle qui va de F 0 dans F 00 , l' application : L' énoncé devient : La démonstration ne est alors qu' une vérification : soit x00 F 00 , alors x00 Im(v ) , donc , il existe Théorème 1.4 Théorème du rang Soit E et E 0 des K - espace vectoriels et f L ( E , E 0 )

**13218**: Réciproquement , si il existe f L ( E , E 0 ) bijective , alors d' après ce qui précède n p et p n , donc Ces propriétés sont très importantes pour démontrer des égalités ou des inégalités de dimensions ! Proposition 1.6 Rang d' une composition Soit E , E 0 et E 00 trois K - espaces vectoriels de dimensions finies , u L ( E , E 0 ) et v L ( E 0 , E 00 ) , alors : rang(v u ) dim E 0 rang(v ) rang(u ) Démonstration On peut déjà ***remarquer*** que : donc , en introduisant des supplémentaires : l' inégalité demandée devient : Or , il existe une application naturelle qui va de F 0 dans F 00 , l' application : L' énoncé devient : La démonstration ne est alors qu' une vérification : soit x00 F 00 , alors x00 Im(v ) , donc , il existe Théorème 1.4 Théorème du rang Soit E et E 0 des K - espace vectoriels et f L ( E , E 0 )

**13422**: Soit E un K - espace vectoriel de dimension finie et f L ( E ) , alors : ( a ) En posant f 0 idE , on a : ( b ) De plus , ( c ) On peut alors ***poser*** : Proposition 1.7 Caractérisation des automorphismes en dimension finie Soit E un K - espace vectoriel de dimension finie et f L ( E ) , alors : f injective f surjective f bijective C' est faux en dimension infinie

**13479**: On peut ***remarquer*** que le résultat est encore vrai lorsque f L ( E , E 0 ) et dim E dim E 0

**13510**: En dimension infinie , on peut ***considérer*** , par exemple , la dérivation sur C ( R , R ) qui est surjective , mais pas injective ! Proposition 1.8 Soit E et E 0 deux K - espaces vectoriels de dimensions finies , alors L ( E E 0 ) est de dimension finie , égale à dim E dim E 0 Démonstration Si E 0E ou E 0 0E 0 , il ne y a rien à démontrer

**13583**: En dimension infinie , on peut considérer , par exemple , la dérivation sur C ( R , R ) qui est surjective , mais pas injective ! Proposition 1.8 Soit E et E 0 deux K - espaces vectoriels de dimensions finies , alors L ( E E 0 ) est de dimension finie , égale à dim E dim E 0 Démonstration Si E 0E ou E 0 0E 0 , il ne y a rien à ***démontrer***

**13629**: e0n ) une base de E 0 , il suffit de ***vérifier*** alors que : où si ( k , l ) 1 , n 1 , p , uk , l est définie par a : a. On rappelle la définition du symbole de Kronecker : On voit donc que si E et E 0 sont de dimensions finies , alors L ( E E 0 ) et L ( E 0 E ) sont isomorphes car ils ont même dimension ! Nous verrons que c' est faux en dimension infinie ! Il y a en fait deux sortes d' isomorphismes : 1

**13732**: Des isomorphismes géométriques : c' est - à - ***dire*** vrais sans propriétés de dimensions

**13751**: Des isomorphismes non géométriques : c' est - à - ***dire*** qu' ils ne traduisent qu' une égalité de dimensions

**13791**: ***Démontrer*** ( a ) Pour toute L ( E 0 , E ) surjective , rang(f ) rang f

**13855**: 1.11.3 Soit E un K - espace vectoriel de dimension n et f L ( E ) tel que : ( a ) ***Démontrer*** que : ( b ) Démontrer que , si f n1 6 0L ( E ) , alors 1.11.4 Soit E un K - espace vectoriel de dimension finie et f L ( E ) , démontrer qu' il existe un automorphisme g GL ( E ) et p un projecteur de E tel que : 1.11.5 Soit E un K - espace vectoriel de dimension finie et f L ( E ) , on considère les applications : ( a ) Démontrer que et sont dans L ( L ( E ) )

**13861**: 1.11.3 Soit E un K - espace vectoriel de dimension n et f L ( E ) tel que : ( a ) Démontrer que : ( b ) ***Démontrer*** que , si f n1 6 0L ( E ) , alors 1.11.4 Soit E un K - espace vectoriel de dimension finie et f L ( E ) , démontrer qu' il existe un automorphisme g GL ( E ) et p un projecteur de E tel que : 1.11.5 Soit E un K - espace vectoriel de dimension finie et f L ( E ) , on considère les applications : ( a ) Démontrer que et sont dans L ( L ( E ) )

**13892**: 1.11.3 Soit E un K - espace vectoriel de dimension n et f L ( E ) tel que : ( a ) Démontrer que : ( b ) Démontrer que , si f n1 6 0L ( E ) , alors 1.11.4 Soit E un K - espace vectoriel de dimension finie et f L ( E ) , ***démontrer*** qu' il existe un automorphisme g GL ( E ) et p un projecteur de E tel que : 1.11.5 Soit E un K - espace vectoriel de dimension finie et f L ( E ) , on considère les applications : ( a ) Démontrer que et sont dans L ( L ( E ) )

**13938**: 1.11.3 Soit E un K - espace vectoriel de dimension n et f L ( E ) tel que : ( a ) Démontrer que : ( b ) Démontrer que , si f n1 6 0L ( E ) , alors 1.11.4 Soit E un K - espace vectoriel de dimension finie et f L ( E ) , démontrer qu' il existe un automorphisme g GL ( E ) et p un projecteur de E tel que : 1.11.5 Soit E un K - espace vectoriel de dimension finie et f L ( E ) , on considère les applications : ( a ) ***Démontrer*** que et sont dans L ( L ( E ) )

**13954**: ( b ) ***Calculer*** rang ( ) et rang ( )

**13983**: On considère ( a ) ***Démontrer*** que F est non vide

**13997**: ( b ) Soit v0 F , ***démontrer*** que v0 F v v0 , v F est un sous-espace vectoriel de L ( E ) On suppose dorénavant que E est de dimension finie n. ( c ) Calculer la dimension de v0 F. ( d ) Que peut -on dire du rang de v lorsque v F ? 1.11.7 Soit E un K - espace vectoriel de dimension finie et f L ( E ) , démontrer que : rang f k rang f k2 1.11.8 Soit E un K - espace vectoriel de dimension finie et f L ( E ) , démontrer que : 1.11.9 Soit E , E 0 , E 00 et E 000 quatre K - espaces vectoriels de dimensions finies , f L ( E , E 0 ) , g L ( E 0 , E 00 ) 1.11.10 Soit E un K - espace vectoriel de dimension finie , f L ( E ) GL ( E )

**14028**: ( b ) Soit v0 F , démontrer que v0 F v v0 , v F est un sous-espace vectoriel de L ( E ) On suppose dorénavant que E est de dimension finie n. ( c ) ***Calculer*** la dimension de v0 F. ( d ) Que peut -on dire du rang de v lorsque v F ? 1.11.7 Soit E un K - espace vectoriel de dimension finie et f L ( E ) , démontrer que : rang f k rang f k2 1.11.8 Soit E un K - espace vectoriel de dimension finie et f L ( E ) , démontrer que : 1.11.9 Soit E , E 0 , E 00 et E 000 quatre K - espaces vectoriels de dimensions finies , f L ( E , E 0 ) , g L ( E 0 , E 00 ) 1.11.10 Soit E un K - espace vectoriel de dimension finie , f L ( E ) GL ( E )

**14040**: ( b ) Soit v0 F , démontrer que v0 F v v0 , v F est un sous-espace vectoriel de L ( E ) On suppose dorénavant que E est de dimension finie n. ( c ) Calculer la dimension de v0 F. ( d ) Que peut -on ***dire*** du rang de v lorsque v F ? 1.11.7 Soit E un K - espace vectoriel de dimension finie et f L ( E ) , démontrer que : rang f k rang f k2 1.11.8 Soit E un K - espace vectoriel de dimension finie et f L ( E ) , démontrer que : 1.11.9 Soit E , E 0 , E 00 et E 000 quatre K - espaces vectoriels de dimensions finies , f L ( E , E 0 ) , g L ( E 0 , E 00 ) 1.11.10 Soit E un K - espace vectoriel de dimension finie , f L ( E ) GL ( E )

**14067**: ( b ) Soit v0 F , démontrer que v0 F v v0 , v F est un sous-espace vectoriel de L ( E ) On suppose dorénavant que E est de dimension finie n. ( c ) Calculer la dimension de v0 F. ( d ) Que peut -on dire du rang de v lorsque v F ? 1.11.7 Soit E un K - espace vectoriel de dimension finie et f L ( E ) , ***démontrer*** que : rang f k rang f k2 1.11.8 Soit E un K - espace vectoriel de dimension finie et f L ( E ) , démontrer que : 1.11.9 Soit E , E 0 , E 00 et E 000 quatre K - espaces vectoriels de dimensions finies , f L ( E , E 0 ) , g L ( E 0 , E 00 ) 1.11.10 Soit E un K - espace vectoriel de dimension finie , f L ( E ) GL ( E )

**14094**: ( b ) Soit v0 F , démontrer que v0 F v v0 , v F est un sous-espace vectoriel de L ( E ) On suppose dorénavant que E est de dimension finie n. ( c ) Calculer la dimension de v0 F. ( d ) Que peut -on dire du rang de v lorsque v F ? 1.11.7 Soit E un K - espace vectoriel de dimension finie et f L ( E ) , démontrer que : rang f k rang f k2 1.11.8 Soit E un K - espace vectoriel de dimension finie et f L ( E ) , ***démontrer*** que : 1.11.9 Soit E , E 0 , E 00 et E 000 quatre K - espaces vectoriels de dimensions finies , f L ( E , E 0 ) , g L ( E 0 , E 00 ) 1.11.10 Soit E un K - espace vectoriel de dimension finie , f L ( E ) GL ( E )

**14161**: ( a ) ***Démontrer*** que : Démontrer que c' est un K - espace vectoriel et en calculer sa dimension

**14164**: ( a ) Démontrer que : ***Démontrer*** que c' est un K - espace vectoriel et en calculer sa dimension

**14175**: ( a ) Démontrer que : Démontrer que c' est un K - espace vectoriel et en ***calculer*** sa dimension

**14494**: Notation 1.2 Inclusion canonique Soit E un K - espace vectoriel , F un sous-espace vectoriel de E , on peut ***définir*** l' inclusion canonique de F dans E par : On a donc : iF E ( idE ) F Si G est un supplémentaire de F dans E ( E F G ) , on a : iF E idF Ce ne sont pas des réciproques ! Pour connaître une application linéaire définie sur un K - espace vectoriel dont on connaît une décomposition en somme directe , il faut et il suffit d' en connaître ses restrictions à chaque sous-espace vectoriel composant la décomposition

**14543**: Notation 1.2 Inclusion canonique Soit E un K - espace vectoriel , F un sous-espace vectoriel de E , on peut définir l' inclusion canonique de F dans E par : On a donc : iF E ( idE ) F Si G est un supplémentaire de F dans E ( E F G ) , on a : iF E idF Ce ne sont pas des réciproques ! Pour ***connaître*** une application linéaire définie sur un K - espace vectoriel dont on connaît une décomposition en somme directe , il faut et il suffit d' en connaître ses restrictions à chaque sous-espace vectoriel composant la décomposition

**14570**: Notation 1.2 Inclusion canonique Soit E un K - espace vectoriel , F un sous-espace vectoriel de E , on peut définir l' inclusion canonique de F dans E par : On a donc : iF E ( idE ) F Si G est un supplémentaire de F dans E ( E F G ) , on a : iF E idF Ce ne sont pas des réciproques ! Pour connaître une application linéaire définie sur un K - espace vectoriel dont on connaît une décomposition en somme directe , il faut et il suffit d' en ***connaître*** ses restrictions à chaque sous-espace vectoriel composant la décomposition

**14603**: Supposons connue f L ( E , E 0 ) , il est alors facile de ***connaître*** : 2

**14668**: , in ) de I et des vecteurs xik Eik , quelque soit k 1 , n tels que : On a alors : Une autre façon de ***dire*** est que : Ei L ( E , E 0 ) est isomorphe à grâce à l' application ( clairement linéaire ) : Soit E F G , alors il existe un endomorphisme f L ( E ) , tel que On construit a : a. Remarquons que l' on obtient bien sûr la projection sur G parallèlement à F

**14975**: On a donc obtenu une factorisation de f à l' aide d' applications linéaires simples et d' un isomorphisme : f iIm(f ) E0 fe pF kKer(f ) Figure 1.3 Factorisation d' une application linéaire À quoi cela sert -il ? À ***faire*** apparaître un isomorphisme , ce qui permet d' utiliser sa réciproque ! Ainsi , sur le schéma précédent , il apparaît une application linéaire naturelle permettant d' aller de E 0 dans E ( sans pour autant que f soit inversible ) , en introduisant un supplémentaire F 0 de Im(f ) dans E 0

**14976**: On a donc obtenu une factorisation de f à l' aide d' applications linéaires simples et d' un isomorphisme : f iIm(f ) E0 fe pF kKer(f ) Figure 1.3 Factorisation d' une application linéaire À quoi cela sert -il ? À faire ***apparaître*** un isomorphisme , ce qui permet d' utiliser sa réciproque ! Ainsi , sur le schéma précédent , il apparaît une application linéaire naturelle permettant d' aller de E 0 dans E ( sans pour autant que f soit inversible ) , en introduisant un supplémentaire F 0 de Im(f ) dans E 0

**14984**: On a donc obtenu une factorisation de f à l' aide d' applications linéaires simples et d' un isomorphisme : f iIm(f ) E0 fe pF kKer(f ) Figure 1.3 Factorisation d' une application linéaire À quoi cela sert -il ? À faire apparaître un isomorphisme , ce qui permet d' ***utiliser*** sa réciproque ! Ainsi , sur le schéma précédent , il apparaît une application linéaire naturelle permettant d' aller de E 0 dans E ( sans pour autant que f soit inversible ) , en introduisant un supplémentaire F 0 de Im(f ) dans E 0

**15003**: On a donc obtenu une factorisation de f à l' aide d' applications linéaires simples et d' un isomorphisme : f iIm(f ) E0 fe pF kKer(f ) Figure 1.3 Factorisation d' une application linéaire À quoi cela sert -il ? À faire apparaître un isomorphisme , ce qui permet d' utiliser sa réciproque ! Ainsi , sur le schéma précédent , il apparaît une application linéaire naturelle permettant d' ***aller*** de E 0 dans E ( sans pour autant que f soit inversible ) , en introduisant un supplémentaire F 0 de Im(f ) dans E 0

**15032**: ***Voir*** le diagramme 1.4 , page suivante

**15200**: Quand on aura besoin de ***construire*** une application linéaire allant d' un K - espace vectoriel E à un K - espace vectoriel E 0 , on pourra essayer d' utiliser des chemins naturels allant de E à E 0

**15223**: Quand on aura besoin de construire une application linéaire allant d' un K - espace vectoriel E à un K - espace vectoriel E 0 , on pourra ***essayer*** d' utiliser des chemins naturels allant de E à E 0

**15225**: Quand on aura besoin de construire une application linéaire allant d' un K - espace vectoriel E à un K - espace vectoriel E 0 , on pourra essayer d' ***utiliser*** des chemins naturels allant de E à E 0

**15253**: Quand le problème est simple lorsqu' une application linéaire est bijective , on peut toujours ***essayer*** de se ramener à cette situation avec le théorème de factorisation

**15256**: Quand le problème est simple lorsqu' une application linéaire est bijective , on peut toujours essayer de se ***ramener*** à cette situation avec le théorème de factorisation

**15334**: ( Analyse ) En utilisant le théorème de factorisation , on peut ***construire*** un chemin naturel allant de E à E 0 ( en passant par E 00 )

**15352**: ***Voir*** le diagramme 1.6 , page suivante

**15379**: On obtient un candidat au rôle de u. Il s' écrit : ( Synthèse ) Il suffit alors de ***vérifier*** qu' il convient a , si x E , alors : or w(x ) Im(v ) par hypothèse 2

**15429**: ) Si v est inversible , alors u v 1 w. Dans le cas contraire , nous allons essayer de nous y ***ramener*** : ( Analyse ) Si u existe , alors b w v u donc w Pour pouvoir restreindre v à F 0 ( supplémentaire de Ker(v ) ) , nous allons imposer une condition supplémentaire à u permettant la co-restriction à F 0 de u : e inversible ! donc , dans ce cas , on a la condition nécessaire : ( Synthèse ) Soit u L ( E , E 0 ) défini par : ou , si l' on préfère : Alors , si x E , on a Le candidat ne est parfois pas celui dont on a besoin ! La vérification est indispensable ! b. La co-restriction est possible d' après l' hypothèse

**15446**: ) Si v est inversible , alors u v 1 w. Dans le cas contraire , nous allons essayer de nous y ramener : ( Analyse ) Si u existe , alors b w v u donc w Pour ***pouvoir*** restreindre v à F 0 ( supplémentaire de Ker(v ) ) , nous allons imposer une condition supplémentaire à u permettant la co-restriction à F 0 de u : e inversible ! donc , dans ce cas , on a la condition nécessaire : ( Synthèse ) Soit u L ( E , E 0 ) défini par : ou , si l' on préfère : Alors , si x E , on a Le candidat ne est parfois pas celui dont on a besoin ! La vérification est indispensable ! b. La co-restriction est possible d' après l' hypothèse

**15447**: ) Si v est inversible , alors u v 1 w. Dans le cas contraire , nous allons essayer de nous y ramener : ( Analyse ) Si u existe , alors b w v u donc w Pour pouvoir ***restreindre*** v à F 0 ( supplémentaire de Ker(v ) ) , nous allons imposer une condition supplémentaire à u permettant la co-restriction à F 0 de u : e inversible ! donc , dans ce cas , on a la condition nécessaire : ( Synthèse ) Soit u L ( E , E 0 ) défini par : ou , si l' on préfère : Alors , si x E , on a Le candidat ne est parfois pas celui dont on a besoin ! La vérification est indispensable ! b. La co-restriction est possible d' après l' hypothèse

**15702**: 1.12.1 ***Démontrer*** le théorème d' extension linéaire

**15729**: 1.12.2 Soit E0 , E1 et E2 trois sous-espaces vectoriels d' un K - espace vectoriel E tels que : ***démontrer*** que E1 et E2 sont isomorphes

**15759**: 1.12.3 Soit E1 , E2 , E3 et E4 quatre sous-espaces vectoriels d' un K - espace vectoriel E tels que : ***démontrer*** que E3 et E4 sont isomorphes

**15791**: ( a ) ***Démontrer*** que ( b ) Donner une CNS pour que : ( c ) Donner une CNS pour que : 1.12.5 Soit E un K - espace vectoriel et soit f L ( E ) , démontrer que Étude du dual Soit E un K - espace vectoriel , on appelle dual de E et on note : Les éléments de E ? s' appellent des formes linéaires a

**15827**: ( a ) Démontrer que ( b ) Donner une CNS pour que : ( c ) Donner une CNS pour que : 1.12.5 Soit E un K - espace vectoriel et soit f L ( E ) , ***démontrer*** que Étude du dual Soit E un K - espace vectoriel , on appelle dual de E et on note : Les éléments de E ? s' appellent des formes linéaires a

**15990**: Démonstration Si E est de dimension finie , c' est un cas particulier de la proposition 1.8 , page 58 : Si E ne est pas de dimension finie , ***voir*** l' exemple ci-dessous

**16075**: E ? ne est pas dénombrable car : E ? isomorphe à ( donc en bijection avec ) QN par l' isomorphisme usuel : Or , QN ne est pas dénombrable ( ***voir*** le procédé diagonal de Cantor ) a

**16144**: a. Ceci est aussi un exemple où L ( E , E 0 ) ne est pas isomorphe à L ( E 0 , E ) Si ( ei ) iI est une base de E , on peut ***définir*** la famille duale associée ( e?i ) iI ( E ? ) I par : Cette notation est très dangereuse ! En effet , si l' on change un des vecteurs ei , alors on change tous les vecteurs e?i

**16629**: Comment ***démontrer*** qu' une famille de formes linéaires est une base ? En utilisant la base ante - duale ( si l' on est capable de la trouver )

**16655**: Comment démontrer qu' une famille de formes linéaires est une base ? En utilisant la base ante - duale ( si l' on est capable de la ***trouver*** )

**16660**: On veut ***étudier*** ( 1 ,

**16705**: , en ) , ( ou la famille que l' on imagine ***être*** la base ante - duale ) , c' est alors facile : soit ( 1 ,

**16737**: , n ) Kn des scalaires tels que : ( b ) ***Calculer*** sa base ante - duale

**16747**: ( a ) ***Calculer*** dim E. i. À quelle CNS la famille ( 1 ,

**16782**: Lorsque cette condition ne est pas vérifiée , ***exprimer*** 4 en fonction des trois autres

**16793**: En ***déduire*** une méthode de calcul approché d' une intégrale

**16818**: Lorsque la fonction f C ( a , b , R ) , ***évaluer*** l' erreur de méthode

**16825**: 1.13.3 ***Trouver*** les formes linéaires définies sur E C 0 ( R , R ) telles que : 1.13.4 Soit E un K - espace vectoriel de dimension finie , soit E1 , E2 , ... , Ep des sous-espaces vectoriels de E , donner une CNS pour que : Hyperplans Soit E un K - espace vectoriel , on appelle hyperplan de E , tout sous-espace vectoriel H tel que : L' écriture : s' appelle équation de l' hyperplan H. Il ne y a pas unicité de l' équation , car , si convient , alors , quelque soit K ,

**16868**: 1.13.3 Trouver les formes linéaires définies sur E C 0 ( R , R ) telles que : 1.13.4 Soit E un K - espace vectoriel de dimension finie , soit E1 , E2 , ... , Ep des sous-espaces vectoriels de E , ***donner*** une CNS pour que : Hyperplans Soit E un K - espace vectoriel , on appelle hyperplan de E , tout sous-espace vectoriel H tel que : L' écriture : s' appelle équation de l' hyperplan H. Il ne y a pas unicité de l' équation , car , si convient , alors , quelque soit K ,

**17179**: Proposition 1.12 Caractérisation des hyperplans Soit E un K - espace vectoriel , H un sous-espace vectoriel de E , alors : H hyperplan de E codim H 1 Démonstration ( ) Soit ( x ) 0 une équation de H , comme est non nulle , on peut ***trouver*** un vecteur a E , tel ( ) Si E H K.a , a E 0E , alors , on peut prendre comme forme linéaire associée à H : Si E est de dimension finie , les hyperplans de E sont les sous-espaces vectoriels de dimension dim E1

**17201**: Proposition 1.12 Caractérisation des hyperplans Soit E un K - espace vectoriel , H un sous-espace vectoriel de E , alors : H hyperplan de E codim H 1 Démonstration ( ) Soit ( x ) 0 une équation de H , comme est non nulle , on peut trouver un vecteur a E , tel ( ) Si E H K.a , a E 0E , alors , on peut ***prendre*** comme forme linéaire associée à H : Si E est de dimension finie , les hyperplans de E sont les sous-espaces vectoriels de dimension dim E1

**17311**: Dans C 0 ( R , R ) , un supplémentaire de la droite engendrée par x 7 x , pourrait ***être*** donné par une équation du type : Théorème 1.8 Faisceaux d' hyperplans Soit E un K - espace vectoriel , soit n N , soit ( 1 ,

**17411**: Alors : Il suffit de le ***vérifier*** pour x h .a , où h Ker ( ) et K. ( Hérédité ) : supposons le résultat vrai au rang p 1 , soit ( 1 ,

**17483**: On a on peut donc ***appliquer*** l' hypothèse de récurrence qui nous donne : On a alors : donc , d' après l' initialisation : Dans R3 , les hyperplans sont des plans et on a la situation géométrique de la figure 1.7 , de la présente page

**17769**: On va chercher le plan demandé sous la forme : Pour ***trouver*** , il suffit d' écrire d((1 , 1 , 1 ) , P ) 1

**17774**: On va chercher le plan demandé sous la forme : Pour trouver , il suffit d' ***écrire*** d((1 , 1 , 1 ) , P ) 1

**17832**: Théorème 1.9 Mise en équation des sous-espaces de codimensions finies Soit E un K - espace vectoriel , soit E1 un sous-espace de E , alors , pour p N , on a Démonstration ( ) Si codim(E1 ) p , on peut , par définition ***trouver*** un supplémentaire F de dimension p , et une base de F : ( e1 ,

**17952**: ( Hérédité ) Supposons le résultat vrai au rang p et prenons p 1 formes linéaires indépendantes , D' après l' hypothèse de récurrence , nous savons que E2 est de codimension p. Soit F un supplémentaire de E2 dans E de dimension p. On peut donc ***trouver*** un vecteur a E2 E1

**17962**: Il reste à ***montrer*** que : de dimension p1 donc , en utilisant la première question de l' exercice 1.4.2 , page 32 , on obtient , puisque a E2 C' est ainsi que l' on retrouve que dans l' espace , les droites sont définies par 2 équations

**18041**: Que se passe -t -il lorsque les formes linéaires ( et donc les équations ) ne sont pas indépendantes ? Il est immédiat que : En dimension finie , cela permet de ***calculer*** des dimensions

**18130**: Cependant , l' intersection d' hyperplans affines peut-être vide , aussi faut -il , avant toutes choses , s' ***assurer*** qu' elle ne l' est pas ! Puis , en s' appuyant sur un point trouvé de l' intersection , on est ramené au cas vectoriel

**18243**: , xp ) des vecteurs de E. ***Démontrer*** que : ( b ) Démontrer que C 0 ( R , R ) est isomorphe à un hyperplan de C 1 ( R , R )

**18249**: , xp ) des vecteurs de E. Démontrer que : ( b ) ***Démontrer*** que C 0 ( R , R ) est isomorphe à un hyperplan de C 1 ( R , R )

**18302**: On dit que V sépare les vecteurs , si ***Démontrer*** que V sépare les vecteurs si , et seulement si , V E ?

**18344**: Pour A P(E ) , on appelle orthogonal ( direct ) de A et on note : ***Démontrer*** que : ( a ) A est un sous-espace vectoriel de E ?

**18429**: ( f ) Si E est de dimension finie , alors dim A codim A. 1.14.5 Soit E un K - espace vectoriel , et B P(E ? ) , on appelle orthogonal ( indirect ) de B et on note : ***Démontrer*** que : ( a ) B est un sous-espace vectoriel de E. Dans la suite , A et B sont des sous-espaces vectoriels de E ?

**18476**: ( e ) Si E est de dimension finie , alors dim B codim B ( f ) En ***déduire*** que l' inclusion de la question ( d ) est une inégalité en dimension finie

**18527**: ( h ) Si A est un sous-espace vectoriel de E , ***comparer*** : ( i ) Si B est un sous-espace vectoriel de E ? , comparer : 1.14.6 Soit E et E 0 deux K - espaces vectoriels et soit u L ( E , E 0 )

**18542**: ( h ) Si A est un sous-espace vectoriel de E , comparer : ( i ) Si B est un sous-espace vectoriel de E ? , ***comparer*** : 1.14.6 Soit E et E 0 deux K - espaces vectoriels et soit u L ( E , E 0 )

**18580**: On définit l' application transposée de u et on note : ( a ) ***Démontrer*** que t ( u v ) t u t v. ( b ) Démontrer que : ( c ) Démontrer que : Applications Systèmes linéaires Ce paragraphe , très simple , est fondamental ! Nous nous en servirons très souvent ! Soit E et E 0 deux K - espaces vectoriels , u L ( E , E 0 ) et e0 E 0 , on appelle système linéaire l' équation d' inconnue x E : L' ensemble : est appelé ensemble des solutions de ( S )

**18594**: On définit l' application transposée de u et on note : ( a ) Démontrer que t ( u v ) t u t v. ( b ) ***Démontrer*** que : ( c ) Démontrer que : Applications Systèmes linéaires Ce paragraphe , très simple , est fondamental ! Nous nous en servirons très souvent ! Soit E et E 0 deux K - espaces vectoriels , u L ( E , E 0 ) et e0 E 0 , on appelle système linéaire l' équation d' inconnue x E : L' ensemble : est appelé ensemble des solutions de ( S )

**18600**: On définit l' application transposée de u et on note : ( a ) Démontrer que t ( u v ) t u t v. ( b ) Démontrer que : ( c ) ***Démontrer*** que : Applications Systèmes linéaires Ce paragraphe , très simple , est fondamental ! Nous nous en servirons très souvent ! Soit E et E 0 deux K - espaces vectoriels , u L ( E , E 0 ) et e0 E 0 , on appelle système linéaire l' équation d' inconnue x E : L' ensemble : est appelé ensemble des solutions de ( S )

**19108**: Les équations récurrentes : un1 an un bn , où ( an ) nN et ( bn ) nN sont dans KN 1.15.1 Soit l' équation récurrente : ( a ) ***Démontrer*** que c' est bien un système linéaire en précisant E , E 0 et u. ( b ) Justifier l' existence de solutions

**19127**: Les équations récurrentes : un1 an un bn , où ( an ) nN et ( bn ) nN sont dans KN 1.15.1 Soit l' équation récurrente : ( a ) Démontrer que c' est bien un système linéaire en précisant E , E 0 et u. ( b ) ***Justifier*** l' existence de solutions

**19136**: ( c ) ***Écrire*** le système homogène associé et le résoudre

**19143**: ( c ) Écrire le système homogène associé et le ***résoudre***

**19158**: ( d ) En utilisant une méthode de variation de la constante , ***trouver*** toutes les solutions de ( S )

**19176**: 1.15.2 Soit l' équation différentielle : ( a ) ***Démontrer*** que c' est bien un système linéaire en précisant E , E 0 et u. ( b ) Justifier l' existence de solutions

**19195**: 1.15.2 Soit l' équation différentielle : ( a ) Démontrer que c' est bien un système linéaire en précisant E , E 0 et u. ( b ) ***Justifier*** l' existence de solutions

**19204**: ( c ) ***Écrire*** le système homogène associé et le résoudre

**19211**: ( c ) Écrire le système homogène associé et le ***résoudre***

**19216**: ( d ) ***Trouver*** toutes les solutions de ( S )

**19228**: ( e ) ***Comparer*** aux solutions du système récurrent obtenu par discrétisation : Interpolation Proposition 1.14 Interpolation de Lagrange Soit f : I K , où I est un intervalle de R. Soit x1 xn des réels dans I , on appelle fonction polynomiale d' interpolation de Lagrange l' unique fonction polynomiale P de degré n , telle que Elle est égale à : Démonstration E f polynomiale de degré n Cet espace vectoriel est clairement de dimension n , de base La famille de E ? définie par : étant une base de E ? , on sait qu' il existe une base ante - duale ( Pk ) k1,n qui vérifie : Un calcul simple nous démontre que : On cherche ensuite une solution sous la forme : en évaluant sur les xj , on trouve l' unique solution de l' énoncé

**19396**: Soit la fonction sin sur l' intervalle 0 , 2 , pour un p N , prenons et regardons les interpolations pour différentes valeurs de p. ***Voir*** la session Wxmaxima 1.3 , de la présente 1.16.1 Redémontrer l' existence et l' unicité des fonctions polynomiales d' interpolation de Lagrange en utilisant un raisonnement sur les systèmes linéaires

**19446**: 1.16.2 Soit f : I K de classe C 1 , soit x1 xn des points de I. ***Démontrer*** l' existence et l' unicité d' une fonction polynomiale P de degré 2 n , telle que : 1.16.3 Soit f : a , b K , de classe C

**19505**: Pour p N , on pose Lp ( f ) la fonction polynomiale d' interpolation de Lagrange de f pour les points : On suppose que : ***Démontrer*** que : 1.16.4 Soit f : x 7 x , définie sur 1 , 1

**19548**: Pour p N , p 2 , on pose Lp ( f ) la fonction polynomiale d' interpolation de Lagrange de f pour les points : ***Démontrer*** que : Fonctions spline L' interpolation par les polynômes de Lagrange ne est pas toujours efficace pour être proche de la fonction de base

**19566**: Pour p N , p 2 , on pose Lp ( f ) la fonction polynomiale d' interpolation de Lagrange de f pour les points : Démontrer que : Fonctions spline L' interpolation par les polynômes de Lagrange ne est pas toujours efficace pour ***être*** proche de la fonction de base

**19574**: ***Voir*** la session Wxmaxima 1.4 , de la présente page

**19592**: C' est pourquoi , il a fallu ***faire*** appel à d' autres classes de fonctions telles que : elles soient faciles à calculer elles approximent bien la fonction initiale elles soient insensibles à ce phénomène de divergence

**19607**: C' est pourquoi , il a fallu faire appel à d' autres classes de fonctions telles que : elles soient faciles à ***calculer*** elles approximent bien la fonction initiale elles soient insensibles à ce phénomène de divergence

**19665**: ***Voir*** la session Wxmaxima 1.5 , page suivante

**19951**: L' ensemble des matrices carrées n n à coefficients dans A se note : a. On trouve aussi souvent des parenthèses ( ) , mais nous utiliserons les crochets pour ***différencier*** familles et matrices

**20098**: , e0n ) est une base de E 0 , alors on appelle matrice de f dans les bases E et E 0 et on note : ***Noter*** que n le nombre de lignes est la dimension de l' espace d' arrivée et p le nombre de colonnes est la dimension de l' espace de départ ! 3

**20151**: Réciproquement , si A ai , j ( i , j)1,n1,p Mn , p ( K ) , on peut lui ***associer*** canoniquement l' application linéaire f définie sur Kp ( de base canonique ( e1 ,

**20656**: En particulier , on retrouve le fait que et la propriété de linéarité En dimension finie , ***connaître*** une application linéaire revient à connaître sa matrice dans des bases données

**20662**: En particulier , on retrouve le fait que et la propriété de linéarité En dimension finie , connaître une application linéaire revient à ***connaître*** sa matrice dans des bases données

**20673**: Ainsi , pour ***résoudre*** un problème d' algèbre linéaire en dimension finie , on peut travailler géométriquement avec les applications linéaires , ou bien algébriquement avec des matrices , en fonction de ce qui est le plus pertinent

**20685**: Ainsi , pour résoudre un problème d' algèbre linéaire en dimension finie , on peut ***travailler*** géométriquement avec les applications linéaires , ou bien algébriquement avec des matrices , en fonction de ce qui est le plus pertinent

**20800**: Soit A Mn , p ( K ) et B Mp , q ( K ) , on définit le produit de A par B comme la matrice A B Mn , q ( K ) définie par ***Voir*** la figure 2.1 , page ci - contre a

**20822**: a. Tiré de http : www.texample.nettikzexamplesmatrix - multiplication Il faut bien ***faire*** attention à ce que les dimensions des matrices soient compatibles : lorsque l' on veut faire le produit A B , le nombre de colonnes de A doit être égal au nombre de lignes de B. Soit E et E 0 deux K - espaces vectoriels de dimension finie ( avec p dim E et n dim E 0 ) , soit E une base de E et E 0 une base de E 0 , soit f L ( E , E 0 ) et soit x E. Alors Autrement dit , le produit matriciel MatE , E 0 ( f ) MatE ( x ) traduit le calcul de f ( x )

**20838**: a. Tiré de http : www.texample.nettikzexamplesmatrix - multiplication Il faut bien faire attention à ce que les dimensions des matrices soient compatibles : lorsque l' on veut ***faire*** le produit A B , le nombre de colonnes de A doit être égal au nombre de lignes de B. Soit E et E 0 deux K - espaces vectoriels de dimension finie ( avec p dim E et n dim E 0 ) , soit E une base de E et E 0 une base de E 0 , soit f L ( E , E 0 ) et soit x E. Alors Autrement dit , le produit matriciel MatE , E 0 ( f ) MatE ( x ) traduit le calcul de f ( x )

**20851**: a. Tiré de http : www.texample.nettikzexamplesmatrix - multiplication Il faut bien faire attention à ce que les dimensions des matrices soient compatibles : lorsque l' on veut faire le produit A B , le nombre de colonnes de A doit ***être*** égal au nombre de lignes de B. Soit E et E 0 deux K - espaces vectoriels de dimension finie ( avec p dim E et n dim E 0 ) , soit E une base de E et E 0 une base de E 0 , soit f L ( E , E 0 ) et soit x E. Alors Autrement dit , le produit matriciel MatE , E 0 ( f ) MatE ( x ) traduit le calcul de f ( x )

**21279**: Lorsque p n , on appelle matrice identité d' ordre p et on note : La matrice identité Ip correspond l' endomorphisme idE , l' application identité de E ( avec p dim E ) , dans ne importe quelle base de E. Il est important de ***savoir*** calculer les produits de matrices et de savoir prouver que le résultat est correct ! Ainsi , si Ek , est de taille n p , et Er , s est de taille p q , alors : En effet : Les dimensions sont compatibles , on peut effectuer le produit et : Le produit est associatif : Le produit est distributif à gauche et à droite : Existence d' éléments neutres ( à gauche et à droite ) pour la multiplication : Existence d' éléments absorbants pour la multiplication : Démonstration Deux méthodes : on peut vérifier ces égalités en calculant tous ces produits en utilisant la définition du produit ( définition 2.4 , page 98 ) on peut également utiliser l' isomorphisme de la proposition 2.1 , page 96 , les égalités ci - dessus découlent alors des propriétés de la composition des applications linéaires ( la démonstration est laissée en exercice )

**21280**: Lorsque p n , on appelle matrice identité d' ordre p et on note : La matrice identité Ip correspond l' endomorphisme idE , l' application identité de E ( avec p dim E ) , dans ne importe quelle base de E. Il est important de savoir ***calculer*** les produits de matrices et de savoir prouver que le résultat est correct ! Ainsi , si Ek , est de taille n p , et Er , s est de taille p q , alors : En effet : Les dimensions sont compatibles , on peut effectuer le produit et : Le produit est associatif : Le produit est distributif à gauche et à droite : Existence d' éléments neutres ( à gauche et à droite ) pour la multiplication : Existence d' éléments absorbants pour la multiplication : Démonstration Deux méthodes : on peut vérifier ces égalités en calculant tous ces produits en utilisant la définition du produit ( définition 2.4 , page 98 ) on peut également utiliser l' isomorphisme de la proposition 2.1 , page 96 , les égalités ci - dessus découlent alors des propriétés de la composition des applications linéaires ( la démonstration est laissée en exercice )

**21287**: Lorsque p n , on appelle matrice identité d' ordre p et on note : La matrice identité Ip correspond l' endomorphisme idE , l' application identité de E ( avec p dim E ) , dans ne importe quelle base de E. Il est important de savoir calculer les produits de matrices et de ***savoir*** prouver que le résultat est correct ! Ainsi , si Ek , est de taille n p , et Er , s est de taille p q , alors : En effet : Les dimensions sont compatibles , on peut effectuer le produit et : Le produit est associatif : Le produit est distributif à gauche et à droite : Existence d' éléments neutres ( à gauche et à droite ) pour la multiplication : Existence d' éléments absorbants pour la multiplication : Démonstration Deux méthodes : on peut vérifier ces égalités en calculant tous ces produits en utilisant la définition du produit ( définition 2.4 , page 98 ) on peut également utiliser l' isomorphisme de la proposition 2.1 , page 96 , les égalités ci - dessus découlent alors des propriétés de la composition des applications linéaires ( la démonstration est laissée en exercice )

**21288**: Lorsque p n , on appelle matrice identité d' ordre p et on note : La matrice identité Ip correspond l' endomorphisme idE , l' application identité de E ( avec p dim E ) , dans ne importe quelle base de E. Il est important de savoir calculer les produits de matrices et de savoir ***prouver*** que le résultat est correct ! Ainsi , si Ek , est de taille n p , et Er , s est de taille p q , alors : En effet : Les dimensions sont compatibles , on peut effectuer le produit et : Le produit est associatif : Le produit est distributif à gauche et à droite : Existence d' éléments neutres ( à gauche et à droite ) pour la multiplication : Existence d' éléments absorbants pour la multiplication : Démonstration Deux méthodes : on peut vérifier ces égalités en calculant tous ces produits en utilisant la définition du produit ( définition 2.4 , page 98 ) on peut également utiliser l' isomorphisme de la proposition 2.1 , page 96 , les égalités ci - dessus découlent alors des propriétés de la composition des applications linéaires ( la démonstration est laissée en exercice )

**21328**: Lorsque p n , on appelle matrice identité d' ordre p et on note : La matrice identité Ip correspond l' endomorphisme idE , l' application identité de E ( avec p dim E ) , dans ne importe quelle base de E. Il est important de savoir calculer les produits de matrices et de savoir prouver que le résultat est correct ! Ainsi , si Ek , est de taille n p , et Er , s est de taille p q , alors : En effet : Les dimensions sont compatibles , on peut ***effectuer*** le produit et : Le produit est associatif : Le produit est distributif à gauche et à droite : Existence d' éléments neutres ( à gauche et à droite ) pour la multiplication : Existence d' éléments absorbants pour la multiplication : Démonstration Deux méthodes : on peut vérifier ces égalités en calculant tous ces produits en utilisant la définition du produit ( définition 2.4 , page 98 ) on peut également utiliser l' isomorphisme de la proposition 2.1 , page 96 , les égalités ci - dessus découlent alors des propriétés de la composition des applications linéaires ( la démonstration est laissée en exercice )

**21377**: Lorsque p n , on appelle matrice identité d' ordre p et on note : La matrice identité Ip correspond l' endomorphisme idE , l' application identité de E ( avec p dim E ) , dans ne importe quelle base de E. Il est important de savoir calculer les produits de matrices et de savoir prouver que le résultat est correct ! Ainsi , si Ek , est de taille n p , et Er , s est de taille p q , alors : En effet : Les dimensions sont compatibles , on peut effectuer le produit et : Le produit est associatif : Le produit est distributif à gauche et à droite : Existence d' éléments neutres ( à gauche et à droite ) pour la multiplication : Existence d' éléments absorbants pour la multiplication : Démonstration Deux méthodes : on peut ***vérifier*** ces égalités en calculant tous ces produits en utilisant la définition du produit ( définition 2.4 , page 98 ) on peut également utiliser l' isomorphisme de la proposition 2.1 , page 96 , les égalités ci - dessus découlent alors des propriétés de la composition des applications linéaires ( la démonstration est laissée en exercice )

**21401**: Lorsque p n , on appelle matrice identité d' ordre p et on note : La matrice identité Ip correspond l' endomorphisme idE , l' application identité de E ( avec p dim E ) , dans ne importe quelle base de E. Il est important de savoir calculer les produits de matrices et de savoir prouver que le résultat est correct ! Ainsi , si Ek , est de taille n p , et Er , s est de taille p q , alors : En effet : Les dimensions sont compatibles , on peut effectuer le produit et : Le produit est associatif : Le produit est distributif à gauche et à droite : Existence d' éléments neutres ( à gauche et à droite ) pour la multiplication : Existence d' éléments absorbants pour la multiplication : Démonstration Deux méthodes : on peut vérifier ces égalités en calculant tous ces produits en utilisant la définition du produit ( définition 2.4 , page 98 ) on peut également ***utiliser*** l' isomorphisme de la proposition 2.1 , page 96 , les égalités ci - dessus découlent alors des propriétés de la composition des applications linéaires ( la démonstration est laissée en exercice )

**21502**: En général , 2.1.1 ***Calculer*** pour M Mn , p ( K ) , les matrices M.Ek , et Ek , .M pour les valeurs de k et ( à préciser )

**21528**: En général , 2.1.1 Calculer pour M Mn , p ( K ) , les matrices M.Ek , et Ek , .M pour les valeurs de k et ( à ***préciser*** )

**21531**: ***Calculer*** A2

**21535**: 2.1.3 ***Résoudre*** l' équation M 2 02 d' inconnue M M2 ( R )

**21574**: 2.1.4 Soit ( a , b ) R2 et soit A Mn ( R ) définie par : ai , j a si i j ***Trouver*** toutes les matrices qui commutent avec A , c' est - à - dire déterminer l' ensemble 2.1.5 On suppose que a , b et c sont trois nombrs complexes tels que a2 b2 c2 1

**21588**: 2.1.4 Soit ( a , b ) R2 et soit A Mn ( R ) définie par : ai , j a si i j Trouver toutes les matrices qui commutent avec A , c' est - à - ***dire*** déterminer l' ensemble 2.1.5 On suppose que a , b et c sont trois nombrs complexes tels que a2 b2 c2 1

**21589**: 2.1.4 Soit ( a , b ) R2 et soit A Mn ( R ) définie par : ai , j a si i j Trouver toutes les matrices qui commutent avec A , c' est - à - dire ***déterminer*** l' ensemble 2.1.5 On suppose que a , b et c sont trois nombrs complexes tels que a2 b2 c2 1

**21615**: On pose : ***Démontrer*** que : 2.1.6 Soit A , B et C trois matrices de Mn ( R ) telles que : Démontrer que : Transposition Soit A un ensemble , ( n , p ) N 2 , alors l' application définie par : est appelée transposition

**21635**: On pose : Démontrer que : 2.1.6 Soit A , B et C trois matrices de Mn ( R ) telles que : ***Démontrer*** que : Transposition Soit A un ensemble , ( n , p ) N 2 , alors l' application définie par : est appelée transposition

**21755**: Il y deux manières de ***considérer*** les formes linéaires d' un K - espace vectoriel E de dimension finie : comme des applications linéaires de E dans K elles sont alors représentées par des matrices de M1,p ( K ) en fixant une base de E ( avec p dim E ) comme des vecteurs de E ? elles sont alors représentées dans une base de E ? par des matrices de Y a -t -il un lien entre ces deux représentations ? Soit E ( e1 ,

**22021**: L' ensemble des matrices antisymétriques de Mp ( K ) est noté a. Les matrices M vérifiant t M M sont nécessairement carrées ! ( a ) ***Démontrer*** que Sp ( K ) et Ap ( K ) sont des sous-espaces vectoriels de Mp ( K )

**22045**: ( b ) ***Démontrer*** que ( c ) Déterminer la dimension de Sp ( K ) et la dimension de Ap ( K )

**22050**: ( b ) Démontrer que ( c ) ***Déterminer*** la dimension de Sp ( K ) et la dimension de Ap ( K )

**22091**: Matrices diagonales , matrices triangulaires On dit que A est diagonale si tous ses coefficients non-diagonaux sont nuls , c' est - à - ***dire*** : Autrement dit : On note Dp ( K ) l' ensemble des matrices diagonales de Mp ( K )

**22138**: On dit que A est triangulaire supérieure si tous ses coefficients au - dessous de sa diagonale sont nuls , c' est - à - ***dire*** : Autrement dit : p ( K ) l' ensemble des matrices triangulaires supérieures de Mp ( K )

**22182**: On dit que A est triangulaire inférieur si tous ses coefficients au-dessus de sa diagonale sont nuls , c' est - à - ***dire*** : Autrement dit : p ( K ) l' ensemble des matrices triangulaires inférieures de Mp ( K )

**22216**: Il est indispensable que A soit une matrice carrée ! ( a ) ***Démontrer*** que Dp ( K ) , T p ( K ) et Tp ( K ) sont des sous-espaces vectoriels de Mp ( K )

**22252**: Quelles sont leurs dimension respectives ? ( b ) ***Démontrer*** que ces trois espaces sont stables par produit et exprimer simplement les coefficients diagonaux du produit

**22262**: Quelles sont leurs dimension respectives ? ( b ) Démontrer que ces trois espaces sont stables par produit et ***exprimer*** simplement les coefficients diagonaux du produit

**22372**: La trace est invariante par commutation de deux matrices a : Mais il est faux de ***penser*** que trace(A B C ) trace(A C B ) On peut commuter deux matrices , mais on ne peux pas changer ne importe quel ordre ! Démonstration En exercice

**22384**: La trace est invariante par commutation de deux matrices a : Mais il est faux de penser que trace(A B C ) trace(A C B ) On peut ***commuter*** deux matrices , mais on ne peux pas changer ne importe quel ordre ! Démonstration En exercice

**22393**: La trace est invariante par commutation de deux matrices a : Mais il est faux de penser que trace(A B C ) trace(A C B ) On peut commuter deux matrices , mais on ne peux pas ***changer*** ne importe quel ordre ! Démonstration En exercice

**22671**: À ***noter*** qu' il suffit de vérifier l' inversibilité matriciel dans une seule base

**22676**: À noter qu' il suffit de ***vérifier*** l' inversibilité matriciel dans une seule base

**23416**: Alors ( ***voir*** la figure 2.2 , page suivante ) : Dans le cas particulier où f est un endomorphisme de E ( E 0 E , E 0 E , B 0 B et f L ( E ) ) , on a MatB ( f ) PE Démonstration L' égalité f idE idE 0 f donne c' est - à - dire d' où le résultat

**23733**: Pour tout y E 0 , y Im f si , et seulement si , MatE 0 ( y ) Im A. En particulier , dim Im f dim Im A c' est - à - dire rang f rang A Si A Mn , p ( K ) , on a le théorème du rang ( ***voir*** le théorème 1.4 , page 57 ) : rang A p dim Ker A De plus , si A Mp ( K ) ( matrice carrée ) , les propositions suivantes sont équivalentes : 1

**23870**: La multiplication par une matrice inversible conserve le rang : si A Mn , p ( K ) , alors P GLp ( K ) , Q GLn ( K ) , rang(A P ) rang(Q A ) rang A 2.4.1 Soit A Mn ( K ) , existe -t -il B Mn ( K ) telle que : 2.4.2 Soit A et B dans Mn ( R ) , telles que : ***Démontrer*** que A ou B est la matrice nulle

**23881**: 2.4.3 ***Démontrer*** que toute matrice de Mn ( R ) est somme de deux matrices inversibles

**23898**: 2.4.4 ***Démontrer*** que toute matrice de Mn ( R ) est limite d' une suite de matrices inversibles

**23929**: 2.4.5 Soit A et B dans Mn , p ( K ) , ***démontrer*** que : rang(A ) rang(B ) Relations d' équivalence et matrices Relations d' équivalence Soit E un ensemble non vide , R une relation a sur E. On dit que : R est réflexive si : R est symétrique si : R est transitive si : On dit que R est une relation d' équivalence sur E si R est réflexive , symétrique et transitive

**24002**: a. c' est - à - ***dire*** la donnée d' un sous-ensemble A de E E , où on définit pour tout ( x , y ) E 2 , xRy ( x , y ) A 1

**24049**: ***avoir*** même parité est une relation d' équivalence sur N ou Z. 3

**24063**: ***avoir*** même dimension est une relation d' équivalence sur l' ensemble des sous-espaces vectoriels d' un même espace vectoriel E de dimension finie

**24089**: ***être*** en bijection avec est une relation d' équivalence sur l' ensemble des sous-ensembles d' un ensemble E. 5

**24109**: ***être*** parallèle est une relation d' équivalence sur l' ensemble des droites du plan

**24131**: Pour tout n N , ***avoir*** le même reste dans la division euclidienne par n est une relation d' équivalence sur Z. Soit E un ensemble non vide , on appelle partition de E , la donnée d' une famille ( Ei ) iI de sous-ensembles de E tels que : tous les Ei sont non vides : ils sont disjoints deux-à-deux : ils recouvrent E : 1

**24256**: Plus généralement , si n N , n 2 , on peut s' ***intéresser*** aux ensembles : ( Ek ) k0,n1 est une partition de N Soit ( Ei ) iI une partition d' un ensemble E non vide et soit R la relation sur E définie par : ( autrement dit , x et y sont en relation lorsque x et y appartiennent à un même Ei )

**24776**: 2.5.1 On définit sur C la relation : ( a ) ***Démontrer*** que c' est une relation d' équivalence

**24788**: ( b ) ***Préciser*** les classes d' équivalence

**24832**: 2.5.2 Soit E un ensemble non vide et A E , on définit une relation sur P(E ) par : ( a ) ***Démontrer*** que c' est une relation d' équivalence

**24844**: ( b ) ***Démontrer*** que l' ensemble des classes d' équivalence est en bijection avec P(A )

**24880**: On définit de même la relation sur P(E ) par : ( c ) C' est une relation d' équivalence , ***trouver*** une bijection de l' ensemble des classes d' équivalence avec un ensemble connu

**25001**: On définit les deux relations suivantes : xRy ou yRx Les relations S et T sont - elles réflexives ? Symétriques ? Transitives ? 2.5.5 Soit E un ensemble non vide muni d' une relation d' équivalence R , on pose : Classe(a , R ) Soit A une partie de E. ( a ) ***Démontrer*** que A s(A )

**25009**: Peut -on ***avoir*** A s(A ) ? Donner un exemple

**25014**: Peut -on avoir A s(A ) ? ***Donner*** un exemple

**25032**: ( d ) Soit ( Ai ) iI une famille de sous-ensembles de E. ***Comparer*** pour l' inclusion les ensembles : s(Ai ) , puis s Équivalence et similitudes 1

**25221**: Démonstration Laissée en exercice ( ***utiliser*** la formule de changement de base et les propriété des matrices de passage )

**25358**: Supposons - les équivalentes , il existe P GLn ( K ) et Q GLp ( K ) telles que N P M Q. En notant uX l' application linéaire canoniquement associée à une matrice X , on a uN uP uM uQ La conservation du rang en découle , car uP et uQ sont inversibles ( ***voir*** la remarque 2.14 , page 115 )

**25593**: Il est beaucoup plus difficile de ***caractériser*** les classes d' équivalence pour la similitude ( voir la partie sur les classes de similitude dans chapitre 4 sur la réduction des endormophismes )

**25602**: Il est beaucoup plus difficile de caractériser les classes d' équivalence pour la similitude ( ***voir*** la partie sur les classes de similitude dans chapitre 4 sur la réduction des endormophismes )

**25623**: ( a ) ***Démontrer*** que si A B , alors rang(A ) rang(B ) et trace(A ) trace(B )

**25643**: ( b ) ***Trouver*** un exemple où rang(A ) rang(B ) et trace(A ) trace(B ) mais A et B sont pas semblables

**25667**: ( c ) ***Trouver*** un exemple où A et B sont équivalentes mais ne sont pas semblables

**25704**: ( a ) ***Justifier*** que la trace de MatE ( f ) ne dépend pas de la base E de E choisie

**25762**: On définit alors la trace de f , notée trace(f ) , comme la valeur de trace(MatE ( f ) ) dans ne importe quelle base E de E. ( b ) Soit p un projecteur de E. ***Démontrer*** que trace(p ) rang(p )

**25770**: 2.6.3 ***Démontrer*** que A Mn , p ( K ) , rang(t A ) rang(A ) 2.6.4 Démontrer que toute matrice de Mp ( K ) non inversible est équivalente à une matrice B telle qu' il existe k N tel que B k 0p ( matrice dite nilpotente )

**25786**: 2.6.3 Démontrer que A Mn , p ( K ) , rang(t A ) rang(A ) 2.6.4 ***Démontrer*** que toute matrice de Mp ( K ) non inversible est équivalente à une matrice B telle qu' il existe k N tel que B k 0p ( matrice dite nilpotente )

**25959**: Systèmes linéaires Algorithme du pivot de Gauss Notation 2.3 Soit ( k , ) 1 , p , k 6 et K , on appelle matrice de transvection la matrice de Mp ( K ) définie par : Cette matrice est inversible et son inverse est : Démonstration Un calcul direct donne Notation 2.4 Soit k 1 , p , K , on appelle matrice de dilatation la matrice de Mp ( K ) définie par : à la k - ième place Cette matrice est inversible et son inverse est : Démonstration Un calcul immédiat démontre que Notation 2.5 Soit une permutation a de 1 , p , on appelle matrice de permutation la matrice de Mp ( K ) définie par : Cette matrice est inversible et son inverse est : a. C' est - à - ***dire*** une bijection de de 1 , p dans 1 , p. Démonstration Si et 0 sont deux permutations de 1 , p alors on remarque que : On prend alors 0 1 en remarquant que si id1,p , alors P Ip

**26074**: Transvection Cela revient donc à ***faire*** la transformation ( dite opération élémentaire ) : ( on remplace la k - ième ligne par la k - ième ligne à laquelle on a ajouté fois la -ième ligne )

**26115**: Dilatation Cela revient donc à ***faire*** la transformation ( dite opération élémentaire ) : ( on remplace la k - ième ligne par fois la k - ième ligne )

**26148**: Permutation Cela revient donc à ***faire*** la transformation ( dite opération élémentaire ) : Soit A ai , j ( i , j)1,n1,p Mn , p ( K )

**26229**: Transvection Cela revient donc à ***faire*** la transformation ( dite opération élémentaire ) : ( on remplace la -ième colonne par la -ième colonne à laquelle on a ajouté fois la k - ième colonne )

**26268**: Dilatation Cela revient donc à ***faire*** la transformation ( dite opération élémentaire ) : ( on remplace la k - ième colonne par fois la k - ième colonne )

**26301**: Permutation Cela revient donc à ***faire*** la transformation ( dite opération élémentaire ) : Lorsqu' on utilise des opérations élémentaires , c' est généralement pour faire apparaître le plus de 0 possibles dans la matrice

**26321**: Permutation Cela revient donc à faire la transformation ( dite opération élémentaire ) : Lorsqu' on utilise des opérations élémentaires , c' est généralement pour ***faire*** apparaître le plus de 0 possibles dans la matrice

**26322**: Permutation Cela revient donc à faire la transformation ( dite opération élémentaire ) : Lorsqu' on utilise des opérations élémentaires , c' est généralement pour faire ***apparaître*** le plus de 0 possibles dans la matrice

**26337**: Il est alors indispensable de ***présenter*** les calculs de manière lisible par le lecteur

**26364**: on encadre le pivot ( terme dont on se sert pour ***faire*** apparaître les 0 ) 2

**26365**: on encadre le pivot ( terme dont on se sert pour faire ***apparaître*** les 0 ) 2

**26490**: Si A 0n , p , alors il ne y a rien à ***démontrer*** ( on a A Jn , p,0 0n , p avec r 0 )

**26598**: On obtient donc une matrice de la forme ( ***voir*** la partie suivante sur les matrices - blocs ) : Si A0 est vide ( n 1 ou p 1 ) ou si A0 0n1,p1 , on s' arrête

**26740**: En utilisant Wxmaxima : On peut aussi ***travailler*** à la main

**26766**: Que se passe -t -il lorsque , par exemple , la première colonne est remplie de 0 ? On commence par ***permuter*** les colonnes ! Ici , nous allons écrire les matrices nous - mêmes ... Toute matrice de permutation peut s' exprimer comme produit de matrices de transvection - dilatation

**26787**: Que se passe -t -il lorsque , par exemple , la première colonne est remplie de 0 ? On commence par permuter les colonnes ! Ici , nous allons écrire les matrices nous - mêmes ... Toute matrice de permutation peut s' ***exprimer*** comme produit de matrices de transvection - dilatation

**26808**: Toute permutation de 1 , p peut s' ***exprimer*** comme une composée de transpositions ( une permutation qui échange seulement deux éléments )

**26827**: Ceci peut se ***démontrer*** par récurrence sur p. Initialisation p 1 , c' est évident

**26924**: Il suffit donc de ***démontrer*** le résultat pour une transposition

**26939**: Par décalage d' indices , il suffit de ***démontrer*** cela pour la transposition qui échange 1 et 2

**26952**: On peut ***procéder*** de la manière suivante : Soit A GLp ( K ) , alors il existe des matrices de transvection - dilatation - permutation de Mp ( K ) , notées R1 ,

**27027**: , Ss telles que : Autrement dit , quand A est inversible , on peut se ***contenter*** de travailler soit uniquement sur les lignes , soit uniquement sur les colonnes

**27029**: , Ss telles que : Autrement dit , quand A est inversible , on peut se contenter de ***travailler*** soit uniquement sur les lignes , soit uniquement sur les colonnes

**27163**: Lorsque la matrice A est dans GLp ( K ) , on peut se ***limiter*** à au plus une dilatation de type Dp ( ) ( et ne faire donc autrement que des transvections )

**27177**: Lorsque la matrice A est dans GLp ( K ) , on peut se limiter à au plus une dilatation de type Dp ( ) ( et ne ***faire*** donc autrement que des transvections )

**27191**: En effet , il suffit de ***savoir*** le faire sur une matrice 2 2 ( a 6 0 et b 6 0 ) : Il est important de noter que : 1

**27193**: En effet , il suffit de savoir le ***faire*** sur une matrice 2 2 ( a 6 0 et b 6 0 ) : Il est important de noter que : 1

**27213**: En effet , il suffit de savoir le faire sur une matrice 2 2 ( a 6 0 et b 6 0 ) : Il est important de ***noter*** que : 1

**27227**: Lorsque l' on calcule un rang : on peut ***travailler*** à la fois sur les lignes et les colonnes

**27360**: 2.7.1 Soit la matrice : ( a ) ***Calculer*** son rang r. ( b ) Trouver deux matrices P et Q inversibles telles que : 2.7.2 Déterminer les a K tels que la matrice : soit inversible Démontrer que A est inversible et calculer son inverse

**27367**: 2.7.1 Soit la matrice : ( a ) Calculer son rang r. ( b ) ***Trouver*** deux matrices P et Q inversibles telles que : 2.7.2 Déterminer les a K tels que la matrice : soit inversible Démontrer que A est inversible et calculer son inverse

**27378**: 2.7.1 Soit la matrice : ( a ) Calculer son rang r. ( b ) Trouver deux matrices P et Q inversibles telles que : 2.7.2 ***Déterminer*** les a K tels que la matrice : soit inversible Démontrer que A est inversible et calculer son inverse

**27389**: 2.7.1 Soit la matrice : ( a ) Calculer son rang r. ( b ) Trouver deux matrices P et Q inversibles telles que : 2.7.2 Déterminer les a K tels que la matrice : soit inversible ***Démontrer*** que A est inversible et calculer son inverse

**27395**: 2.7.1 Soit la matrice : ( a ) Calculer son rang r. ( b ) Trouver deux matrices P et Q inversibles telles que : 2.7.2 Déterminer les a K tels que la matrice : soit inversible Démontrer que A est inversible et ***calculer*** son inverse

**27407**: 2.7.4 Soit la matrice : ( a ) ***Déterminer*** le rang de A. ( b ) Déterminer une base de l' image de A. ( c ) Donner des équations de Im(A )

**27415**: 2.7.4 Soit la matrice : ( a ) Déterminer le rang de A. ( b ) ***Déterminer*** une base de l' image de A. ( c ) Donner des équations de Im(A )

**27436**: ( d ) ***Déterminer*** une base du noyau de A. ( a ) Démontrer que est un isomorphisme si , et seulement si , A est inversible

**27446**: ( d ) Déterminer une base du noyau de A. ( a ) ***Démontrer*** que est un isomorphisme si , et seulement si , A est inversible

**27464**: ( b ) ***Calculer*** le rang de en fonction de celui de A. 2.7.6 Soit A une matrice de Mn ( R ) tri-diagonale ( c' est - à - dire vérifiant ai , j 0 dès que i j 2 )

**27509**: On suppose de plus que ***Démontrer*** qu' il existe une matrice diagonale D inversible , telle que D1 A D Sn ( R )

**27537**: n ( K ) , soit 0 , ***démontrer*** qu' il existe une matrice P Dn ( K ) GLn ( K ) telle que : Systèmes linéaires On a déjà vu au chapitre précédent ( section 1.4.1 , page 78 ) qu' en toute généralité , un système linéaire est une équation de la forme : où u L ( E , E 0 ) et b E 0 sont fixés et x est l' inconnue ( E et E 0 sont des K - espaces vectoriels )

**27652**: Dans le cas de la dimension finie et une fois des bases fixées , ce système linéaire est équivalent à un système de n équations à n inconnues , que l' on peut ***écrire*** sous forme matricielle : où A est la matrice n p de u , X la matrice p 1 de x et B la matrice n 1 de b ( avec p dim E et Lorsque l' on a un système de n équations à p inconnues , la condition de compatibilité ( c' est - à - dire la condition pour que le système admette des solutions ) s' écrit ( voir la partie suivante sur les matrices - blocs ) : rang(A ) rang A B ) ce qui se vérifie facilement à l' aide d' une méthode de pivot sur les lignes , où l' on ne prend jamais le pivot sur la colonne constituée des éléments de B. La matrice A B Mn , p1 ( K ) s' appelle la matrice augmentée du système A X B. Un système de n équations à n inconnues : est dit de Cramer , lorsque A est inversible

**27711**: Dans le cas de la dimension finie et une fois des bases fixées , ce système linéaire est équivalent à un système de n équations à n inconnues , que l' on peut écrire sous forme matricielle : où A est la matrice n p de u , X la matrice p 1 de x et B la matrice n 1 de b ( avec p dim E et Lorsque l' on a un système de n équations à p inconnues , la condition de compatibilité ( c' est - à - ***dire*** la condition pour que le système admette des solutions ) s' écrit ( voir la partie suivante sur les matrices - blocs ) : rang(A ) rang A B ) ce qui se vérifie facilement à l' aide d' une méthode de pivot sur les lignes , où l' on ne prend jamais le pivot sur la colonne constituée des éléments de B. La matrice A B Mn , p1 ( K ) s' appelle la matrice augmentée du système A X B. Un système de n équations à n inconnues : est dit de Cramer , lorsque A est inversible

**27725**: Dans le cas de la dimension finie et une fois des bases fixées , ce système linéaire est équivalent à un système de n équations à n inconnues , que l' on peut écrire sous forme matricielle : où A est la matrice n p de u , X la matrice p 1 de x et B la matrice n 1 de b ( avec p dim E et Lorsque l' on a un système de n équations à p inconnues , la condition de compatibilité ( c' est - à - dire la condition pour que le système admette des solutions ) s' écrit ( ***voir*** la partie suivante sur les matrices - blocs ) : rang(A ) rang A B ) ce qui se vérifie facilement à l' aide d' une méthode de pivot sur les lignes , où l' on ne prend jamais le pivot sur la colonne constituée des éléments de B. La matrice A B Mn , p1 ( K ) s' appelle la matrice augmentée du système A X B. Un système de n équations à n inconnues : est dit de Cramer , lorsque A est inversible

**27831**: En ce cas , il y a existence et unicité de la solution , donnée par Pour ***résoudre*** un système de Cramer , on ne calcule jamais l' inverse de la matrice A , on utilise l' algorithme du pivot de Gauss ! Soit à résoudre le système : Appliquons l' algorithme du pivot de Gauss à la matrice augmentée A B : La deuxième ligne permet de discerner trois cas : 1

**27859**: En ce cas , il y a existence et unicité de la solution , donnée par Pour résoudre un système de Cramer , on ne calcule jamais l' inverse de la matrice A , on utilise l' algorithme du pivot de Gauss ! Soit à ***résoudre*** le système : Appliquons l' algorithme du pivot de Gauss à la matrice augmentée A B : La deuxième ligne permet de discerner trois cas : 1

**27882**: En ce cas , il y a existence et unicité de la solution , donnée par Pour résoudre un système de Cramer , on ne calcule jamais l' inverse de la matrice A , on utilise l' algorithme du pivot de Gauss ! Soit à résoudre le système : Appliquons l' algorithme du pivot de Gauss à la matrice augmentée A B : La deuxième ligne permet de ***discerner*** trois cas : 1

**27986**: Donc : l' ordinateur ne fait pas ***apparaître*** le cas ! ! ! Si on a vraiment besoin de calculer l' inverse d' une matrice A GLp ( K ) inversible , on peut appliquer l' algorithme du pivot de Gauss généralisée à la matrice augmentée A Ip , avec des opérations sur les lignes

**27998**: Donc : l' ordinateur ne fait pas apparaître le cas ! ! ! Si on a vraiment besoin de ***calculer*** l' inverse d' une matrice A GLp ( K ) inversible , on peut appliquer l' algorithme du pivot de Gauss généralisée à la matrice augmentée A Ip , avec des opérations sur les lignes

**28013**: Donc : l' ordinateur ne fait pas apparaître le cas ! ! ! Si on a vraiment besoin de calculer l' inverse d' une matrice A GLp ( K ) inversible , on peut ***appliquer*** l' algorithme du pivot de Gauss généralisée à la matrice augmentée A Ip , avec des opérations sur les lignes

**28105**: ***Résoudre*** le système et donner une condition nécessaire et suffisante sur a , b et c pour que les solutions soient réelles

**28109**: Résoudre le système et ***donner*** une condition nécessaire et suffisante sur a , b et c pour que les solutions soient réelles

**28129**: 2.8.2 ***Inverser*** la matrice 2.8.3 Résoudre le système Matrices - blocs Notation 2.6 signifie que : mi , j ai , j mi , j cin1 , j i , j bi , jp1 On parle alors de matrice - blocs

**28133**: 2.8.2 Inverser la matrice 2.8.3 ***Résoudre*** le système Matrices - blocs Notation 2.6 signifie que : mi , j ai , j mi , j cin1 , j i , j bi , jp1 On parle alors de matrice - blocs

**28172**: On peut ***généraliser*** cette notation à un nombre de blocs plus grand

**28191**: La matrice Jn , p , r ( ***voir*** la notation 2.2 , page 119 ) peut s' écrire sous la forme d' une matrice - blocs : 0nr , r 0nr , pr Multiplication d' une matrice - bloc par un scalaire

**28201**: La matrice Jn , p , r ( voir la notation 2.2 , page 119 ) peut s' ***écrire*** sous la forme d' une matrice - blocs : 0nr , r 0nr , pr Multiplication d' une matrice - bloc par un scalaire

**28255**: Si A Mn1 , p1 ( K ) , B Mn1 , p2 ( K ) , C Les sommes entre matrices - blocs incompatibles ne peuvent s' ***exprimer*** en termes de blocs

**28326**: On peut bien sûr , ***généraliser*** à un nombre de blocs plus grand , il faut faire attention à bien conserver les compatibilités entre les dimensions

**28337**: On peut bien sûr , généraliser à un nombre de blocs plus grand , il faut ***faire*** attention à bien conserver les compatibilités entre les dimensions

**28341**: On peut bien sûr , généraliser à un nombre de blocs plus grand , il faut faire attention à bien ***conserver*** les compatibilités entre les dimensions

**28352**: Attention à ne pas ***oublier*** que la multiplication entre matrices ne est pas commutative ! Démonstration Il s' agit de simples vérifications par calculs ( laissées en exercice )

**28569**: A MatE1 , E10 ( 1 1 f E1 ) où 1 est la projection sur E10 parallèlement à E20 C MatE1 , E20 ( 2 2 f E1 ) où 2 idE 0 1 est la projection sur E20 parallèlement à E10 Démonstration Immédiat en décomposant chaque élément de f ( E1 ) et chaque élément de f ( E2 ) sur la base ( E10 , E20 ) ( en exercice ) En particulier , pour le cas des endomorphismes ( c' est - à - dire E E 0 , E10 E1 et E20 E2 ) , on a : E1 stable par f C 0n2 , p1 et E2 stable par f B 0n1 , p2 Ainsi , les matrices - blocs permettent de ***visualiser*** simplement certains sous-espaces stables

**28584**: Utilisation La notation par blocs est extrêmement pratique pour ***faire*** des récurrences , ainsi que pour représenter simplement les matrices

**28591**: Utilisation La notation par blocs est extrêmement pratique pour faire des récurrences , ainsi que pour ***représenter*** simplement les matrices

**28692**: De plus , n ( K ) GLn ( K ) est stable par M 7 M où A GLn1 ( K ) et D GLn2 ( K ) , alors M GLn1 n2 ( K ) et son inverse est de la forme : On rencontre souvent des transvections - blocs , des dilatations - blocs et des permutations - blocs , ainsi : vérifie clairement ( en choisissant k et pour ***avoir*** des dimensions compatibles ) : soit une opération élémentaire sur les blocs : ( produit à gauche ) ( produit à droite ) De même avec les dilatations : ( produit à gauche ) ( produit à droite ) La permutation - bloc serait par exemple : Cela permet ( avec quelques précautions de calcul ) de faire des manipulations sur les matrices - blocs comme sur des matrices usuelles

**28750**: De plus , n ( K ) GLn ( K ) est stable par M 7 M où A GLn1 ( K ) et D GLn2 ( K ) , alors M GLn1 n2 ( K ) et son inverse est de la forme : On rencontre souvent des transvections - blocs , des dilatations - blocs et des permutations - blocs , ainsi : vérifie clairement ( en choisissant k et pour avoir des dimensions compatibles ) : soit une opération élémentaire sur les blocs : ( produit à gauche ) ( produit à droite ) De même avec les dilatations : ( produit à gauche ) ( produit à droite ) La permutation - bloc serait par exemple : Cela permet ( avec quelques précautions de calcul ) de ***faire*** des manipulations sur les matrices - blocs comme sur des matrices usuelles

**28766**: a. doit ***être*** inversible , car on veut conserver le rang ! ! 1

**28772**: a. doit être inversible , car on veut ***conserver*** le rang ! ! 1

**28799**: On peut en ***déduire*** que si A GLn ( K ) , alors il existe une matrice de permutation P , une matrice T1 triangulaire inférieure avec des 1 sur la diagonale et une matrice T2 triangulaire supérieure telles Produit de Kronecker Soit A ai , j Mn1 , p1 ( K ) et B Mn2 , p2 ( K ) , on définit le produit de Kronecker de A et B comme la matrice - blocs : alors pour toute matrice B à coefficients dans K , on a 2

**28959**: ( a ) ***Démontrer*** que : rang(M ) rang ( b ) En déduire le rang de M

**28969**: ( a ) Démontrer que : rang(M ) rang ( b ) En ***déduire*** le rang de M

**28983**: ***Calculer*** M 1

**28988**: 2.9.2 ***Inverser*** la matrice : 2.9.3 Calculer rang(A B ) en fonction de rang(A ) et rang(B ) pour A Mn , p ( K ) et B Mq , s ( K )

**28993**: 2.9.2 Inverser la matrice : 2.9.3 ***Calculer*** rang(A B ) en fonction de rang(A ) et rang(B ) pour A Mn , p ( K ) et B Mq , s ( K )

**29040**: ***Trouver*** une condition nécessaire et suffisante sur E pour que M soit inversible et , dans ce cas , calculer M 1

**29059**: Trouver une condition nécessaire et suffisante sur E pour que M soit inversible et , dans ce cas , ***calculer*** M 1

**29093**: On considère la matrice diagonale par blocs : ( a ) ***Démontrer*** que ( b ) Démontrer que : rang(A ) rang(B ) rang(D ) ( c ) Donner un exemple où l' inégalité est stricte

**29098**: On considère la matrice diagonale par blocs : ( a ) Démontrer que ( b ) ***Démontrer*** que : rang(A ) rang(B ) rang(D ) ( c ) Donner un exemple où l' inégalité est stricte

**29122**: ( d ) ***Démontrer*** que si B ou D est une matrice carrée inversible , alors il y a égalité

**29304**: On a card Sp p ! Démonstration Pour ***construire*** une permutation Sp : On a p choix possibles pour ( 1 ) ( les p éléments de 1 , p ) Une fois ( 1 ) choisi , on a p 1 choix possibles pour ( 2 ) ( les p 1 éléments de 1 , p ( 1 ) ) Plus généralement , une fois ( 1 ) ,

**29430**: , ( p 1 ) choisis , il ne reste plus qu' un seul choix pour ( p ) ( l' unique élément de Finalement , on a choix possibles pour ***construire*** , d' où le résultat

**29441**: La démonstration peut se ***faire*** plus rigoureusement par récurrence sur p. Soit p N , p 2 , et soit ( i , j ) 1 , p , i 6 j. La transposition i , j est la permutation de Sp qui échange i et j et qui laisse stable les autres entiers : Soit p N , p 2

**29517**: Toute permutation 1 , p s' écrit à l' aide de transpositions , c' est - à - ***dire*** qu' il existe des transpositions de Sp , notée 1 ,

**29627**: On a ( ) ( 1)N , où N est le nombre d' inversions , c' est - à - ***dire*** les couples ( i , j ) 1 , n tels que i j et ( i ) ( j )

**29687**: La signature est à valeurs dans 1 , 1 et : Démonstration En effet , pour le premier produit , on peut ***faire*** le changement de variable ( i , j ) ( 0 ( i ) , 0 ( j ) ) ( grâce à la bijectivité de 0 )

**29788**: Cela nous donne un moyen effectif de ***calculer*** la signature d' une permutation ( bien qu' il existe des algorithmes nettement plus performants )

**29919**: En effet : on a ( 1 ) 3 et ( 3 ) 1 , ce qui donne la transposition 1,3 Finalement , on a une décomposition en 6 transpositions : a. C' est - à - ***dire*** que l' entier en ( 2 , j ) ( deuxième ligne ) est l' image par de l' entier en ( 1 , j ) ( première ligne )

**29952**: Bien ***retenir*** qu' il suffit de regarder ce qui se passe avec les transpositions ! Formes p - linéaires sur un espace vectoriel de dimension n Soit E un K - espace vectoriel de dimension finie , soit p N

**29957**: Bien retenir qu' il suffit de ***regarder*** ce qui se passe avec les transpositions ! Formes p - linéaires sur un espace vectoriel de dimension n Soit E un K - espace vectoriel de dimension finie , soit p N

**30077**: Attention à ne pas ***confondre*** les formes p - linéaires sur E avec les formes linéaires sur E p

**30342**: D' après l' étude de Sp de la partie précédent , pour ***savoir*** si une forme p - linéaire est symétrique ou anti-symétrique , il suffit de se restreindre aux transpositions

**30358**: D' après l' étude de Sp de la partie précédent , pour savoir si une forme p - linéaire est symétrique ou anti-symétrique , il suffit de se ***restreindre*** aux transpositions

**30373**: En particulier : est symétrique si , et seulement si , ***échanger*** deux vecteurs ne change pas le signe ( ci-dessous seules les i - èmes et j - ièmes variables sont explicitées ) : est antisymétrique si , et seulement si , échanger deux vecteurs change le signe ( ci-dessous seules les i - èmes et j - ièmes variables sont explicitées ) : Soit Lp ( E , K )

**30405**: En particulier : est symétrique si , et seulement si , échanger deux vecteurs ne change pas le signe ( ci-dessous seules les i - èmes et j - ièmes variables sont explicitées ) : est antisymétrique si , et seulement si , ***échanger*** deux vecteurs change le signe ( ci-dessous seules les i - èmes et j - ièmes variables sont explicitées ) : Soit Lp ( E , K )

**30453**: Alors est antisymétrique si , et seulement si , elle est alternée , c' est - à - ***dire*** : Démonstration Soit ( x1 ,

**30554**: ) donc est antisymétrique ( car on peut se ***restreindre*** aux transpositions , voir la remarque ci - dessus )

**30558**: ) donc est antisymétrique ( car on peut se restreindre aux transpositions , ***voir*** la remarque ci - dessus )

**30702**: , xp ) est liée , cela veut ***dire*** qu' il existe i 1 , p tel que xi soit une combinaison linéaire des Puisque est linéaire par rapport à sa i - ème variable : puisque xk apparaît deux fois dans (

**30828**: , ein ) 0 dès que deux éléments sont égaux car est alternée ( ***voir*** la propriété 3.5 , page précédente )

**30846**: Dans la somme ci - dessus , on peut ***garder*** uniquement les familles ( i1 ,

**30887**: , in ) d' indices tous distincts , ce qui correspond exactement aux permutations de 1 , n. On a donc , en utilisant le fait que est antisymétrique : Pour ***conclure*** , il reste à démontrer que est une forme n - linéaire alternée non nulle

**30892**: , in ) d' indices tous distincts , ce qui correspond exactement aux permutations de 1 , n. On a donc , en utilisant le fait que est antisymétrique : Pour conclure , il reste à ***démontrer*** que est une forme n - linéaire alternée non nulle

**30951**: Par le changement de variable k ( j ) : L' application s 7 ( 0 ) 1 est une bijection de Sn dans lui-même donc on peut ***faire*** le changement ce qui démontre que D est antisymétrique

**31202**: , xn ) dans la base E et on note : a. Attention , le nombre de vecteurs doit ***être*** égal à la dimension de l' espace

**32191**: Si c' est le cas , U est inversible donc Méthodes de calcul de déterminants La formule définissant le déterminant et faisant ***intervenir*** Sn est utile théoriquement a mais inutilisable en pratique dès que n est plus grand que 4 ou 5

**32231**: Ainsi , pour ***calculer*** un déterminant d' une matrice carrée d' ordre 5 , il faut effectuer Pire encore , 60 ! ' 1082 est supérieur au nombre d' atomes observables dans l' univers , alors que les problèmes de mathématiques appliquées et d' ingénierie moderne nécessitent de traiter des matrices qui ont des centaines de milliers voire des millions de lignes ... Il faut donc trouver des méthodes plus efficaces

**32244**: Ainsi , pour calculer un déterminant d' une matrice carrée d' ordre 5 , il faut ***effectuer*** Pire encore , 60 ! ' 1082 est supérieur au nombre d' atomes observables dans l' univers , alors que les problèmes de mathématiques appliquées et d' ingénierie moderne nécessitent de traiter des matrices qui ont des centaines de milliers voire des millions de lignes ... Il faut donc trouver des méthodes plus efficaces

**32276**: Ainsi , pour calculer un déterminant d' une matrice carrée d' ordre 5 , il faut effectuer Pire encore , 60 ! ' 1082 est supérieur au nombre d' atomes observables dans l' univers , alors que les problèmes de mathématiques appliquées et d' ingénierie moderne nécessitent de ***traiter*** des matrices qui ont des centaines de milliers voire des millions de lignes ... Il faut donc trouver des méthodes plus efficaces

**32294**: Ainsi , pour calculer un déterminant d' une matrice carrée d' ordre 5 , il faut effectuer Pire encore , 60 ! ' 1082 est supérieur au nombre d' atomes observables dans l' univers , alors que les problèmes de mathématiques appliquées et d' ingénierie moderne nécessitent de traiter des matrices qui ont des centaines de milliers voire des millions de lignes ... Il faut donc ***trouver*** des méthodes plus efficaces

**32304**: a. Par exemple pour ***démontrer*** que ( ai , j ) ( i , j)1,n2 7 det ai , j ( i , j)1,n2 est polynomiale donc de classe C

**32490**: Supposons que s1,k soit l' identité pour un k 1 , n. On a d' une part ( k 1 ) k 1 mais comme est injective , ( k 1 ) 1 , k d' où ( k 1 ) k 1 , c' est - à - ***dire*** que 1,k1 est l' identité

**32698**: , Bn2 sont les colonnes d' une matrice B Mn2 , 1 ( K ) : det(B ) det(A ) car c' est une matrice triangulaire supérieure ( ***voir*** la propriété 3.12 , page précédente ) , d' où le résultat

**32899**: Ainsi , cet algorithme permet de ***calculer*** des déterminants en se ramenant à des matrices triangulaires supérieures

**32913**: On peut ***démontrer*** que le calcul du déterminant d' une matrice carrée de taille n par la méthode du pivot de Gauss nécessite un nombre d' opération de l' ordre de n3 , ce qui est bien meilleur que n!. Soit à calculer ( n 2 ) : En faisant les transvections successives ( qui conservent le déterminant ) : On fait apparaître deux lignes identiques , donc : Si a , b , c , d , e , f , g , h et i sont dans K , alors e f aei dhc gbf gec ahf dbi que l' on peut mémoriser par la règle de Sarrus : On remarque , qu' avant développement , Wxmaxima nous proposait une formule non développée , qu' on peut ré-écrire : Que se passe -t -il pour n plus grand ? On reconnaît l' expression : Soit A Mn ( K ) , soit ( k , ) 1 , n , on note a Ak , la matrice de Mn1 ( K ) obtenue à partir de A en supprimant sa k - ième ligne et sa -ième colonne

**32953**: On peut démontrer que le calcul du déterminant d' une matrice carrée de taille n par la méthode du pivot de Gauss nécessite un nombre d' opération de l' ordre de n3 , ce qui est bien meilleur que n!. Soit à ***calculer*** ( n 2 ) : En faisant les transvections successives ( qui conservent le déterminant ) : On fait apparaître deux lignes identiques , donc : Si a , b , c , d , e , f , g , h et i sont dans K , alors e f aei dhc gbf gec ahf dbi que l' on peut mémoriser par la règle de Sarrus : On remarque , qu' avant développement , Wxmaxima nous proposait une formule non développée , qu' on peut ré-écrire : Que se passe -t -il pour n plus grand ? On reconnaît l' expression : Soit A Mn ( K ) , soit ( k , ) 1 , n , on note a Ak , la matrice de Mn1 ( K ) obtenue à partir de A en supprimant sa k - ième ligne et sa -ième colonne

**32973**: On peut démontrer que le calcul du déterminant d' une matrice carrée de taille n par la méthode du pivot de Gauss nécessite un nombre d' opération de l' ordre de n3 , ce qui est bien meilleur que n!. Soit à calculer ( n 2 ) : En faisant les transvections successives ( qui conservent le déterminant ) : On fait ***apparaître*** deux lignes identiques , donc : Si a , b , c , d , e , f , g , h et i sont dans K , alors e f aei dhc gbf gec ahf dbi que l' on peut mémoriser par la règle de Sarrus : On remarque , qu' avant développement , Wxmaxima nous proposait une formule non développée , qu' on peut ré-écrire : Que se passe -t -il pour n plus grand ? On reconnaît l' expression : Soit A Mn ( K ) , soit ( k , ) 1 , n , on note a Ak , la matrice de Mn1 ( K ) obtenue à partir de A en supprimant sa k - ième ligne et sa -ième colonne

**33015**: On peut démontrer que le calcul du déterminant d' une matrice carrée de taille n par la méthode du pivot de Gauss nécessite un nombre d' opération de l' ordre de n3 , ce qui est bien meilleur que n!. Soit à calculer ( n 2 ) : En faisant les transvections successives ( qui conservent le déterminant ) : On fait apparaître deux lignes identiques , donc : Si a , b , c , d , e , f , g , h et i sont dans K , alors e f aei dhc gbf gec ahf dbi que l' on peut ***mémoriser*** par la règle de Sarrus : On remarque , qu' avant développement , Wxmaxima nous proposait une formule non développée , qu' on peut ré-écrire : Que se passe -t -il pour n plus grand ? On reconnaît l' expression : Soit A Mn ( K ) , soit ( k , ) 1 , n , on note a Ak , la matrice de Mn1 ( K ) obtenue à partir de A en supprimant sa k - ième ligne et sa -ième colonne

**33040**: On peut démontrer que le calcul du déterminant d' une matrice carrée de taille n par la méthode du pivot de Gauss nécessite un nombre d' opération de l' ordre de n3 , ce qui est bien meilleur que n!. Soit à calculer ( n 2 ) : En faisant les transvections successives ( qui conservent le déterminant ) : On fait apparaître deux lignes identiques , donc : Si a , b , c , d , e , f , g , h et i sont dans K , alors e f aei dhc gbf gec ahf dbi que l' on peut mémoriser par la règle de Sarrus : On remarque , qu' avant développement , Wxmaxima nous proposait une formule non développée , qu' on peut ***ré-écrire*** : Que se passe -t -il pour n plus grand ? On reconnaît l' expression : Soit A Mn ( K ) , soit ( k , ) 1 , n , on note a Ak , la matrice de Mn1 ( K ) obtenue à partir de A en supprimant sa k - ième ligne et sa -ième colonne

**33087**: On peut démontrer que le calcul du déterminant d' une matrice carrée de taille n par la méthode du pivot de Gauss nécessite un nombre d' opération de l' ordre de n3 , ce qui est bien meilleur que n!. Soit à calculer ( n 2 ) : En faisant les transvections successives ( qui conservent le déterminant ) : On fait apparaître deux lignes identiques , donc : Si a , b , c , d , e , f , g , h et i sont dans K , alors e f aei dhc gbf gec ahf dbi que l' on peut mémoriser par la règle de Sarrus : On remarque , qu' avant développement , Wxmaxima nous proposait une formule non développée , qu' on peut ré-écrire : Que se passe -t -il pour n plus grand ? On reconnaît l' expression : Soit A Mn ( K ) , soit ( k , ) 1 , n , on note a Ak , la matrice de Mn1 ( K ) obtenue à ***partir*** de A en supprimant sa k - ième ligne et sa -ième colonne

**33190**: on appelle comatrice de A la matrice de Mn ( K ) définie par : Cofacteur1,1 ( A ) Com(A ) Cofacteuri , j ( A)(i , j)1,n2 Cofacteurn,1 ( A ) a. Attention , cette notation peut également ***désigner*** le coefficient en ( k , ) de A. Cofacteurn,1 ( A ) Cofacteurn , n ( A ) ACom(A ) ) A Pour retrouver les signes dans la comatrice , il suffit d' alterner les signes lorsque qu' on se déplace de case en case dans la comatrice : Proposition 3.1 Développement selon une ligne ou une colonne 1

**33215**: on appelle comatrice de A la matrice de Mn ( K ) définie par : Cofacteur1,1 ( A ) Com(A ) Cofacteuri , j ( A)(i , j)1,n2 Cofacteurn,1 ( A ) a. Attention , cette notation peut également désigner le coefficient en ( k , ) de A. Cofacteurn,1 ( A ) Cofacteurn , n ( A ) ACom(A ) ) A Pour ***retrouver*** les signes dans la comatrice , il suffit d' alterner les signes lorsque qu' on se déplace de case en case dans la comatrice : Proposition 3.1 Développement selon une ligne ou une colonne 1

**33225**: on appelle comatrice de A la matrice de Mn ( K ) définie par : Cofacteur1,1 ( A ) Com(A ) Cofacteuri , j ( A)(i , j)1,n2 Cofacteurn,1 ( A ) a. Attention , cette notation peut également désigner le coefficient en ( k , ) de A. Cofacteurn,1 ( A ) Cofacteurn , n ( A ) ACom(A ) ) A Pour retrouver les signes dans la comatrice , il suffit d' ***alterner*** les signes lorsque qu' on se déplace de case en case dans la comatrice : Proposition 3.1 Développement selon une ligne ou une colonne 1

**33567**: En itérant , nous avons donc au total n ! calculs à ***faire***

**33590**: Par contre , ces formules sont très utiles lorsque la matrice comporte plein de zéros ( matrice creuse ) ou pour ***obtenir*** des formules de récurrence

**33606**: Soit ( a , b , c ) K3 , ***calculer*** : On développe suivant la première colonne , puis le cofacteur d' indice ( 2 , 1 ) suivant la première ligne

**33648**: On peut ***obtenir*** son terme général en utilisant le fait que 1 a et 2 a2 b c. On considère la fonction : C' est une fonction polynomiale en x. En effectuant les opérations élémentaires k 2 , n , Ck Ck C1 , puis en développant suivant la première colonne , on en déduit que cette fonction polynomiale est de degré inférieur ou égale à 1

**33891**: Théorème 3.2 Propriété de la comatrice Soit A Mn ( K ) , alors : En particulier , si A est inversible : Démonstration Pour i j , le coefficient en ( i , i ) de A t Com(A ) vaut , en utilisant la formule du développement suivant la i - ième ligne : ai , k Cofacteuri , k ( A ) det A Pour i 6 j , posons B la matrice obtenue à ***partir*** de A en remplaçant la j - ième ligne par la i - ème ligne de A. Puisque B a deux lignes égales , det B 0

**34025**: Cette formule est inutile pour ***calculer*** un inverse ! En effet , elle mène à des calculs trop Pour calculer l' inverse d' une matrice A , on peut par exemple utiliser la méthode du pivot de Gauss sur la matrice augmentée A In ( voir la partie sur les systèmes linéaires du chapitre précédent ) , ou résoudre , toujours avec la méthode du pivot de Gauss , un système générique A X Y , où X et Y sont dans Mn,1 ( K ) , ce qui donne X A1 Y

**34039**: Cette formule est inutile pour calculer un inverse ! En effet , elle mène à des calculs trop Pour ***calculer*** l' inverse d' une matrice A , on peut par exemple utiliser la méthode du pivot de Gauss sur la matrice augmentée A In ( voir la partie sur les systèmes linéaires du chapitre précédent ) , ou résoudre , toujours avec la méthode du pivot de Gauss , un système générique A X Y , où X et Y sont dans Mn,1 ( K ) , ce qui donne X A1 Y

**34051**: Cette formule est inutile pour calculer un inverse ! En effet , elle mène à des calculs trop Pour calculer l' inverse d' une matrice A , on peut par exemple ***utiliser*** la méthode du pivot de Gauss sur la matrice augmentée A In ( voir la partie sur les systèmes linéaires du chapitre précédent ) , ou résoudre , toujours avec la méthode du pivot de Gauss , un système générique A X Y , où X et Y sont dans Mn,1 ( K ) , ce qui donne X A1 Y

**34065**: Cette formule est inutile pour calculer un inverse ! En effet , elle mène à des calculs trop Pour calculer l' inverse d' une matrice A , on peut par exemple utiliser la méthode du pivot de Gauss sur la matrice augmentée A In ( ***voir*** la partie sur les systèmes linéaires du chapitre précédent ) , ou résoudre , toujours avec la méthode du pivot de Gauss , un système générique A X Y , où X et Y sont dans Mn,1 ( K ) , ce qui donne X A1 Y

**34078**: Cette formule est inutile pour calculer un inverse ! En effet , elle mène à des calculs trop Pour calculer l' inverse d' une matrice A , on peut par exemple utiliser la méthode du pivot de Gauss sur la matrice augmentée A In ( voir la partie sur les systèmes linéaires du chapitre précédent ) , ou ***résoudre*** , toujours avec la méthode du pivot de Gauss , un système générique A X Y , où X et Y sont dans Mn,1 ( K ) , ce qui donne X A1 Y

**34170**: Si on note A1 i , j ( i , j)1,n2 , alors l' application : est de classe C ( en particulier continue ) , donc une petite variation sur les coefficients de A provoque une petite variation sur les coefficients de A1 : on peut donc ***faire*** un calcul approché de A1 ! Faisons quelques calculs en Wxmaxima : Dans Rn , nous avons une base de référence : la base canonique Cn

**34245**: On peut alors ***interpréter*** le déterminant de la manière suivante : v deux vecteurs de R2 , alors : où ( ) désigne l' aire de , le parallélogramme construit sur v

**34278**: On peut alors ***donner*** un sens à une aire orientée en considérant le déterminant sans la valeur absolue

**34378**: On démontre alors que la relation ***avoir*** la même orientation est une relation d' équivalence sur l' ensemble des bases de E. En fixant une base E de E , nous pouvons ainsi séparer les bases de E en deux ensembles ( les deux classes d' équivalences ) : celles qui ont la même orientation que E et celles qui ne ont pas la même orientation que E

**34405**: On démontre alors que la relation avoir la même orientation est une relation d' équivalence sur l' ensemble des bases de E. En fixant une base E de E , nous pouvons ainsi ***séparer*** les bases de E en deux ensembles ( les deux classes d' équivalences ) : celles qui ont la même orientation que E et celles qui ne ont pas la même orientation que E

**34444**: On peut alors ***décréter*** arbitrairement qu' une base E est une base directe , on dit alors que E est orienté

**34489**: Dans Rn , il est bien entendu naturel de ***décréter*** que la base canonique est directe ( ce qui est cohérent avec la remarque précédente )

**34677**: Cette proposition ne est pas une méthode pratique de résolution ( il est bien plus efficace d' ***utiliser*** la méthode du pivot de Gauss )

**34696**: Elle a cependant un intérêt théorique , elle permet d' ***obtenir*** que la solution X dépend de manière continue ( et même C ) des coefficients de A et B : une petite variation sur les coefficients de A ou de B provoque une petite variation sur les coefficients de X : on peut donc faire un calcul approché de X ! Démontrer que A est inversible et que : 3.1.2 Soit V un K - espace vectoriel de dimension finie et soit p1 N , p2 N , p2 n. On considère l' ensemble des formes ( p1 p2 ) -linéaires vérifiant pour tout ( x1 ,

**34741**: Elle a cependant un intérêt théorique , elle permet d' obtenir que la solution X dépend de manière continue ( et même C ) des coefficients de A et B : une petite variation sur les coefficients de A ou de B provoque une petite variation sur les coefficients de X : on peut donc ***faire*** un calcul approché de X ! Démontrer que A est inversible et que : 3.1.2 Soit V un K - espace vectoriel de dimension finie et soit p1 N , p2 N , p2 n. On considère l' ensemble des formes ( p1 p2 ) -linéaires vérifiant pour tout ( x1 ,

**34748**: Elle a cependant un intérêt théorique , elle permet d' obtenir que la solution X dépend de manière continue ( et même C ) des coefficients de A et B : une petite variation sur les coefficients de A ou de B provoque une petite variation sur les coefficients de X : on peut donc faire un calcul approché de X ! ***Démontrer*** que A est inversible et que : 3.1.2 Soit V un K - espace vectoriel de dimension finie et soit p1 N , p2 N , p2 n. On considère l' ensemble des formes ( p1 p2 ) -linéaires vérifiant pour tout ( x1 ,

**34835**: , xp1 p2 ) V p1 p2 , toute 1 Sp1 et toute 2 Sp2 : Quelle est la dimension du sous-espace vectoriel des formes p - linéaires vérifiant cette propriété ? det(A B ) det(A)p det(B)n 3.1.4 ***Démontrer*** que le volume d' un tétraèdre de sommets A , B , C et D , vaut : det(AB , AC , AD ) 3.1.5 Calculer les déterminants suivants : 3.1.6 Soit A Mn ( K ) , démontrer que : ( a ) On suppose D inversible démontrer que Démontrer par un exemple que ce ne est pas toujours vrai si D est non inversible

**34861**: , xp1 p2 ) V p1 p2 , toute 1 Sp1 et toute 2 Sp2 : Quelle est la dimension du sous-espace vectoriel des formes p - linéaires vérifiant cette propriété ? det(A B ) det(A)p det(B)n 3.1.4 Démontrer que le volume d' un tétraèdre de sommets A , B , C et D , vaut : det(AB , AC , AD ) 3.1.5 ***Calculer*** les déterminants suivants : 3.1.6 Soit A Mn ( K ) , démontrer que : ( a ) On suppose D inversible démontrer que Démontrer par un exemple que ce ne est pas toujours vrai si D est non inversible

**34874**: , xp1 p2 ) V p1 p2 , toute 1 Sp1 et toute 2 Sp2 : Quelle est la dimension du sous-espace vectoriel des formes p - linéaires vérifiant cette propriété ? det(A B ) det(A)p det(B)n 3.1.4 Démontrer que le volume d' un tétraèdre de sommets A , B , C et D , vaut : det(AB , AC , AD ) 3.1.5 Calculer les déterminants suivants : 3.1.6 Soit A Mn ( K ) , ***démontrer*** que : ( a ) On suppose D inversible démontrer que Démontrer par un exemple que ce ne est pas toujours vrai si D est non inversible

**34884**: , xp1 p2 ) V p1 p2 , toute 1 Sp1 et toute 2 Sp2 : Quelle est la dimension du sous-espace vectoriel des formes p - linéaires vérifiant cette propriété ? det(A B ) det(A)p det(B)n 3.1.4 Démontrer que le volume d' un tétraèdre de sommets A , B , C et D , vaut : det(AB , AC , AD ) 3.1.5 Calculer les déterminants suivants : 3.1.6 Soit A Mn ( K ) , démontrer que : ( a ) On suppose D inversible ***démontrer*** que Démontrer par un exemple que ce ne est pas toujours vrai si D est non inversible

**34886**: , xp1 p2 ) V p1 p2 , toute 1 Sp1 et toute 2 Sp2 : Quelle est la dimension du sous-espace vectoriel des formes p - linéaires vérifiant cette propriété ? det(A B ) det(A)p det(B)n 3.1.4 Démontrer que le volume d' un tétraèdre de sommets A , B , C et D , vaut : det(AB , AC , AD ) 3.1.5 Calculer les déterminants suivants : 3.1.6 Soit A Mn ( K ) , démontrer que : ( a ) On suppose D inversible démontrer que ***Démontrer*** par un exemple que ce ne est pas toujours vrai si D est non inversible

**34906**: ( b ) ***Démontrer*** que pour D quelconque , ( c ) Calculer , dans le cas général det 3.1.8 On appelle décomposition LU d' une matrice A GLn ( K ) , la donnée de deux matrices L et U de Mn ( K ) telles que : L est triangulaire inférieure ( lower ) , avec des 1 sur la diagonale U est triangulaire supérieure ( upper )

**34915**: ( b ) Démontrer que pour D quelconque , ( c ) ***Calculer*** , dans le cas général det 3.1.8 On appelle décomposition LU d' une matrice A GLn ( K ) , la donnée de deux matrices L et U de Mn ( K ) telles que : L est triangulaire inférieure ( lower ) , avec des 1 sur la diagonale U est triangulaire supérieure ( upper )

**34977**: ( a ) ***Démontrer*** si une décomposition LU existe , alors elle est unique

**34992**: ( b ) ***Démontrer*** que A possède une décomposition LU si , et seulement si , tous ses mineurs principaux m1 , ... mn sont non nuls , définis par : 3.1.9 ( a ) Démontrer que si A , B , C et D sont dans Mn ( R ) et que A C C A , alors : ( b ) Démontrer que c' est faux , en général , lorsqu' il ne y a plus commutation

**35024**: ( b ) Démontrer que A possède une décomposition LU si , et seulement si , tous ses mineurs principaux m1 , ... mn sont non nuls , définis par : 3.1.9 ( a ) ***Démontrer*** que si A , B , C et D sont dans Mn ( R ) et que A C C A , alors : ( b ) Démontrer que c' est faux , en général , lorsqu' il ne y a plus commutation

**35052**: ( b ) Démontrer que A possède une décomposition LU si , et seulement si , tous ses mineurs principaux m1 , ... mn sont non nuls , définis par : 3.1.9 ( a ) Démontrer que si A , B , C et D sont dans Mn ( R ) et que A C C A , alors : ( b ) ***Démontrer*** que c' est faux , en général , lorsqu' il ne y a plus commutation

**35080**: ***Démontrer*** que : 3.1.11 Soit A Mn ( K ) avec n 2

**35094**: ***Démontrer*** que : rang(A ) n 3.1.12 Démontrer que : rang ( Com(A ) ) n 3.1.13 Soit A et B dans Mn ( R )

**35101**: Démontrer que : rang(A ) n 3.1.12 ***Démontrer*** que : rang ( Com(A ) ) n 3.1.13 Soit A et B dans Mn ( R )

**35121**: ***Résoudre*** les équations suivantes d' inconnues X Mn ( R ) : 3.1.14 À quelle(s ) condition(s ) , connaissant les affixes des milieux des côtés d' un polygone fermé à n côtés , existe -t -il un tel polygone ? Préciser dans tous les cas le procédé de construction du ou des polygone(s ) solution(s )

**35162**: Résoudre les équations suivantes d' inconnues X Mn ( R ) : 3.1.14 À quelle(s ) condition(s ) , connaissant les affixes des milieux des côtés d' un polygone fermé à n côtés , existe -t -il un tel polygone ? ***Préciser*** dans tous les cas le procédé de construction du ou des polygone(s ) solution(s )

**35189**: Que signifie géométriquement la condition de compatibilité obtenue ? 3.1.15 ***Déterminer*** les ensembles de quatre points du plan tels que la somme des distances d' un point au trois autres est constante

**35471**: Si A MatE ( u ) est la matrice de u dans une base E de E ( en dimension finie ) , alors Sp(A ) Sp(u ) et x est un vecteur propre de u si , et seulement si , MatE ( x ) est un vecteur propre de A. La recherche des valeurs propres et vecteurs propres d' un endomorphisme u ( on parle d' éléments propres ) revient à ***résoudre*** un système linéaire homogène : On utilise donc les diverses méthodes de résolution des systèmes linéaires

**35546**: Par ailleurs , comme nous avons ***travailler*** sur les lignes uniquement , les vecteurs propres sont solutions d' un système triangulaire très facile à résoudre

**35564**: Par ailleurs , comme nous avons travailler sur les lignes uniquement , les vecteurs propres sont solutions d' un système triangulaire très facile à ***résoudre***

**35569**: On peut parfois ***trouver*** des valeurs propres et les vecteurs propres directement à partir de la matrice , sans résoudre un système linéaire

**35579**: On peut parfois trouver des valeurs propres et les vecteurs propres directement à ***partir*** de la matrice , sans résoudre un système linéaire

**35585**: On peut parfois trouver des valeurs propres et les vecteurs propres directement à partir de la matrice , sans ***résoudre*** un système linéaire

**35683**: Par exemple , si n 2 et si a et b sont dans K , a 6 b , la matrice : possède les valeurs propres a ( n 1 ) b et a b ( on verra qu' il ne y en a pas d' autre ) et les espaces propres associés sont : Si E est le R - espace vectoriel des fonctions polynomiales de degré inférieur ou égal à 2 n et si k R , alors l' endomorphisme u L ( E ) défini par : Il faut parfois ***faire*** preuve de vision géométrique : si E est le R - espace vectoriel des fonctions polynomiales de degré inférieur ou égal à n et si u L ( E ) est défini par : alors alors les valeurs propres de u sont 1 et 1 et les vecteurs propres se calculent facilement dans une base adaptée

**35903**: Le polynôme caractéristique de u , noté u , correspond à la fonction polynomiale : Afin d' ***alléger*** les notations et les calculs , on note le polynôme caractéristique u sous la forme d' un polynôme formel ( voir le cours sur les polynômes ) : au lieu d' une fonction polynomiale , où X est l' indéterminée , une variable ayant les mêmes règles de calcul que celles d' une variable dans K. Ainsi , une fonction polynomiale sur K de la forme se représente par Autrement dit , X correspond à la fonction polynomiale x 7 x. On note KX le K - espace vectoriel des polynômes ( formels ) à coefficients dans K et Kn X le sousespace vectoriel de KX des polynômes de degré inférieur ou égal à n. On définit de la même manière le polynôme caractéristique A det(A X.In ) d' une matrice carrée A Mn ( K )

**35924**: Le polynôme caractéristique de u , noté u , correspond à la fonction polynomiale : Afin d' alléger les notations et les calculs , on note le polynôme caractéristique u sous la forme d' un polynôme formel ( ***voir*** le cours sur les polynômes ) : au lieu d' une fonction polynomiale , où X est l' indéterminée , une variable ayant les mêmes règles de calcul que celles d' une variable dans K. Ainsi , une fonction polynomiale sur K de la forme se représente par Autrement dit , X correspond à la fonction polynomiale x 7 x. On note KX le K - espace vectoriel des polynômes ( formels ) à coefficients dans K et Kn X le sousespace vectoriel de KX des polynômes de degré inférieur ou égal à n. On définit de la même manière le polynôme caractéristique A det(A X.In ) d' une matrice carrée A Mn ( K )

**36350**: Il pourrait ***être*** tentant de passer systématiquement par le polynôme caractéristique pour trouver les éléments propres de u , ce serait pourtant une grosse erreur , car si il nous permet de trouver les valeurs propres de u , il ne nous donne aucune information sur les espaces propres

**36353**: Il pourrait être tentant de ***passer*** systématiquement par le polynôme caractéristique pour trouver les éléments propres de u , ce serait pourtant une grosse erreur , car si il nous permet de trouver les valeurs propres de u , il ne nous donne aucune information sur les espaces propres

**36360**: Il pourrait être tentant de passer systématiquement par le polynôme caractéristique pour ***trouver*** les éléments propres de u , ce serait pourtant une grosse erreur , car si il nous permet de trouver les valeurs propres de u , il ne nous donne aucune information sur les espaces propres

**36380**: Il pourrait être tentant de passer systématiquement par le polynôme caractéristique pour trouver les éléments propres de u , ce serait pourtant une grosse erreur , car si il nous permet de ***trouver*** les valeurs propres de u , il ne nous donne aucune information sur les espaces propres

**37007**: Cependant , pour une matrice , il est fondamental de ***préciser*** le corps K dans lequel on travaille ( il est possible qu' une matrice Mn ( R ) ne soit pas diagonalisable mais qu' elle soit diagonalisable si on la voit comme une matrice de Mn ( C ) )

**37523**: C' est le seul cas où il ne est pas nécessaire de ***calculer*** les dimensions des espaces propres de u , et où l' étude du polynôme caractéristique u suffit pour démontrer que u est diagonalisable

**37542**: C' est le seul cas où il ne est pas nécessaire de calculer les dimensions des espaces propres de u , et où l' étude du polynôme caractéristique u suffit pour ***démontrer*** que u est diagonalisable

**37557**: On retrouve le fait qu' il est indispensable de ***préciser*** le corps dans lequel on se place quand on s' intéresse à la diagonalisation d' une matrice : sur C tous les polynômes non constants sont scindés , ce qui est faux sur R. La matrice de l' exemple 4.1 , page 184 ne est pas diagonalisable ( sur R ou sur C )

**37677**: 4.1.2 Diagonaliser ( c' est - à - ***dire*** démontrer qu' elle est diagonalisable et l' écrire sous la forme P D P 1 avec P GL3 ( R ) et D M3 ( R ) diagonale ) la matrice suivante : 4.1.3 Démontrer que les matrices suivantes sont semblables : 4.1.4 Diagonaliser l' endomorphisme de Kn X défini par ( pour n N ) : 4.1.5 Soit A Mn ( K ) diagonalisable et B Mp ( K ) diagonalisable , démontrer que A B est diagonalisable et préciser les éléments propres de A B en fonction de ceux de A et de B. 4.1.6 Trouver une condition nécessaire et suffisante sur A Mn ( C ) pour que soit diagonalisable 4.1.7 Démontrer que toute matrice circulante , c' est - à - dire de la forme : est diagonalisable dans Mn ( C ) et donner ses éléments propres

**37678**: 4.1.2 Diagonaliser ( c' est - à - dire ***démontrer*** qu' elle est diagonalisable et l' écrire sous la forme P D P 1 avec P GL3 ( R ) et D M3 ( R ) diagonale ) la matrice suivante : 4.1.3 Démontrer que les matrices suivantes sont semblables : 4.1.4 Diagonaliser l' endomorphisme de Kn X défini par ( pour n N ) : 4.1.5 Soit A Mn ( K ) diagonalisable et B Mp ( K ) diagonalisable , démontrer que A B est diagonalisable et préciser les éléments propres de A B en fonction de ceux de A et de B. 4.1.6 Trouver une condition nécessaire et suffisante sur A Mn ( C ) pour que soit diagonalisable 4.1.7 Démontrer que toute matrice circulante , c' est - à - dire de la forme : est diagonalisable dans Mn ( C ) et donner ses éléments propres

**37685**: 4.1.2 Diagonaliser ( c' est - à - dire démontrer qu' elle est diagonalisable et l' ***écrire*** sous la forme P D P 1 avec P GL3 ( R ) et D M3 ( R ) diagonale ) la matrice suivante : 4.1.3 Démontrer que les matrices suivantes sont semblables : 4.1.4 Diagonaliser l' endomorphisme de Kn X défini par ( pour n N ) : 4.1.5 Soit A Mn ( K ) diagonalisable et B Mp ( K ) diagonalisable , démontrer que A B est diagonalisable et préciser les éléments propres de A B en fonction de ceux de A et de B. 4.1.6 Trouver une condition nécessaire et suffisante sur A Mn ( C ) pour que soit diagonalisable 4.1.7 Démontrer que toute matrice circulante , c' est - à - dire de la forme : est diagonalisable dans Mn ( C ) et donner ses éléments propres

**37712**: 4.1.2 Diagonaliser ( c' est - à - dire démontrer qu' elle est diagonalisable et l' écrire sous la forme P D P 1 avec P GL3 ( R ) et D M3 ( R ) diagonale ) la matrice suivante : 4.1.3 ***Démontrer*** que les matrices suivantes sont semblables : 4.1.4 Diagonaliser l' endomorphisme de Kn X défini par ( pour n N ) : 4.1.5 Soit A Mn ( K ) diagonalisable et B Mp ( K ) diagonalisable , démontrer que A B est diagonalisable et préciser les éléments propres de A B en fonction de ceux de A et de B. 4.1.6 Trouver une condition nécessaire et suffisante sur A Mn ( C ) pour que soit diagonalisable 4.1.7 Démontrer que toute matrice circulante , c' est - à - dire de la forme : est diagonalisable dans Mn ( C ) et donner ses éléments propres

**37751**: 4.1.2 Diagonaliser ( c' est - à - dire démontrer qu' elle est diagonalisable et l' écrire sous la forme P D P 1 avec P GL3 ( R ) et D M3 ( R ) diagonale ) la matrice suivante : 4.1.3 Démontrer que les matrices suivantes sont semblables : 4.1.4 Diagonaliser l' endomorphisme de Kn X défini par ( pour n N ) : 4.1.5 Soit A Mn ( K ) diagonalisable et B Mp ( K ) diagonalisable , ***démontrer*** que A B est diagonalisable et préciser les éléments propres de A B en fonction de ceux de A et de B. 4.1.6 Trouver une condition nécessaire et suffisante sur A Mn ( C ) pour que soit diagonalisable 4.1.7 Démontrer que toute matrice circulante , c' est - à - dire de la forme : est diagonalisable dans Mn ( C ) et donner ses éléments propres

**37758**: 4.1.2 Diagonaliser ( c' est - à - dire démontrer qu' elle est diagonalisable et l' écrire sous la forme P D P 1 avec P GL3 ( R ) et D M3 ( R ) diagonale ) la matrice suivante : 4.1.3 Démontrer que les matrices suivantes sont semblables : 4.1.4 Diagonaliser l' endomorphisme de Kn X défini par ( pour n N ) : 4.1.5 Soit A Mn ( K ) diagonalisable et B Mp ( K ) diagonalisable , démontrer que A B est diagonalisable et ***préciser*** les éléments propres de A B en fonction de ceux de A et de B. 4.1.6 Trouver une condition nécessaire et suffisante sur A Mn ( C ) pour que soit diagonalisable 4.1.7 Démontrer que toute matrice circulante , c' est - à - dire de la forme : est diagonalisable dans Mn ( C ) et donner ses éléments propres

**37775**: 4.1.2 Diagonaliser ( c' est - à - dire démontrer qu' elle est diagonalisable et l' écrire sous la forme P D P 1 avec P GL3 ( R ) et D M3 ( R ) diagonale ) la matrice suivante : 4.1.3 Démontrer que les matrices suivantes sont semblables : 4.1.4 Diagonaliser l' endomorphisme de Kn X défini par ( pour n N ) : 4.1.5 Soit A Mn ( K ) diagonalisable et B Mp ( K ) diagonalisable , démontrer que A B est diagonalisable et préciser les éléments propres de A B en fonction de ceux de A et de B. 4.1.6 ***Trouver*** une condition nécessaire et suffisante sur A Mn ( C ) pour que soit diagonalisable 4.1.7 Démontrer que toute matrice circulante , c' est - à - dire de la forme : est diagonalisable dans Mn ( C ) et donner ses éléments propres

**37792**: 4.1.2 Diagonaliser ( c' est - à - dire démontrer qu' elle est diagonalisable et l' écrire sous la forme P D P 1 avec P GL3 ( R ) et D M3 ( R ) diagonale ) la matrice suivante : 4.1.3 Démontrer que les matrices suivantes sont semblables : 4.1.4 Diagonaliser l' endomorphisme de Kn X défini par ( pour n N ) : 4.1.5 Soit A Mn ( K ) diagonalisable et B Mp ( K ) diagonalisable , démontrer que A B est diagonalisable et préciser les éléments propres de A B en fonction de ceux de A et de B. 4.1.6 Trouver une condition nécessaire et suffisante sur A Mn ( C ) pour que soit diagonalisable 4.1.7 ***Démontrer*** que toute matrice circulante , c' est - à - dire de la forme : est diagonalisable dans Mn ( C ) et donner ses éléments propres

**37803**: 4.1.2 Diagonaliser ( c' est - à - dire démontrer qu' elle est diagonalisable et l' écrire sous la forme P D P 1 avec P GL3 ( R ) et D M3 ( R ) diagonale ) la matrice suivante : 4.1.3 Démontrer que les matrices suivantes sont semblables : 4.1.4 Diagonaliser l' endomorphisme de Kn X défini par ( pour n N ) : 4.1.5 Soit A Mn ( K ) diagonalisable et B Mp ( K ) diagonalisable , démontrer que A B est diagonalisable et préciser les éléments propres de A B en fonction de ceux de A et de B. 4.1.6 Trouver une condition nécessaire et suffisante sur A Mn ( C ) pour que soit diagonalisable 4.1.7 Démontrer que toute matrice circulante , c' est - à - ***dire*** de la forme : est diagonalisable dans Mn ( C ) et donner ses éléments propres

**37816**: 4.1.2 Diagonaliser ( c' est - à - dire démontrer qu' elle est diagonalisable et l' écrire sous la forme P D P 1 avec P GL3 ( R ) et D M3 ( R ) diagonale ) la matrice suivante : 4.1.3 Démontrer que les matrices suivantes sont semblables : 4.1.4 Diagonaliser l' endomorphisme de Kn X défini par ( pour n N ) : 4.1.5 Soit A Mn ( K ) diagonalisable et B Mp ( K ) diagonalisable , démontrer que A B est diagonalisable et préciser les éléments propres de A B en fonction de ceux de A et de B. 4.1.6 Trouver une condition nécessaire et suffisante sur A Mn ( C ) pour que soit diagonalisable 4.1.7 Démontrer que toute matrice circulante , c' est - à - dire de la forme : est diagonalisable dans Mn ( C ) et ***donner*** ses éléments propres

**37870**: À quelle condition nécessaire et suffisante la matrice M suivante est-elle diagonalisable ? 4.1.11 ***Trouver*** une condition nécessaire et suffisante pour que la matrice suivante soit diagonalisable : 4.1.12 Soit E un K - espace vectoriel de dimension finie non nulle et u L ( E )

**37904**: ***Démontrer*** l' équivalence de : ( a ) u diagonalisable ( b ) tout sous-espace de E stable par u admet un supplémentaire stable par u. 4.1.13 Trouver les valeurs propres et vecteurs propres de l' endomorphisme de Rn X défini par : Trigonalisation Soit E un K - espace vectoriel de dimension finie n 1 et soit u L ( E )

**37931**: Démontrer l' équivalence de : ( a ) u diagonalisable ( b ) tout sous-espace de E stable par u admet un supplémentaire stable par u. 4.1.13 ***Trouver*** les valeurs propres et vecteurs propres de l' endomorphisme de Rn X défini par : Trigonalisation Soit E un K - espace vectoriel de dimension finie n 1 et soit u L ( E )

**38047**: , Vn de E qui sont stables par u et tels que : Nécessairement pour tout k 1 , n , dim Vk k. u est trigonalisable si , et seulement si , il existe une base de E dans laquelle la matrice de u est triangulaire supérieure ( ***considérer*** une base ( e1 ,

**38070**: , en ) de E adaptée au drapeau , c' est - à - ***dire*** telle La diagonale de cette matrice est alors constituée des valeurs propres de u ( avec leurs multiplicités )

**38144**: De même que pour la diagonalisation , il est indispensable de ***préciser*** le corps K dans lequel on travaille

**38262**: Démontrons la réciproque par récurrence sur n dim E. Pour n 1 , il ne y a rien à ***démontrer***

**38332**: Comme e1 6 0E , on peut ***compléter*** ( e1 ) Puisque u est scindé , nécessairement N est aussi scindé

**38529**: La matrice : se trigonalise dans C. Il suffit pour ***effectuer*** la trigonalisation de suivre la démonstration du théorème

**38533**: La matrice : se trigonalise dans C. Il suffit pour effectuer la trigonalisation de ***suivre*** la démonstration du théorème

**38594**: On peut ***compléter*** en une base B1 ( e1 , e2 , e3 ) en prenant e2 c1 et e3 c2

**38615**: Bien ***vérifier*** que l' on a une base !

**38627**: Pour ***trouver*** la matrice de u dans la base B1 , on procède comme ceci : de la matrice A )

**38655**: On peut ***vérifier*** en Wxmaxima , mais il faut savoir le faire à la main ! On recommence sur la sous-matrice 2 2 : A1 est la matrice d' un endomorphisme u1 de E1 dans la base ( e2 , e3 ) , où E1 Vecte2 , e3

**38662**: On peut vérifier en Wxmaxima , mais il faut ***savoir*** le faire à la main ! On recommence sur la sous-matrice 2 2 : A1 est la matrice d' un endomorphisme u1 de E1 dans la base ( e2 , e3 ) , où E1 Vecte2 , e3

**38664**: On peut vérifier en Wxmaxima , mais il faut savoir le ***faire*** à la main ! On recommence sur la sous-matrice 2 2 : A1 est la matrice d' un endomorphisme u1 de E1 dans la base ( e2 , e3 ) , où E1 Vecte2 , e3

**38767**: Ce vecteur est exprimé dans la base ( e2 , e3 ) , c' est donc : où b1 est choisi pour ***conserver*** le vecteur propre de A et b3 est choisi pour compléter b2 en une base 4

**38778**: Ce vecteur est exprimé dans la base ( e2 , e3 ) , c' est donc : où b1 est choisi pour conserver le vecteur propre de A et b3 est choisi pour ***compléter*** b2 en une base 4

**38890**: diagonalisable , il existe une base de vecteurs propres de E donc on peut ***écrire*** : avec , pour tout i 1 , k , xi Eu ( i ) On a donc : Autrement dit , on a un système linéaire d' inconnues x1 ,

**38936**: Pour se ***ramener*** à un système linéaire d' inconnues scalaires , considérons E ? une forme linéaire

**39009**: On peut donc ***écrire*** : Puisque que ceci est vrai pour toute forme linéaire E ? et en remarquant que les i , j ne dépendent pas de ( formules de Cramer ) , on a : en utilisant le fait que F est stable par tous les uj

**39114**: Si F E , il ne y a rien à ***démontrer***

**39182**: On peut ***démontrer*** le point 2 beaucoup plus rapidement avec la notion de polynôme d' endomorphisme ( voir le chapitre suivant )

**39197**: On peut démontrer le point 2 beaucoup plus rapidement avec la notion de polynôme d' endomorphisme ( ***voir*** le chapitre suivant )

**39205**: On peut ***retenir*** cette idée : lorsqu' on a un système linéaire dont les inconnues x1 ,

**39241**: , xp sont des vecteurs d' un espace vectoriel E : ai , j .xj bi on peut ***utiliser*** la dualité

**39280**: , ( xp ) sont des scalaires , que l' on sait ***résoudre*** ( typiquement avec l' al- gorithme du pivot de Gauss )

**39452**: Alors u et v commutent ( u v v u ) si , et seulement si , ils sont co-diagonalisables , c' est - à - ***dire*** qu' ils se diagonalisent dans une même base de vecteurs propres

**39637**: Mais ces vecteurs propres sont dans Eu ( ) , donc ce sont aussi des vecteurs propres pour u. Puisque u est diagonalisable , on a D' après ce qui précède , pour toute Sp(u ) , on peut ***considérer*** une base de Eu ( ) de vecteurs propres à la fois de u et de v , donc on construit par somme directe une base de E de vecteurs propres à la fois de u et de v , donc u et v sont co-diagonalisables

**39736**: Si u et v commutent ( u v v u ) alors ils sont co-trigonalisables , c' est - à - ***dire*** qu' ils se trigonalisent dans une même base de vecteurs propres

**39768**: Démonstration On procède par récurrence sur n dim E. Si n 1 , il ne y a rien à ***démontrer***

**39834**: On démontre comme dans la démonstration du théorème 4.3 , page précédente qu' il existe un vecteur propre x commun à u et v. En particulier il est non nul donc on peut ***compléter*** ( x ) en une base E ( x , e2 ,

**40073**: On peut ***généraliser*** les résultats des théorèmes 4.3 , page précédente et 4.4 , page précédente à un nombre quelconque d' endomorphismes qui commutent deux à deux

**40099**: ***Démontrer*** que u et v sont co-diagonalisables et trouver une base de R3 pour laquelle MatC ( u ) et MatC ( v ) sont diagonales

**40107**: Démontrer que u et v sont co-diagonalisables et ***trouver*** une base de R3 pour laquelle MatC ( u ) et MatC ( v ) sont diagonales

**40151**: 4.2.2 Soit E est C - espace vectoriel de dimension finie non nulle et u et v sont deux endomorphismes de E qui vérifient : ***Démontrer*** que u et v possèdent au moins un vecteur propre commun

**40190**: 4.2.3 Soit E est C - espace vectoriel de dimension finie non nulle et u , v et w trois endomorphismes de E qui vérifient : ***Démontrer*** que u et v possèdent au moins rang(w ) valeurs propres communes ( en comptant les multiplicités )

**40241**: ***Démontrer*** que u et v sont co-trigonalisables

**40278**: Applications de la réduction Wxmaxima Python , Systèmes linéaires récurrents à coefficients constants On appelle système linéaire récurrent à coefficients constants tout ensemble d' équations récurrentes qui peut se ***mettre*** sous la forme : X0 s' appelle la condition initiale et Bn le second membre

**40361**: On peut ***utiliser*** la formule du binôme de Newton , notamment lorsque A est somme d' une matrice d' homothétie .In et d' une matrice nilpotente N ( c' est - à - dire qu' il existe p N tel que N p 0n ) : On a ainsi : Lorsque la matrice A est diagonalisable , il suffit de la diagonaliser , car si A P Diag(1 ,

**40392**: On peut utiliser la formule du binôme de Newton , notamment lorsque A est somme d' une matrice d' homothétie .In et d' une matrice nilpotente N ( c' est - à - ***dire*** qu' il existe p N tel que N p 0n ) : On a ainsi : Lorsque la matrice A est diagonalisable , il suffit de la diagonaliser , car si A P Diag(1 ,

**40462**: , p ) P 1 , Par exemple si : alors A est diagonalisable et on trouve : Dans le cas où A est trigonalisable ( ce qu' on peut toujours ***supposer*** en se plaçant dans C ) , on se contente de trigonaliser la matrice et on résout le système triangulaire associé : ce qui est facile car il est triangulaire

**40501**: Il ne est alors pas utile de ***calculer*** la matrice inverse de la matrice de passage , car on a seulement Xn P Yn

**40551**: Lorsque l' on part d' une suite récurrente multiple ( les coefficients étant constants ) , on peut vectorialiser et la ***considérer*** comme un système récurrent

**40596**: Par exemple , on peut ***transformer*** : 4.3.1 Résoudre le système récurrent : 4.3.2 Calculer les puissances de A , où ( a ) A est-elle diagonalisable ? ( b ) Calculer An , pour n N. 4.3.4 Calculer An , n N lorsque : ( a ) A est-elle diagonalisable ? ( b ) Démontrer que A est semblable à ( c ) Calculer An pour n Z. Systèmes linéaires différentiels à coefficients constants On appelle système linéaire différentiel à coefficients constants tout système d' équations différentielles qui peut se mettre sous la forme : avec I un intervalle de R et où X0 X(t0 ) est la condition initiale à l' instant t0 I. La résolution passe par : 1

**40599**: Par exemple , on peut transformer : 4.3.1 ***Résoudre*** le système récurrent : 4.3.2 Calculer les puissances de A , où ( a ) A est-elle diagonalisable ? ( b ) Calculer An , pour n N. 4.3.4 Calculer An , n N lorsque : ( a ) A est-elle diagonalisable ? ( b ) Démontrer que A est semblable à ( c ) Calculer An pour n Z. Systèmes linéaires différentiels à coefficients constants On appelle système linéaire différentiel à coefficients constants tout système d' équations différentielles qui peut se mettre sous la forme : avec I un intervalle de R et où X0 X(t0 ) est la condition initiale à l' instant t0 I. La résolution passe par : 1

**40605**: Par exemple , on peut transformer : 4.3.1 Résoudre le système récurrent : 4.3.2 ***Calculer*** les puissances de A , où ( a ) A est-elle diagonalisable ? ( b ) Calculer An , pour n N. 4.3.4 Calculer An , n N lorsque : ( a ) A est-elle diagonalisable ? ( b ) Démontrer que A est semblable à ( c ) Calculer An pour n Z. Systèmes linéaires différentiels à coefficients constants On appelle système linéaire différentiel à coefficients constants tout système d' équations différentielles qui peut se mettre sous la forme : avec I un intervalle de R et où X0 X(t0 ) est la condition initiale à l' instant t0 I. La résolution passe par : 1

**40622**: Par exemple , on peut transformer : 4.3.1 Résoudre le système récurrent : 4.3.2 Calculer les puissances de A , où ( a ) A est-elle diagonalisable ? ( b ) ***Calculer*** An , pour n N. 4.3.4 Calculer An , n N lorsque : ( a ) A est-elle diagonalisable ? ( b ) Démontrer que A est semblable à ( c ) Calculer An pour n Z. Systèmes linéaires différentiels à coefficients constants On appelle système linéaire différentiel à coefficients constants tout système d' équations différentielles qui peut se mettre sous la forme : avec I un intervalle de R et où X0 X(t0 ) est la condition initiale à l' instant t0 I. La résolution passe par : 1

**40629**: Par exemple , on peut transformer : 4.3.1 Résoudre le système récurrent : 4.3.2 Calculer les puissances de A , où ( a ) A est-elle diagonalisable ? ( b ) Calculer An , pour n N. 4.3.4 ***Calculer*** An , n N lorsque : ( a ) A est-elle diagonalisable ? ( b ) Démontrer que A est semblable à ( c ) Calculer An pour n Z. Systèmes linéaires différentiels à coefficients constants On appelle système linéaire différentiel à coefficients constants tout système d' équations différentielles qui peut se mettre sous la forme : avec I un intervalle de R et où X0 X(t0 ) est la condition initiale à l' instant t0 I. La résolution passe par : 1

**40646**: Par exemple , on peut transformer : 4.3.1 Résoudre le système récurrent : 4.3.2 Calculer les puissances de A , où ( a ) A est-elle diagonalisable ? ( b ) Calculer An , pour n N. 4.3.4 Calculer An , n N lorsque : ( a ) A est-elle diagonalisable ? ( b ) ***Démontrer*** que A est semblable à ( c ) Calculer An pour n Z. Systèmes linéaires différentiels à coefficients constants On appelle système linéaire différentiel à coefficients constants tout système d' équations différentielles qui peut se mettre sous la forme : avec I un intervalle de R et où X0 X(t0 ) est la condition initiale à l' instant t0 I. La résolution passe par : 1

**40655**: Par exemple , on peut transformer : 4.3.1 Résoudre le système récurrent : 4.3.2 Calculer les puissances de A , où ( a ) A est-elle diagonalisable ? ( b ) Calculer An , pour n N. 4.3.4 Calculer An , n N lorsque : ( a ) A est-elle diagonalisable ? ( b ) Démontrer que A est semblable à ( c ) ***Calculer*** An pour n Z. Systèmes linéaires différentiels à coefficients constants On appelle système linéaire différentiel à coefficients constants tout système d' équations différentielles qui peut se mettre sous la forme : avec I un intervalle de R et où X0 X(t0 ) est la condition initiale à l' instant t0 I. La résolution passe par : 1

**40682**: Par exemple , on peut transformer : 4.3.1 Résoudre le système récurrent : 4.3.2 Calculer les puissances de A , où ( a ) A est-elle diagonalisable ? ( b ) Calculer An , pour n N. 4.3.4 Calculer An , n N lorsque : ( a ) A est-elle diagonalisable ? ( b ) Démontrer que A est semblable à ( c ) Calculer An pour n Z. Systèmes linéaires différentiels à coefficients constants On appelle système linéaire différentiel à coefficients constants tout système d' équations différentielles qui peut se ***mettre*** sous la forme : avec I un intervalle de R et où X0 X(t0 ) est la condition initiale à l' instant t0 I. La résolution passe par : 1

**40769**: Lorsque l' on part d' une équation différentielle linéaire d' ordre p , à coefficients constants de la forme : on peut la vectorialiser , pour se ***ramener*** à un système en posant Par exemple , on peut transformer : Le cas où la matrice A est diagonalisable est facile car si A P D P 1 avec D Diag(1 ,

**40780**: Lorsque l' on part d' une équation différentielle linéaire d' ordre p , à coefficients constants de la forme : on peut la vectorialiser , pour se ramener à un système en posant Par exemple , on peut ***transformer*** : Le cas où la matrice A est diagonalisable est facile car si A P D P 1 avec D Diag(1 ,

**40866**: En particulier , on a jamais besoin de ***calculer*** l' inverse de P

**40886**: Par exemple , en reprenant le système de la remarque précédente ( obtenu à ***partir*** de 00 ( t ) ( t ) 0 ) , on a Il ne est pas difficile de démontrer que A est diagonalisable sur C , ses valeurs propres sont i et En posant Y P 1 X , on a le système donc il existe ( c1 , c2 ) C2 tel que : Si on ajoute la condition initiale ( qui correspond à ( 0 ) 1 et 0 ( 0 ) 0 ) , on trouve c1 c2 21 donc en particulier : exp(i t ) exp(i t ) On retrouve donc la solution bien connue de 00 ( t ) ( t ) 0 , ( 0 ) 1 et 0 ( 0 ) 0

**40906**: Par exemple , en reprenant le système de la remarque précédente ( obtenu à partir de 00 ( t ) ( t ) 0 ) , on a Il ne est pas difficile de ***démontrer*** que A est diagonalisable sur C , ses valeurs propres sont i et En posant Y P 1 X , on a le système donc il existe ( c1 , c2 ) C2 tel que : Si on ajoute la condition initiale ( qui correspond à ( 0 ) 1 et 0 ( 0 ) 0 ) , on trouve c1 c2 21 donc en particulier : exp(i t ) exp(i t ) On retrouve donc la solution bien connue de 00 ( t ) ( t ) 0 , ( 0 ) 1 et 0 ( 0 ) 0

**41084**: On est donc ramené ( par la même démarche qu' à l' exemple précédent en posant Y ( t ) P 1 X(t ) ) à un système de la forme où T est une matrice triangulaire supérieure que l' on peut ***résoudre*** facilement et on revient à X grâce à la relation X(t ) P Y ( t )

**41108**: 4.4.1 Résoudre 4.4.2 Résoudre 4.4.3 ***Résoudre*** le système différentiel : 4.4.4 Soit A M3 ( R ) non inversible

**41123**: ***Démontrer*** que les solutions de X 0 A X sont des courbes planes

**41138**: 4.4.5 ***Résoudre*** le système différentiel 4.4.6 Déterminer les a R tels que le système admette au moins une solution non nulle bornée au voisinage de

**41143**: 4.4.5 Résoudre le système différentiel 4.4.6 ***Déterminer*** les a R tels que le système admette au moins une solution non nulle bornée au voisinage de

**41229**: Si u est diagonalisable et E1 est un sous-espace vectoriel stable par u , alors : ( ***voir*** la propriété 4.6 , page 203 )

**41428**: ide ) H. I Ces résultats suffisent en général lorsque l' on est en dimension 3 , car il ne y a que les droites dirigées par un vecteur propre et les hyperplans qui peuvent ***être*** stables ( avec en plus , bien évidemment , 0E Soit la matrice a : Le polynôme caractéristique est bien X 3

**41506**: ***Démontrer*** que u laisse un plan stable

**41532**: 4.5.2 Soit E Rn , Sn , on note T l' application de E dans E définie par ***Démontrer*** que T est dans GL ( E )

**41542**: ***Trouver*** les sous-espaces vectoriels F de E tels que , pour tout 4.5.3 Trouver tous les sous-espaces stables de la matrice : 4.5.4 Soit E un K - espace vectoriel de dimension finie n 1 et f L ( E ) telle que f n 0L ( E ) et f n1 6 0L ( E )

**41600**: ***Démontrer*** que les sous espaces stables par f sont les Ker(f k ) pour k 0 , n. 4.5.5 Soit E un C - espace vectoriel de dimension finie n 1 et u L(E )

**41639**: ( a ) ***Démontrer*** que si u ne admet qu' un nombre fini de sous-espaces vectoriels stables alors chaque sous-espace propre est de dimension 1

**41683**: ( b ) Quels sont les sous-espaces vectoriels stables par u si un 0L ( E ) ? ( c ) ***Démontrer*** la réciproque de la question ( a )

**41713**: ***Démontrer*** que u est diagonalisable si , et seulement si , le polynôme caractéristique u de u est scindé et que tout sous-espace vectoriel de E stable par u admet un supplémentaire stable

**41763**: 4.5.7 On considère dans R3 l' endomorphisme f dont la matrice dans la base canonique est ***Déterminer*** les sous-espaces vectoriels de R3 qui sont stables par f

**42108**: Ainsi , ***connaître*** les racines d' un polynôme annulateur de u ne donne que des candidats potentiels pour les valeurs propres de u. Le lemme des noyaux Théorème 5.1 dit lemme des noyaux Soit E un K - espace vectoriel et u L ( E )

**42459**: On a donc P ( u ) 0L ( E ) , c' est - à - ***dire*** que P est un polynôme annulateur de u scindé à racines simples

**42951**: c' est - à - ***dire*** que Soit E un K - espace vectoriel de dimension finie non nulle et soit u L ( E )

**43041**: Le polynôme minimal de u est l' unique polynôme unitaire de degré 1 u KX tel que Autrement dit , si P KX est annulateur de u , alors il existe Q KX tel que P u Q. L' existence et l' unicité du polynôme minimal sont assurées par le fait que KX est principal et que Iu est un idéal de KX non réduit à 0KX ( ***voir*** le cours sur les anneaux )

**43349**: idE ne est pas injectif , c' est - à - ***dire*** que Sp(u )

**43786**: Le théorème de Cayley - Hamilton peut se ***reformuler*** ainsi : le polynôme minimal u divise le polynôme caractéristique u

**43823**: En particulier , puisque deg u dim E et u 6 0KX , on a : 1 deg u dim E On peut également ***démontrer*** ce théorème sans passer par la notion de matrice compagnon , en le démontrant d' abord dans le cas d' une matrice trigonalisable ( en utilisant notamment le fait que dans ce cas son polynôme caractéristique est scindé )

**43827**: En particulier , puisque deg u dim E et u 6 0KX , on a : 1 deg u dim E On peut également démontrer ce théorème sans ***passer*** par la notion de matrice compagnon , en le démontrant d' abord dans le cas d' une matrice trigonalisable ( en utilisant notamment le fait que dans ce cas son polynôme caractéristique est scindé )

**43870**: Mais on peut toujours s' y ***ramener*** en se plaçant dans le corps des racines de A u avec A la matrice de u dans une base de E ( dans le cas où K R , cela revient à considérer A comme une matrice à coefficients dans C )

**43904**: Mais on peut toujours s' y ramener en se plaçant dans le corps des racines de A u avec A la matrice de u dans une base de E ( dans le cas où K R , cela revient à ***considérer*** A comme une matrice à coefficients dans C )

**43926**: On peut également , dans le cas K R ou C ***utiliser*** un argument topologique ( voir la partie suivante )

**43931**: On peut également , dans le cas K R ou C utiliser un argument topologique ( ***voir*** la partie suivante )

**44016**: Retour sur le calcul de puissances de matrices Lorsqu' on connaît un polynôme annulateur P KX d' une matrice A Mp ( K ) , pour ***calculer*** An on peut utiliser la division euclidienne de X n par P : La matrice : a pour polynôme annulateur ( X 2)3 donc : 5.1.1 Pour les matrices suivantes , préciser les polynômes caractéristiques , minimaux , espaces propres et préciser si elles sont diagonalisables ( dans Mn ( C ) ) : ( a ) Dk ( ) ( matrice de dilatation ) ( b ) Tk , ( ) ( matrice de transvection ) ( c ) P ( matrice de permutation )

**44020**: Retour sur le calcul de puissances de matrices Lorsqu' on connaît un polynôme annulateur P KX d' une matrice A Mp ( K ) , pour calculer An on peut ***utiliser*** la division euclidienne de X n par P : La matrice : a pour polynôme annulateur ( X 2)3 donc : 5.1.1 Pour les matrices suivantes , préciser les polynômes caractéristiques , minimaux , espaces propres et préciser si elles sont diagonalisables ( dans Mn ( C ) ) : ( a ) Dk ( ) ( matrice de dilatation ) ( b ) Tk , ( ) ( matrice de transvection ) ( c ) P ( matrice de permutation )

**44048**: Retour sur le calcul de puissances de matrices Lorsqu' on connaît un polynôme annulateur P KX d' une matrice A Mp ( K ) , pour calculer An on peut utiliser la division euclidienne de X n par P : La matrice : a pour polynôme annulateur ( X 2)3 donc : 5.1.1 Pour les matrices suivantes , ***préciser*** les polynômes caractéristiques , minimaux , espaces propres et préciser si elles sont diagonalisables ( dans Mn ( C ) ) : ( a ) Dk ( ) ( matrice de dilatation ) ( b ) Tk , ( ) ( matrice de transvection ) ( c ) P ( matrice de permutation )

**44058**: Retour sur le calcul de puissances de matrices Lorsqu' on connaît un polynôme annulateur P KX d' une matrice A Mp ( K ) , pour calculer An on peut utiliser la division euclidienne de X n par P : La matrice : a pour polynôme annulateur ( X 2)3 donc : 5.1.1 Pour les matrices suivantes , préciser les polynômes caractéristiques , minimaux , espaces propres et ***préciser*** si elles sont diagonalisables ( dans Mn ( C ) ) : ( a ) Dk ( ) ( matrice de dilatation ) ( b ) Tk , ( ) ( matrice de transvection ) ( c ) P ( matrice de permutation )

**44131**: Quelle est la structure algébrique de E ? ***Démontrer*** que si A E vérifie Ap I2 pour un p N , alors A12 I2

**44174**: ( a ) ***Démontrer*** qu' il existe un unique polynôme unitaire P KX vérifiant : On note mx ce polynôme

**44204**: ( b ) Soit mx et my premiers deux à deux , ***démontrer*** que mxy mx my

**44213**: ( c ) ***Démontrer*** que le polynôme minimal f de f vérifie : iii

**44255**: 5.1.5 Soit E un C - espace vectoriel de dimension finie non nulle et u L ( E ) , ***donner*** une condition nécessaire et suffisante pour que : u2 diagonalisable u diagonalisable Que devient ce résultat lorsque le corps est R ? 5.1.6 Soit A Mn ( R ) telle que A3 3 A 2 In 0n

**44298**: A est-elle diagonalisable ? ***Calculer*** Ap pour p Z. Topologie sur les endomorphismes Soit ( E , k k ) un espace vectoriel normé a , on peut munir Lc ( E ) ( l' espace des endomorphismes continus de E ) de la norme subordonnée donnée par : On a alors : De plus , est une norme d' algèbre : Si E est de dimension finie , tous les endomorphismes sont continues : Lc ( E ) L ( E ) ( c' est faux en dimension infinie )

**44322**: A est-elle diagonalisable ? Calculer Ap pour p Z. Topologie sur les endomorphismes Soit ( E , k k ) un espace vectoriel normé a , on peut ***munir*** Lc ( E ) ( l' espace des endomorphismes continus de E ) de la norme subordonnée donnée par : On a alors : De plus , est une norme d' algèbre : Si E est de dimension finie , tous les endomorphismes sont continues : Lc ( E ) L ( E ) ( c' est faux en dimension infinie )

**44791**: Ces propriétés de densité sont utiles pour ***démontrer*** des résultats sur L ( E ) : on démontre le résultat pour les endomorphismes inversibles ou digonalisables , puis on étend le résultat par densité ( voir les exercices 5.2 , page 244 )

**44819**: Ces propriétés de densité sont utiles pour démontrer des résultats sur L ( E ) : on démontre le résultat pour les endomorphismes inversibles ou digonalisables , puis on étend le résultat par densité ( ***voir*** les exercices 5.2 , page 244 )

**45021**: On Un calcul démontre que : donc en particulier : Posons alors : D' après ce qui précède : Par conséquent , pour tout 0 , si 0 est assez petit : Il reste alors à ***vérifier*** que A , est une norme subordonnée ( ce qui donne alors l' inégalité AA , ( A ) d' après la remarque 5.10 , de la présente page )

**45110**: Dans beaucoup d' applications , on s' intéresse à des suites récurrentes de la forme : par exemple pour ***résoudre*** de manière approchée des équations différentielles ou des équations aux dérivées partielles

**45141**: Il est souvent crucial que la suite ( Uk ) kN soit bornée ( par exemple pour ***garantir*** la stabilité du schéma numérique considéré )

**45215**: La propriété précédente implique que : ( Ak ) kN est bornée , alors ( A ) 1 et si ( A ) 1 alors ( Ak ) kN est bornée Ainsi , le calcul du rayon spectral de A ( souvent calculé de manière approchée dans les applications ) nous permet de ***démontrer*** la stabilité d' une méthode numérique

**45437**: k est normale sur tous les disques u L' argument ci - dessus démontre que la convergence de L ( E ) , u r avec r 0 , R. Pour tout k N , u 7 ak .uk est continue , donc u 7 k0 ak .u est continu sur u L ( E ) , u r pour tout r 0 , R , donc sur u L ( E ) , u R. On peut ainsi ***parler*** d' exponentielle , de sinus , de logarithmes , etc. d' endomorphismes ou de matrices

**45631**: Immédiat à ***partir*** de la définition

**45722**: L' exponentielle de matrices sert notamment pour ***étudier*** les systèmes linéaires différentiels à coefficients constants ( voir le chapitre 4 ) : La solution vérifiant la condition initiale X(t0 ) X0 est donnée par : exp(s

**45731**: L' exponentielle de matrices sert notamment pour étudier les systèmes linéaires différentiels à coefficients constants ( ***voir*** le chapitre 4 ) : La solution vérifiant la condition initiale X(t0 ) X0 est donnée par : exp(s

**45769**: A ) Pour ***calculer*** exp(t

**45779**: ***Calculer*** An puis sommer la série n t n!.A ( c' est rarement une méthode efficace )

**45782**: Calculer An puis ***sommer*** la série n t n!.A ( c' est rarement une méthode efficace )

**45821**: , p ) P 1 , on a : ( ***voir*** le code ci-dessous )

**45836**: Dans le cas général , on peut ***utiliser*** la décomposition de Dunford ( voir la partie suivante )

**45842**: Dans le cas général , on peut utiliser la décomposition de Dunford ( ***voir*** la partie suivante )

**45865**: I Cependant , si la matrice ne est pas diagonalisable , il est souvent plus efficace pour ***résoudre*** un système linéaire différentielle de trigonaliser la matrice A et de résoudre un système différentiel triangulaire ( voir le chapitre 4 )

**45877**: I Cependant , si la matrice ne est pas diagonalisable , il est souvent plus efficace pour résoudre un système linéaire différentielle de trigonaliser la matrice A et de ***résoudre*** un système différentiel triangulaire ( voir le chapitre 4 )

**45883**: I Cependant , si la matrice ne est pas diagonalisable , il est souvent plus efficace pour résoudre un système linéaire différentielle de trigonaliser la matrice A et de résoudre un système différentiel triangulaire ( ***voir*** le chapitre 4 )

**45910**: ( a ) ***Démontrer*** que u 7 u est continue de L ( E ) dans Kn X. ( b ) En déduire par un argument de densité que : ( c ) Démontrer que le résultat est encore vrai dans ne importe quel corps K et ne importe quel K - espace vectoriel E ( par un argument algébrique )

**45929**: ( a ) Démontrer que u 7 u est continue de L ( E ) dans Kn X. ( b ) En ***déduire*** par un argument de densité que : ( c ) Démontrer que le résultat est encore vrai dans ne importe quel corps K et ne importe quel K - espace vectoriel E ( par un argument algébrique )

**45940**: ( a ) Démontrer que u 7 u est continue de L ( E ) dans Kn X. ( b ) En déduire par un argument de densité que : ( c ) ***Démontrer*** que le résultat est encore vrai dans ne importe quel corps K et ne importe quel K - espace vectoriel E ( par un argument algébrique )

**45970**: 5.2.2 ***Démontrer*** le théorème de Cayley - Hamilton pour K C par un argument de densité

**46007**: ( a ) ***Démontrer*** que l' intérieur de l' ensemble des endomorphismes de E diagonalisables est l' ensemble des endomorphismes de E diagonalisables avec n valeurs propres distinctes

**46036**: ( b ) ***Démontrer*** que l' adhérence des endomorphismes de E diagonalisables est l' ensemble des endomorphismes de E trigonalisables

**46057**: ( a ) ***Démontrer*** que p A Mn ( R ) , rang A p est fermé dans Mn ( R )

**46080**: ( b ) ***Déterminer*** l' adhérence de p A Mn ( R ) , rang A p dans Mn ( R )

**46116**: ***Démontrer*** que : 5.2.6 Démontrer que : A Mn ( C ) , det(exp(A ) ) exp(trace(A ) ) Décomposition de Dunford Soit E un K - espace vectoriel de dimension finie non nulle et u L ( E ) nilpotent a

**46120**: Démontrer que : 5.2.6 ***Démontrer*** que : A Mn ( C ) , det(exp(A ) ) exp(trace(A ) ) Décomposition de Dunford Soit E un K - espace vectoriel de dimension finie non nulle et u L ( E ) nilpotent a

**46174**: Alors : u ( 1)dim E X dim E a. C' est - à - ***dire*** qu' il existe p N tel que up 0L ( E )

**46746**: En particulier , les projecteurs sur les espaces propres sont des polynômes en u. Il est toujours possible de se ***ramener*** au cas où u est scindé en se plaçant dans le corps des racines de u ( si K R , on se place dans K C )

**46901**: D' après le point 2 , il suffit de ***définir*** d et n sur chacun des Fu ( k ) : Par construction d est diagonalisable

**46960**: ***Voir*** la remarque ci-dessous

**46967**: On peut ***démontrer*** que d et n sont des polynômes en u , puisque ( en reprenant les notations de la En particulier , le couple ( d , n ) est unique

**47039**: Si ( d0 , n0 ) est un autre couple convenant , alors d0 et n0 ( qui sont des polynômes en u ) commutent avec u donc avec d et n. Ainsi , d et d0 sont co-diagonalisables ( ***voir*** le théorème 4.3 , page 205 du chapitre 4 ) donc d d0 n n0 est diagonalisable

**47168**: En effet , on a ( u ) ( u , 0L ( E ) ) pour tout u L ( E ) diagonalisable donc si était continue , par densité des endomorphismes diagonalisables ( proposition 5.2 , page 238 ) , on aurait ( u ) ( u , 0L ( E ) ) pour tout u L ( E ) , c' est - à - ***dire*** que tout endomorphisme serait diagonalisable

**47232**: On peut se ***servir*** de la décomposition de Dunford pour calculer les puissances An ou l' exponentielle exp(A ) d' une matrice carrée A. Soit A D N avec D diagonalisable et N nilpotent la décomposition de Dunford de A. On note q l' indice de nilpotence de N ( le plus petit entier q N tel que N q 0n )

**47239**: On peut se servir de la décomposition de Dunford pour ***calculer*** les puissances An ou l' exponentielle exp(A ) d' une matrice carrée A. Soit A D N avec D diagonalisable et N nilpotent la décomposition de Dunford de A. On note q l' indice de nilpotence de N ( le plus petit entier q N tel que N q 0n )

**47329**: Puisque D et N commutent , on a d' après la formule du binôme de Newton : Puisque D et N commutent , on a : exp(A ) exp(D ) exp(N ) On a déjà vu comment ***calculer*** l' exponentielle d' une matrice diagonalisable

**47367**: on prend une base E de E adaptée à la décomposition de E en espaces caractéristiques , pour ***obtenir*** la matrice A de u dans cette base sous la forme d' une matrice diagonale par blocs : 2

**47395**: on trigonalise Bk de manière à la ***mettre*** sous la forme : Bk k .Ink Nk où Nk est triangulaire supérieure nilpotente

**47426**: I Mais ces méthodes sont fastidieuses ( et peu adaptées au calcul numérique approchée , ***voir*** la remarque 5.15 , page précédente )

**47438**: On préfère donc ***passer*** par la trigonalisation de A et résoudre des systèmes triangulaires

**47445**: On préfère donc passer par la trigonalisation de A et ***résoudre*** des systèmes triangulaires

**47733**: Si on veut ***déterminer*** C ( u ) , on peut utiliser la décomposition de Dunford : u d n , d diagonalisable , n nilpotent , et qui commutent ce qui revient à trouver C ( d ) ( on utilise ce qui précède ) et C ( n )

**47741**: Si on veut déterminer C ( u ) , on peut ***utiliser*** la décomposition de Dunford : u d n , d diagonalisable , n nilpotent , et qui commutent ce qui revient à trouver C ( d ) ( on utilise ce qui précède ) et C ( n )

**47764**: Si on veut déterminer C ( u ) , on peut utiliser la décomposition de Dunford : u d n , d diagonalisable , n nilpotent , et qui commutent ce qui revient à ***trouver*** C ( d ) ( on utilise ce qui précède ) et C ( n )

**47786**: On doit donc maintenant ***étudier*** ce qui se passe pour un endomorphisme nilpotent

**47865**: Alors il existe une base E de E pour laquelle : où les blocs Bk , appelés blocs de Jordan , sont soit nuls , soit de la forme : Démonstration On passe par les invariants de similitude ( ***voir*** la dernière partie ) : si ( P1 ,

**47961**: On conclut alors en appliquant la réduction de Frobenius à u. On peut aussi le ***démontrer*** directement ( voir l' exercice 5.3.11 , page 251 )

**47964**: On conclut alors en appliquant la réduction de Frobenius à u. On peut aussi le démontrer directement ( ***voir*** l' exercice 5.3.11 , page 251 )

**48135**: Lorsque les valeurs propres sont confondues , il y a de mauvaises surprises , ainsi : 5.3.1 ***Trouver*** le commutant de la matrice : 5.3.2 Soit E un C - espace vectoriel de dimension finie n 1 et soit u L(E )

**48161**: ***Démontrer*** qu' il existe des entiers n1 ,

**48178**: , np ( avec p à ***déterminer*** ) tels que : 5.3.3 Soit E un C - espace vectoriel de dimension finie de dimension n , soit f1 ,

**48216**: ***Démontrer*** que 5.3.4 Soit E un K - espace vectoriel de dimension n 1 et f L(E ) telle que f n1 6 0L ( E ) et f n 0L ( E )

**48254**: ( b ) ***Démontrer*** que l' ensemble des endomorphismes qui commutent avec f est un sous-espace vectoriel de L ( E ) de base 5.3.5 Soit E un K - espace vectoriel de dimension 2 et u L ( E ) qui ne est pas une homothétie

**48299**: ***Déterminer*** la dimension du commutant de u. 5.3.6 Soit ( a , b , c ) K3

**48317**: ***Calculer*** la dimension du commutant de 5.3.7 Soit A une matrice réelle triangulaire supérieure

**48332**: ***Démontrer*** qu' elle commute avec sa transposée si , et seulement si , elle est diagonale

**48370**: ( a ) ***Démontrer*** que est de dimension au moins n. ( b ) Démontrer que si A Mn ( C ) alors son commutant est de dimension au moins n. ( c ) Que dire d' une matrice A de Mn ( C ) dont le commutant est égal à l' ensemble CA ? 5.3.9 Pour quels entiers n le groupe GLn ( R ) admet -il un sous-groupe isomorphe à Z4 Z ? ( a ) Démontrer que A est semblable à : ( b ) Trouver les matrices réelles qui commutent avec A. 5.3.11 Soit E un K - espace vectoriel et u L ( E ) un endomorphisme nilpotent de E. Soit q l' indice de nilpotence de u : Soit x E tel que : ( a ) Démontrer que la famille x , u(x ) ,

**48381**: ( a ) Démontrer que est de dimension au moins n. ( b ) ***Démontrer*** que si A Mn ( C ) alors son commutant est de dimension au moins n. ( c ) Que dire d' une matrice A de Mn ( C ) dont le commutant est égal à l' ensemble CA ? 5.3.9 Pour quels entiers n le groupe GLn ( R ) admet -il un sous-groupe isomorphe à Z4 Z ? ( a ) Démontrer que A est semblable à : ( b ) Trouver les matrices réelles qui commutent avec A. 5.3.11 Soit E un K - espace vectoriel et u L ( E ) un endomorphisme nilpotent de E. Soit q l' indice de nilpotence de u : Soit x E tel que : ( a ) Démontrer que la famille x , u(x ) ,

**48402**: ( a ) Démontrer que est de dimension au moins n. ( b ) Démontrer que si A Mn ( C ) alors son commutant est de dimension au moins n. ( c ) Que ***dire*** d' une matrice A de Mn ( C ) dont le commutant est égal à l' ensemble CA ? 5.3.9 Pour quels entiers n le groupe GLn ( R ) admet -il un sous-groupe isomorphe à Z4 Z ? ( a ) Démontrer que A est semblable à : ( b ) Trouver les matrices réelles qui commutent avec A. 5.3.11 Soit E un K - espace vectoriel et u L ( E ) un endomorphisme nilpotent de E. Soit q l' indice de nilpotence de u : Soit x E tel que : ( a ) Démontrer que la famille x , u(x ) ,

**48445**: ( a ) Démontrer que est de dimension au moins n. ( b ) Démontrer que si A Mn ( C ) alors son commutant est de dimension au moins n. ( c ) Que dire d' une matrice A de Mn ( C ) dont le commutant est égal à l' ensemble CA ? 5.3.9 Pour quels entiers n le groupe GLn ( R ) admet -il un sous-groupe isomorphe à Z4 Z ? ( a ) ***Démontrer*** que A est semblable à : ( b ) Trouver les matrices réelles qui commutent avec A. 5.3.11 Soit E un K - espace vectoriel et u L ( E ) un endomorphisme nilpotent de E. Soit q l' indice de nilpotence de u : Soit x E tel que : ( a ) Démontrer que la famille x , u(x ) ,

**48455**: ( a ) Démontrer que est de dimension au moins n. ( b ) Démontrer que si A Mn ( C ) alors son commutant est de dimension au moins n. ( c ) Que dire d' une matrice A de Mn ( C ) dont le commutant est égal à l' ensemble CA ? 5.3.9 Pour quels entiers n le groupe GLn ( R ) admet -il un sous-groupe isomorphe à Z4 Z ? ( a ) Démontrer que A est semblable à : ( b ) ***Trouver*** les matrices réelles qui commutent avec A. 5.3.11 Soit E un K - espace vectoriel et u L ( E ) un endomorphisme nilpotent de E. Soit q l' indice de nilpotence de u : Soit x E tel que : ( a ) Démontrer que la famille x , u(x ) ,

**48500**: ( a ) Démontrer que est de dimension au moins n. ( b ) Démontrer que si A Mn ( C ) alors son commutant est de dimension au moins n. ( c ) Que dire d' une matrice A de Mn ( C ) dont le commutant est égal à l' ensemble CA ? 5.3.9 Pour quels entiers n le groupe GLn ( R ) admet -il un sous-groupe isomorphe à Z4 Z ? ( a ) Démontrer que A est semblable à : ( b ) Trouver les matrices réelles qui commutent avec A. 5.3.11 Soit E un K - espace vectoriel et u L ( E ) un endomorphisme nilpotent de E. Soit q l' indice de nilpotence de u : Soit x E tel que : ( a ) ***Démontrer*** que la famille x , u(x ) ,

**48524**: ( b ) En ***déduire*** que si E est de dimension finie alors dim E q. I On pose E1 Vect x , u(x ) ,

**48591**: , uq1 ( x ) et on suppose que E est de dimension finie n p. I Par ailleurs , soit E ? une forme linéaire telle que : On pose alors : I Finalement , on pose : ( c ) ***Justifier*** l' existence de

**48606**: ( d ) Quelle est la dimension de ? ( ***Justifier*** )

**48620**: ( e ) Quelle est la dimension de G ? ( ***Justifier*** )

**48626**: ( f ) ***Démontrer*** que : ( g ) Démontrer que : ( h ) En déduire la proposition 5.3 , page 249 Résolution d' équations matricielles Nous allons nous intéresser à deux types d' équations : 1

**48632**: ( f ) Démontrer que : ( g ) ***Démontrer*** que : ( h ) En déduire la proposition 5.3 , page 249 Résolution d' équations matricielles Nous allons nous intéresser à deux types d' équations : 1

**48639**: ( f ) Démontrer que : ( g ) Démontrer que : ( h ) En ***déduire*** la proposition 5.3 , page 249 Résolution d' équations matricielles Nous allons nous intéresser à deux types d' équations : 1

**48653**: ( f ) Démontrer que : ( g ) Démontrer que : ( h ) En déduire la proposition 5.3 , page 249 Résolution d' équations matricielles Nous allons nous ***intéresser*** à deux types d' équations : 1

**48697**: Extraction de racine : soit A Mn ( K ) et p N , existe -t -il des matrices B telles que B p A ? Et si c' est le cas , comment les ***trouver*** toutes ? 2

**48738**: Logarithme : soit A Mn ( K ) ( K R ou C ) , existe -t -il des matrices B telles que B p A ? Et si c' est le cas , comment les ***trouver*** toutes ? L' extraction de racine possède deux propriétés immédiates : 1

**48957**: On doit donc ***résoudre*** B13 I2 et 3 2

**49022**: On en déduit que B1 est diagonalisable dans C , égale à I2 ou semblable à Diag(j , j 2 ) avec j exp(2 i 3 ) , ce qui ramené dans R nous donne : Finalement , les B qui conviennent vérifient : Le calcul brutal ne est pas efficace ! Même si l' on pense à ***montrer*** que B C ( A )

**49093**: On obtient : Il vient alors : que l' on peut ***résoudre*** en utilisant le développement en série entière de x 7 ( 1 x)1p et le fait que la matrice D0 N 0 est nilpotente

**49225**: En utilisant la série entière du logarithme , on a donc : où p est l' indice de nilpotence de N , c' est - à - ***dire*** le plus petit entier p N tel que N p 0n

**49261**: Avec Wxmaxima : Soit n N , existe -t -il h L ( RX ) tel que hn T ? Si oui , ***déterminer*** h. 5.4.2 Quelles sont les A GL2 ( R ) telles qu' il existe X GL2 ( R ) telle que A X 3 ? 5.4.3 Démontrer que exp Mn ( C ) GLn ( C ) 5.4.4 ( a ) Démontrer que si A Mn ( C ) vérifie exp(A ) In , alors A est diagonalisable

**49288**: Avec Wxmaxima : Soit n N , existe -t -il h L ( RX ) tel que hn T ? Si oui , déterminer h. 5.4.2 Quelles sont les A GL2 ( R ) telles qu' il existe X GL2 ( R ) telle que A X 3 ? 5.4.3 ***Démontrer*** que exp Mn ( C ) GLn ( C ) 5.4.4 ( a ) Démontrer que si A Mn ( C ) vérifie exp(A ) In , alors A est diagonalisable

**49303**: Avec Wxmaxima : Soit n N , existe -t -il h L ( RX ) tel que hn T ? Si oui , déterminer h. 5.4.2 Quelles sont les A GL2 ( R ) telles qu' il existe X GL2 ( R ) telle que A X 3 ? 5.4.3 Démontrer que exp Mn ( C ) GLn ( C ) 5.4.4 ( a ) ***Démontrer*** que si A Mn ( C ) vérifie exp(A ) In , alors A est diagonalisable

**49324**: ( b ) ***Résoudre*** l' équation exp(X ) In

**49332**: 5.4.5 ***Résoudre*** l' équation 5.4.6 Soit n N , résoudre l' équation 5.4.7 Soit A Mn ( R ) , donner une condition nécessaire et suffisante pour que l' équation suivante ait une solution dans Mn ( R ) : 5.4.8 Soit A la matrice de l' exemple 5.5 , page 252

**49340**: 5.4.5 Résoudre l' équation 5.4.6 Soit n N , ***résoudre*** l' équation 5.4.7 Soit A Mn ( R ) , donner une condition nécessaire et suffisante pour que l' équation suivante ait une solution dans Mn ( R ) : 5.4.8 Soit A la matrice de l' exemple 5.5 , page 252

**49351**: 5.4.5 Résoudre l' équation 5.4.6 Soit n N , résoudre l' équation 5.4.7 Soit A Mn ( R ) , ***donner*** une condition nécessaire et suffisante pour que l' équation suivante ait une solution dans Mn ( R ) : 5.4.8 Soit A la matrice de l' exemple 5.5 , page 252

**49384**: ***Trouver*** toutes les solutions dans M3 ( R ) de l' équation : 5.4.9 Soit A la matrice de l' exemple 5.7 , page 259

**49410**: ***Trouver*** toutes les solutions dans M3 ( R ) de l' équation : Invariants de similitudes Quand on a une relation d' équivalence , il est naturel d' essayer de caractériser ses classes d' équivalence

**49438**: Trouver toutes les solutions dans M3 ( R ) de l' équation : Invariants de similitudes Quand on a une relation d' équivalence , il est naturel d' ***essayer*** de caractériser ses classes d' équivalence

**49440**: Trouver toutes les solutions dans M3 ( R ) de l' équation : Invariants de similitudes Quand on a une relation d' équivalence , il est naturel d' essayer de ***caractériser*** ses classes d' équivalence

**49702**: Si K C et n 3 , les classes de similitude sont : ( a ) les homothéties ( avec ( X ) 3 et X ) ( b ) les matrices semblables à ( c ) les matrices semblables à ( d ) les matrices semblables à ( e ) les matrices semblables à ( f ) les matrices semblables à La méthode générale pour ***montrer*** que A B est de ramener A et B à la même forme réduite : diagonale , Dunford , Frobenius ( voir plus loin ) , etc. Cela revient souvent à résoudre des systèmes linéaires

**49708**: Si K C et n 3 , les classes de similitude sont : ( a ) les homothéties ( avec ( X ) 3 et X ) ( b ) les matrices semblables à ( c ) les matrices semblables à ( d ) les matrices semblables à ( e ) les matrices semblables à ( f ) les matrices semblables à La méthode générale pour montrer que A B est de ***ramener*** A et B à la même forme réduite : diagonale , Dunford , Frobenius ( voir plus loin ) , etc. Cela revient souvent à résoudre des systèmes linéaires

**49724**: Si K C et n 3 , les classes de similitude sont : ( a ) les homothéties ( avec ( X ) 3 et X ) ( b ) les matrices semblables à ( c ) les matrices semblables à ( d ) les matrices semblables à ( e ) les matrices semblables à ( f ) les matrices semblables à La méthode générale pour montrer que A B est de ramener A et B à la même forme réduite : diagonale , Dunford , Frobenius ( ***voir*** plus loin ) , etc. Cela revient souvent à résoudre des systèmes linéaires

**49734**: Si K C et n 3 , les classes de similitude sont : ( a ) les homothéties ( avec ( X ) 3 et X ) ( b ) les matrices semblables à ( c ) les matrices semblables à ( d ) les matrices semblables à ( e ) les matrices semblables à ( f ) les matrices semblables à La méthode générale pour montrer que A B est de ramener A et B à la même forme réduite : diagonale , Dunford , Frobenius ( voir plus loin ) , etc. Cela revient souvent à ***résoudre*** des systèmes linéaires

**49782**: Les matrices suivantes sont semblables : Soit E un K - espace vectoriel de dimension finie non nulle , u L ( E ) et x E. On définit : Ix l' idéal des polynômes annulateurs x , c' est - à - ***dire*** le noyau de : KX E définie par ( P ) x le polynôme minimal de x ( le polynôme unitaire engendrant l' idéal Ix )

**49877**: , uq1 ( x ) ) est la matrice compagnon de x ( ***voir*** la définition 5.5 , page 232 ) : Il existe x E tel que x u ( voir l' exercice 4 de la série d' exercices 5.1 , page 236 )

**49895**: , uq1 ( x ) ) est la matrice compagnon de x ( voir la définition 5.5 , page 232 ) : Il existe x E tel que x u ( ***voir*** l' exercice 4 de la série d' exercices 5.1 , page 236 )

**49966**: Alors il existe r N et hxi i et , pour tout i 1 , r 1 , xi xi1 et xr u Démonstration Soit x E tel que x u ( ***voir*** la remarque précédente )

**50068**: Par dualité , pour ***montrer*** que dim G n dim(hxi ) n k , il suffit de montrer que Considérons l' application de Ku dans Vect qui a P ( u ) Ku associe e?k P ( u )

**50081**: Par dualité , pour montrer que dim G n dim(hxi ) n k , il suffit de ***montrer*** que Considérons l' application de Ku dans Vect qui a P ( u ) Ku associe e?k P ( u )

**50455**: Les théorèmes 5.7 , page précédente et 5.8 , de la présente page permettent de ***montrer*** de nombreux résultats théoriques , par exemple : la réduction de Jordan des endomorphismes nilpotents ( voir la proposition 5.3 , page 249 ) le fait que toute matrice est semblable à sa transposée si deux matrices A et B de Mn ( K ) sont semblables en tant que matrices de Mn ( L ) , où L est un surcorps de K , alors elles sont semblables sur Mn ( K ) ( en effet , par unicité , les invariants de similitude dans Mn ( K ) sont les invariants de similitudes dans Mn ( L ) )

**50472**: Les théorèmes 5.7 , page précédente et 5.8 , de la présente page permettent de montrer de nombreux résultats théoriques , par exemple : la réduction de Jordan des endomorphismes nilpotents ( ***voir*** la proposition 5.3 , page 249 ) le fait que toute matrice est semblable à sa transposée si deux matrices A et B de Mn ( K ) sont semblables en tant que matrices de Mn ( L ) , où L est un surcorps de K , alors elles sont semblables sur Mn ( K ) ( en effet , par unicité , les invariants de similitude dans Mn ( K ) sont les invariants de similitudes dans Mn ( L ) )

**50572**: Si C(P ) est une matrice compagnon , sa forme de Jordan ne fait ***apparaître*** qu' un et un seul bloc pour chaque valeur propre ( est une racine de P et la taille du bloc est son ordre de multiplicité )

**50604**: On peut ainsi ***obtenir*** la forme de Jordan d' une matrice à partir de sa forme de Frobenius

**50613**: On peut ainsi obtenir la forme de Jordan d' une matrice à ***partir*** de sa forme de Frobenius

**50622**: On peut ***montrer*** que si une matrice A Mn ( K a pour invariants de similitude P1 ,

**50665**: On a un algorithme simple ( à base de pivots , ***voir*** plus bas ) qui permet de calculer cette forme et ainsi trouver les invariants de similitude de A et sa forme de Frobenius

**50672**: On a un algorithme simple ( à base de pivots , voir plus bas ) qui permet de ***calculer*** cette forme et ainsi trouver les invariants de similitude de A et sa forme de Frobenius

**50677**: On a un algorithme simple ( à base de pivots , voir plus bas ) qui permet de calculer cette forme et ainsi ***trouver*** les invariants de similitude de A et sa forme de Frobenius

**50694**: Cela permet notamment de ***répondre*** à la question : Les matrices A et B sont - elles semblables ? De plus , dans cet algorithme , il ne y a pas besoin de factoriser les polynômes , cela fonctionne dans ne importe quel corps

**50723**: Cela permet notamment de répondre à la question : Les matrices A et B sont - elles semblables ? De plus , dans cet algorithme , il ne y a pas besoin de ***factoriser*** les polynômes , cela fonctionne dans ne importe quel corps

**50881**: Étape 2 Si il existe sur la première ligne ( ou la première colonne ) un élément m1,k ( ou mk,1 ) non multiple de m1,1 , on le remplace ( en utilisant une transvection ) par le reste de la division euclidienne de m1,k ( ou mk,1 ) par m1,1 et on revient à l' étape 1 en permutant les colonnes ( ou les lignes ) 1 et k. Etape 3 L' étape 2 a pour effet de ***diminuer*** strictement ( M ) , elle ne peut donc se réaliser qu' un nombre fini de fois

**50892**: Étape 2 Si il existe sur la première ligne ( ou la première colonne ) un élément m1,k ( ou mk,1 ) non multiple de m1,1 , on le remplace ( en utilisant une transvection ) par le reste de la division euclidienne de m1,k ( ou mk,1 ) par m1,1 et on revient à l' étape 1 en permutant les colonnes ( ou les lignes ) 1 et k. Etape 3 L' étape 2 a pour effet de diminuer strictement ( M ) , elle ne peut donc se ***réaliser*** qu' un nombre fini de fois

**50933**: On utilise alors m1,1 comme pivot pour les ***annuler***

**50965**: Étape 4 On obtient une matrice de la forme et , si m1,1 ne divise pas un des éléments de M1 , par exemple mi , j , on fait ***apparaître*** ( par des transvections ) le reste de la division euclidienne de mi , j par m1,1 puis par des permutations on l' échange avec m1,1 et on recommence l' étape 1

**51032**: Étape 5 Au bout d' un nombre fini d' étapes , on obtient une matrice de la forme où m1,1 divise tous les éléments de M1 et on recommence l' étape 1 à ***partir*** de la matrice M1 qui est de taille strictement plus petite

**51115**: On en déduit que sa forme de Frobenius 5.5.1 ***Déterminer*** la forme de Frobenius de la matrice : 5.5.2 Démontrer que : sont semblables

**51125**: On en déduit que sa forme de Frobenius 5.5.1 Déterminer la forme de Frobenius de la matrice : 5.5.2 ***Démontrer*** que : sont semblables

**51132**: 5.5.3 ***Démontrer*** que si n 2 , 3 , deux matrices de Mn ( K ) sont semblables si , et seulement si , elles ont le même polynôme caractéristique et le même polynôme minimal

**51167**: ***Démontrer*** que ce résultat est faux 5.5.5 Démontrer que : est un ouvert dense de Mn ( C )

**51174**: Démontrer que ce résultat est faux 5.5.5 ***Démontrer*** que : est un ouvert dense de Mn ( C )

**51188**: 5.5.6 ***Démontrer*** que l' adhérence de : est l' ensemble des matrices A telles que Sp(A ) U z C , z 1

**51241**: ( a ) On suppose que P est scindé dans K , à quelle condition C(P ) est-elle diagonalisable ? ( b ) On suppose que P est irréductible , ***montrer*** qu' en ce cas KC(P ) est un corps P admet au moins une racine ( laquelle ? )

**51263**: En ***déduire*** la construction d' un corps à 4 éléments et d' un corps à 8 Un exemple d' utilisation de la réduction sur un corps fini Dans tout ce chapitre , nous avons travaillé dans un corps commutatif quelconque , et plus nécessairement dans R ou C. Voici un petit exemple de synthèse montrant comment on peu utiliser les notions vues ici dans un corps fini

**51320**: En déduire la construction d' un corps à 4 éléments et d' un corps à 8 Un exemple d' utilisation de la réduction sur un corps fini Dans tout ce chapitre , nous avons travaillé dans un corps commutatif quelconque , et plus nécessairement dans R ou C. Voici un petit exemple de synthèse montrant comment on peu ***utiliser*** les notions vues ici dans un corps fini

**51379**: La suite ( vn ) nN est périodique à ***partir*** d' un certain rang

**51445**: Il existe donc deux entiers distincts ( p , q ) N2 , p q tels que Il est alors facile de ***démontrer*** par récurrence sur n que : la suite est donc périodique à partir du rang p , et sa période est un diviseur de q p. Démonstration des valeurs possibles de la période On peut considérer qu' on travaille en fait dans l' anneau Z10 Z qui , par théorème chinois , est isomorphe à Z2 Z Z5 Z. Nous pouvons donc travailler dans des corps

**51458**: Il existe donc deux entiers distincts ( p , q ) N2 , p q tels que Il est alors facile de démontrer par récurrence sur n que : la suite est donc périodique à ***partir*** du rang p , et sa période est un diviseur de q p. Démonstration des valeurs possibles de la période On peut considérer qu' on travaille en fait dans l' anneau Z10 Z qui , par théorème chinois , est isomorphe à Z2 Z Z5 Z. Nous pouvons donc travailler dans des corps

**51481**: Il existe donc deux entiers distincts ( p , q ) N2 , p q tels que Il est alors facile de démontrer par récurrence sur n que : la suite est donc périodique à partir du rang p , et sa période est un diviseur de q p. Démonstration des valeurs possibles de la période On peut ***considérer*** qu' on travaille en fait dans l' anneau Z10 Z qui , par théorème chinois , est isomorphe à Z2 Z Z5 Z. Nous pouvons donc travailler dans des corps

**51508**: Il existe donc deux entiers distincts ( p , q ) N2 , p q tels que Il est alors facile de démontrer par récurrence sur n que : la suite est donc périodique à partir du rang p , et sa période est un diviseur de q p. Démonstration des valeurs possibles de la période On peut considérer qu' on travaille en fait dans l' anneau Z10 Z qui , par théorème chinois , est isomorphe à Z2 Z Z5 Z. Nous pouvons donc ***travailler*** dans des corps

**51654**: Dans Z2 Z les périodes de la suite ( un ) nN sont , à ***partir*** d' un certain rang 1 , 2 ou 3

**51780**: De plus , si n N , à l' aide de la formule du binôme de Newton , on a si 6 0 ( cas évident où la période est 1 , à ***partir*** du second rang ) et 6 1 ( cas simple ou la périodicité est 5 , la première condition ci-dessous étant inutile ) , la matrice est égale à I2 si ce qui nous donne une période de 10 ou 20

**51924**: En enlevant celle qu' on connaît ( 1 , 2 et 4 correspondant aux matrices précédemment vues ) Dans Z5 Z les périodes de la suite ( un ) nN sont , à ***partir*** d' un certain rang dans Finalement les périodes possibles sont , d' après le théorème chinois ( on fait le PPCM des périodes dans Z2 Z et dans Z5 Z ) Juste pour le plaisir , construisons une situation où la période est 60

**51977**: Le polynôme caractéristique dans Z Z doit ***être*** X 2 X 1 ( pour obtenir le 3 ) , et être de la forme ( X ) 2 dans Z5 Z , ( matrice étant non-diagonalisable ( pour obtenir le 20 )

**51984**: Le polynôme caractéristique dans Z Z doit être X 2 X 1 ( pour ***obtenir*** le 3 ) , et être de la forme ( X ) 2 dans Z5 Z , ( matrice étant non-diagonalisable ( pour obtenir le 20 )

**51990**: Le polynôme caractéristique dans Z Z doit être X 2 X 1 ( pour obtenir le 3 ) , et ***être*** de la forme ( X ) 2 dans Z5 Z , ( matrice étant non-diagonalisable ( pour obtenir le 20 )

**52008**: Le polynôme caractéristique dans Z Z doit être X 2 X 1 ( pour obtenir le 3 ) , et être de la forme ( X ) 2 dans Z5 Z , ( matrice étant non-diagonalisable ( pour ***obtenir*** le 20 )