import numpy as np
import matplotlib.pyplot as plt

tau = 120e-6
density = float(5)/9834
M = 1 / tau
theta = np.pi / 6


def p_collision(N):
    sum = 0
    for i in range(1, N):
        sum += np.log((M - i)/M)
    return 10 ** sum

def get_N(alt):
    r = np.tan(theta) * alt
    A = np.pi * r ** 2
    N = density * A
    return int(N)

altitudes = np.linspace(300, 1000, 701)
rx = [p_collision(get_N(alt))*get_N(alt) for alt in altitudes]
print get_N(408)
print p_collision(1)

plt.plot(altitudes, rx, 'r')
plt.axvline(x=408)
plt.xlabel('Altitude (km)')
plt.ylabel('Messages per second')
plt.show()
