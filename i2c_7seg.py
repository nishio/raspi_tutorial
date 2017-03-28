#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
sample code to use HT16K33 Adafruit 7-segments LED
"""

import smbus
from time import sleep

# address of I2C client (use i2cdetect to find)
addr = 0x70

# ON/OFF data for character 0~9
numeric_data = [
    0x3F, 0x06, 0x5B, 0x4F, 0x66,
    0x6D, 0x7D, 0x07, 0x7F, 0x6F,
]


def initialize():
    global bus
    data = [0x21, 0x81, 0xEF]
    wait = [10, 10, 10]  # milliseconds

    bus = smbus.SMBus(1)
    for d, w in zip(data, wait):
        print 'write', hex(d), 'wait', w, 'ms'
        bus.write_byte(addr, d)
        sleep(w / 1000.0)
    sleep(0.1)


def draw(v1, v2, v3, v4):
    buf = [0] * 16
    buf[0] = numeric_data[v1]
    buf[2] = numeric_data[v2]
    buf[6] = numeric_data[v3]
    buf[8] = numeric_data[v4]

    for i, v in enumerate(buf):
        bus.write_byte_data(addr, i, v)


def sample():
    count = 9999
    while count:
        draw(
            count / 1000,
            count / 100 % 10,
            count / 10 % 10,
            count % 10
        )
        count -= 1
        sleep(0.01)


if __name__ == "__main__":
    initialize()
    sample()
