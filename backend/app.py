import os
import psycopg
from flask import Flask, jsonify, request

app = Flask(__name__)

def get_conn():
    # Connection settings come from environment variables, never from the code
    return psycopg.connect(
        host=os.environ["DB_HOST"],
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
    )

@app.get("/api/health")
def health():
    return {"status": "ok"}

@app.get("/api/products")
def list_products():
    with get_conn() as conn:
        rows = conn.execute("SELECT id, name, price FROM products ORDER BY id").fetchall()
    return jsonify([{"id": r[0], "name": r[1], "price": float(r[2])} for r in rows])

@app.post("/api/products")
def add_product():
    data = request.get_json()
    with get_conn() as conn:  # the block commits the transaction when it ends
        row = conn.execute(
            "INSERT INTO products (name, price) VALUES (%s, %s) RETURNING id",
            (data["name"], data["price"]),
        ).fetchone()
    return {"id": row[0], "name": data["name"], "price": data["price"]}, 201

if __name__ == "__main__":
    # 0.0.0.0 = listen on all interfaces, so other containers can reach the API
    app.run(host="0.0.0.0", port=5000)
