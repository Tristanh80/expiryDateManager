
# Choix techniques

Pour la représentation des données, j'ai fait le choix de stocker uniquement le numéro du produit (gtin) ainsi qu'une date correspondant a la date d'expiration.

  

## Views

J'ai ensuite créé plusieurs views. Une première qui va lister tous les produits par date d'expiration croissante. Ainsi, on va pouvoir voir quel produit expire le plus rapidement et agir en conséquence.

J'ai également créé une seconde vue pour l'ajout des produits. Si la méthode employé est POST, alors c'est que nous voulons ajouter un produit dans la base de données, dans ce cas on vérifie si le produit existe déjà, si oui on modifie sa date, sinon on créé le produit. Si la méthode est GET, alors on affiche juste le formulaire pour saisir le produit et la date d'expiration.

J'ai aussi créé une page d'administration avec django pour pouvoir modifier les données si nécessaire.

## Axes d'amélioration
Les possibilités d’amélioration sont multiples. Tout d'abord, revoir le design du site pour le rendre un peu plus attractif a l’œil.

On peut également imaginer ajouter un tri par date d'expiration croissante ou décroissante.

Un troisième point d’amélioration serait de pouvoir supprimer un produit. La seule façon pour l'instant de le faire est en étant dans la page d'administration du site.