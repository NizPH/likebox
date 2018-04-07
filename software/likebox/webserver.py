#!/usr/bin/env python3

from http.server import HTTPServer
from http.server import SimpleHTTPRequestHandler
import asyncio
import datetime
import random
import os
import websockets
from threading import Thread


class LikesServer:
  httpd_port = 8080
  websocket_port = 5678
  PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__)) + '/..'

  def __init__(self, event_loop):
    self.counter = 0

    os.chdir( "../html/" )
    handler = SimpleHTTPRequestHandler
    server_address = ('', LikesServer.httpd_port)
    self.httpd = HTTPServer(server_address, handler)

    self.websocket = websockets.serve(self.count, '0.0.0.0', LikesServer.websocket_port)
    event_loop.run_until_complete(self.websocket)
    print( "Started WebSocket server" )

  def start_web_server(self):
    print( "Starting Web HTTP server" )
    self.httpd.serve_forever()

  def start_websocket(self):
    print( "Starting WebSocket server" )
    asyncio.get_event_loop().run_until_complete(self.websocket)
    asyncio.get_event_loop().run_forever()

  async def count(self, websocket, path):
    while True:
      self.counter = self.counter + 1
      await websocket.send(str(self.counter))
      await asyncio.sleep(random.random() * 3 + 2)

"""
  def __init__(self):
#    self.counter = IOCounter.load_counter()
    self.counter = 0
    loop = asyncio.get_event_loop()
    self.app = web.Application(loop=loop)
    self.app['websockets'] = defaultdict(set)
    self.app.router.add_static('/', path=LikesServer.PROJECT_ROOT + '/html', name='html')
    self.app.router.add_route('POST', '/count', self.count_handler)

  async def count_handler(self, request):
    print( "Client connected" )

  async def add_plus_one(self):
    while True:
      self.counter = self.counter + 1
      await asyncio.sleep(random.random() * 5 + 5)

  async def update_count(self):
    while True:
      counter = await add_plus_one()
#      IOCounter.save_counter(counter)
      await websocket.send(counter)

  def start(self):
    web.run_app(self.app, host='127.0.0.1', port=LikesServer.httpd_port)
"""
