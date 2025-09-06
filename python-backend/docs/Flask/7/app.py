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
def fibonacci(number):
    # String to hold Fibonacci numbers
    fibs = "First " + str(number) + " Fibonacci numbers: "

    # Initialize first two Fibonacci numbers
    fib1, fib2 = 0, 1

    # Generate Fibonacci sequence
    for i in range(number):
        fibs += str(fib1) + ", "
        fib1, fib2 = fib2, fib1 + fib2

    # Return the Fibonacci sequence as a string
    return fibs

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
