# Corn Ninja - Le jeu

## Contexte
L'idée initiale était de créer un jeu inspiré de *Fruit Ninja*, mais avec une touche originale : remplacer les fruits par des **popcorns** ! Le tout dans une ambiance cinéma, car les popcorns sont l'aliment emblématique du cinéma. 

Dans *Corn Ninja*, les **maïs** n'ont pas à être tranchés, mais **explosent** pour se transformer en délicieux **popcorns**. La bombe dans le jeu est représentée par une **poule**, ce qui apporte une touche humoristique, car la poule picore du maïs et, si on ne désamorce pas la bombe, on perd ! 

De plus, les **glaçons** sont des **granités**, un clin d'œil supplémentaire à l'atmosphère typique des cinémas.

## Ambiance sonore
- **Musique d'accueil** : Bruit d'un accueil de cinéma avec des sons de distributeurs de boissons et de foule.
- **Musique de jeu** : Ambiance de théâtre japonais, pour rappeler l'esprit ninja.

## Gameplay

1. **Menus interactifs**  
   Le joueur commence par choisir entre différents menus : le menu principal, le niveau de difficulté (facile ou difficile), et le choix de la langue.

2. **Transformations du maïs**  
   Le maïs (représenté par des objets à l'écran) se transforme en popcorn lorsqu'il est frappé. Le joueur doit appuyer sur les touches correspondantes pour "faire exploser" le maïs en popcorn.

3. **Objets spéciaux**  
   - **La poule-bombe** : Si le joueur appuie sur la touche correspondante avant que la bombe n'atteigne le bas de l'écran, il désamorce la bombe, sinon c'est la fin du jeu.
   - **Les granités** : Si un granité (glace) touche le bas de l'écran, il se dissipe, mais si le joueur appuie sur la touche, il gèle les objets et ralentit leur mouvement.

4. **Game Over**  
   Lorsque la poule-bombe atteint le bas de l'écran et que le joueur n'a pas réagi à temps, le jeu se termine et le score final est affiché.

## Code Technique

### Structure modulaire
Le code est structuré de manière modulaire pour assurer une flexibilité et faciliter les modifications :
- **Menu** : Différents menus pour gérer les options de jeu, de langue et de niveau.
- **Gestion des objets** : Les popcorns et les objets spéciaux sont gérés de façon modulaire, facilitant l'ajout de nouvelles fonctionnalités ou objets dans le futur.
- **Effets sonores et musiques** : Les sons sont gérés par Pygame avec des boucles et des événements pour ajouter une ambiance immersive.

### Graphismes et animations
Le jeu affiche les objets (popcorns, bombes, granités) avec des couleurs vives pour rendre l'expérience visuelle attrayante. Les animations incluent l'explosion des popcorns et la transition entre les différents états du jeu (normal, game over, etc.).

## Conclusion
*Corn Ninja* combine **technique** et **créativité** pour offrir une expérience de jeu unique. L'humour, l'originalité des objets et l'ambiance cinéma rendent ce jeu à la fois fun et dynamique.
