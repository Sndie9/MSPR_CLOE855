from flask import Flask, render_template, jsonify, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # Clé secrète pour les sessions

# Fonction pour vérifier si l'utilisateur est authentifié en tant qu'administrateur
def est_authentifie():
    return session.get('authentifie')

# Fonction pour vérifier si l'utilisateur est authentifié en tant qu'utilisateur ordinaire
def est_authentifie_user():
    return session.get('authentifie_user')

# Route pour la page d'accueil
@app.route('/')
def hello_world():
    return render_template('hello.html')

# Route pour la page de lecture (accessible uniquement aux administrateurs)
@app.route('/lecture')
def lecture():
    if not est_authentifie():
        # Redirection vers la page d'authentification si l'utilisateur n'est pas authentifié
        return redirect(url_for('authentification'))

    # Si l'utilisateur est authentifié, affichage de la page de lecture
    return "<h2>Bravo, vous êtes authentifié</h2>"

# Route pour l'authentification (page de connexion)
@app.route('/authentification', methods=['GET', 'POST'])
def authentification():
    if request.method == 'POST':
        # Vérification des identifiants administrateur
        if request.form['username'] == 'admin' and request.form['password'] == 'password':
            session['authentifie'] = True
            # Redirection vers la page de lecture après une authentification réussie
            return redirect(url_for('lecture'))
        else:
            # Affichage d'un message d'erreur si les identifiants sont incorrects
            return render_template('formulaire_authentification.html', error=True)

    return render_template('formulaire_authentification.html', error=False)

# Route pour afficher les détails d'un client en fonction de son ID
@app.route('/fiche_client/<int:post_id>')
def Readfiche(post_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients WHERE id = ?', (post_id,))
    data = cursor.fetchall()
    conn.close()
    # Rendre le template HTML et transmettre les données
    return render_template('read_data.html', data=data)

# Route pour afficher tous les clients (accessible uniquement aux administrateurs)
@app.route('/consultation/')
def ReadBDD():
    if not est_authentifie():
        # Redirection vers la page d'authentification si l'utilisateur n'est pas authentifié
        return redirect(url_for('authentification'))

    # Connexion à la base de données pour récupérer tous les clients
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients;')
    data = cursor.fetchall()
    conn.close()
    # Rendre le template HTML et transmettre les données
    return render_template('read_data.html', data=data)

# Route pour afficher le formulaire d'ajout d'un nouveau client
@app.route('/enregistrer_client', methods=['GET'])
def formulaire_client():
    return render_template('formulaire.html')  # Afficher le formulaire

# Route pour enregistrer un nouveau client dans la base de données
@app.route('/enregistrer_client', methods=['POST'])
def enregistrer_client():
    nom = request.form['nom']
    prenom = request.form['prenom']

    # Connexion à la base de données
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Exécution de la requête SQL pour insérer un nouveau client
    cursor.execute('INSERT INTO clients (created, nom, prenom, adresse) VALUES (?, ?, ?, ?)', (1002938, nom, prenom, "ICI"))
    conn.commit()
    conn.close()
    return redirect('/consultation/')  # Redirection vers la page d'accueil après l'enregistrement

# Route pour afficher le formulaire d'authentification utilisateur
@app.route('/authentification_user', methods=['GET', 'POST'])
def authentification_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        nom = request.form['nom']  # Récupération du nom

        # Vérification des identifiants utilisateur
        if username == 'user' and password == '12345':
            session['authentifie_user'] = True
            # Redirection vers la page de fiche_nom avec le nom fourni
            return redirect(url_for('ReadFicheNom', nom=nom))
        else:
            return render_template('formulaire_authentification_user.html', error=True)

    return render_template('formulaire_authentification_user.html', error=False)

# Route pour afficher les détails d'un client en fonction de son nom (accessible aux utilisateurs authentifiés)
@app.route('/fiche_nom/<string:nom>')
def ReadFicheNom(nom):
    if not est_authentifie_user():
        return redirect(url_for('authentification_user'))

    nom = nom.upper()  # Convertir en majuscule pour la recherche
    # Connexion à la base de données pour récupérer les détails du client par nom
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients WHERE nom = ?', (nom,))
    data = cursor.fetchall()
    conn.close()
    # Si le client n'est pas trouvé, retourner une erreur 404
    if not data:
        return jsonify({"error": "Client not found"}), 404
    # Rendre le template HTML et transmettre les données
    return render_template('read_data.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)
