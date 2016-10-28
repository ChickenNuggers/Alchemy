import json
import sys
import posix


def get_config():
    config = {}
    with open("config.json") as conffile:
        config = json.loads(conffile.read())

    for item in (item for item in sys.argv if len(item) > 0 and item[0] == "-"):
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
    return config
