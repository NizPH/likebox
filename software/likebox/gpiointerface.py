#!/usr/bin/env python3

import RPi.GPIO as GPIO


class GPIOInterface:
  def __init__(self):
    # Setup GPIO interface
    GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(channel, GPIO.RISING, callback=my_callback)
