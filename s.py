from flask import Flask, render_template
from flask_socketio import SocketIO
import random
async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


# 使用json数据
@socketio.on('json')
def handle_json(json):
    print('received json:' + str(json))


#handle the default namespace


@socketio.on('my_event')
def get_message(message):
    print(message['data'])
    while True:
        socketio.sleep(15)
        t = random_int_list(1, 100, 10)
        socketio.emit('server_response', t)


def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop),
                                                                 int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list


if __name__ == '__main__':
    socketio.run(app, debug=True, port=3300)
