# La Likes box

La *Like Box* est une petite boîte qui reprend l'idée des *likes* du réseau social *facebook*. La *Likes Box* est un dispositif physique qui rend concret l'action de « liker » une page sur le réseau social.

Les *likes* sur le réseau étant soumis à l'identification préalable de chaque utilisateur, nous avons opté pour une page non liée au réseau *facebook*, mais reprenant son identité visuelle. Notre idée sera de comparer la popularité de cette page non officielle, avec celle de la page officielle.

# Le festival *Panoramic*

Le [festival *Panoramic*](http://associationlecercle.fr/cinema/panoramic/) de Saint-Brieuc est un « événement entièrement dédié au cinéma et à l’éducation à l’image ». [L'édition 2018](http://associationlecercle.fr/actualites/festival-panoramic-2018/) se déroule du lundi 23 avril au mardi 1er mai 2018; elle est dédiée au cinéma argentin.

Le festival est organisé par [l'association Le Cercle](http://associationlecercle.fr/).

# Conception

La base matérielle de la *Likes Box* utilise une Rapsberry Pi, connectée à un bouton. Le logiciel associé est écrit en Python.

STEPS:

1. Setup websocket server.
   CA: make the first exchange with the (static) page
2. Setup web server.
   CA: load the page from the browser
3. Add the mechanics for updating the counter, saving and loading the state at startup
   CA: test: start the program, and update the counter on the webpage
4. Add the GPIO mechanics through callback, check if an emulator exists for testing the code
   CA: test the whole program, if possible
5. Add a statistics module?
