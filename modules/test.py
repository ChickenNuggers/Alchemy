import Alchemy
import flask
import psutil

psutil.cpu_percent() # Initializer

def getnums():
    items = []
    items.append(('CPU Usage', psutil.cpu_percent(interval=1)))
    items.append(('Memory', psutil.virtual_memory().percent))

    return dict(items)

def render():
    numbers = getnums()
    template = flask.render_template('test.html', **numbers)

