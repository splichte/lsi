# plots the line segments and the intersections
import matplotlib.pyplot as plt
from lsi import intersection
from helper import *
from gen_random_segs import gen_random_segs

plt.style.use('ggplot')

N = 100
S = gen_random_segs(N)

i = intersection(S)

intersections = i.keys()
# flatten list of lists into one list
segs = [seg for seglist in i.values() for seg in seglist]

(x,y) = zip(*intersections)
plt.scatter(x,y,c='r',s=[20]*len(x))

for seg in segs:
  # each s in segs is an individual segment.
  pt1x = seg[0]
  pt2x = seg[1]
  (x,y) = zip(*seg)
  plt.plot(x,y,'k-',lw=0.5)

plt.show()
