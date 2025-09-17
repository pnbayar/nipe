from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')   

@app.route('/about')
def about():
    return render_template('about.html')   

@app.route('/social')
def social():
    return render_template('social.html')   


if __name__ == '__main__':
    app.run(debug=True, port=5001)
