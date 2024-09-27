from flask import Flask
from livereload import Server

app = Flask(__name__)
@app.route('/')
def main_screen():
    return '''
        <html>
            <head>
                <title>Leadership Board</title>
            </head>
            <body>
                <h1>Hello, World!</h1>
                <p>Welcome to my Flask app!</p>
            </body>
        </html>
    '''

if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.watch('templates/')
    server.watch('static/')
    server.serve(port=5000, debug=True)