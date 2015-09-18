# Generate N random line segments in the plane.

import random

def scale(i):
  return float(i)

def gen_random_segs(N):
  S = [] 
  for i in range(N):
    p1 = (scale(random.randint(0, 1000)), scale(random.randint(0, 1000)))
    p2 = (scale(random.randint(0, 1000)), scale(random.randint(0, 1000)))
    s = (p1, p2)
    S.append(s)

  return S
