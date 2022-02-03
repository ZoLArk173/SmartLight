from crypt import methods
from flask import Flask, render_template, request
import json
from yeelight import Bulb, flows

bulb = Bulb("192.168.100.108")
app = Flask(__name__)

@app.route("/on/")
def on():
    bulb.turn_on()
    return "ON"

@app.route("/off/")
def off():
    bulb.turn_off()
    return "OFF"

@app.route("/setBrightness/", methods=['POST'])
def setBrightness():
    brightness = json.loads(request.data)['value']
    bulb.set_brightness(brightness)
    return "OK"

@app.route("/setMode/", methods=['POST'])
def setMode():
    m = json.loads(request.data)['value']
    if m == "white":
        bulb.set_rgb(255, 255, 255)
    elif m == "candle":
        bulb.start_flow(flows.candle_flicker())
    return "OK"

@app.route("/")
def index():
    return render_template("index.html")

app.run("zolark173.com", "443", debug=True, ssl_context=('fullchain.pem', 'privkey.pem'))