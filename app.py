from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET KEY'] = 'secretkey'
app.config['DEBUG'] = True

# instantiate socket.io
socketio = SocketIO(app)

# routing
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    socketio.run(app)