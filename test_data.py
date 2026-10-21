import json

can_message = {
    "can_id": "0x100",
    "data": {"soc": 85.5, "voltage": 395.2},
    "timestamp": 1697702400
}

# Convert dictionary to formatted JSON string
json_data = json.dumps(can_message, indent=2)
print("Serialized JSON Output:")
print(json_data)