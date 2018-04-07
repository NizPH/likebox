#!/usr/bin/env python3

import RPi.GPIO as GPIO


class GPIOInterface:
  channel = 10
  def __init__(self, event_loop):
    self.event_loop = event_loop
    # Setup GPIO interface
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(GPIOInterface.channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(GPIOInterface.channel, GPIO.RISING, callback=lambda x: self.button_pressed(self.message_manager_f), bouncetime=500)

  def button_pressed(self, manager):
    print( "The button has been pressed" )
    # this enqueues a call to message_manager_f() 
    self.event_loop.call_soon_threadsafe(manager)

  def message_manager_f(self):
    print( "Managing the pressed button" )
