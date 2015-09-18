import matplotlib

# can't blit on OS X without a different backend
# and the animation is slower otherwise
# needs to come before pyplot import
matplotlib.use('TKAgg')

import matplotlib.pyplot as plt
from ccw import *
import random
import numpy as np
from matplotlib import animation

# prettier
plt.style.use('ggplot')

# canvas size
height = 400
width = 400

# set up figure, axis, plot element
fig = plt.figure()
ax = plt.axes()
ax.set_xlim(0,width)
ax.set_ylim(0,height)
line, = ax.plot([], [], lw=1)
midpoints = []

def init():
  line.set_data([], [])
  return line,

def animate(j):
  j = height-j;
  # line has to be the same object -- that's why we use set_data
  line.set_data([0,width], [j, j])
  return line,

ani = animation.FuncAnimation(fig, animate, frames=height, interval=10, repeat=False, blit=True, init_func=init)

# frames is the period length of variable j...does it really do anything beyond 
# changing the number that gets passed to animate? no, i think that's it.
# this will repeat indefinitely, whereas i guess artistanimation will stop eventually.

# set repeat=False to get funcanimation to stop running after the specified number of frames.

plt.show()
