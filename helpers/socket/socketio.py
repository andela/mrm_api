from flask import request
from threading import Lock
from flask_socketio import Namespace, emit, disconnect

thread = None
thread_lock = Lock()


class Namespaceio(Namespace):
    """
    Any event received by the server are dispatched to the
    method named as the event with the 'on_' prefix

    :method on_connect: establish connection between server & client
    :method  on_my_event: handles events
    :method on_disconnect_request: disconnect the connection
    """

    def __init__(self, namespace=None, background_thread=None, socketio=None):
        super(Namespaceio, self).__init__(namespace)
        self.background_thread = background_thread
        self.socketio = socketio

    def on_connect(self):
        global thread
        with thread_lock:
            if thread is None:
                thread = self.socketio.start_background_task(
                    self.background_thread)
        emit('my_response', {'data': 'Connected'})

    def on_my_event(self, message):
        emit('my_response', {'data': message['data']})

    def on_disconnect_request(self):
        emit('my_response', {'data': 'Disconnected!'})
        disconnect()

    def on_disconnect(self):
        print('Client disconnected', request.sid)
