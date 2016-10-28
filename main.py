#!/usr/bin/env python3
try:
    import hurricane
    import hurricane.config
    import hurricane.template
    import modules
    import os
except ImportError as e:
    import sys
    import traceback
    print("Did you remember to run `pip install -r requirements.txt`?")
    traceback.print_exc(file=sys.stdout)
    raise SystemExit

config = hurricane.config.get_config()

if os.getuid() != 0:
    print(" * No sudo permissions")

# does not actually add a filter?
#def idsafe(input):
#    return input.lower().replace(" ", "_")
#app.jinja_env.filters['idsafe'] = idsafe

hurricane.hurricane_server.construct()
_acceptable_settings = ('host', 'port')
hurricane.hurricane_server.serve(**dict((key, value)
                                    for key, value in config.items()
                                    if key in _acceptable_settings))
