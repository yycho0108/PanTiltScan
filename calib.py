import numpy as np
from matplotlib import pyplot as plt

arr =[
#         [2.3, 1.75],
#         [3.3, 1.4],
#         [4.3, 2.1],
#         [5.3, 2.7],
#         [6.3, 2.65],
#         [7.3, 2.5],
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

dist,voltage = zip(*arr) #dist, voltage
p = np.polyfit(voltage,dist,4) # map voltage to distance
calibrate = np.poly1d(p)


if __name__ == "__main__":
    plt.plot(voltage,dist)
    plt.plot(voltage,calibrate(voltage))
    plt.show()
