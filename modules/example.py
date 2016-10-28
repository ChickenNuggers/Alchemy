import hurricane
import collections
import jinja2
import json
import psutil
from tornado.gen import sleep, coroutine
from tornado.websocket import WebSocketHandler

psutil.cpu_percent()  # Initialize percent calculator


def _getnums():
    numbers = []
    numbers.append({
        'label': 'CPU Usage',
        'label_safe': 'ex_cpu_usage',
        'value': psutil.cpu_percent(interval=1)
    })
    numbers.append({
        'label': 'Memory',
        'label_safe': 'ex_memory',
        'value': psutil.virtual_memory().percent
    })

    return numbers


def render():
    numbers = _getnums()
    with open('templates/example.html') as template:
        return jinja2.Template(template.read()).render(data=numbers)


def render_actions():
    with open('templates/example-actions.html') as template:
        return jinja2.Template(template.read()).render()

class ExampleWebsocket(WebSocketHandler):
    @coroutine
    def open(self):
        while True:
            self.write_message(json.dumps(_getnums()))
            yield sleep(5)

    def on_message(self, message):
        pass

    def on_close(self):
        pass

def init():
    hurricane.hurricane_server.add_websocket_handler("/example", ExampleWebsocket)
