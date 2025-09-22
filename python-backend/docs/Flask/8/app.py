import mysql.connector
from flask import Flask, request, jsonify

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="flaskdb"
)
cursor = db.cursor()

@app.route('/users', methods=['GET'])
def get_users():
    cursor.execute("SELECT * FROM users")
    return jsonify(cursor.fetchall())

@app.route('/createuser', methods=['POST','GET'])
def add_users():
    if(request.method != 'POST'):
        return '''<form method="post">
        Username: <input type="text" name="name" required><br>
        Password: <input type="email" name="email" required><br>
        <input type="submit" value="Register">
        </form>'''
    else:
        name=request.form["name"]
        email=request.form["email"]
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        db.commit()
        return jsonify({"message": "User added successfully!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)