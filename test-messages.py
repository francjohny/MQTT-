#!/usr/bin/python3
# 
# test-messages.py - This script publish a random MQTT messages every 2 s.
#

import random
import time
import paho.mqtt.client as mqtt

timestamp = int(time.time())

broker = '127.0.0.1'
port = 1884
element = 'hello/world'
states = ['true', 'false']

print('Messages are published on topic %s/#... -> CTRL + C to shutdown' \
    % element)

while True:
    mqttclient = mqtt.Client("localhost", 1884, "mqtt", "mqtt_panel")
    mqttclient.connect("ws://localhost:1884/mqtt")
    mqttclient.subscribe("hello/world")
    time.sleep(2)

