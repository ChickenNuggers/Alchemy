#!/usr/bin/env python3
import hurricane.config
import collections
import jinja2
import modules
import re
import os
from tornado.wsgi import WSGIContainer
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop

_config = hurricane.config.get_config()


class HurricaneServer:

    def __init__(self, websockets=[], request_handlers=[]):
        self._request_handlers = request_handlers
        self._websockets = websockets

    def add_request_handler(self, requst_url, request_class):
        self._request_handlers.append((requst_url, request_class))

    def add_websocket_handler(self, websocket_url, websocket_class):
        self._websockets.append((websocket_url, websocket_class))

    def construct(self):
        settings = {
            'static_path':
            os.path.join(os.path.dirname(__file__), "..", "static")
        }
        self._server = Application(self._websockets + self._request_handlers,
                                   **settings)

    def serve(self, host, port):
        self._server.listen(port, host)
        IOLoop.instance().start()


_whitelist = None
if 'whitelist' in _config.keys():
    _whitelist = [re.compile(re.escape(ip)) for ip in _config['whitelist']]


class HurricaneMainPage(RequestHandler):
    _module_pattern = re.compile(r'modules\.(.+)')

    def get(self):
        is_allowed = False
        if 'whitelist' in _config.keys():
            for pattern in _whitelist:
                if pattern.match(self.request.remote_ip):
                    is_allowed = True
            if not is_allowed:
                print('Unallowed user: ' + self.request.remote_ip)
                self.clear()
                self.set_status(403)
                with open('templates/error.html') as template:
                    self.write(
                        jinja2.Template(template.read()).render(
                            error=403,
                            message='Access denied',
                            reason='Non-whitelisted IP address'))
        elements = {
            "settings": {
                "title": "Hurricane"
            },
            "su": os.getuid() == 0,
            "nowarn": _config.get('nowarn') or False,
            "module_data": collections.OrderedDict()
        }
        for module in modules.enabled_modules:
            name = self._module_pattern.match(module.__name__).group(
                1).capitalize()
            elements['module_data'][name] = {'main': module.render()}
            if hasattr(module, "render_actions"):
                elements['module_data'][name]['has_actions'] = True
                elements['module_data'][name][
                    'actions'] = module.render_actions()
        with open('templates/index.html') as template:
            self.write(jinja2.Template(template.read()).render(**elements))


hurricane_server = HurricaneServer()
hurricane_server.add_request_handler(r"/", HurricaneMainPage)
hurricane_server.add_request_handler(r"/index", HurricaneMainPage)

for module in modules.enabled_modules:
    if hasattr(module, 'init'):
        module.init()
