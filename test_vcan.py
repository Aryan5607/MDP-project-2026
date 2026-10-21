import can

try:
    # Initialize python-can virtual interface
    bus = can.interface.Bus(channel='vcan0', bustype='virtual')
    print("Virtual CAN interface setup successfully in VS Code!")
    bus.shutdown()
except Exception as e:
    print(f"Error initializing virtual CAN: {e}")