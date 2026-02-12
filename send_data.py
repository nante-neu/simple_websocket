import websocket
import json
import ssl

# Use your actual RPi ID
DEVICE_ID = "rpi_01"
URL = f"wss://192.168.103.53/ws/video/{DEVICE_ID}/"

def on_message(ws, message):
    print(f"Server replied: {message}")

def on_error(ws, error):
    print(f"!!! CONNECTION ERROR: {error}")

def on_close(ws, close_status_code, close_msg):
    print("### Closed ###")

def on_open(ws):
    print("### Connected! Sending data... ###")
    data = {
        "device_id": DEVICE_ID,
        "message": "Hello from RPi 01 - Production Test"
    }
    ws.send(json.dumps(data))
    print("Data sent.")

# The sslopt={"cert_reqs": ssl.CERT_NONE} is KEY for local HTTPS tests
ws = websocket.WebSocketApp(
    URL,
    on_open=on_open,
    on_message=on_message,
    on_error=on_error,
    on_close=on_close
)

ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
