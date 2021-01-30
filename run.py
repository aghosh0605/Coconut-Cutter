from flask import Flask
from flask import render_template, request
import RPi.GPIO as GPIO
import time
import serial

app = Flask(__name__)

#serial Communication Arduino
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.flush()

# Hold release Motors Left
top_pos_left = 18
top_neg_left = 23
bottom_pos_left = 24
bottom_neg_left = 25

# Hold release Motors Right
top_pos_right = 17
top_neg_right = 19
bottom_pos_right = 20
bottom_neg_right = 21

#Spine Motor
sp1 = 15
sp2 = 16


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(top_pos_left, GPIO.OUT)
GPIO.setup(top_neg_left, GPIO.OUT)
GPIO.setup(bottom_pos_left, GPIO.OUT)
GPIO.setup(bottom_neg_left, GPIO.OUT)
GPIO.setup(top_pos_right, GPIO.OUT)
GPIO.setup(top_neg_right, GPIO.OUT)
GPIO.setup(bottom_pos_right, GPIO.OUT)
GPIO.setup(bottom_neg_right, GPIO.OUT)
GPIO.setup(sp1, GPIO.OUT)
GPIO.setup(sp2, GPIO.OUT)

GPIO.output(top_pos_left, 0)
GPIO.output(top_neg_left, 0)
GPIO.output(bottom_pos_left, 0)
GPIO.output(bottom_neg_left, 0)
GPIO.output(top_pos_right, 0)
GPIO.output(top_neg_right, 0)
GPIO.output(bottom_pos_right, 0)
GPIO.output(bottom_neg_right, 0)
GPIO.output(sp1, 0)
GPIO.output(sp2, 0)
print("Done")

a = 1


@app.route("/")
def index():
    return render_template('robot.html')


@app.route('/holdup')
def holdup():
    data1 = "holdup"
    GPIO.output(top_pos_left, 1)
    GPIO.output(top_neg_left, 0)
    GPIO.output(top_pos_right, 0)
    GPIO.output(top_neg_right, 1)

    return 'true'

@app.route('/releaseup')
def releaseup():
    data1 = "releaseup"
    GPIO.output(bottom_pos_left, 0)
    GPIO.output(bottom_neg_left, 1)
    GPIO.output(bottom_pos_right, 1)
    GPIO.output(bottom_neg_right, 0)
    return 'true' 

@app.route('/holddown')
def holddown():
    data1 = "holddown"
    GPIO.output(bottom_pos_left, 1)
    GPIO.output(bottom_neg_left, 0)
    GPIO.output(bottom_pos_right, 0)
    GPIO.output(bottom_neg_right, 1)
    return 'true'    


@app.route('/releasedown')
def releasedown():
    data1 = "releasedown"
    GPIO.output(top_pos_left, 0)
    GPIO.output(top_neg_left, 1)
    GPIO.output(top_pos_right, 1)
    GPIO.output(top_neg_right, 0)
    return 'true'

       

@app.route('/shrink')
def shrink():
    data1 = "shrink"
    GPIO.output(sp1, 1)
    GPIO.output(sp2, 0)
    # GPIO.output(bottom_pos_left, 1)
    # GPIO.output(bottom_neg_left, 0)
    return 'true'


@app.route('/extend')
def extend():
    data1 = "extend"
    GPIO.output(sp1, 0)
    GPIO.output(sp2, 1)
    # GPIO.output(bottom_pos_left, 0)
    # GPIO.output(bottom_neg_left, 1)
    return 'true'


@app.route('/stop')
def stop():
    data1 = "STOP"
    GPIO.output(top_pos_left, 0)
    GPIO.output(top_neg_left, 0)
    GPIO.output(bottom_pos_left, 0)
    GPIO.output(bottom_neg_left, 0)
    GPIO.output(top_pos_right, 0)
    GPIO.output(top_neg_right, 0)
    GPIO.output(bottom_pos_right, 0)
    GPIO.output(bottom_neg_right, 0)
    GPIO.output(sp1, 0)
    GPIO.output(sp2, 0)
    return 'true'


if __name__ == "__main__":
    print("Start")
    app.run(debug=True, host='0.0.0.0', port=8888)
