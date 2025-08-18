from flask import Flask,redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello From Praveen'

@app.route('/nipe')
def hello_nipe():
    return redirect("https://nitte.edu.in/nipe")

# main driver function
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)