from flask import Flask, render_template, jsonify, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)                                                                                                                  
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # Clé secrète pour les sessions

# Fonction pour créer une clé "authentifie" dans la session utilisateur
def est_authentifie():
    return session.get('authentifie')

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/lecture')
def lecture():
    if not est_authentifie():
        # Rediriger vers la page d'authentification si l'utilisateur n'est pas authentifié
        return redirect(url_for('authentification'))

    # Si l'utilisateur est authentifié
    return "<h2>Bravo, vous êtes authentifié</h2>"

@app.route('/authentification', methods=['GET', 'POST'])
def authentification():
    if request.method == 'POST':
        # Vérifier les identifiants
        if request.form['username'] == 'user' and request.form['password'] == '12345':  # Changement des identifiants
            session['authentifie'] = True
            # Rediriger vers la route lecture après une authentification réussie
            return redirect(url_for('lecture'))
        else:
            # Afficher un message d'erreur si les identifiants sont incorrects
            return render_template('formulaire_authentification.html', error=True)

    return render_template('formulaire_authentification.html', error=False)

@app.route('/fiche_client/<int:post_id>')
def Readfiche(post_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients WHERE id = ?', (post_id,))
    data = cursor.fetchall()
    conn.close()
    # Rendre le template HTML et transmettre les données
    return render_template('read_data.html', data=data)

@app.route('/consultation/')
def ReadBDD():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients;')
    data = cursor.fetchall()
    conn.close()
    return render_template('read_data.html', data=data)

@app.route('/enregistrer_client', methods=['GET'])
def formulaire_client():
    return render_template('formulaire.html')  # afficher le formulaire

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
    return redirect('/consultation/')  # Rediriger vers la page d'accueil après l'enregistrement

# Contrôle d'accès utilisateur
def check_user_auth(username, password):
    return username == 'user' and password == '12345'

# Fonction pour demander l'authentification
def authenticate():
    return jsonify({"message": "Authentification requise"}), 401

# Décorateur pour le contrôle d'accès utilisateur
def requires_user_auth(f):
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_user_auth(auth.username, auth.password):
            return authenticate()  # Redirection vers la page d'authentification si les identifiants sont incorrects
        return f(*args, **kwargs)
    return decorated

# Route pour consulter les fiches clients
@app.route('/fiche_nom/<nom>')
@requires_user_auth  # Contrôle d'accès utilisateur requis
def fiche_nom(nom):
    nom = nom.capitalize()  # Assurez-vous que le nom est en majuscule
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients WHERE nom = ?', (nom,))
    client = cursor.fetchone()
    conn.close()

    if client:
        return jsonify({
            "id": client[0],
            "nom": client[1],
            "prenom": client[2],
            "adresse": client[3]
        })
    else:
        return jsonify({"error": "Client non trouvé"}), 404

if __name__ == "__main__":
    app.run(debug=True)
