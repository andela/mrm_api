def req_thread(socketio, status):
    """
    Send server generated events to the client
    """
    count = 4

    while status and count > 0:
        count -= 1
        if count == 0:
            socketio.emit('my_response', events(count), namespace='/io')
        else:
            socketio.emit('my_response', events(count), namespace='/io')
            socketio.sleep(9)


def events(val):
        return {
                3: {'data': 'processing request'},
                2: {'data': 'data analysis'},
                1: {'data': 'almost done'},
                0: {'data': 'done'}
        }[val]
