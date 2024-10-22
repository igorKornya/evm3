import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return np.sin(x)**3 + np.cos(x)**2

x_values = np.linspace(3*np.pi/2, 8*np.pi, 500)

y_values = func(x_values)

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label=r'Sin$^3(x)$ + Cos$^2(x)$')
plt.title(f'Graph of the function Sin^3(x) + Cos^2(x)\nMax value: {np.max(y_values):.2f} at x = {x_values[np.argmax(y_values)]:.2f}', fontsize=14)
plt.xlabel('x values')
plt.ylabel('y values')

plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.xticks([3*np.pi/2, 2*np.pi, 3*np.pi, 4*np.pi, 5*np.pi, 6*np.pi, 7*np.pi, 8*np.pi],
           [r'$3\pi/2$', r'$2\pi$', r'$3\pi$', r'$4\pi$', r'$5\pi$', r'$6\pi$', r'$7\pi$', r'$8\pi$'])

max_value = np.max(y_values)
max_x_value = x_values[np.argmax(y_values)]

plt.annotate(f'Max value: {max_value:.2f}\nat x = {max_x_value:.2f}',
             xy=(max_x_value, max_value),
             xytext=(max_x_value+1, max_value),
             arrowprops=dict(facecolor='black', arrowstyle="->"))

plt.legend()
plt.show()
