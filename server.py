#!/usr/bin/python

from flask import Flask, render_template, Response, request, jsonify
import serial
import threading
from calib import calibrate
import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__,static_url_path='')

PI = 3.141593

delta = 0.
theta = 0. 
phi = 0.

def d2r(d):
    return d * PI / 180

def r2d(r):
    return r * 180 / PI

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan',methods=['POST'])
def scan():
    global delta, theta, phi
    theta, phi = float(request.form["theta"]), float(request.form["phi"])

    if theta < 0:
        theta += 2 * PI # sanitize

    if phi < 0:
        phi += 2 * PI # sanitize

    print "theta : {}, phi : {}".format(theta,phi)

    return jsonify(delta=delta) # return scanned distance

def r2d(r):
    return int(r * 180 / 3.141592)

def fetchData():
    global delta, theta, phi
    with serial.Serial(port='/dev/ttyUSB0',baudrate=9600) as ser:
        while ser.isOpen():
            try:
                s = bytearray([int(r2d(theta)), int(r2d(phi))])
                ser.write(s)
                tmp = ser.readline() 
                print "tmp : ", tmp
                tmp = float(tmp) # temporary delta
                delta = calibrate(tmp) # fetch delta from arduino
                #print tmp, '-->', delta
            except Exception as e:
                print e
                pass

if __name__ == "__main__":

    serial_reader = threading.Thread(target = fetchData);
    serial_reader.setDaemon(True);
    serial_reader.start();

    app.run(host='0.0.0.0', debug=False)
