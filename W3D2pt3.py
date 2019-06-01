from matplotlib.pyplot import *
from numpy import *
t = arange(0,1,0.01)
y = 2*(2*pi*t)
length = len(y)
y1 = zeros(length)

for i in range(length):
	yi = y[i]
	if yi > 1.5:
		y1[i] = 1.5
	elif yi < -1.5:
		y1[i] = -1.5
    else:
		y1[i] = yi
		
figure(1)
clf()
plot(t,y1)
xlabel('Time (s)')
ylabel('y(t)')

#pt 2

for i, yi in enumerate(y):
	if yi > 1.5:
		y1[i] = 1.5
	elif yi < -1.5:
		y1[i] = -1.5
    else:
		y1[i] = yi
		

figure(2)
clf()
plot(t,y1)
xlabel('Time (s)')
ylabel('y(t)')

#pt 3

import copy
y1 = copy.copy(y)
y1[y1>1.5] = 1.5
y1[y1<-1.5] = -1.5

figure(3)
clf()
plot(t,y1)
xlabel('Time (s)')
ylabel('y(t)')


inds = where(y > 1.5)[0]
y1[inds] = 1.5
indss = where(y < -1.5)[0]
y1[indss] = -1.5

figure(4)
clf()
plot(t,y1)
xlabel('Time (s)')
ylabel('y(t)')
