#!/usr/bin/env python3
try:
    import flask
    import json
    import os
    import re
    import posix
    import sys
except ImportError:
    print("Did you remember to run `pip install -r requirements.txt`?")
    raise SystemExit

with open("config.json") as conffile:
    config = json.loads(conffile.read())

for item in [item for item in sys.argv if item[0] == "-"]:
    if "=" in item:
        groups = re.match('^(.+)=(.+)$', item[1:]).groups()
        try:
            config[groups[0]] = int(groups[1])
        except:
            config[groups[0]] = groups[1]
    else:
        config[item[1:]] = True

if posix.getuid() != 0 and config.get('escalate'):
    posix.execv('/usr/bin/sudo', ['/usr/bin/sudo', '/usr/bin/env', 'python', sys.argv[0]])

if posix.getuid() == 0:
    su = True
else:
    print(" * No sudo permissions")
    su = False

app = flask.Flask(__name__)
app.jinja_env.autoescape = False

import modules
_module_list = sorted([item[:-3] for item in os.listdir('modules') if item[0] != "." and item[0] != "_"])
for module in _module_list:
    if module[0] != "." and module[0] != "_":
        __import__('modules.' + module, globals(), locals())
enabled_modules = [getattr(modules, module) for module in _module_list if getattr(getattr(modules, module), "render")]

_module_pattern = re.compile(r'modules\.(.+)')

if 'whitelist' in config.keys():
    _whitelist = []
    for ip in config['whitelist']:
        _whitelist.append(re.compile(re.escape(ip)))
    @app.before_request
    def whitelist():
        is_allowed = False
        for pattern in _whitelist:
            if pattern.match(flask.request.remote_addr):
                is_allowed = True
        if not is_allowed:
            print('Unallowed user: ' + flask.request.remote_addr)
            flask.abort(403)

@app.errorhandler(403)
def access_error(e):
    try:
        return flask.render_template('error.html', error = 403, message = 'Access denied', reason = 'Non-whitelisted IP address'), 403
    except Exception as e:
        print(e)

@app.route("/")
def master():
    elements = {
        "settings": {
            "title": "Alchemy"
        },
        "su": su,
        "nowarn": config.get('nowarn') or False,
        "module_data": {}
    }
    for module in enabled_modules:
        elements['module_data'][_module_pattern.match(module.__name__).group(1).capitalize()] = module.render()
    return flask.render_template("index.html", **elements)

_acceptable_settings = ['host', 'port', 'use_reloader']

if __name__ == "__main__":
    werkzeug_settings = [(key, value) for key, value in config.items() if key in _acceptable_settings]
    app.run(**dict(werkzeug_settings), debug=True)
