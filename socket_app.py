from flask import Flask
from flask_socketio import SocketIO, send, join_room, emit
import eventlet
eventlet.monkey_patch()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(
    app=app,
    message_queue='redis://127.0.0.1:6379/0',
    channel='the_best_channel_in_the_world'
)


@socketio.on('connect')
def on_connect():
    room_id = 777
    print('SERVER 5001>>> A user has been connected.')
    join_room(room_id)
    send('SERVER 5001>>> User has joined the room: ' + str(room_id) + '.', room=room_id)
    print('SERVER 5001>>> User has joined the room ' + str(room_id) + '.')
    socketio.emit('my_event', 'data_string1')
    emit('my_event', 'data_string2')


@socketio.on('message')
def handle_message(message):
    print('SERVER 5001>>> received message: ' + message)
    send(message, room=777)


if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=5001)
