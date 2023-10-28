185

**34**: Algèbre linéaire Alain Chillès ( ) , , , Valentin Vinoles , Adrien Joseph Remerciements Nous tenons à remercier chaudement tous les professeurs qui nous ont aidés à écrire ce livre , notamment en ***corrigeant*** les inévitables fautes

**222**: Le cours est découpé en quatre parties : espaces vectoriels sur R ou C matrices et systèmes linéaires ***déterminant*** réduction des endomorphismes

**260**: Les calculs et les dessins ont été , pour la plupart , effectués grâce aux logiciels Wxmaxima et Python , sympy , matplotlib , outils d' une très grande qualité , gratuits et ***fonctionnant*** sur tout système ( Linux , Windows , Mac , Androïd )

**1074**: Signifie x E , y E L' écriture x , y E ne est pas correcte ! Opérations Signification Multiplication externe Multiplication des matrices Notations de définitions Introduit une nouvelle notation Introduit une nouvelle définition Espaces vectoriels dim E ou dim(E ) ou dimK E ou Ensemble des fonctions définies sur l' ensemble X à valeurs dans l' ensemble Y Ensemble des fonctions continues définies sur l' intervalle I R à valeurs dans Ensemble des fonctions continues par morceaux définies sur l' intervalle I R à valeurs dans K R ou C Ensemble des fonctions de classe C k où k N , définies sur l' intervalle I R à valeurs dans K R ou C Droite vectorielle engendrée par x Sous-espace vectoriel de l' espace vectoriel E engendré par la partie A Somme des sous-espaces vectoriels E1 et E2 d' un même espace vectoriel E Somme des Ei , où ( Ei ) iI est une famille de sous-espaces vectoriels d' un même espace vectoriel E et où I est un ensemble quelconque Somme directe des sous-espaces vectoriels E1 et E2 d' un même espace vectoriel Somme directe des Ei , où ( Ei ) iI est une famille de sous-espaces vectoriels d' un même espace vectoriel E et où I est un ensemble quelconque La dimension du K - espace vectoriel E Ensemble des applications linéaires de l' espace vectoriel E dans l' espace vectoriel L ( E , E ) , ensemble des endomorphismes de l' espace vectoriel E Ensemble des automorphismes de l' espace vectoriel E L ( E , K ) , où E est un K - espace vectoriel c' est l' ensemble des formes linéaires sur l' espace vectoriel E ( noter le ? et non pas ) Noyau d' une application linéaire f L ( E , F ) Image d' une application linéaire f L ( E , F ) Application linéaire identité de l' espace vectoriel E Restriction d' une application linéaire f L ( E , F ) à un sous-espace vectoriel Co-restriction d' une application linéaire f L ( E , F ) à un sous-espace vectoriel F 0 de F ***contenant*** Im(f ) Projection sur F parallèlement à G , où E F G Symétrie par rapport à F parallèlement à G Rang de l' application linéaire f Famille duale de la base ( ei ) iI d' un espace vectoriel E Dimension d' un supplémentaire de F Ensemble des solutions du système linéaire S Matrice n p dont les coefficients sont les ( ai , j ) ( i , j)1,n1,p Im(A ) , Ker(A ) , rang(A ) Déterminants Signification Nous utiliserons systématiquement les crochets pour noter les matrices ! Ensemble des matrices à coefficients dans l' ensemble A ayant n lignes et p colonnes Matrice identité de Mp ( K ) Matrice nulle de Mn , p ( K ) Matrice du vecteur x E dans la base E de l' espace vectoriel E Matrice de l' application linéaire f L ( E , E 0 ) dans les bases E de E et E 0 de Matrice de l' endomorphisme f L ( E ) dans la base E de E ( correspond à Matrice ne contenant que des 0 sauf sur la k - ième ligne et la l - ième colonne où il y a un 1 ( Attention : les dimensions de ces matrices ne sont pas précisées ... ) Transposée de A , où A Mn , p ( K ) Ensemble des matrices symétriques de Mp ( K ) Ensemble des matrices antisymétriques de Mp ( K ) Matrice diagonale Ensemble des matrices diagonales de Mp ( K ) Matrice du système de vecteurs X ( x1 ,

**1175**: Signifie x E , y E L' écriture x , y E ne est pas correcte ! Opérations Signification Multiplication externe Multiplication des matrices Notations de définitions Introduit une nouvelle notation Introduit une nouvelle définition Espaces vectoriels dim E ou dim(E ) ou dimK E ou Ensemble des fonctions définies sur l' ensemble X à valeurs dans l' ensemble Y Ensemble des fonctions continues définies sur l' intervalle I R à valeurs dans Ensemble des fonctions continues par morceaux définies sur l' intervalle I R à valeurs dans K R ou C Ensemble des fonctions de classe C k où k N , définies sur l' intervalle I R à valeurs dans K R ou C Droite vectorielle engendrée par x Sous-espace vectoriel de l' espace vectoriel E engendré par la partie A Somme des sous-espaces vectoriels E1 et E2 d' un même espace vectoriel E Somme des Ei , où ( Ei ) iI est une famille de sous-espaces vectoriels d' un même espace vectoriel E et où I est un ensemble quelconque Somme directe des sous-espaces vectoriels E1 et E2 d' un même espace vectoriel Somme directe des Ei , où ( Ei ) iI est une famille de sous-espaces vectoriels d' un même espace vectoriel E et où I est un ensemble quelconque La dimension du K - espace vectoriel E Ensemble des applications linéaires de l' espace vectoriel E dans l' espace vectoriel L ( E , E ) , ensemble des endomorphismes de l' espace vectoriel E Ensemble des automorphismes de l' espace vectoriel E L ( E , K ) , où E est un K - espace vectoriel c' est l' ensemble des formes linéaires sur l' espace vectoriel E ( noter le ? et non pas ) Noyau d' une application linéaire f L ( E , F ) Image d' une application linéaire f L ( E , F ) Application linéaire identité de l' espace vectoriel E Restriction d' une application linéaire f L ( E , F ) à un sous-espace vectoriel Co-restriction d' une application linéaire f L ( E , F ) à un sous-espace vectoriel F 0 de F contenant Im(f ) Projection sur F parallèlement à G , où E F G Symétrie par rapport à F parallèlement à G Rang de l' application linéaire f Famille duale de la base ( ei ) iI d' un espace vectoriel E Dimension d' un supplémentaire de F Ensemble des solutions du système linéaire S Matrice n p dont les coefficients sont les ( ai , j ) ( i , j)1,n1,p Im(A ) , Ker(A ) , rang(A ) Déterminants Signification Nous utiliserons systématiquement les crochets pour noter les matrices ! Ensemble des matrices à coefficients dans l' ensemble A ***ayant*** n lignes et p colonnes Matrice identité de Mp ( K ) Matrice nulle de Mn , p ( K ) Matrice du vecteur x E dans la base E de l' espace vectoriel E Matrice de l' application linéaire f L ( E , E 0 ) dans les bases E de E et E 0 de Matrice de l' endomorphisme f L ( E ) dans la base E de E ( correspond à Matrice ne contenant que des 0 sauf sur la k - ième ligne et la l - ième colonne où il y a un 1 ( Attention : les dimensions de ces matrices ne sont pas précisées ... ) Transposée de A , où A Mn , p ( K ) Ensemble des matrices symétriques de Mp ( K ) Ensemble des matrices antisymétriques de Mp ( K ) Matrice diagonale Ensemble des matrices diagonales de Mp ( K ) Matrice du système de vecteurs X ( x1 ,

**1254**: Signifie x E , y E L' écriture x , y E ne est pas correcte ! Opérations Signification Multiplication externe Multiplication des matrices Notations de définitions Introduit une nouvelle notation Introduit une nouvelle définition Espaces vectoriels dim E ou dim(E ) ou dimK E ou Ensemble des fonctions définies sur l' ensemble X à valeurs dans l' ensemble Y Ensemble des fonctions continues définies sur l' intervalle I R à valeurs dans Ensemble des fonctions continues par morceaux définies sur l' intervalle I R à valeurs dans K R ou C Ensemble des fonctions de classe C k où k N , définies sur l' intervalle I R à valeurs dans K R ou C Droite vectorielle engendrée par x Sous-espace vectoriel de l' espace vectoriel E engendré par la partie A Somme des sous-espaces vectoriels E1 et E2 d' un même espace vectoriel E Somme des Ei , où ( Ei ) iI est une famille de sous-espaces vectoriels d' un même espace vectoriel E et où I est un ensemble quelconque Somme directe des sous-espaces vectoriels E1 et E2 d' un même espace vectoriel Somme directe des Ei , où ( Ei ) iI est une famille de sous-espaces vectoriels d' un même espace vectoriel E et où I est un ensemble quelconque La dimension du K - espace vectoriel E Ensemble des applications linéaires de l' espace vectoriel E dans l' espace vectoriel L ( E , E ) , ensemble des endomorphismes de l' espace vectoriel E Ensemble des automorphismes de l' espace vectoriel E L ( E , K ) , où E est un K - espace vectoriel c' est l' ensemble des formes linéaires sur l' espace vectoriel E ( noter le ? et non pas ) Noyau d' une application linéaire f L ( E , F ) Image d' une application linéaire f L ( E , F ) Application linéaire identité de l' espace vectoriel E Restriction d' une application linéaire f L ( E , F ) à un sous-espace vectoriel Co-restriction d' une application linéaire f L ( E , F ) à un sous-espace vectoriel F 0 de F contenant Im(f ) Projection sur F parallèlement à G , où E F G Symétrie par rapport à F parallèlement à G Rang de l' application linéaire f Famille duale de la base ( ei ) iI d' un espace vectoriel E Dimension d' un supplémentaire de F Ensemble des solutions du système linéaire S Matrice n p dont les coefficients sont les ( ai , j ) ( i , j)1,n1,p Im(A ) , Ker(A ) , rang(A ) Déterminants Signification Nous utiliserons systématiquement les crochets pour noter les matrices ! Ensemble des matrices à coefficients dans l' ensemble A ayant n lignes et p colonnes Matrice identité de Mp ( K ) Matrice nulle de Mn , p ( K ) Matrice du vecteur x E dans la base E de l' espace vectoriel E Matrice de l' application linéaire f L ( E , E 0 ) dans les bases E de E et E 0 de Matrice de l' endomorphisme f L ( E ) dans la base E de E ( correspond à Matrice ne ***contenant*** que des 0 sauf sur la k - ième ligne et la l - ième colonne où il y a un 1 ( Attention : les dimensions de ces matrices ne sont pas précisées ... ) Transposée de A , où A Mn , p ( K ) Ensemble des matrices symétriques de Mp ( K ) Ensemble des matrices antisymétriques de Mp ( K ) Matrice diagonale Ensemble des matrices diagonales de Mp ( K ) Matrice du système de vecteurs X ( x1 ,

**1383**: , xp ) E p ( p N ) dans la base E de l' espace vectoriel E MatE ( B ) , matrice de passage de E à B Matrice de Mn , p ( K ) ne ***contenant*** que des 0 , sauf lorsque i j 1 , r où il y a Matrice de transvection dans Mp ( K ) ( où p max(k , l ) ) , égale à Ip .Ek , l Matrice de dilatation dans Mp ( K ) ( où p n ) , égale à Ip ( 1).Ek , k Matrice de permutation Groupe des matrices inversibles d' ordre n à coefficients dans K Ensemble des matrices triangulaires supérieures d' ordre n à coefficients dans K Ensemble des matrices triangulaires inférieures d' ordre n à coefficients dans K Trace de la matrice A Image , noyau et rang d' une matrice A Mn , p ( K ) Produit de Kronecker des matrices A et B A semblable à B A équivalente à B Cofacteuri , j ( A ) Déterminant de la matrice Déterminant des vecteurs ( x1 ,

**1527**: , xp ) E p ( p N ) dans la base E de l' espace vectoriel E MatE ( B ) , matrice de passage de E à B Matrice de Mn , p ( K ) ne contenant que des 0 , sauf lorsque i j 1 , r où il y a Matrice de transvection dans Mp ( K ) ( où p max(k , l ) ) , égale à Ip .Ek , l Matrice de dilatation dans Mp ( K ) ( où p n ) , égale à Ip ( 1).Ek , k Matrice de permutation Groupe des matrices inversibles d' ordre n à coefficients dans K Ensemble des matrices triangulaires supérieures d' ordre n à coefficients dans K Ensemble des matrices triangulaires inférieures d' ordre n à coefficients dans K Trace de la matrice A Image , noyau et rang d' une matrice A Mn , p ( K ) Produit de Kronecker des matrices A et B A semblable à B A équivalente à B Cofacteuri , j ( A ) Déterminant de la matrice ***Déterminant*** des vecteurs ( x1 ,

**1543**: , xn ) dans la base E ***Déterminant*** d' un endomorphisme u L ( E ) Cofacteur d' indices ( i , j ) de la matrice A Comatrice de A Déterminant de Vandermonde Ensemble des formes p - linéaires de E dans K Ensemble des formes p - linéaires symétriques de E dans K Ensemble des formes p - linéaires antisymétriques de E dans K Réduction des endomorphismes Sp(u ) ou Sp(A ) multu ( ) ou multA ( ) Espace propre de u L ( E ) ou A pour la valeur propre K Spectre de u L ( E ) ou A Polynôme caractéristique de u L ( E ) ou A Multiplicité de dans u ou A Algèbre engendrée par u ou A Signification Polynôme d' endomorphisme ou de matrice Idéal annulateur de u ou A Polynôme minimal de u ou A Matrice compagnon du polynôme P Norme subordonnée de u ou A Espace des endomorphismes continus de E Rayon spectral de u ou A Commutant de u ou A Espace caractéristique de u ou A Chapitre 1 Espaces vectoriels sur R ou C Dans ce chapitre , nous noterons K les corps R ou C. Cela signifie alors que le résultat énoncé est vrai dans R et dans C. Généralités Premières définitions Soit E un ensemble non vide , on dit que E est un K - espace vectoriel ( ou un espace vectoriel sur K ) si il vérifie les axiomes suivants : 1

**1567**: , xn ) dans la base E Déterminant d' un endomorphisme u L ( E ) Cofacteur d' indices ( i , j ) de la matrice A Comatrice de A ***Déterminant*** de Vandermonde Ensemble des formes p - linéaires de E dans K Ensemble des formes p - linéaires symétriques de E dans K Ensemble des formes p - linéaires antisymétriques de E dans K Réduction des endomorphismes Sp(u ) ou Sp(A ) multu ( ) ou multA ( ) Espace propre de u L ( E ) ou A pour la valeur propre K Spectre de u L ( E ) ou A Polynôme caractéristique de u L ( E ) ou A Multiplicité de dans u ou A Algèbre engendrée par u ou A Signification Polynôme d' endomorphisme ou de matrice Idéal annulateur de u ou A Polynôme minimal de u ou A Matrice compagnon du polynôme P Norme subordonnée de u ou A Espace des endomorphismes continus de E Rayon spectral de u ou A Commutant de u ou A Espace caractéristique de u ou A Chapitre 1 Espaces vectoriels sur R ou C Dans ce chapitre , nous noterons K les corps R ou C. Cela signifie alors que le résultat énoncé est vrai dans R et dans C. Généralités Premières définitions Soit E un ensemble non vide , on dit que E est un K - espace vectoriel ( ou un espace vectoriel sur K ) si il vérifie les axiomes suivants : 1

**1705**: , xn ) dans la base E Déterminant d' un endomorphisme u L ( E ) Cofacteur d' indices ( i , j ) de la matrice A Comatrice de A Déterminant de Vandermonde Ensemble des formes p - linéaires de E dans K Ensemble des formes p - linéaires symétriques de E dans K Ensemble des formes p - linéaires antisymétriques de E dans K Réduction des endomorphismes Sp(u ) ou Sp(A ) multu ( ) ou multA ( ) Espace propre de u L ( E ) ou A pour la valeur propre K Spectre de u L ( E ) ou A Polynôme caractéristique de u L ( E ) ou A Multiplicité de dans u ou A Algèbre engendrée par u ou A Signification Polynôme d' endomorphisme ou de matrice Idéal annulateur de u ou A Polynôme minimal de u ou A Matrice compagnon du polynôme P Norme subordonnée de u ou A Espace des endomorphismes continus de E Rayon spectral de u ou A ***Commutant*** de u ou A Espace caractéristique de u ou A Chapitre 1 Espaces vectoriels sur R ou C Dans ce chapitre , nous noterons K les corps R ou C. Cela signifie alors que le résultat énoncé est vrai dans R et dans C. Généralités Premières définitions Soit E un ensemble non vide , on dit que E est un K - espace vectoriel ( ou un espace vectoriel sur K ) si il vérifie les axiomes suivants : 1

**3543**: Soit E un K - espace vectoriel et soit A E , on appelle sous-espace vectoriel engendré par A le plus petit sous-espace vectoriel de E ***contenant*** A. On le note : Démonstration que la notion de sous-espace vectoriel engendré par une partie est bien définie L' existence d' un plus petit sous-espace vectoriel contenant A mérite une justification

**3571**: Soit E un K - espace vectoriel et soit A E , on appelle sous-espace vectoriel engendré par A le plus petit sous-espace vectoriel de E contenant A. On le note : Démonstration que la notion de sous-espace vectoriel engendré par une partie est bien définie L' existence d' un plus petit sous-espace vectoriel ***contenant*** A mérite une justification

**3642**: Par définition , tout sous-espace vectoriel de E qui contient A contient aussi Vect(A ) , c' est donc bien le petit sous-espace vectoriel de E ***contenant*** A. Soit E un K - espace vectoriel

**4534**: En ***reprenant*** les notations de la définition 1.7 , page ci - contre , on a où xik iI Ei Eik pour tout k 1 , n. Le vecteur x s' écrit donc comme une combinaison linéaire d' éléments de iI Ei , donc x Vect ( ) Soit x Vect iI Ei

**5725**: En ***prenant*** en considération un supplémentaire de Vect(1 , 2 ) dans R qu' il existe une fonction f : R R qui est 1-périodique et une fonction g : R R qui est 2-périodique telles que : Soit E un K - espace vectoriel

**7206**: On peut échanger certains vecteurs de la famille génératrice avec des vecteurs de la famille libre tout en ***gardant*** la propriété d' être génératrice , soit : Démonstration Puisque ( g1 ,

**7329**: Par le même argument qui ci - dessus , on a donc Il reste à démontrer que p n. Si p n , en ***prenant*** k n 1 dans la construction ci - dessus , on obtient que ( 1 ,

**7438**: On a donc p n. On peut aussi énoncer ce résultat avec une famille génératrice de cardinal quelconque ( peut-être infini ) , où l' on pourra échanger p vecteurs de cette famille tout en la ***gardant*** génératrice

**7737**: On peut compléter la famille libre en une base , soit : Démonstration C' est une application immédiate du théorème de l' échange , en ***prenant*** comme famille génératrice une base de E ( qui a n éléments )

**8158**: On utilise le théorème de l' échange pour extraire une base B G de E ( en ***partant*** d' une une sous-famille libre de G )

**8375**: Le théorème de la base incomplète permet alors de construire une base de E en ***complétant*** la famille ( x ) par des éléments de G. Soit E un K - espace vectoriel

**9001**: Notons ce nombre p. Démonstration C' est immédiat en ***considérant*** une base adaptée à cette décomposition en somme directe

**9099**: alors on vérifie que est une base de E1 E2 ( en ***démontrant*** que c' est une famille libre et génératrice ) et qui a n1 n2 dim E1 dim E2 éléments

**9473**: Démontrer qu' il existe un supplémentaire de F ***contenant*** G. 1.7.5 Soit E un K - espace vectoriel de dimension finie et F un sous-espace vectoriel strict de E ( F 6 E )

**10613**: On peut utiliser les images et noyaux pour démontrer que des ensembles sont des sous-espaces vectoriels : ( a ) ( Image peu fréquent ) : est un sous-espace vectoriel de C 0 ( a , b , R ) en ***considérant*** l' endomorphisme de C 0 ( a , b , R ) : ( b ) ( Noyau très fréquent ) : est un sous-espace vectoriel de C 1 ( a , b , R ) en considérant la forme linéaire de C 1 ( a , b , R ) : Proposition 1.4 Soit E et E 0 deux K - espaces vectoriels , f L ( E , E 0 ) , alors : f est injective si , et seulement si , Ker(f ) 0E f est surjective si , et seulement si , Im(f ) E 0 Démonstration La caractérisation de la surjectivité est immédiate

**10651**: On peut utiliser les images et noyaux pour démontrer que des ensembles sont des sous-espaces vectoriels : ( a ) ( Image peu fréquent ) : est un sous-espace vectoriel de C 0 ( a , b , R ) en considérant l' endomorphisme de C 0 ( a , b , R ) : ( b ) ( Noyau très fréquent ) : est un sous-espace vectoriel de C 1 ( a , b , R ) en ***considérant*** la forme linéaire de C 1 ( a , b , R ) : Proposition 1.4 Soit E et E 0 deux K - espaces vectoriels , f L ( E , E 0 ) , alors : f est injective si , et seulement si , Ker(f ) 0E f est surjective si , et seulement si , Im(f ) E 0 Démonstration La caractérisation de la surjectivité est immédiate

**11145**: Il s' agit du point 2 en remplaçant E 0 par Im f et en ***remarquant*** que f est surjective sur son image

**13224**: Réciproquement , si il existe f L ( E , E 0 ) bijective , alors d' après ce qui précède n p et p n , donc Ces propriétés sont très importantes pour démontrer des égalités ou des inégalités de dimensions ! Proposition 1.6 Rang d' une composition Soit E , E 0 et E 00 trois K - espaces vectoriels de dimensions finies , u L ( E , E 0 ) et v L ( E 0 , E 00 ) , alors : rang(v u ) dim E 0 rang(v ) rang(u ) Démonstration On peut déjà remarquer que : donc , en ***introduisant*** des supplémentaires : l' inégalité demandée devient : Or , il existe une application naturelle qui va de F 0 dans F 00 , l' application : L' énoncé devient : La démonstration ne est alors qu' une vérification : soit x00 F 00 , alors x00 Im(v ) , donc , il existe Théorème 1.4 Théorème du rang Soit E et E 0 des K - espace vectoriels et f L ( E , E 0 )

**13402**: Soit E un K - espace vectoriel de dimension finie et f L ( E ) , alors : ( a ) En ***posant*** f 0 idE , on a : ( b ) De plus , ( c ) On peut alors poser : Proposition 1.7 Caractérisation des automorphismes en dimension finie Soit E un K - espace vectoriel de dimension finie et f L ( E ) , alors : f injective f surjective f bijective C' est faux en dimension infinie

**14395**: Si F est un sous-espace vectoriel de E , si f L ( E , E 0 ) et g L ( E 0 , E 00 ) alors : De même , si F 00 est un sous-espace vectoriel de E 00 ***contenant*** g(E 0 ) , alors : Si F est un sous-espace vectoriel d' un K - espace vectoriel E et f une application linéaire de E dans E 0 , Ker fF F Ker(f ) Démonstration Soit x Ker fF

**14577**: Notation 1.2 Inclusion canonique Soit E un K - espace vectoriel , F un sous-espace vectoriel de E , on peut définir l' inclusion canonique de F dans E par : On a donc : iF E ( idE ) F Si G est un supplémentaire de F dans E ( E F G ) , on a : iF E idF Ce ne sont pas des réciproques ! Pour connaître une application linéaire définie sur un K - espace vectoriel dont on connaît une décomposition en somme directe , il faut et il suffit d' en connaître ses restrictions à chaque sous-espace vectoriel ***composant*** la décomposition

**14837**: Mais , par décomposition en somme directe , on a : En ***appliquant*** f , il vient : Dans le cas de la dimension finie ( dim E ) , on obtient que Im(f ) est de dimension finie et que dim Im(f ) dim F Or , la formule de Grasmann ( proposition 1.3 , page 44 ) nous donne que dim F dim E dim Ker(f ) soit , le théorème du rang ! ( théorème 1.4 , page 57 ) Pourquoi appelle -t -on ce résultat théorème de factorisation des applications linéaires ? Si on regarde le diagramme 1.3 , de la présente page

**15001**: On a donc obtenu une factorisation de f à l' aide d' applications linéaires simples et d' un isomorphisme : f iIm(f ) E0 fe pF kKer(f ) Figure 1.3 Factorisation d' une application linéaire À quoi cela sert -il ? À faire apparaître un isomorphisme , ce qui permet d' utiliser sa réciproque ! Ainsi , sur le schéma précédent , il apparaît une application linéaire naturelle ***permettant*** d' aller de E 0 dans E ( sans pour autant que f soit inversible ) , en introduisant un supplémentaire F 0 de Im(f ) dans E 0

**15020**: On a donc obtenu une factorisation de f à l' aide d' applications linéaires simples et d' un isomorphisme : f iIm(f ) E0 fe pF kKer(f ) Figure 1.3 Factorisation d' une application linéaire À quoi cela sert -il ? À faire apparaître un isomorphisme , ce qui permet d' utiliser sa réciproque ! Ainsi , sur le schéma précédent , il apparaît une application linéaire naturelle permettant d' aller de E 0 dans E ( sans pour autant que f soit inversible ) , en ***introduisant*** un supplémentaire F 0 de Im(f ) dans E 0

**15063**: Notons cette application : regardons ce que deviennent g f et f g. Soit un élément x E , que l' on décompose ***suivant*** la somme directe F Ker(f ) , alors iF E fe1 pIm(f ) kF 0 fe(xF ) iF E fe1 fe(xF ) De même , si x0 E 0 que l' on décompose sous la forme x0 xF 0 f ( x ) xF 0 fe(xF ) , alors : Finalement , on obtient : Figure 1.4 Utilisation de la factorisation g dépend du choix de F 0 ( et bien sûr de F )

**15204**: Quand on aura besoin de construire une application linéaire ***allant*** d' un K - espace vectoriel E à un K - espace vectoriel E 0 , on pourra essayer d' utiliser des chemins naturels allant de E à E 0

**15229**: Quand on aura besoin de construire une application linéaire allant d' un K - espace vectoriel E à un K - espace vectoriel E 0 , on pourra essayer d' utiliser des chemins naturels ***allant*** de E à E 0

**15326**: ( Analyse ) En ***utilisant*** le théorème de factorisation , on peut construire un chemin naturel allant de E à E 0 ( en passant par E 00 )

**15338**: ( Analyse ) En utilisant le théorème de factorisation , on peut construire un chemin naturel ***allant*** de E à E 0 ( en passant par E 00 )

**15346**: ( Analyse ) En utilisant le théorème de factorisation , on peut construire un chemin naturel allant de E à E 0 ( en ***passant*** par E 00 )

**15467**: ) Si v est inversible , alors u v 1 w. Dans le cas contraire , nous allons essayer de nous y ramener : ( Analyse ) Si u existe , alors b w v u donc w Pour pouvoir restreindre v à F 0 ( supplémentaire de Ker(v ) ) , nous allons imposer une condition supplémentaire à u ***permettant*** la co-restriction à F 0 de u : e inversible ! donc , dans ce cas , on a la condition nécessaire : ( Synthèse ) Soit u L ( E , E 0 ) défini par : ou , si l' on préfère : Alors , si x E , on a Le candidat ne est parfois pas celui dont on a besoin ! La vérification est indispensable ! b. La co-restriction est possible d' après l' hypothèse

**16462**: En ***considérant*** j I tel que j i1 ,

**16641**: Comment démontrer qu' une famille de formes linéaires est une base ? En ***utilisant*** la base ante - duale ( si l' on est capable de la trouver )

**17548**: Notons H1 Ker(1 ) , H2 Ker(2 ) , si 1 et 2 sont indépendantes , les deux plans se coupent ***suivant*** la droite D. Soit K un plan contenant D ( comme sur le dessin ) , où K Ker ( ) , le théorème nous assure alors Le plan K a donc pour équation : Cette équation est définie à un coefficient de proportionnalité près , donc Figure 1.7 Hyperplans de R3 Le résultat de cette proposition est particulièrement intéressant en géométrie affine

**17556**: Notons H1 Ker(1 ) , H2 Ker(2 ) , si 1 et 2 sont indépendantes , les deux plans se coupent suivant la droite D. Soit K un plan ***contenant*** D ( comme sur le dessin ) , où K Ker ( ) , le théorème nous assure alors Le plan K a donc pour équation : Cette équation est définie à un coefficient de proportionnalité près , donc Figure 1.7 Hyperplans de R3 Le résultat de cette proposition est particulièrement intéressant en géométrie affine

**17627**: Ainsi si H1 , ... , Hp sont des hyperplans affines ( espaces affines ***ayant*** pour directions des hyperplans vectoriels ) d' intersection non vide ( soit A un point de l' intersection ) , d' équations : alors , pour tout hyperplan H d' équation ( AM ) 0 , contenant cette intersection , Soit V R3 , l' espace usuel muni de sa structure affine euclidienne usuelle

**17664**: Ainsi si H1 , ... , Hp sont des hyperplans affines ( espaces affines ayant pour directions des hyperplans vectoriels ) d' intersection non vide ( soit A un point de l' intersection ) , d' équations : alors , pour tout hyperplan H d' équation ( AM ) 0 , ***contenant*** cette intersection , Soit V R3 , l' espace usuel muni de sa structure affine euclidienne usuelle

**17707**: Soit D une droite affine et A un point , cherchons les plans tangents à la sphère de centre A de rayon 1 , ***contenant*** D. Par exemple : Soit D la droite définie par : 4 x y z 0 , 2 x 5 y 3 z 4 0

**17738**: Cherchons le plan P ***contenant*** D tel que P soit à une distance 1 du point ( 1 , 1 , 1 )

**17895**: , p ) sont indépendantes et ( ) Par récurrence sur p. ( Initialisation ) C' est la proposition ***caractérisant*** les hyperplans comme les espaces de codimension 1

**17971**: Il reste à montrer que : de dimension p1 donc , en ***utilisant*** la première question de l' exercice 1.4.2 , page 32 , on obtient , puisque a E2 C' est ainsi que l' on retrouve que dans l' espace , les droites sont définies par 2 équations

**18142**: Cependant , l' intersection d' hyperplans affines peut-être vide , aussi faut -il , avant toutes choses , s' assurer qu' elle ne l' est pas ! Puis , en s' ***appuyant*** sur un point trouvé de l' intersection , on est ramené au cas vectoriel

**19117**: Les équations récurrentes : un1 an un bn , où ( an ) nN et ( bn ) nN sont dans KN 1.15.1 Soit l' équation récurrente : ( a ) Démontrer que c' est bien un système linéaire en ***précisant*** E , E 0 et u. ( b ) Justifier l' existence de solutions

**19149**: ( d ) En ***utilisant*** une méthode de variation de la constante , trouver toutes les solutions de ( S )

**19185**: 1.15.2 Soit l' équation différentielle : ( a ) Démontrer que c' est bien un système linéaire en ***précisant*** E , E 0 et u. ( b ) Justifier l' existence de solutions

**19315**: ( e ) Comparer aux solutions du système récurrent obtenu par discrétisation : Interpolation Proposition 1.14 Interpolation de Lagrange Soit f : I K , où I est un intervalle de R. Soit x1 xn des réels dans I , on appelle fonction polynomiale d' interpolation de Lagrange l' unique fonction polynomiale P de degré n , telle que Elle est égale à : Démonstration E f polynomiale de degré n Cet espace vectoriel est clairement de dimension n , de base La famille de E ? définie par : ***étant*** une base de E ? , on sait qu' il existe une base ante - duale ( Pk ) k1,n qui vérifie : Un calcul simple nous démontre que : On cherche ensuite une solution sous la forme : en évaluant sur les xj , on trouve l' unique solution de l' énoncé

**19420**: Soit la fonction sin sur l' intervalle 0 , 2 , pour un p N , prenons et regardons les interpolations pour différentes valeurs de p. Voir la session Wxmaxima 1.3 , de la présente 1.16.1 Redémontrer l' existence et l' unicité des fonctions polynomiales d' interpolation de Lagrange en ***utilisant*** un raisonnement sur les systèmes linéaires

**19706**: , ep ) une base de E , alors : Autrement dit , en ***utilisant*** la dualité , pour tout k 1 , p , xk e?k ( x )

**19765**: , e0n ) des bases de E Autrement dit , en ***utilisant*** la dualité , pour tout ( i , j ) 1 , n 1 , p , ai , j ( e0i ) ? ( u(ej ) )

**20564**: Autrement dit , pour tout i 1 , n et en ***notant*** E ( e1 ,

**21161**: Soit j 1 , p. La j - ième colonne de MatE , E 00 ( g f ) est donnée par en ***remarquant*** que MatE ( ej ) Mp,1 ( K ) a des zéros partout sauf en position j et en utilisant plusieurs fois la propriété 2.1 , page 98

**21181**: Soit j 1 , p. La j - ième colonne de MatE , E 00 ( g f ) est donnée par en remarquant que MatE ( ej ) Mp,1 ( K ) a des zéros partout sauf en position j et en ***utilisant*** plusieurs fois la propriété 2.1 , page 98

**21381**: Lorsque p n , on appelle matrice identité d' ordre p et on note : La matrice identité Ip correspond l' endomorphisme idE , l' application identité de E ( avec p dim E ) , dans ne importe quelle base de E. Il est important de savoir calculer les produits de matrices et de savoir prouver que le résultat est correct ! Ainsi , si Ek , est de taille n p , et Er , s est de taille p q , alors : En effet : Les dimensions sont compatibles , on peut effectuer le produit et : Le produit est associatif : Le produit est distributif à gauche et à droite : Existence d' éléments neutres ( à gauche et à droite ) pour la multiplication : Existence d' éléments absorbants pour la multiplication : Démonstration Deux méthodes : on peut vérifier ces égalités en ***calculant*** tous ces produits en utilisant la définition du produit ( définition 2.4 , page 98 ) on peut également utiliser l' isomorphisme de la proposition 2.1 , page 96 , les égalités ci - dessus découlent alors des propriétés de la composition des applications linéaires ( la démonstration est laissée en exercice )

**21386**: Lorsque p n , on appelle matrice identité d' ordre p et on note : La matrice identité Ip correspond l' endomorphisme idE , l' application identité de E ( avec p dim E ) , dans ne importe quelle base de E. Il est important de savoir calculer les produits de matrices et de savoir prouver que le résultat est correct ! Ainsi , si Ek , est de taille n p , et Er , s est de taille p q , alors : En effet : Les dimensions sont compatibles , on peut effectuer le produit et : Le produit est associatif : Le produit est distributif à gauche et à droite : Existence d' éléments neutres ( à gauche et à droite ) pour la multiplication : Existence d' éléments absorbants pour la multiplication : Démonstration Deux méthodes : on peut vérifier ces égalités en calculant tous ces produits en ***utilisant*** la définition du produit ( définition 2.4 , page 98 ) on peut également utiliser l' isomorphisme de la proposition 2.1 , page 96 , les égalités ci - dessus découlent alors des propriétés de la composition des applications linéaires ( la démonstration est laissée en exercice )

**21715**: En ***notant*** Xi , j le coefficient en ( i , j ) d' une matrice Bk , i Aj , k Aj , k Bk , i d' où le troisième point

**21791**: Il y deux manières de considérer les formes linéaires d' un K - espace vectoriel E de dimension finie : comme des applications linéaires de E dans K elles sont alors représentées par des matrices de M1,p ( K ) en ***fixant*** une base de E ( avec p dim E ) comme des vecteurs de E ? elles sont alors représentées dans une base de E ? par des matrices de Y a -t -il un lien entre ces deux représentations ? Soit E ( e1 ,

**21853**: , ep ) une base de E et E ? , en ***prenant*** ( 1 ) comme base de K , on a : On a donc , pour tout x E : Notation 2.1 Dans la suite de ce cours , on conviendra que les matrices à 1 ligne et 1 colonne seront notées comme des scalaires

**22010**: L' ensemble des matrices antisymétriques de Mp ( K ) est noté a. Les matrices M ***vérifiant*** t M M sont nécessairement carrées ! ( a ) Démontrer que Sp ( K ) et Ap ( K ) sont des sous-espaces vectoriels de Mp ( K )

**22742**: Par récurrence sur k en ***utilisant*** le point 2

**23322**: Proposition 2.4 Changement de base pour les vecteurs Soit E un K - espace vectoriel de dimension finie , E et B deux bases de E , x E. Alors : MatE ( x ) PE Autrement dit , en ***multipliant*** à gauche par PE , on obtient les anciennes coordonnées en fonction des nouvelles coordonnées

**25326**: Supposons - les équivalentes , il existe P GLn ( K ) et Q GLp ( K ) telles que N P M Q. En ***notant*** uX l' application linéaire canoniquement associée à une matrice X , on a uN uP uM uQ La conservation du rang en découle , car uP et uQ sont inversibles ( voir la remarque 2.14 , page 115 )

**25993**: Systèmes linéaires Algorithme du pivot de Gauss Notation 2.3 Soit ( k , ) 1 , p , k 6 et K , on appelle matrice de transvection la matrice de Mp ( K ) définie par : Cette matrice est inversible et son inverse est : Démonstration Un calcul direct donne Notation 2.4 Soit k 1 , p , K , on appelle matrice de dilatation la matrice de Mp ( K ) définie par : à la k - ième place Cette matrice est inversible et son inverse est : Démonstration Un calcul immédiat démontre que Notation 2.5 Soit une permutation a de 1 , p , on appelle matrice de permutation la matrice de Mp ( K ) définie par : Cette matrice est inversible et son inverse est : a. C' est - à - dire une bijection de de 1 , p dans 1 , p. Démonstration Si et 0 sont deux permutations de 1 , p alors on remarque que : On prend alors 0 1 en ***remarquant*** que si id1,p , alors P Ip

**26734**: En ***utilisant*** Wxmaxima : On peut aussi travailler à la main

**27044**: Démonstration En ***reprenant*** le résultat du théorème 2.1 , page 127 , il existe un produit de matrices de transvection - dilatationpermutation de Mn ( K ) , noté R et un produit de matrices de transvection - dilatation - permutation de Mp ( K ) , noté S tels que : car rang(A ) p ( car A est inversible ) et Jp , p , p Ip

**27113**: En ***multipliant*** à gauche par S et à droite par S 1 , on obtient ( S R ) A Ip

**27492**: ( b ) Calculer le rang de en fonction de celui de A. 2.7.6 Soit A une matrice de Mn ( R ) tri-diagonale ( c' est - à - dire ***vérifiant*** ai , j 0 dès que i j 2 )

**28083**: Autrement dit , en ***effectuant*** les mêmes opérations sur Ip , on obtient A1

**28487**: A MatE1 , E10 ( 1 1 f E1 ) où 1 est la projection sur E10 parallèlement à E20 C MatE1 , E20 ( 2 2 f E1 ) où 2 idE 0 1 est la projection sur E20 parallèlement à E10 Démonstration Immédiat en ***décomposant*** chaque élément de f ( E1 ) et chaque élément de f ( E2 ) sur la base ( E10 , E20 ) ( en exercice ) En particulier , pour le cas des endomorphismes ( c' est - à - dire E E 0 , E10 E1 et E20 E2 ) , on a : E1 stable par f C 0n2 , p1 et E2 stable par f B 0n1 , p2 Ainsi , les matrices - blocs permettent de visualiser simplement certains sous-espaces stables

**28688**: De plus , n ( K ) GLn ( K ) est stable par M 7 M où A GLn1 ( K ) et D GLn2 ( K ) , alors M GLn1 n2 ( K ) et son inverse est de la forme : On rencontre souvent des transvections - blocs , des dilatations - blocs et des permutations - blocs , ainsi : vérifie clairement ( en ***choisissant*** k et pour avoir des dimensions compatibles ) : soit une opération élémentaire sur les blocs : ( produit à gauche ) ( produit à droite ) De même avec les dilatations : ( produit à gauche ) ( produit à droite ) La permutation - bloc serait par exemple : Cela permet ( avec quelques précautions de calcul ) de faire des manipulations sur les matrices - blocs comme sur des matrices usuelles

**28915**: En ***prenant*** le même ordre de la base canonique , pour toute A Mn ( K ) la matrice de de l' application : Proposition 2.8 Démonstration Il s' agit d' une simple vérification par calculs ( laissée en exercice )

**29810**: En effet , en ***décomposant*** une permutation à l' aide de transpositions : et cela ne dépend pas de la décomposition choisie ( qui ne est pas unique ) car si est une autre décomposition à l' aide de transpositions , on a ( ) ( 1)r ( 1)s ( r et s ont même parité )

**30661**: , xp ) ne change pas en ***ajoutant*** à xi une combinaison linéaire de tous les xk avec k 1 ,

**30879**: , in ) d' indices tous distincts , ce qui correspond exactement aux permutations de 1 , n. On a donc , en ***utilisant*** le fait que est antisymétrique : Pour conclure , il reste à démontrer que est une forme n - linéaire alternée non nulle

**31135**: ***Déterminant*** d' une famille de vecteurs Soit E un K - espace vectoriel de dimension finie avec n dim E 1 , soit E ( e1 ,

**31174**: , en ) une base de E On appelle ***déterminant*** des vecteurs ( x1 ,

**31341**: , xp ) ne change pas en ***ajoutant*** à xi une combinaison linéaire de tous les xj avec j 1 ,

**31448**: C' est le point 2 de la propriété 3.7 , de la présente page en ***remarquant*** que detB est une forme n - linéaire alternée sur E. 2

**31517**: ***Déterminant*** d' une matrice carrée Soit a A ai , j ( i , j)1,n2 Mn ( K ) , on appelle déterminant de A et on note Autrement dit , c' est le déterminant de la famille des n colonnes de A dans la base canonique de Mn,1 ( K )

**31539**: Déterminant d' une matrice carrée Soit a A ai , j ( i , j)1,n2 Mn ( K ) , on appelle ***déterminant*** de A et on note Autrement dit , c' est le déterminant de la famille des n colonnes de A dans la base canonique de Mn,1 ( K )

**31958**: ***Déterminant*** d' un endomorphisme Soit E un K - espace vectoriel de dimension finie et soit u L ( E )

**32031**: Le déterminant de u , noté det u , est défini par det u det MatE ( u ) où E est une base quelconque de E Cette définition a bien un sens : les matrices de u dans deux bases de E différentes sont semblables , donc elles ont même ***déterminant*** ( remarque 3.9 , page précédente )

**32186**: Si c' est le cas , U est inversible donc Méthodes de calcul de déterminants La formule ***définissant*** le déterminant et faisant intervenir Sn est utile théoriquement a mais inutilisable en pratique dès que n est plus grand que 4 ou 5

**32190**: Si c' est le cas , U est inversible donc Méthodes de calcul de déterminants La formule définissant le déterminant et ***faisant*** intervenir Sn est utile théoriquement a mais inutilisable en pratique dès que n est plus grand que 4 ou 5

**32331**: ***Déterminant*** d' une matrice triangulaire Soit A ai , j ( i , j)1,n2 Mn ( K )

**32416**: Dans l' expression ci - dessus , il ne reste plus que les termes ***correspondant*** à une permutation telle que ( j ) j pour tout j 1 , n. Démontrons qu' une telle permutation est l' identité

**32510**: Dans la formule du ***déterminant*** ci - dessus , il ne reste donc plus que le terme correspondant à id1,n , d' où Pour une matrice triangulaire inférieure , on utilise le fait que sa transposée est triangulaire supérieure

**32523**: Dans la formule du déterminant ci - dessus , il ne reste donc plus que le terme ***correspondant*** à id1,n , d' où Pour une matrice triangulaire inférieure , on utilise le fait que sa transposée est triangulaire supérieure

**32573**: det(A ) det(D ) Démonstration Considérons l' application On vérifie que c' est une forme n1 -linéaire alternée sur Mn1 , 1 ( K)p donc , en ***notant*** C ( C1 ,

**32643**: , An1 sont les colonnes d' une matrice A Mn1 ( K ) : Considérons maintenant l' application 0 ) la base On vérifie que c' est une forme n2 -linéaire alternée sur Mn2 , 1 ( K)n2 donc , en ***notant*** C 0 ( C10 ,

**32809**: les opérations Li Li .Lj et Ci Ci .Cj ( transvections ) ne modifient pas la valeur du ***déterminant*** ( d' après le point 5 de la propriété 3.7 , page 159 ) 2

**32838**: les opérations Li .Li et Ci .Ci ( dilatations ) multiplient le ***déterminant*** par ( car le détermiPage 164292 nant est n - linéaire par rapport aux colonnes et aux lignes ) 3

**32872**: les opérations Li Lj et Ci Cj ( échanges ) multiplient le ***déterminant*** par 1 ( car le déterminant est n - linéaire alternée par rapport aux colonnes et aux lignes )

**32904**: Ainsi , cet algorithme permet de calculer des déterminants en se ***ramenant*** à des matrices triangulaires supérieures

**32960**: On peut démontrer que le calcul du déterminant d' une matrice carrée de taille n par la méthode du pivot de Gauss nécessite un nombre d' opération de l' ordre de n3 , ce qui est bien meilleur que n!. Soit à calculer ( n 2 ) : En ***faisant*** les transvections successives ( qui conservent le déterminant ) : On fait apparaître deux lignes identiques , donc : Si a , b , c , d , e , f , g , h et i sont dans K , alors e f aei dhc gbf gec ahf dbi que l' on peut mémoriser par la règle de Sarrus : On remarque , qu' avant développement , Wxmaxima nous proposait une formule non développée , qu' on peut ré-écrire : Que se passe -t -il pour n plus grand ? On reconnaît l' expression : Soit A Mn ( K ) , soit ( k , ) 1 , n , on note a Ak , la matrice de Mn1 ( K ) obtenue à partir de A en supprimant sa k - ième ligne et sa -ième colonne

**33091**: On peut démontrer que le calcul du déterminant d' une matrice carrée de taille n par la méthode du pivot de Gauss nécessite un nombre d' opération de l' ordre de n3 , ce qui est bien meilleur que n!. Soit à calculer ( n 2 ) : En faisant les transvections successives ( qui conservent le déterminant ) : On fait apparaître deux lignes identiques , donc : Si a , b , c , d , e , f , g , h et i sont dans K , alors e f aei dhc gbf gec ahf dbi que l' on peut mémoriser par la règle de Sarrus : On remarque , qu' avant développement , Wxmaxima nous proposait une formule non développée , qu' on peut ré-écrire : Que se passe -t -il pour n plus grand ? On reconnaît l' expression : Soit A Mn ( K ) , soit ( k , ) 1 , n , on note a Ak , la matrice de Mn1 ( K ) obtenue à partir de A en ***supprimant*** sa k - ième ligne et sa -ième colonne

**33267**: , n , on a le développement ***suivant*** la i - ème ligne : ai , j Cofacteuri , j ( A ) 2

**33300**: , n , on a le développement ***suivant*** la j - ième colonne : ai , j Cofacteuri , j ( A ) Démonstration Notons A1 ,

**33370**: Soit j 1 , n. Comme le déterminant est une forme n - linéaire par rapport aux colonnes : En ***échangeant*** la j - ième colonne avec la j 1-ième , puis la j 1-ième avec la j 1-ième jusqu' à ce que la première colonne soit Ci , puisqu' il y a au total j 1 échanges : En échangeant la i - ème ligne avec la i 1-ième , puis la i 1-ième avec la i 1-ième jusqu' à ce que la première ligne soit 1 0 0 , puisqu' il y a au total i1 échanges , on a par la formule du déterminant d' une matrice - blocs ( 1)ij ai , j det(1 ) det Ai , j ai , j Cofacteuri , j ( A ) La formule du développement selon une colonne se démontre de la même façon ( ou en utilisant la transposée )

**33410**: Soit j 1 , n. Comme le déterminant est une forme n - linéaire par rapport aux colonnes : En échangeant la j - ième colonne avec la j 1-ième , puis la j 1-ième avec la j 1-ième jusqu' à ce que la première colonne soit Ci , puisqu' il y a au total j 1 échanges : En ***échangeant*** la i - ème ligne avec la i 1-ième , puis la i 1-ième avec la i 1-ième jusqu' à ce que la première ligne soit 1 0 0 , puisqu' il y a au total i1 échanges , on a par la formule du déterminant d' une matrice - blocs ( 1)ij ai , j det(1 ) det Ai , j ai , j Cofacteuri , j ( A ) La formule du développement selon une colonne se démontre de la même façon ( ou en utilisant la transposée )

**33498**: Soit j 1 , n. Comme le déterminant est une forme n - linéaire par rapport aux colonnes : En échangeant la j - ième colonne avec la j 1-ième , puis la j 1-ième avec la j 1-ième jusqu' à ce que la première colonne soit Ci , puisqu' il y a au total j 1 échanges : En échangeant la i - ème ligne avec la i 1-ième , puis la i 1-ième avec la i 1-ième jusqu' à ce que la première ligne soit 1 0 0 , puisqu' il y a au total i1 échanges , on a par la formule du déterminant d' une matrice - blocs ( 1)ij ai , j det(1 ) det Ai , j ai , j Cofacteuri , j ( A ) La formule du développement selon une colonne se démontre de la même façon ( ou en ***utilisant*** la transposée )

**33556**: En ***itérant*** , nous avons donc au total n ! calculs à faire

**33610**: Soit ( a , b , c ) K3 , calculer : On développe ***suivant*** la première colonne , puis le cofacteur d' indice ( 2 , 1 ) suivant la première ligne

**33625**: Soit ( a , b , c ) K3 , calculer : On développe suivant la première colonne , puis le cofacteur d' indice ( 2 , 1 ) ***suivant*** la première ligne

**33653**: On peut obtenir son terme général en ***utilisant*** le fait que 1 a et 2 a2 b c. On considère la fonction : C' est une fonction polynomiale en x. En effectuant les opérations élémentaires k 2 , n , Ck Ck C1 , puis en développant suivant la première colonne , on en déduit que cette fonction polynomiale est de degré inférieur ou égale à 1

**33677**: On peut obtenir son terme général en utilisant le fait que 1 a et 2 a2 b c. On considère la fonction : C' est une fonction polynomiale en x. En ***effectuant*** les opérations élémentaires k 2 , n , Ck Ck C1 , puis en développant suivant la première colonne , on en déduit que cette fonction polynomiale est de degré inférieur ou égale à 1

**33692**: On peut obtenir son terme général en utilisant le fait que 1 a et 2 a2 b c. On considère la fonction : C' est une fonction polynomiale en x. En effectuant les opérations élémentaires k 2 , n , Ck Ck C1 , puis en ***développant*** suivant la première colonne , on en déduit que cette fonction polynomiale est de degré inférieur ou égale à 1

**33693**: On peut obtenir son terme général en utilisant le fait que 1 a et 2 a2 b c. On considère la fonction : C' est une fonction polynomiale en x. En effectuant les opérations élémentaires k 2 , n , Ck Ck C1 , puis en développant ***suivant*** la première colonne , on en déduit que cette fonction polynomiale est de degré inférieur ou égale à 1

**33749**: Pour x a , le déterminant vaut Pour x b , le déterminant vaut On en déduit alors , puis la valeur du déterminant en ***évaluant*** en x 0

**33857**: Théorème 3.2 Propriété de la comatrice Soit A Mn ( K ) , alors : En particulier , si A est inversible : Démonstration Pour i j , le coefficient en ( i , i ) de A t Com(A ) vaut , en ***utilisant*** la formule du développement suivant la i - ième ligne : ai , k Cofacteuri , k ( A ) det A Pour i 6 j , posons B la matrice obtenue à partir de A en remplaçant la j - ième ligne par la i - ème ligne de A. Puisque B a deux lignes égales , det B 0

**33862**: Théorème 3.2 Propriété de la comatrice Soit A Mn ( K ) , alors : En particulier , si A est inversible : Démonstration Pour i j , le coefficient en ( i , i ) de A t Com(A ) vaut , en utilisant la formule du développement ***suivant*** la i - ième ligne : ai , k Cofacteuri , k ( A ) det A Pour i 6 j , posons B la matrice obtenue à partir de A en remplaçant la j - ième ligne par la i - ème ligne de A. Puisque B a deux lignes égales , det B 0

**33895**: Théorème 3.2 Propriété de la comatrice Soit A Mn ( K ) , alors : En particulier , si A est inversible : Démonstration Pour i j , le coefficient en ( i , i ) de A t Com(A ) vaut , en utilisant la formule du développement suivant la i - ième ligne : ai , k Cofacteuri , k ( A ) det A Pour i 6 j , posons B la matrice obtenue à partir de A en ***remplaçant*** la j - ième ligne par la i - ème ligne de A. Puisque B a deux lignes égales , det B 0

**34001**: Si A est inversible , en ***multipliant*** par A1 : Com(A ) det(A).A1 et comme det A 6 0 , on obtient le résultat

**34286**: On peut alors donner un sens à une aire orientée en ***considérant*** le déterminant sans la valeur absolue

**34395**: On démontre alors que la relation avoir la même orientation est une relation d' équivalence sur l' ensemble des bases de E. En ***fixant*** une base E de E , nous pouvons ainsi séparer les bases de E en deux ensembles ( les deux classes d' équivalences ) : celles qui ont la même orientation que E et celles qui ne ont pas la même orientation que E

**34466**: Toutes les bases ***ayant*** la même orientation que E sont dites directes et les autres indirectes

**34635**: Alors l' unique solution du système de Cramer est donnée par Démonstration donc pour tout k 1 , n , Lorsque k 6 j , le ***déterminant*** ci - dessus est nul puisque deux colonnes sont égales , donc : ce qui donne le résultat puisque det A 6 0

**34788**: Elle a cependant un intérêt théorique , elle permet d' obtenir que la solution X dépend de manière continue ( et même C ) des coefficients de A et B : une petite variation sur les coefficients de A ou de B provoque une petite variation sur les coefficients de X : on peut donc faire un calcul approché de X ! Démontrer que A est inversible et que : 3.1.2 Soit V un K - espace vectoriel de dimension finie et soit p1 N , p2 N , p2 n. On considère l' ensemble des formes ( p1 p2 ) -linéaires ***vérifiant*** pour tout ( x1 ,

**34825**: , xp1 p2 ) V p1 p2 , toute 1 Sp1 et toute 2 Sp2 : Quelle est la dimension du sous-espace vectoriel des formes p - linéaires ***vérifiant*** cette propriété ? det(A B ) det(A)p det(B)n 3.1.4 Démontrer que le volume d' un tétraèdre de sommets A , B , C et D , vaut : det(AB , AC , AD ) 3.1.5 Calculer les déterminants suivants : 3.1.6 Soit A Mn ( K ) , démontrer que : ( a ) On suppose D inversible démontrer que Démontrer par un exemple que ce ne est pas toujours vrai si D est non inversible

**35140**: Résoudre les équations suivantes d' inconnues X Mn ( R ) : 3.1.14 À quelle(s ) condition(s ) , ***connaissant*** les affixes des milieux des côtés d' un polygone fermé à n côtés , existe -t -il un tel polygone ? Préciser dans tous les cas le procédé de construction du ou des polygone(s ) solution(s )

**35863**: Si E est de dimension finie , u est inversible si , et seulement si , il est injectif , d' où le résultat en ***prenant*** 0

**35947**: Le polynôme caractéristique de u , noté u , correspond à la fonction polynomiale : Afin d' alléger les notations et les calculs , on note le polynôme caractéristique u sous la forme d' un polynôme formel ( voir le cours sur les polynômes ) : au lieu d' une fonction polynomiale , où X est l' indéterminée , une variable ***ayant*** les mêmes règles de calcul que celles d' une variable dans K. Ainsi , une fonction polynomiale sur K de la forme se représente par Autrement dit , X correspond à la fonction polynomiale x 7 x. On note KX le K - espace vectoriel des polynômes ( formels ) à coefficients dans K et Kn X le sousespace vectoriel de KX des polynômes de degré inférieur ou égal à n. On définit de la même manière le polynôme caractéristique A det(A X.In ) d' une matrice carrée A Mn ( K )

**36185**: Posons : ai , j si i 6 j trace Atrace u puisque ( k),k a(k),k et ( ) , a ( ) , ne dépendent pas de X. On en déduit le résultat , en ***remarquant*** que le terme constant est u ( 0 ) det(u 0

**36248**: Autrement dit : Démonstration Immédiat en ***utilisant*** la propriété 4.1 , page précédente et en remarquant que u

**36257**: Autrement dit : Démonstration Immédiat en utilisant la propriété 4.1 , page précédente et en ***remarquant*** que u

**36351**: Il pourrait être ***tentant*** de passer systématiquement par le polynôme caractéristique pour trouver les éléments propres de u , ce serait pourtant une grosse erreur , car si il nous permet de trouver les valeurs propres de u , il ne nous donne aucune information sur les espaces propres

**36433**: Ainsi : i1 Ei , i1 Mk ( K ) sont telles que toutes les Ak ( k 1 , n ) ont même polynôme caractéristique alors que les espaces propres associés ont des dimensions ***allant*** de 1 à n. Soit E un K - espace vectoriel de dimension finie non nulle , soit u L ( E ) et soit Sp(u )

**37115**: Alors u est diagonalisable si , et seulement si , dim Eu ( ) dim E Démonstration Le sens direct est immédiat en ***considérant*** une base adaptée à la décomposition de E en somme directe d' espaces propres de u. Notons Sp(u ) 1 ,

**38607**: On peut compléter en une base B1 ( e1 , e2 , e3 ) en ***prenant*** e2 c1 et e3 c2

**39024**: On peut donc écrire : Puisque que ceci est vrai pour toute forme linéaire E ? et en ***remarquant*** que les i , j ne dépendent pas de ( formules de Cramer ) , on a : en utilisant le fait que F est stable par tous les uj

**39044**: On peut donc écrire : Puisque que ceci est vrai pour toute forme linéaire E ? et en remarquant que les i , j ne dépendent pas de ( formules de Cramer ) , on a : en ***utilisant*** le fait que F est stable par tous les uj

**39939**: En ***notant*** H Vect(e2 ,

**40205**: 4.2.3 Soit E est C - espace vectoriel de dimension finie non nulle et u , v et w trois endomorphismes de E qui vérifient : Démontrer que u et v possèdent au moins rang(w ) valeurs propres communes ( en ***comptant*** les multiplicités )

**40465**: , p ) P 1 , Par exemple si : alors A est diagonalisable et on trouve : Dans le cas où A est trigonalisable ( ce qu' on peut toujours supposer en se ***plaçant*** dans C ) , on se contente de trigonaliser la matrice et on résout le système triangulaire associé : ce qui est facile car il est triangulaire

**40542**: Lorsque l' on part d' une suite récurrente multiple ( les coefficients ***étant*** constants ) , on peut vectorialiser et la considérer comme un système récurrent

**40774**: Lorsque l' on part d' une équation différentielle linéaire d' ordre p , à coefficients constants de la forme : on peut la vectorialiser , pour se ramener à un système en ***posant*** Par exemple , on peut transformer : Le cas où la matrice A est diagonalisable est facile car si A P D P 1 avec D Diag(1 ,

**40812**: , p ) , alors En ***posant*** Y ( t ) P 1 X(t ) , on est ramené au système différentiel : qui est un système diagonal

**40836**: En ***notant*** yi les composantes de Y , on a donc : On calcule alors X(t ) P Y ( t )

**40876**: Par exemple , en ***reprenant*** le système de la remarque précédente ( obtenu à partir de 00 ( t ) ( t ) 0 ) , on a Il ne est pas difficile de démontrer que A est diagonalisable sur C , ses valeurs propres sont i et En posant Y P 1 X , on a le système donc il existe ( c1 , c2 ) C2 tel que : Si on ajoute la condition initiale ( qui correspond à ( 0 ) 1 et 0 ( 0 ) 0 ) , on trouve c1 c2 21 donc en particulier : exp(i t ) exp(i t ) On retrouve donc la solution bien connue de 00 ( t ) ( t ) 0 , ( 0 ) 1 et 0 ( 0 ) 0

**40921**: Par exemple , en reprenant le système de la remarque précédente ( obtenu à partir de 00 ( t ) ( t ) 0 ) , on a Il ne est pas difficile de démontrer que A est diagonalisable sur C , ses valeurs propres sont i et En ***posant*** Y P 1 X , on a le système donc il existe ( c1 , c2 ) C2 tel que : Si on ajoute la condition initiale ( qui correspond à ( 0 ) 1 et 0 ( 0 ) 0 ) , on trouve c1 c2 21 donc en particulier : exp(i t ) exp(i t ) On retrouve donc la solution bien connue de 00 ( t ) ( t ) 0 , ( 0 ) 1 et 0 ( 0 ) 0

**41024**: Dans le cas général , on trigonalise A ( ce qui est toujours possible en se ***plaçant*** dans C ) par A P T P 1 où T est une matrice triangulaire supérieure

**41057**: On est donc ramené ( par la même démarche qu' à l' exemple précédent en ***posant*** Y ( t ) P 1 X(t ) ) à un système de la forme où T est une matrice triangulaire supérieure que l' on peut résoudre facilement et on revient à X grâce à la relation X(t ) P Y ( t )

**43711**: En particulier , il existe ak X k KX en ***reconnaissant*** la matrice compagnon C(P ) de P ( qui est unitaire )

**43837**: En particulier , puisque deg u dim E et u 6 0KX , on a : 1 deg u dim E On peut également démontrer ce théorème sans passer par la notion de matrice compagnon , en le ***démontrant*** d' abord dans le cas d' une matrice trigonalisable ( en utilisant notamment le fait que dans ce cas son polynôme caractéristique est scindé )

**43849**: En particulier , puisque deg u dim E et u 6 0KX , on a : 1 deg u dim E On peut également démontrer ce théorème sans passer par la notion de matrice compagnon , en le démontrant d' abord dans le cas d' une matrice trigonalisable ( en ***utilisant*** notamment le fait que dans ce cas son polynôme caractéristique est scindé )

**43873**: Mais on peut toujours s' y ramener en se ***plaçant*** dans le corps des racines de A u avec A la matrice de u dans une base de E ( dans le cas où K R , cela revient à considérer A comme une matrice à coefficients dans C )

**44118**: 5.1.2 Soit E l' ensemble des matrices 2 2 à coefficients dans Z de ***déterminant*** égal à 1

**44184**: ( a ) Démontrer qu' il existe un unique polynôme unitaire P KX ***vérifiant*** : On note mx ce polynôme

**44706**: Puisque K C , il existe une base E dans laquelle T MatE ( u ) est triangulaire supérieure ( n dim E ) : si les valeurs propres i sont toutes égales Alors , pour tout p N , p 2 , Tp est diagonalisable car elle a n valeurs propres distinctes par construction et Tp T quand p , donc u est bien la limite d' une suite d' endomorphismes diagonalisables de E ( les up ***correspondant*** aux matrices Tp dans la base E de E )

**44866**: Alors : pour toute valeur propre de u , u Démonstration Si est une valeur propre de u , en ***notant*** x E 0E un vecteur propre associé , on a ku(x)k u kxk ku(x)k k.xk kxk d' où u en divisant par kxk 6 0E

**44887**: Alors : pour toute valeur propre de u , u Démonstration Si est une valeur propre de u , en notant x E 0E un vecteur propre associé , on a ku(x)k u kxk ku(x)k k.xk kxk d' où u en ***divisant*** par kxk 6 0E

**45709**: d' où le résultat en ***passant*** à la limite N

**45739**: L' exponentielle de matrices sert notamment pour étudier les systèmes linéaires différentiels à coefficients constants ( voir le chapitre 4 ) : La solution ***vérifiant*** la condition initiale X(t0 ) X0 est donnée par : exp(s

**46688**: On conclut en ***démontrant*** que Im i Fu ( i ) et Ker i ( en exercice )

**46755**: En particulier , les projecteurs sur les espaces propres sont des polynômes en u. Il est toujours possible de se ramener au cas où u est scindé en se ***plaçant*** dans le corps des racines de u ( si K R , on se place dans K C )

**46981**: On peut démontrer que d et n sont des polynômes en u , puisque ( en ***reprenant*** les notations de la En particulier , le couple ( d , n ) est unique

**47950**: On conclut alors en ***appliquant*** la réduction de Frobenius à u. On peut aussi le démontrer directement ( voir l' exercice 5.3.11 , page 251 )

**49095**: On obtient : Il vient alors : que l' on peut résoudre en ***utilisant*** le développement en série entière de x 7 ( 1 x)1p et le fait que la matrice D0 N 0 est nilpotente

**49127**: Soit A la matrice : Elle est de ***déterminant*** 2 0

**49199**: En ***utilisant*** la série entière du logarithme , on a donc : où p est l' indice de nilpotence de N , c' est - à - dire le plus petit entier p N tel que N p 0n

**49516**: Les matrices ont le même rang ( 4 ) , la même trace ( 0 ) , le même ***déterminant*** ( 0 ) , le même polynôme caractéristique ( ( X)7 ) , le même polynôme minimal ( X 3 ) , le même spectre ( 0 ) , la même dimension des espaces propres ( 3 ) et la même dimension des espaces caractéristiques ( 7 )

**49804**: Les matrices suivantes sont semblables : Soit E un K - espace vectoriel de dimension finie non nulle , u L ( E ) et x E. On définit : Ix l' idéal des polynômes annulateurs x , c' est - à - dire le noyau de : KX E définie par ( P ) x le polynôme minimal de x ( le polynôme unitaire ***engendrant*** l' idéal Ix )

**49985**: En ***notant*** k deg u , une base de hxi est donnée par : On complète en une base ( e1 ,

**50834**: Étape 2 Si il existe sur la première ligne ( ou la première colonne ) un élément m1,k ( ou mk,1 ) non multiple de m1,1 , on le remplace ( en ***utilisant*** une transvection ) par le reste de la division euclidienne de m1,k ( ou mk,1 ) par m1,1 et on revient à l' étape 1 en permutant les colonnes ( ou les lignes ) 1 et k. Etape 3 L' étape 2 a pour effet de diminuer strictement ( M ) , elle ne peut donc se réaliser qu' un nombre fini de fois

**51316**: En déduire la construction d' un corps à 4 éléments et d' un corps à 8 Un exemple d' utilisation de la réduction sur un corps fini Dans tout ce chapitre , nous avons travaillé dans un corps commutatif quelconque , et plus nécessairement dans R ou C. Voici un petit exemple de synthèse ***montrant*** comment on peu utiliser les notions vues ici dans un corps fini

**51525**: Dans Z2 Z La vectorialisation de la suite ( en ***notant*** a la classe de a dans Z2 Z ) donne On obtient alors que A est semblable à une matrice parmi ( Z2 Z ) impossible de période 1 ou 2 de période 1 si son polynôme caractéristique est scindé

**51595**: Lorsque son polynôme caractéristique ne est pas scindé , de degré 2 , il est alors irréductible ( c' est X 2 X 1 ) donc , en ***posant*** C(A ) , et en se plaçant dans M2 ( Z2 Z ) , les racines de A sont alors et I2 , distinctes

**51602**: Lorsque son polynôme caractéristique ne est pas scindé , de degré 2 , il est alors irréductible ( c' est X 2 X 1 ) donc , en posant C(A ) , et en se ***plaçant*** dans M2 ( Z2 Z ) , les racines de A sont alors et I2 , distinctes

**51801**: De plus , si n N , à l' aide de la formule du binôme de Newton , on a si 6 0 ( cas évident où la période est 1 , à partir du second rang ) et 6 1 ( cas simple ou la périodicité est 5 , la première condition ci-dessous ***étant*** inutile ) , la matrice est égale à I2 si ce qui nous donne une période de 10 ou 20

**51849**: mod 5 et n Lorsque le polynôme caractéristique de A ne est plus scindé , il est irréductible ( car de degré 2 ) , en ***posant*** C(A ) , et en travaillant dans le corps K Z5 Z qui est de cardinal 25 , on a ( même démonstration que Fermat ) on a donc de période 3 , 6 , 8 , 12 ou 24

**51855**: mod 5 et n Lorsque le polynôme caractéristique de A ne est plus scindé , il est irréductible ( car de degré 2 ) , en posant C(A ) , et en ***travaillant*** dans le corps K Z5 Z qui est de cardinal 25 , on a ( même démonstration que Fermat ) on a donc de période 3 , 6 , 8 , 12 ou 24

**51892**: En ***enlevant*** celle qu' on connaît ( 1 , 2 et 4 correspondant aux matrices précédemment vues ) Dans Z5 Z les périodes de la suite ( un ) nN sont , à partir d' un certain rang dans Finalement les périodes possibles sont , d' après le théorème chinois ( on fait le PPCM des périodes dans Z2 Z et dans Z5 Z ) Juste pour le plaisir , construisons une situation où la période est 60

**51903**: En enlevant celle qu' on connaît ( 1 , 2 et 4 ***correspondant*** aux matrices précédemment vues ) Dans Z5 Z les périodes de la suite ( un ) nN sont , à partir d' un certain rang dans Finalement les périodes possibles sont , d' après le théorème chinois ( on fait le PPCM des périodes dans Z2 Z et dans Z5 Z ) Juste pour le plaisir , construisons une situation où la période est 60

**52004**: Le polynôme caractéristique dans Z Z doit être X 2 X 1 ( pour obtenir le 3 ) , et être de la forme ( X ) 2 dans Z5 Z , ( matrice ***étant*** non-diagonalisable ( pour obtenir le 20 )

**52099**: La vérification par le calcul donne , pour les 63 premiers termes ( avec u0 u1 1 ) Application linéaire , 46 Automorphisme , 46 adaptée à une somme directe , 43 ante - duale , 70 d' un espace vectoriel , 35 Codimension , 72 Coefficients d' une matrice , 90 Cofacteur d' une matrice carrée , 170 Comatrice , 170 Combinaison linéaire , 21 ***Commutant*** d' un endomorphisme , 248 Condition initiale ( d' un système linéaire ) , 207 Décomposition LU , 180 Dimension d' un espace vectoriel , 39 Drapeau stable , 199 Droite vectorielle , 39 Dual d' un espace vectoriel , 68 Décomposition de Dunford , 247 Décomposition en somme directe , 32 Déterminant d' un endomorphisme , 162 d' une famille de vecteurs , 158 d' une matrice carrée , 160 de Vandermonde , 173 Éléments propres , 184 Endomorphisme , 46 diagonalisable , 196 trigonalisable , 199 Équation d' un hyperplan , 71 Espace caractéristique , 245 Espace propre d' un endomorphisme , 183 d' une matrice , 183 Espace vectoriel , 19 de dimension finie , 38 Exponentielle d' endomorphisme , 240 Famille duale , 69 Fonctions spline , 85 Forme p - linéaire , 154 anti-symétrique , 155 symétrique , 155 Forme de Smith , 273 Forme linéaire , 46 , 68 Groupe symétrique , 151 Hyperplan d' un espace vectoriel , 71 Idéal annulateur , 230 d' une application linéaire , 49 d' une matrice , 114 Interpolation de Lagrange , 80 Isomorphisme , 46 Matrice , 89 anti-symétrique , 106 augmentée , 140 circulante , 198 compagnon , 232 d' un vecteur , 90 d' une application linéaire , 90 d' une famille de vecteurs , 109 de dilatation , 121 de passage , 110 de permutation , 121 de transvection , 121 diagonale , 106 diagonalisable , 196 identité , 100 inversible , 108 symétrique , 106 triangulaire , 106 trigonalisable , 200 semblables , 119 équivalentes , 119 Mineur d' une matrice carrée , 170 Multiplicité d' une valeur propre , 195 d' une application linéaire , 49 d' une matrice , 114 Orthogonal ( direct ) d' une partie , 77 ( indirect ) d' une partie , 77 Partie ou famille génératrice , 25 Partition d' un ensemble , 116 Permutation , 151 Plan vectoriel , 39 caractéristique , 193 d' endomorphisme , 227 de matrice , 227 minimal , 231 d' espaces vectoriels , 22 de deux matrices , 98 de Kronecker , 146 Projecteur , 53 Projection , 52 Trace d' une matrice , 107 Transposition , 152 Transposée d' une matrice , 103 Valeur propre d' un endomorphisme , 183 d' une matrice , 183 Vecteur propre d' un endomorphisme , 183 d' une matrice , 183 Vecteurs , 20 indépendants , 34 linéairement dépendants , 34 d' une application linéaire , 55 d' une matrice , 114 Rayon spectral , 239 d' équivalence , 116 réflexive , 116 symétrique , 116 transitive , 116 Scalaires , 20 Second membre ( d' un système linéaire ) , 207 Signature d' une permutation , 152 de sous-espaces vectoriels , 28 d' une famille d' espaces vectoriels , 31 de deux sous-espaces vectoriels , 30 Sous-espace vectoriel , 23 engendré par une partie , 25 stable , 52 d' un endomorphisme , 183 d' une matrice , 183 Supplémentaire d' un sous-espace vectoriel , 32 Support d' une famille , 26 Symbole de Kronecker , 58 Symétrie , 54 associé , 207 Système linéaire , 78 de Cramer , 140 différentiel , 215 homogène , 78 associé , 78 récurrent , 207 Caractérisation des applications linéaires injectives , 67 surjectives , 67 des automorphismes en dimension finie , 57 des classes de similitude , 270 des endomorphismes diagonalisables , 197 , 229 trigonalisables , 200 , 234 des hyperplans , 72 des matrices équivalentes , 120 Changement de base pour les applications linéaires , 111 pour les vecteurs , 111 Correspondance matrices - blocs et décomposition en somme directe , 144 de co-diagonalisation , 205 de co-trigonalisation , 205 Développement d' un déterminant , 171 Forme de Jordan d' un endomorphisme nilpotent , 249 trigonalisable , 249 Formule de Grassman , 44 Invariants de similitude , 270 Lemme des noyaux , 228 Mise en équation des sous-espaces de codimensions finies , 75 Pivot de Gauss , 127 Rang d' une composée , 56 d' extension linéaire , 66 de Cayley - Hamilton , 233 de factorisation des applications linéaires , 62 de Frobenius , 269 de l' échange , 38 de la base incomplète , 40 des faisceaux d' hyperplans , 73 du rang , 57 du relèvement linéaire , 65 Commandes Wxmaxima binomial , 208 charpoly , 234 columnswap , 279 eigenvalues , 184 , 190 identfor , 175 cspline , 86 length , 136 load(solverec ) , 211 polytocompanion , 270 , 271 randompermutation , 137 setify , 26 solverec , 211 kroneckerproduct , 147 Commandes Python matplotlib , 26 binomial , 208 Dictionnaire , 113 .factorlist , 235 BlockDiagMatrix , 272 BlockMatrix , 148 expand , 186 Function , 192 initsession , 26 interpolate , 82 , 85 interpolatingspline , 86 .charpoly , 235 .cofactormatrix , 176 .extract , 170 .allcoeffs , 271 rsolve , 213 integer , 192 Figure 5.1 Similitude Trajectoires du système :