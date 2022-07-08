import sys
import asyncio
import platform
from bleak import BleakClient

#This script gets all BLE services from the given MAC address

ADDRESS = (
    "60:77:71:7D:9E:03"
)


async def main(address: str):
    async with BleakClient(address) as client:
        svcs = await client.get_services()
        print("Services:")
        for service in svcs:
            print(service)


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1] if len(sys.argv) == 2 else ADDRESS))
