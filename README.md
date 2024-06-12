------------------------------------------------------------------------------------------------------
PROJET CLOE855
------------------------------------------------------------------------------------------------------
Quelles sont les notions qui vont être abordées au cours de cet atelier ?  
Ce support a été créé pour vous accompagner dans la réalisation de votre atelier "développer et sécuriser une solution cloud". Il s'agit ici de concevoir et sécuriser des solutions d'infrastructure virtualisées et cloud. Plus précisement, cet atelier a pour objectif de mettre en pratique vos connaissances informatiques liées à la sécurisation d’une infrastructure IT virtualisée. Il s'agit d'une étude de cas concernant une entreprise « fictive » ayant un besoin de sécuriser sa solution cloud. Dans cette étude de cas vous devrez réaliser :
 - Mise en service d'une solution Web.  
 - Mettre en place une solution pour sécuriser les clés SSH de la solution.  
 - Mettre en place des scripts d'automatisation.
  
Cet atelier a également pour objectif de vous apprendre à créer des bases de données grace à Python et SQLite. Vous allez ensuite exploiter cette base de données via la construction d'API. Vous allez donc utiliser et mettre en oeuvre au travers de cet atelier, un serveur Python utilisant le Framework Flask. 
Vous allez créer des API, découvrir les Actions et les Secrets GitHUB pour au final mettre en service et exploiter une base de données sur un serveur Web.  
  
Large programme mais tout à fait accessible et ne nécessitant pas de base technique particulière. Juste de l'observation et de la rigueur dans votre travail.

-------------------------------------------------------------------------------------------------------
Séquence 1 : GitHUB
-------------------------------------------------------------------------------------------------------
Objectif : Création d'un Repository GitHUB pour travailler avec son projet  
Difficulté : Très facile (~10 minutes)
-------------------------------------------------------------------------------------------------------
GitHUB est une plateforme en ligne utilisée pour stocker le code de son programme.
GitHUB est organisé en "Repository", c'est à dire en répertoire (contenant lui même des sous répertoires et des fichiers). Chaque Repository sera indépendant les un des autres. Un Repository doit être vu comme un projet unique (1 Repository = 1 Projet). GitHUB est une plateforme très utilisée par les informaticiens.

**Procedure à suivre :**  
1° - Créez vous un compte sur GitHub : https://github.com/  
Si besoin, une vidéo pour vous aider à créer votre propre compte GitHUB : [Créer un compte GitHUB](https://docs.github.com/fr/get-started/onboarding/getting-started-with-your-github-account)  
A noter que **si vous possédez déjà un compte GitHUB, vous pouvez le conserver pour réaliser cet atelier**. Pas besion d'en créer un nouveau.  
Remarque importante : **Lors de votre inscription, utilisez une adresse mail valide. GitHUB n'accepte pas les adresses mails temporaires**  

2° - Faites un Fork de ce Repository : [MSPR_CLO855](https://github.com/bstocker/MSPR_CLOE855)  
Voici une vidéo d'accompagnement pour vous aider dans les "Forks" : [Forker ce projet](https://youtu.be/p33-7XQ29zQ)    
  
**Travail demandé :** Créé votre compte GitHUB, faites le fork de ce projet et **copier l'URL de votre Repository GitHUB dans la discussion Discord**.

Notion acquise lors de cette séquence :  
Vous avez appris lors de cette séquence à créer des Repository pour stocker et travailler avec votre code informatique. Vous pourez par la suite travailler en groupe sur un projet. Vous avez également appris à faire des Forks. C'est à dire, faire des copies de projets déjà existant dans GitHUB que vous pourrez ensuite adapter à vos besoins.
  
---------------------------------------------------
Séquence 2 : Création d'un hébergement en ligne
---------------------------------------------------
Objectif : Créer un hébergement sur Alawaysdata  
Difficulté : Faible (~15 minutes)
---------------------------------------------------

Rendez-vous sur **https://www.alwaysdata.com/fr/**  
  
Remarque : **Attention à bien vous rappeler de vos Login/Password** lors de la création de votre compte site car vous en aurez besoin plus tard pour la création de vos Secrets GitHUB.  
  
Voici une vidéo d'accompagnement pour vous aider dans cette séquence de création d'un site sur Alwaysdata : [Vidéo Alwaysdata](https://youtu.be/6cuHjy8n968)  
  
**Procédure :**  
1° - Créez votre compte Alwaysdata (gratuit jusqu'à 100Mo, aucune carte nécéssaire).  
2° - Depuis la console d'administration (Le panel d'administration de Alwaysdata) :  
 . 2.1 - Cliquez sur "Sites" (Colonne de gauche) puis **supprimer votre site PHP** (via l'icone de la Poubelle).  
 . 2.2 - **Installer ensuite une application Flask** (Bouton **+ Installer une application**).  
 . . 2.2.1 Adresses = utilisez le sous-domaine qui vous appartient que vous trouverez dans l'information " Les sous-domaines suivants vous appartiennent et sont actuellement inutilisés : {Site}.alwaysdata.net  
 . . 2.2.2 Répertoire d'installation = **/www/flask**  
 . 2.2.3 N'oubliez pas d'Accepter les conditions.  
3° - Autoriser les connexions SSH :  
 . 3.1 - Cliquez sur SSH (Accès distant).  
 . 3.2 - Modifier les paramètres de votre utilisateur.  
 . 3.3 - Définissez si besion un nouveau mot de passe.  
 . 3.4 - Cliquez sur **Activer la connexion par mot de passe**.  
  
**Travail demandé :** Mettre en ligne votre application Flask "Hello World !" et **copier l'URL de votre site dans la discussion Discord**.  
  
Notions acquises lors de cette séquence :  
Vous avez créer un hébergement (gratuit) et découvert également que vous pouvez installer bien d'autres applications (Django, Drupal, Jenkins, Magento, Symphony, etc...). Les perspectives sont nombreuses.

---------------------------------------------------
Séquence 3 : Les actions GitHUB (Industrialisation Continue)
---------------------------------------------------
Objectif : Automatiser la mise à jour de votre hébergement Alwaysdata
Difficulté : Moyen (~25 minutes)
---------------------------------------------------
Depuis le repository que vous venez de créer dans GitHUB vous allez à présent créer une Action afin de déployer votre code automatiquement sur votre serveur Alwaysdata via une connexion SSH. Cette action passe par la création d'un fichier **CICD.yml** dans GitHub dont le contenu sera executé à chaque commit des devellopeurs (c'est à dire à chaque modification de votre code dans GitHUB). Ce fichier est à déposer dans le répertoire **.github/workflows/CICD.yml** de votre repository. **Attention au point devant .github**/workflows/CICD.yml qui est obligatoire puisqu'il s'agit d'un répertoire caché pour le système.

-------------
**Etape 1 : Création d'une action dans GitHUB**  
Créer une Action dans votre repository GitHUB pour y deposer le script suivant (fichier .github/workflows/CICD.yml) :

```
name: Industrialisation continue sur le serveur Alwaysdata
on: push
jobs:
  Connexion:
    runs-on: ubuntu-latest
    steps:
      - name: Connexion SSH avec le serveur
        uses: appleboy/ssh-action@master
        with:
          host: "ssh-${{ secrets.USERNAME }}.alwaysdata.net"
          username: ${{ secrets.USERNAME }}
          key: ${{ secrets.SSH_KEY }}
          script: |
            cd $HOME/www/

  Copy:
    needs: Connexion
    runs-on: ubuntu-latest
    steps:
      - name: Connexion SSH avec le serveur
        uses: appleboy/ssh-action@master
        with:
          host: "ssh-${{ secrets.USERNAME }}.alwaysdata.net"
          username: ${{ secrets.USERNAME }}
          key: ${{ secrets.SSH_KEY }}
          script: |
            last_directory=$(basename ${{ runner.workspace }})
            cd $HOME/www/
            git clone https://github.com/${{ github.repository }}.git
            # Vérifier si le répertoire de destination existe
            if [ "$(ls -A ./flask)" ]; then
              rsync -r ./$last_directory/ ./flask
              rm -rf ./$last_directory
            else
              echo "Le répertoire flask de destination sur votre serveur n'existe pas"
              exit 1
            fi
  Restart:
    needs: Copy
    runs-on: ubuntu-latest
    steps:
      - name: Restart Alwaysdata site
        run: |
          response_code=$(curl -s -o /dev/null -w "%{http_code}" -X POST --basic --user "${{ secrets.ALWAYSDATA_TOKEN }}:" https://api.alwaysdata.com/v1/site/${{ secrets.ALWAYSDATA_SITE_ID }}/restart/)
          # Vérifier le code de réponse HTTP
          if [ "$response_code" -eq 204 ]; then
            echo "Relance de votre site réussi"
          elif [ "$response_code" -eq 404 ]; then
            echo "Vous n'avez pas renseigner correctement votre secret ALWAYSDATA_SITE_ID"
            exit 1  # Quitter avec un code d'erreur
          elif [ "$response_code" -eq 401 ]; then
            echo "Vous n'avez pas renseigner correctement votre secret ALWAYSDATA_TOKEN"
          exit 1  # Quitter avec un code d'erreur
          else
            echo "Échec du redémarrage avec le code de réponse : $response_code"
            exit 1  # Quitter avec un code d'erreur
          fi
```
-------------
**Etape 2 - Création des secrets :**  
Vous avez besoin de créer des secrets dans GitHUB afin de ne pas divulguer des informations sensibles aux internautes de passage dans votre repository (vos login, clés, dns, etc..). Ci-dessous une vidéo pour vous expliquer le processus de création d'un secret dans GitHUB. Par exemple le création d'un secret qui serait intitulé HOST_DNS (ce secret n'est pas utilisé dans ce projet) https://www.youtube.com/watch?v=7CZde1a7rq0

-----
Les secrets dans votre Repository Github que vous avez à créer sont les suivants (il y a **4 secrets au total** à créer dans ce projet) :  
**USERNAME** = Le login que vous avez utilisé lors de la création de votre site (également appelé abonnement) doit être stocké dans ce secret USERNAME.  
**SSH_KEY** = Vous devez mettre dans ce secret l'intégralité de la clé privée ci-dessous (de ----BEGIN jusqu'à la fin KEY----- inclut)  
```
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
QyNTUxOQAAACC4LTWO3FUlXJLlxmPXy2enZnARnnqRgZ6+7lzNvwL7OwAAAJBn8JtCZ/Cb
QgAAAAtzc2gtZWQyNTUxOQAAACC4LTWO3FUlXJLlxmPXy2enZnARnnqRgZ6+7lzNvwL7Ow
AAAEC67kacvftsZrOeW19wnOUYHgxqwzb4YYdACf5+MV1tVLgtNY7cVSVckuXGY9fLZ6dm
cBGeepGBnr7uXM2/Avs7AAAABm5vbmFtZQECAwQFBgc=
-----END OPENSSH PRIVATE KEY-----
```

En revanche la clé public doit être déposée directement sur votre serveur Alwaysdata. C'est à dire que vous devez vous connecter en SSH sur le serveur Alwaysdata. Pour cette connection en SSH, vous pouvez utiliser le logiciel de votre choix (putty, cmd, ...) ou utiliser directement l'interface web proposé par Alwaysdata dans la console d'administration. Voici un exemple de console SSH proposée par Alwaysdata : https//ssh-etudiant11.alwaysdata.net
Attention !! Vous devez activer la connexion par mot de passe pour votre utilisateur SSH dans la console d'administration Alwasdata (Voir paragraphe 3.1 de la séquence 2).

**Procédure pour la clé public :**  
 . 2.1 - Connectez vous à votre serveur Alwaysdata via la console ssh de votre choix (ex : https://ssh-etudiant11.alwaysdata.net/). Remarque importante : Activer la connexion par mot de passe pour votre utilisateur SSH.  
 . . 2.1.1 : Le login est celui de votre compte site (celui en haut à gauche dans la console d'administration d'Alwaysdata).  
 . . 2.1.1 : Le mot de passe du compte site est à taper en aveugle (c'est à dire que le curseur de la console ne bouge pas et c'est tout à fait normal).  
 . 2.2 - Ensuite, toujours depuis cette même console SSH, créer à présent le répertoire .ssh en tapant le commande suivante : **mkdir .ssh**  
 . 2.3 - Récupérer la clé public en tappant la commande suivant dans la console SSH : **git clone https://github.com/bstocker/keyalwaysdata.git**  
 . 2.4 - Déplacer cette clé pour la mettre dans le bon répertoire de votre serveur via la commande : **mv keyalwaysdata/authorized_keys .ssh**  
  
Astuce : Pour coller du texte dans votre navigateur, vous pouvez utiliser la combinaison de touche Ctrl+Shift+v pour coller votre texte dans le navigateur.
  
Pour vérifier que tout est en ordre et que votre clé public est bien déclarée sur votre serveur, tapez la commande suivante depuis votre console ssh :
**cat .ssh/authorized_keys**. Le résultat dans votre console doit être le suivant :
```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILgtNY7cVSVckuXGY9fLZ6dmcBGeepGBnr7uXM2/Avs7 noname
```
Si c'est le cas, c'est que l'opération est réussie.  
  
**3° - Génération d'un token :**  
Afin de pouvoir utiliser les API de la solution Alwaysdata (dans notre cas demanderons des relances régulaires de serveur), il faut créer un token dans Alwaysdata.

**ALWAYSDATA_TOKEN** = Le token est à créer depuis l'interface d'administration Alwaysdata. Cliquez sur votre profil en haut à droite, puis sur 'Profil' puis sur 'Gérer les tokens'. Laissez le champ "Adresses IP autorisées" vide. Dans le cas contraire vous limiteriez les connexions seulement à une adresse IP. Pour le champ Application* mettez "flask" par exemple.

**ALWAYSDATA_SITE_ID** = Vous trouverez l'ID de votre site depuis l'interface d'administration Alwaysdata puis dans les paramètres de votre site. Il s'agit du petit engrenage à droite de votre site (dans le titre #XXXXX) XXXXX étant l'ID de votre site. Ne prenez pas le # mais juste les chiffres.

Votre script CICD est à présent prêt à être déclanché. Celui-ci se déclenchera automatiquement à chaque Commit de votre code (c'est à dire à chaque modification de votre code dans Github). Procédez à une modification de votre code dans Github pour vérifier que votre action fonctionne bien correctement. Vous pouvez modifier ce Readme par exemple et faire ensuite votre Commit.    
  
Notions acquises de cette séquence :  
Vous avez vu dans cette séquence comment créer des secrets GiHUB afin de mettre en place de l'industrialisation continue. Nous avons créé des secrets ainsi que des clés public et privée. L'utilité des scripts d'actions (C'est à dire des scripts exécutés lors des Commits) est très importante mais sortes malheureusement du cadre de cet atelier faute de temps. Toutefois, je vous invites à découvrir cet outil via les différentes sources du Web (Google, ChatGPT, etc..).  

---------------------------------------------------
Séquence 4 : Créer la base de données sur votre serveur
---------------------------------------------------
Objectif : Créer la base de données SQLite sur votre serveur  
Difficulté : Faible (~10 minutes)
---------------------------------------------------
1° - Connectez vous en SSH à votre serveur Alwaysdata via l'adresse suivante :**https://ssh-{compte}.alwaysdata.net**. Remarque importante, {compte} est à remplacer par votre compte Alwaysdata. C'est à dire le compte que vous avez utilisé pour renseigner votre secret GitHUB USERNAME.   
2° - Une fois connecté, depuis de la console SSH, executez la commande suivante : **cd www/flask** puis **python3 create_db.py**  
Votre base de données est à présent opérationnelle sur votre serveur (Le fichier **database.db** à été créé dans votre répertoire sur le serveur)
Vous pouvez, si vous le souhaitez, tappez la commande **ls** dans votre console pour voir la présence de la base de données.

LES ROUTES (API)
-------------------------------------------
Bravo ! Votre solution est à présent opérationnelle sur votre site Web. Vous pouvez testez vos routes (API) comme suit :  
  
https://{Votre_URL}**/**  
Pointe sur le fichier helloWorld d'accueil  

https://{Votre_URL}**/lecture**  
L'accès est conditionné à un contrôle d'accès  

https://{Votre_URL}**/authentification**  
Page d'authentification (Login = **admin**, Mot de passe = **password**)  

https://{Votre_URL}**/fiche_client/1**  
Permet de faire un filtre sur un client. Vous pouvez changer la valeur de 1 par le N° du client de votre choix  

https://{Votre_URL}**/consultation/**  
Permet de consulter tous les clients de la base de données  

https://{Votre_URL}**/enregistrer_client**  
API pour enregistrer un nouveau client  

---------------------------------------------------
Séquence 5 : Exercices d'appropriation de la solution Web
---------------------------------------------------
Objectif : Travailler sur le code  
Difficulté : Moyenne (~60 minutes)
---------------------------------------------------
**Exercice 1 : Création d'une nouvelle fonctionnalité (1 point)**    
Créez une nouvelle route dans votre application afin de faire une recherche sur la base du nom d'un client (Même fonctionnement que sur le N° du client).  
Cette fonctionnalité sera accéssible via la route suivante : **/fiche_nom/**  

**Exercice 2 : Protection (2 points)**  
Cette nouvelle route "/fiche_nom/" est soumise à un contrôle d'accès User. C'est à dire différent des login et mot de passe administrateur.  
Pour accéder à cette fonctionnalité, l'utilisateur sera authentifié sous les login et mot de passe suivant : **user/12345**
  
---------------------------------------------------
Séquence 6 : MSPR CLOE855
---------------------------------------------------
Objectif : Sécurisation de votre infrastructure  
Difficulté : Moyenne (~10 heures)
---------------------------------------------------
Problème : Les administrateurs système de l'entreprise CLO855 ont constaté des tentatives d'accès non autorisées à leurs serveurs d'application via des clés SSH compromises. De plus, ils sont préoccupés par la qualité et la sécurité du code et des scripts utilisés dans le cadre de ce projet.  
  
Besoin : L'entreprise CLOE855 recherche donc des solutions pour sécuriser son infrastructure virtuelle, ses clés SSH et le code de son application.  
  
Les solutions techniques demandées dans le cadre de cette MSPR sont les suivantes :  
**1. - Sécurisation de votre Infrastructure Web :**    
. 1.1 - La base de données database.db de votre serveur doit être sauvegarder automatiquement sur un serveur tiers (3 points).   
. 1.2 - Mettre en place un contrôle d'accès (traçabilité) pour suivre le trafic des connections (1 point).  
. 1.3 - Mettre en place une détection des menaces pour surveiller les activités suspectes (1 point).  
**2.	Sécurisation des Clés SSH :**  
 . 2.1 -	Utilisation d'une solution de gestion des clés SSH centralisée pour stocker et gérer les clés SSH de manière sécurisée (2 points).  
 . 2.2 -	Mise en place d'une rotation régulière des clés SSH pour réduire les risques associés aux clés compromises (1 point).  
 . 2.3 -	Intégration de mécanismes d'authentification à plusieurs facteurs (MFA) pour renforcer la sécurité des connexions SSH (1 point).  
**3.	Sécurisation de votre code :**  
 . 3.1 -	Utilisation de services de contrôle de code source pour vérifier la qualité et la sécurité de votre code source (2 points).  
 . 3.2 -	Mise en place de pipelines CI/CD pour automatiser les tests de vos API (2 points).  
 
---------------------------------------------------
Séquence 6 : RAPPORT DE MSPR (4 points)
---------------------------------------------------
Objectif : Produire un rapport pour détailler le fonctionnement de votre solution  
Difficulté : Moyenne (~2 heures)
---------------------------------------------------
Votre MSPR fera l'objet d'un rapport venant accompagner et compléter les travaux techniques que vous avez pu réalisé dans le cadre de votre projet. 
Complétez directement ce Readme pour nous expliquer comment avez sécuriser votre infrastructure.  

**Expliquez nous dans cette section comment fonctionne la sécurisation de votre infrastructure :**  
   - La sauvegarde automatique de la base de données (`database.db`) est effectuée périodiquement sur un serveur distant Alwaysdata.
     
   - Le script établit une connexion sécurisée SSH avec le serveur Alwaysdata.
     
   - Il crée une sauvegarde de la base de données au format SQL (`sauvegarde.sql`) et la transfère sur le serveur distant.

**Expliquez nous dans cette section comment avez vous sécuriser vos clés SSH :**  
   - Le script utilise des clés SSH pour sécuriser les connexions au serveur Alwaysdata.
     
   - Il configure les clés SSH et établit une connexion sécurisée avec le serveur.
     
   - Les clés SSH sont stockées de manière sécurisée dans les secrets GitHub pour éviter toute compromission.

**Expliquez nous dans cette section comment avez vous sécuriser votre code :**  
   - Le code du script est sécurisé en utilisant des pratiques de développement sécurisé.
     
   - Les secrets sensibles, tels que les clés SSH, sont stockés de manière sécurisée dans les secrets GitHub.
     
   - Les fichiers temporaires utilisés pour le transfert de données sont supprimés après leur utilisation pour éviter les fuites potentielles.


--------------------------------------------------------------------
Troubleshooting :
---------------------------------------------------
Objectif : Visualiser ses logs et découvrir ses erreurs
---------------------------------------------------
Lors de vos développements, vous serez peut-être confronté à des erreurs systèmes car vous avez faits des erreurs de syntaxes dans votre code, faits de mauvaises déclarations de fonctions, appelez des modules inexistants, mal renseigner vos secrets, etc…  
Les causes d'erreurs sont quasi illimitées. **Vous devez donc vous tourner vers les logs de votre système pour comprendre d'où vient le problème** :  
Voici une vidéo pour accéder aux logs de vos Actions GitHUB : [Vidéo Log GitHUB](https://youtu.be/rhGrDLSFH7Y)  
Voici une vidéo pour vous expliquer comment accéder au logs de votre serveur Alwaysdata : [Vidéo Log Alwaysdata](https://youtu.be/URWMWqVMS2U)  
  
