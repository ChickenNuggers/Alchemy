#!/usr/bin/env python3
try:
    import flask
    import json
    import os
    import re
    import posix
    import sys
    import collections
except ImportError:
    print("Did you remember to run `pip install -r requirements.txt`?")
    raise SystemExit

with open("config.json") as conffile:
    config = json.loads(conffile.read())

for item in (item for item in sys.argv if item[0] == "-"):
    if "=" in item:
        groups = re.match('^(.+)=(.+)$', item[1:]).groups()
        try:
            config[groups[0]] = int(groups[1])
        except:
            config[groups[0]] = groups[1]
    else:
        config[item[1:]] = True

if posix.getuid() != 0 and config.get('escalate'):
    posix.execv('/usr/bin/sudo',
                ['/usr/bin/sudo', '/usr/bin/env', 'python', sys.argv[0]])

if posix.getuid() == 0:
    su = True
else:
    print(" * No sudo permissions")
    su = False

app = flask.Flask(__name__)
app.jinja_env.autoescape = False

import modules
_module_list = sorted(
    [item[:-3] for item in os.listdir('modules') if item[-3:] == ".py"])
# use .py.disabled to disable a module
for module in _module_list:
    if module[0] != "." and module[0] != "_":
        __import__('modules.' + module, globals(), locals())
enabled_modules = [
    getattr(modules, module) for module in _module_list
    if hasattr(getattr(modules, module), "render")
]

for module in enabled_modules:
    if hasattr(module, "init"):
        module.init(app)

if 'whitelist' in config.keys():
    _whitelist = []
    for ip in config['whitelist']:
        _whitelist.append(re.compile(re.escape(ip)))


@app.errorhandler(403)
def access_error(e):
    try:
        return flask.render_template(
            'error.html',
            error=403,
            message='Access denied',
            reason='Non-whitelisted IP address'), 403
    except Exception as e:
        print(e)

_module_pattern = re.compile(r'modules\.(.+)')

@app.route("/")
def master():
    is_allowed = False
    for pattern in _whitelist:
        if pattern.match(flask.request.remote_addr):
            is_allowed = True
    if not is_allowed:
        print('Unallowed user: ' + flask.request.remote_addr)
        flask.abort(403)
    elements = {
        "settings": {
            "title": "Alchemy"
        },
        "su": su,
        "nowarn": config.get('nowarn') or False,
        "module_data": collections.OrderedDict()
    }
    for module in enabled_modules:
        name = _module_pattern.match(module.__name__).group(1).capitalize()
        elements['module_data'][name] = {'main': module.render()}
        if hasattr(module, "render_actions"):
            elements['module_data'][name]['has_actions'] = True
            elements['module_data'][name]['actions'] = module.render_actions()
            print(module.render_actions())
    return flask.render_template("index.html", **elements)


_acceptable_settings = ('host', 'port', 'use_reloader')

if __name__ == "__main__":
    werkzeug_settings = [(key, value) for key, value in config.items()
                         if key in _acceptable_settings]
    app.run(**dict(werkzeug_settings))
