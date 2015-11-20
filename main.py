#!/usr/bin/env python3
try:
    import flask
    import json
    import os
    import re
    import collections
except ImportError:
    print("Did you remember to run `pip install -r requirements.txt`?")
    raise SystemExit

app = flask.Flask(__name__)
app.jinja_env.autoescape = False

import modules
_module_list = sorted([item[:-3] for item in os.listdir('modules') if item[0] != "." and item[0] != "_"])
for module in _module_list:
    if module[0] != "." and module[0] != "_":
        __import__('modules.' + module, globals(), locals())
enabled_modules = [getattr(modules, module) for module in _module_list if getattr(getattr(modules, module), "render")]

_module_pattern = re.compile(r'modules\.(.+)')

@app.route("/")
def master():
    elements = {
        "settings": {
            "title": "Alchemy"
        },
        "module_data": {}
    }
    for module in enabled_modules:
        elements['module_data'][_module_pattern.match(module.__name__).group(1).capitalize()] = module.render()
    return flask.render_template("index.html", **elements)

if __name__ == "__main__":
    with open("config.json") as config:
        app.run(**json.loads(config.read()))
