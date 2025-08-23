from flask import Flask

app = Flask(__name__)

@app.route('/')
def social_links():
    return '''
        <h2>Follow us on:</h2>
        <ul>
            <li><a href="https://www.facebook.com" target="_blank">Facebook</a></li>
            <li><a href="https://www.twitter.com" target="_blank">Twitter</a></li>
            <li><a href="https://www.instagram.com" target="_blank">Instagram</a></li>
            <li><a href="https://www.linkedin.com" target="_blank">LinkedIn</a></li>
            <li><a href="https://www.youtube.com" target="_blank">YouTube</a></li>
        </ul>
        
    '''

if __name__ == '__main__':
    app.run(debug=True)
    