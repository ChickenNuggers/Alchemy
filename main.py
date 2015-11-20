#!/usr/bin/env python3
try:
    import flask
    import json
    import os
except ImportError:
    print("Did you remember to run `pip install -r requirements.txt`?")
    raise SystemExit

app = flask.Flask(__name__)

import modules
for module in os.listdir('modules'):
    if module[0] != "." and module[0] != "_":
        __import__('modules.' + module[:-3])
enabled_modules = [getattr(modules, module) for module in dir(modules) if module[:2] != "__" and getattr(getattr(modules, module), "render")]

@app.route("/")
def master():
    elements = {
        "settings": {
            "title": "Alchemy"
        },
        "module_data": {}
    }
    return flask.render_template("index.html", **elements)

if __name__ == "__main__":
    with open("config.json") as config:
        app.run(**json.loads(config.read()))
