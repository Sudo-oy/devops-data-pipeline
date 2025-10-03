from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

@app.route("/")
def health():
    return jsonify({"status": "ok", "message": "DevOps pipeline demo running!"})

@app.route("/db")
def db_check():
    try:
        conn = psycopg2.connect(
            host="db",
            database="mydb",
            user="admin",
            password="admin"
        )
        cur = conn.cursor()
        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        cur.close()
        conn.close()
        return jsonify({"database": "connected", "version": db_version})
    except Exception as e:
        return jsonify({"database": "error", "details": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
