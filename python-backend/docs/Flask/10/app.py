from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure MySQL database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/flaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define ORM model
class User1(db.Model):
    __tablename__ = 'user1'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<User1 {self.name}>"

# Create tables and insert sample data (runs at startup)
with app.app_context():
    db.create_all()
    if not User1.query.first():  # insert only if empty
        user1 = User1(name="Alice", email="alice@example.com")
        user2 = User1(name="Bob", email="bob@example.com")
        user3 = User1(name="Charlie", email="charlie@example.com")
        db.session.add_all([user1, user2, user3])
        db.session.commit()

# Route to display all users
@app.route("/users")
def show_users():
    users = User1.query.all()
    return render_template("users.html", users=users)

if __name__ == "__main__":
    app.run(debug=True)
