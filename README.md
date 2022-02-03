# SmartLight
Control smart bulb via hand gestures with Google Pixel 4 Soli radar.

# Controls
- `Tap` to turn on or off the light.
- `Swipe` left or right to switch between light profiles.
- `Hover` on the Pixel 4 around 5 to 25 cm to adjust the brightness.
- `Presence` to keep the light on, or it will turn off if there is no people around within 1 m.

# Requirements
- Google Pixel 4 with Soli Radar enabled
- Soli Sandbox app
- Raspberry Pi or any computer that can run Python3
- Light bulb that made my Yeelight

# Setup
1. Setup the light bulb by Yeelight App and obtain IP address of the bulb.
2. Install required python packages: `pip3 install flask pyopenssl yeelight`
3. Modify IP address to `server.py`
4. Since `Soli Sandbox` only connect certrified `HTTPS` connection, thus you must have a **domain name** and the **cert file** (Can obtain from Lets Encrypt)
5. run `python3 server.py` to start the server.
