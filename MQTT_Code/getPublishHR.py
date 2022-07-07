import sys
import asyncio
import platform
import pickle
from bleak import BleakClient
import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttBroker ="10.38.4.212"
client = mqtt.Client("Temperature_Inside")
LOGTIME = 60

def notification_handler(sender, data):
    client.publish("HeartRate", data[1])


async def main(address, char_uuid, time):
    async with BleakClient(address) as client:
        print(f"Connected: {client.is_connected}")
        await client.start_notify(char_uuid, notification_handler)
        await asyncio.sleep(time)
        await client.stop_notify(char_uuid)


if __name__ == "__main__":
    client.connect(mqttBroker, 1883)
    f = open('ADRESSES.pckl', 'rb')
    ADDRESS, CHARACTERISTIC_UUID = pickle.load(f)
    f.close()
    asyncio.run(
        main(ADDRESS, CHARACTERISTIC_UUID,  int(sys.argv[1]) if len(sys.argv) > 1 else LOGTIME)
    )