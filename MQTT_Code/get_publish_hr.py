#!/usr/bin/env python
'''
This script gets the heart rate from the Bluetooth watch and
publishes in under the topic "HeartRate" via MQTT
'''
import sys
import asyncio
import pickle
from bleak import BleakClient
import paho.mqtt.client as mqtt
import addr_info

client = mqtt.Client("Jetson")
RUNTIME = 60

def notification_handler(sender, data):
    '''Handles the reception of data via bluetooth and sends it back out over MQTT'''
    print(str(data[1]), " ", end='\r')
    client.publish("HeartRate", str(data[1]))


async def main(address, char_uuid, time):
    '''
    Handles the connection to the bluetooth watch
    and waits until the designated time is up to terminate
    '''
    async with BleakClient(address) as bluetooth_client:
        print(f"Connected: {client.is_connected}")
        await bluetooth_client.start_notify(char_uuid, notification_handler)
        await asyncio.sleep(time)
        await bluetooth_client.stop_notify(char_uuid)


if __name__ == "__main__":
    client.connect(addr_info.MOSQUITTO_IP, 1883)
    ADDRESS = addr_info.BLUETOOTH_MAC
    CHARACTERISTIC_UUID = addr_info.CHAR_UUID
    asyncio.run(
        main(ADDRESS, CHARACTERISTIC_UUID,  int(sys.argv[1]) if len(sys.argv) > 1 else RUNTIME)
    )
