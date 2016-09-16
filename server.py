#!/usr/bin/python

from flask import Flask, render_template, Response, jsonify
import serial
import threading

app = Flask(__name__,static_url_path='')

PI = 3.141592

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

@app.route('/scan')
def scan():
    global delta, theta, phi
    return jsonify(delta=delta,theta=d2r(theta),phi=d2r(phi))

def fetchData():
    global delta, theta, phi
    with serial.Serial(port='/dev/ttyACM0',baudrate=9600) as ser:
        data = [0.0,0.0,0.0]
        while ser.isOpen():
            try:
                tmp = [float(d) for d in str(ser.readline()).split(',')]
                if len(tmp) == 3:
                    data = tmp
            except:
                pass
            delta, theta, phi = data[0], data[1], data[2] 

if __name__ == "__main__":

    serial_reader = threading.Thread(target = fetchData);
    serial_reader.setDaemon(True);
    serial_reader.start();

    app.run(host='0.0.0.0', debug=False)
