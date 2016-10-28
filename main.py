#!/usr/bin/env python3
try:
    import alchemy
    import alchemy.config
    import alchemy.template
    import modules
    import posix
except ImportError as e:
    import sys
    import traceback
    print("Did you remember to run `pip install -r requirements.txt`?")
    traceback.print_exc(file=sys.stdout)
    raise SystemExit

config = alchemy.config.get_config()

if posix.getuid() == 0:
    su = True
else:
    print(" * No sudo permissions")
    su = False

# does not actually add a filter?
#def idsafe(input):
#    return input.lower().replace(" ", "_")
#app.jinja_env.filters['idsafe'] = idsafe

alchemy.alchemy_server.construct()
_acceptable_settings = ('host', 'port')
alchemy.alchemy_server.serve(**dict((key, value)
                                    for key, value in config.items()
                                    if key in _acceptable_settings))
