from flask import render_template
from flask import Flask
app = Flask(__name__)
from datetime import datetime

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )
if __name__ == '__main__':
   app.run()