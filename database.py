import paho.mqtt.client as mqtt
from PIL import Image, ImageDraw, ImageFont


def on_connect(client, userdata, flags, rc):
    print("Connected with result code {0}".format(rc))
    client.subscribe("rnd/#")


def on_message(client, userdata, msg):
    t, h = [float(x) for x in msg.payloade.decode("utf-8").split(",")]
    print("{0}°C{1}%".format(t, h))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883, 60)
