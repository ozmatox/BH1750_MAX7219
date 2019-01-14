#!/usr/bin/env python
# >>>>ozmatox<<<<

import smbus
import re
import time
import argparse
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT


serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=-90, rotate=0)
device2 = 0x23
ONE_TIME_HIGH_RES_MODE_1 = 0x20
bus = smbus.SMBus(1)

def convertToNumber(data):
  result=(data[1] + (256 * data[0])) / 1.2
  return (result)

def readLight(addr=device2):
  data = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE_1)
  return convertToNumber(data)

def main():
  while True:
    lightLevel=readLight()
    msg=("Poziom " + format(lightLevel,'.2f') + " lx")
    print("Light Level : " + format(lightLevel,'.2f') + " lx")
    show_message(device, msg, fill="white", font=proportional(LCD_FONT))
    time.sleep(5)

if __name__=="__main__":
   main()
