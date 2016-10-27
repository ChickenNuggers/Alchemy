from alchemy import app
import collections
import flask
import jinja2
import psutil

psutil.cpu_percent() # Initialize percent calculator

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

@app.route("/example")
def render_json_stats():
    return flask.jsonify(*_getnums())
