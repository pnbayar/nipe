from flask import Flask
app = Flask(__name__)

@app.route('/<name>')
def hello_name(name):
   msg = '<h1>Hello %s!</h1>' % name
   msg += '<p>Welcome to Flask!</p>'
   msg += '<p>Enjoy your stay.</p>'
   msg += '<p>Have a great day!</p>'
   msg += '<p>Goodbye!</p>'
   msg += '<p>See you soon!</p>'
   msg += '<p>Take care!</p>'
   return msg

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000, debug=True)