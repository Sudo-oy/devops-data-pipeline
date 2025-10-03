from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

# Charger les informations de connexion depuis les variables d'environnement
DB_HOST = os.environ.get("DB_HOST", "db_placeholder")
DB_NAME = os.environ.get("DB_NAME", "mydb_placeholder")
DB_USER = os.environ.get("DB_USER", "user_placeholder")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "password_placeholder")

@app.route("/")
def health():
    return jsonify({"status": "ok", "message": "DevOps pipeline demo running!"})

@app.route("/db")
def db_check():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            connect_timeout=5 # Ajout d'un timeout pour éviter les blocages
        )
        cur = conn.cursor()
        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        cur.close()
        conn.close()
        return jsonify({"database": "connected", "version": db_version[0]})
    except Exception as e:
        # Afficher le nom d'hôte pour le debug
        error_msg = f"Failed to connect to DB at {DB_HOST}. Details: {str(e)}"
        return jsonify({"database": "error", "details": error_msg})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
