python3
import matplotlib.pyplot as plt
import numpy as np
t = np.arange(1.,3.,0.02)
y = 6*np.log(t) - 7*np.exp(0.2*t)
plt.plot(t,y)
plt.xlabel('Time (sec)')
plt.ylabel('Temperature (C)')
plt.title('Reeser-Plot')
plt.show()

print('Hello World! I just wrote my first Python Program. Yayyyyyyyy \n')
print('Gabriel Reeser')

