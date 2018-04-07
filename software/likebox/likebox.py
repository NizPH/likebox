#!/usr/bin/env python3

from webserver import LikesServer
from threading import Thread
from gpiointerface import GPIOInterface
import asyncio


class LikesBox:
  def __init__(self):
    self.loop = asyncio.get_event_loop()

    self.webserver = LikesServer(self.loop)
    httpd_thread = Thread(target = self.webserver.start_web_server)
    httpd_thread.start()

#    self.webserver.start_websocket()
    
    gpio = GPIOInterface(self.loop)

  def start(self):
    self.loop.run_forever()
    self.loop.close()

if __name__ == "__main__":
    likesBox = LikesBox();
    likesBox.start()
    likesBox.webserver.join()
