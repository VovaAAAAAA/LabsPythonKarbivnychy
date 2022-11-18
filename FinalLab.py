import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

speed = np.array([25, 35, 45, 30, 60, 120, 100, 100, 70, 75, 80, 65])
time = np.linspace(0, 11, 12)

print(time)

f_cubic = interp1d(time, speed, kind="cubic")
f_quadratic = interp1d(time, speed, kind='quadratic')
plt.plot(time, speed, 'o',time, f_quadratic(time), '-',
         time, f_cubic(time), ':')
plt.grid()
plt.show()
