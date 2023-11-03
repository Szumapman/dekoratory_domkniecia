from flask import Flask

app = Flask(__name__)

@app.route('/') # dekorator - przypisuje funkcję do adresu / (root)
def index():
    return '<h1>Index Page</h1>'

@app.route('/hello') # dekorator - przypisuje funkcję do adresu /hello
def hello():
    return '<h1>Hello, World</h1>'

# flask run command:
# flask --app flask_app run