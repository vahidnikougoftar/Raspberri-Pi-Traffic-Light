from gpiozero import LED
from flask import Flask, render_template, jsonify

# Define the GPIO pins for each color
green_led = LED(17)
yellow_led = LED(27)
red_led = LED(22)

app = Flask(__name__)

# Initial state of the lights
lights = {
    "green": False,
    "yellow": False,
    "red": False
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/activate/<color>')
def activate(color):
    global lights
    # Check if the clicked color is already active
    if lights[color]:
        # If already active, turn it off
        lights[color] = False
        if color == "green":
            green_led.off()
        elif color == "yellow":
            yellow_led.off()
        elif color == "red":
            red_led.off()
    else:
        # Reset all lights
        lights = {k: False for k in lights}
        # Turn off all LEDs
        green_led.off()
        yellow_led.off()
        red_led.off()
        
        # Activate the chosen light
        lights[color] = True
        if color == "green":
            green_led.on()  # Turn on the green LED
        elif color == "yellow":
            yellow_led.on()  # Turn on the yellow LED
        elif color == "red":
            red_led.on()  # Turn on the red LED
            
    return jsonify(lights)

@app.route('/activate/none')
def deactivate_all():
    green_led.off()
    yellow_led.off()
    red_led.off()
    return jsonify(lights)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
