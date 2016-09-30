import numpy as np
from matplotlib import pyplot as plt

arr =[
        [2.3, 1.75],
        [3.3, 1.4],
        [4.3, 2.1],
        [5.3, 2.7],
        [6.3, 2.65],
        [7.3, 2.5],
        [8.3, 2.38],
        [9.3, 2.21],
        [10.3, 2.04],
        [11.3, 1.96],
        [12.3, 1.86],
        [13.3, 1.66],
        [14.3, 1.6],
        [15.3, 1.47],
        [16.3, 1.33],
        [17.3, 1.25],
        [18.3, 1.2],
        [19.3, 1.13],
        [20.3, 1.08],
        [21.3, 1.04],
        [22.3, 1],
        [23.3, 0.95],
        [24.3, 0.91],
        [25.3, 0.87],
        [26.3, 0.86],
        [27.3, 0.83],
        [28.3, 0.8],
        [29.3, 0.76]
        ]

arr2 = [
[9 , 3.42]    ,
[9.5 , 3.06]  ,
[10 , 2.68]   ,
[10.5 , 2.58] ,
[11 , 2.58]   ,
[11.5 , 2.63] ,
[12 , 2.72]   ,
[12.5 , 2.78] ,
[13 , 2.85]   ,
[13.5 , 2.93] ,
[14 , 3.01]   ,
[14.5 , 3.06] ,
[15 , 3.17]   ,
[15.5 , 3.25] ,
[16 , 3.34]   ,
[16.5 , 3.42] ,
[17 , 3.52]   ,
[17.5 , 3.58] ,
[18 , 3.64]   ,
[18.5 , 3.73] ,
[19 , 3.80]   ,
[19.5 , 3.88] ,
[20 , 3.92]   ,
[20.5 , 3.99] ,
[21 , 4.04]   ,
[21.5 , 4.11] ,
[22 , 4.15]   ,
[22.5 , 4.20] ,
[23 , 4.23]   ,
[23.5 , 4.28] ,
[24 , 4.33]   ,
[24.5 , 4.36] ,
[25 , 4.41]   ,
[25.5 , 4.43] ,
[26 , 4.49]   ,
[26.5 , 4.51] ,
[27 , 4.53]   ,
[27.5 , 4.57] ,
[28 , 4.59]   ,
[28.5 , 4.62] ,
[29 , 4.64]   ,
[29.5 , 4.68] ,
[30 , 4.71]   ,
[30.5 , 4.72] ,
[31 , 4.74]   ,
[31.5 , 4.78] ,
[32 , 4.80]   ,
[32.5 , 4.82] ,
[33 , 4.84]   ,
[33.5 , 4.85] ,
[34 , 4.86]   ,
[34.5 , 4.88] ,
[35 , 4.91]   ,
[35.5 , 4.93] ,
[36 , 4.95]   ,
[36.5 , 4.96] ,
[37 , 4.98]   ,
[37.5 , 4.98] ,
[38 , 4.99]]

arr2 = np.asarray(arr2)
arr2[:,0] += (-9.0 + 3.421875)

dist,voltage = zip(*arr2) #dist, voltage
p = np.polyfit(voltage,dist,4) # map voltage to distance
calibrate = np.poly1d(p)

if __name__ == "__main__":
    fig = plt.figure()
    fig.suptitle('Calibration Curve for Output Voltage of IR Sensor\n vs Distance of Object from Sensor', fontsize=16)
    plt.xlabel('Distance', fontsize=14)
    plt.ylabel('Output Voltage', fontsize=14)
    plt.scatter(voltage, dist)
    plt.plot(voltage, calibrate(voltage))
    plt.show()
    