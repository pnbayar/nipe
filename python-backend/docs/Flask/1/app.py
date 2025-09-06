from flask import Flask

# Create Flask application
app = Flask(__name__)

# Define a route and view function
@app.route('/')
def hello():
    return "Hello, World!"

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
