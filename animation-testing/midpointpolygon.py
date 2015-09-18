# creates a random polygon with N points in range R
import matplotlib.pyplot as plt
from ccw import *
import random
from matplotlib import animation

# polygon functions create polygon with N points; each has coords in range (0,R)
def makesimplepoly(N, R):
  V = []
  random.seed()
  for i in range(N):
    V.append((R*random.random(), R*random.random()))
  L_upper = []
  L_lower = []
  minx = min(V, key=lambda x: x[0])
  maxx = max(V, key=lambda x: x[0])
  for v in sorted(V, key=lambda x: x[0]):
    if v is not minx and v is not maxx:
      if ccw(minx, maxx, v)==-1:
        L_upper.append(v)
      else:
        L_lower.append(v)
  L_lower.reverse()
  L = [minx]+L_upper+[maxx]+L_lower
  return L

def makepoly(N, R):
  V = []
  random.seed()
  for i in range(N):
          V.append((R*random.random(), R*random.random()))
  return V

# set up figure, axis, plot element
fig = plt.figure()
ax = plt.axes()
line, = ax.plot([], [], marker='o', lw=2)
L = makepoly(100, 100)
midpoints = []

def animate(j):
  global L, ax
  midpoints = []
  X = []
  Y = []
  print j
  global L
  end = len(L)-1
  for i in range(0, end):
    X.append(L[i][0])
    Y.append(L[i][1])
    midpoints.append(((L[i][0]+L[i+1][0])/2, (L[i][1]+L[i+1][1])/2))
  X.append(L[0][0])
  Y.append(L[0][1])
  line.set_data(X, Y)

  ax.relim()
  ax.autoscale_view()
  midpoints.append(((L[end][0]+L[0][0])/2, (L[end][1]+L[0][1])/2))
  L = midpoints
  return line,

ani = animation.FuncAnimation(fig, animate, interval=10)

# frames is the period length of variable j...does it really do anything beyond 
# changing the number that gets passed to animate? no, i think that's it.
# this will repeat indefinitely, whereas i guess artistanimation will stop eventually.

plt.show()
