from flask import Flask
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(
    message_queue='redis://127.0.0.1:6379/0',
    channel='the_best_channel_in_the_world'
)


@app.route('/')
def hello_world():
    #send('SERVER 5000>>> message from server 5000', broadcast=True)
    try:
        emit('my_event', 'fwggqwwgqgwqgwgwqgwq')
    except Exception:
        print('First error')
    try:
        socketio.emit('my_event', 'fwggqwwgqgwqgwgwqgwq')
        socketio.send('my_event', 'fwggqwwgqgwqgwgwqgwq')
    except Exception:
        print('Second error')

    return "Hello, world!"


@socketio.on('message')
def handle_message(message):
    print('SERVER 5000>>> received message: ' + message)
    send(message, broadcast=True)


if __name__ == '__main__':
    app.run()
