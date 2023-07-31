<h1> init_projet_python </h1>

## Pour partager votre projet dans GitHub afin que d’autres utilisateurs puissent travailler dessus, effectuez les étapes suivantes :

1. **Générer le fichier `requirements.txt`** :
   - Ouvrez une invite de commande (ou un terminal) dans le répertoire racine de votre projet Python.
   - Exécutez la commande `pip freeze > requirements.txt`.
   - Cette commande générera un fichier `requirements.txt` qui contient la liste de toutes les dépendances (packages) dont votre programme a besoin, ainsi que leurs versions spécifiées. Cela permettra aux autres utilisateurs de recréer facilement l'environnement virtuel avec les mêmes dépendances que celles que vous utilisez pour le projet.

2. **Créer le fichier `.gitignore`** :
   - Dans le répertoire racine de votre projet, créez un fichier `.gitignore` à l'aide d'un éditeur de texte.
   - Ajoutez les règles d'ignorance appropriées au fichier `.gitignore`.
   - Assurez-vous d'inclure dans le fichier `.gitignore` les fichiers que vous ne souhaitez pas inclure dans le référentiel Git, tels que les fichiers de sauvegarde, les fichiers binaires, les fichiers d'environnement local, etc.
   - **Important** : Assurez-vous de ne pas inclure `requirements.txt` dans le fichier `.gitignore`, car vous souhaitez que les autres utilisateurs aient accès à ce fichier pour installer les dépendances requises.

3. ~~**Enregistrer votre code sur GitHub** :~~ <sub>(extension github pull request)</sub>
  ~~- Initialisez un référentiel Git dans le répertoire racine de votre projet si vous ne l'avez pas déjà fait, en utilisant la commande `git init`.~~
  ~~- Ajoutez tous les fichiers du projet au suivi avec la commande `git add .`.~~
  ~~- Effectuez un commit pour enregistrer les fichiers dans l'historique du référentiel local avec la commande `git commit -m "Initial commit"`.~~
  ~~- Créez un nouveau référentiel sur GitHub (si vous n'en avez pas déjà un) et suivez les instructions pour lier votre référentiel local à votre référentiel distant sur GitHub en utilisant la commande `git remote add origin URL_DU_REPO_GITHUB`.~~
  ~~- Enfin, poussez vos fichiers vers le référentiel distant sur GitHub avec la commande `git push origin master` (ou le nom de votre branche principale).~~


## Pour consommer un projet en tant que contributeur (collègue développeur), effectuez les étapes suivantes :

1. **Récupérer le projet depuis GitHub** :
   - Clonez le référentiel GitHub sur votre machine en utilisant la commande `git clone URL_DU_REPO_GITHUB`.
   - Cela créera une copie locale du projet sur votre machine.

2. **Créer un environnement virtuel** :
   - Dans le répertoire racine du projet que vous venez de cloner, créez un nouvel environnement virtuel en utilisant `virtualenv`, `venv`, ou tout autre outil de gestion d'environnement virtuel que vous préférez.

3. **Activer l'environnement virtuel** :
   - Activez l'environnement virtuel nouvellement créé en utilisant la commande spécifique à l'outil que vous avez utilisé pour le créer.

4. **Restaurer le projet avec les dépendances** :
   - Dans l'environnement virtuel, exécutez la commande `pip install -r requirements.txt`.
   - Cette commande recherchera le fichier `requirements.txt` et installera automatiquement toutes les dépendances spécifiées dans ce fichier. Ainsi, vous aurez un environnement identique à celui de l'auteur du projet.

5. **Lancer l'application** :
   - Avec l'environnement virtuel activé et les dépendances installées, vous pouvez désormais exécuter l'application en utilisant la commande appropriée (par exemple, `python code.py` si `code.py` est le fichier principal de l'application).
________________________
# Mettre à jour un package :
`pip install <name of package> --upgrade`
