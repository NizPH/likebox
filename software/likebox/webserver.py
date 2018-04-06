#!/usr/bin/env python3

import asyncio
import datetime
import random
from aiohttp import web
import os
from collections import defaultdict


class LikesServer:
  httpd_port = 8080
  websocket_port = 8000
  PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__)) + '/..'

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


if __name__ == "__main__":
    server = LikesServer()
    server.start()
