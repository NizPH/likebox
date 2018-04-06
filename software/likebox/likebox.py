#!/usr/bin/env python3

from webserver import LikesServer

class LikesBox:
  def __init__(self):
    self.webserver = WebServer()

    server = LikesServer()
    httpd_thread = Thread(target = server.start_web_server)
    httpd_thread.start()

    server.start_websocket()
    
    print( "Websocket server closed" )

    httpd_thread.join()
    print( "Web HTTP server closed" )

if __name__ == "__main__":
    likesBox = LikesBox();
