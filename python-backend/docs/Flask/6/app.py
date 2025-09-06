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
def prime(number):
    primes = ""  # String to hold prime numbers
    
    # Loop through all numbers from 2 to 'number'
    for i in range(2, number + 1):
        # Check if 'i' is prime
        for n in range(2, (i // 2) + 1):
            if i % n == 0:   # If divisible, not a prime
                break
        else:
            # If no divisor found, it is prime → add to result string
            primes += str(i) + ", "
    
    # Return all prime numbers as a string
    return primes

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
