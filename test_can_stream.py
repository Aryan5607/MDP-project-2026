import can
import time

# Connect to virtual CAN bus
bus = can.interface.Bus(channel='vcan0', bustype='virtual')

print("Broadcasting dummy CAN frames (Press Ctrl+C to stop)...")

try:
    while True:
        # Construct a standard 8-byte CAN message
        msg = can.Message(
            arbitration_id=0x100,
            data=[0x55, 0xAA, 0x12, 0x34, 0x00, 0x00, 0x00, 0x00],
            is_extended_id=False
        )
        bus.send(msg)
        print(f"Sent frame: {msg}")
        time.sleep(1)  # Send 1 frame per second
except KeyboardInterrupt:
    print("\nStopped CAN stream.")
    bus.shutdown()