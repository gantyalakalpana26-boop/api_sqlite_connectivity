
from flask import Flask, jsonify, request
from database import get_connection, create_table

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to Student Management API"})

@app.route("/students", methods=["GET"])
def get_students():
    conn = get_connection()
    students = conn.execute("SELECT * FROM students").fetchall()
    conn.close()
    return jsonify([dict(student) for student in students])

@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json(silent=True) or {}

    name = data.get("name")
    email = data.get("email")
    age = data.get("age")

    if not name or not email or age is None:
        return jsonify({"error": "Name, email and age are required"}), 400

    conn = get_connection()
    try:
        cursor = conn.execute(
            "INSERT INTO students (name, email, age) VALUES (?, ?, ?)",
            (name, email, age)
        )
        conn.commit()
        return jsonify({
            "message": "Student added successfully",
            "student_id": cursor.lastrowid
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        conn.close()

if __name__ == "__main__":
    create_table()
    app.run(host="127.0.0.1", port=5001, debug=False)
