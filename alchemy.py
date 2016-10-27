#!/usr/bin/env python3
from tornado.wsgi import WSGIContainer
from tornado.web import Application, FallbackHandler
from tornado.websocket import WebSocketHandler
from tornado.ioloop import IOLoop
from flask import Flask

class AlchemyServer:

    def __init__(self, websockets=[], pages=[]):
        self._websockets = websockets
        self.app = Flask(__name__)

    def add_websocket(self, websocket_url, websocket_class):
        self._websockets.append((websocket_url, websocket_class))

    def construct(self):
        container = WSGIContainer(self.app)
        self._server = Application(self._websockets.append((r'.*',
            FallbackHandler, dict(fallback=container)))) #lisp, anyone?

    def serve(self, host, port):
        self._server.listen(port, host)
        IOLoop.instance().start()

alchemy_server = AlchemyServer()
app = alchemy_server.app
