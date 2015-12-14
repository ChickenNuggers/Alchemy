import jinja2
import psutil

psutil.cpu_percent() # Initialize percent calculator

def _getsockets(protocol='inet'):
    return [ socket for socket in psutil.net_connections(protocol) ]

def _getlistening(protocol='inet'):
    return [ socket for socket in _getsockets(protocol) if socket.status == psutil.CONN_LISTEN ]

def _getnotlistening(protocol='inet'):
    return [ socket for socket in _getsockets(protocol) if socket.status != psutil.CONN_LISTEN and socket.status != psutil.CONN_NONE ]

def render():
    with open('templates/network.html') as template:
        return jinja2.Template(template.read()).render(sockets=_getnotlistening(), listening = _getlistening())
