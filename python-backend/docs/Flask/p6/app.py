from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Route for the home page
@app.route("/")
def home():
    # Message asking user to enter a number in the URL
    return "Please add a number to the URL, like /5 or /10"

# Route that accepts an integer from the URL
@app.route("/<int:number>")
def factorial(number):
    # Calculate factorial
    fact = 1
    for i in range(1, number + 1):
        fact *= i

    # Return the factorial result as a string
    return f"Factorial of {number} is: {fact}"

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
