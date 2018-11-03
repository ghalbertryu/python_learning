import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure(num='Flower of Life', figsize=(5, 5))
plt.xlim(-20, 20)
plt.ylim(-20, 20)

R = 5
halfR = R / 2
sin60R = R * np.sin(np.pi / 3) # ns = (r ** 2 - halfR ** 2) ** (1 / 2)

sin60R2 = sin60R * 2
RhalfR = halfR + R
R2 = R * 2

circle0 = plt.Circle((0, 0), R2, facecolor='none', edgecolor='silver')

circle_c1 = plt.Circle((0, R), R, facecolor='none', edgecolor='silver')
circle_c2 = plt.Circle((0, 0), R, facecolor='none', edgecolor='silver')
circle_c3 = plt.Circle((0, -R), R, facecolor='none', edgecolor='silver')

circle_r1 = plt.Circle((sin60R, halfR), R, facecolor='none', edgecolor='silver')
circle_r2 = plt.Circle((sin60R, -halfR), R, facecolor='none', edgecolor='silver')

circle_l1 = plt.Circle((-sin60R, halfR), R, facecolor='none', edgecolor='silver')
circle_l2 = plt.Circle((-sin60R, -halfR), R, facecolor='none', edgecolor='silver')

circle_rr1 = plt.Circle((sin60R2, R), R, facecolor='none', edgecolor='silver')
circle_rr2 = plt.Circle((sin60R2, 0), R, facecolor='none', edgecolor='silver')
circle_rr3 = plt.Circle((sin60R2, -R), R, facecolor='none', edgecolor='silver')

circle_ll1 = plt.Circle((-sin60R2, R), R, facecolor='none', edgecolor='silver')
circle_ll2 = plt.Circle((-sin60R2, 0), R, facecolor='none', edgecolor='silver')
circle_ll3 = plt.Circle((-sin60R2, -R), R, facecolor='none', edgecolor='silver')

circle_uu1 = plt.Circle((-sin60R, RhalfR), R, facecolor='none', edgecolor='silver')
circle_uu2 = plt.Circle((0, R2), R, facecolor='none', edgecolor='silver')
circle_uu3 = plt.Circle((sin60R, RhalfR), R, facecolor='none', edgecolor='silver')

circle_dd1 = plt.Circle((-sin60R, -RhalfR), R, facecolor='none', edgecolor='silver')
circle_dd2 = plt.Circle((0, - R2), R, facecolor='none', edgecolor='silver')
circle_dd3 = plt.Circle((sin60R, -RhalfR), R, facecolor='none', edgecolor='silver')

# ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
# (or if you have an existing figure)
ax = plt.gcf().gca()

# ax.add_artist(circle0)

ax.add_artist(circle_c1)
ax.add_artist(circle_c2)
ax.add_artist(circle_c3)

ax.add_artist(circle_r1)
ax.add_artist(circle_r2)

ax.add_artist(circle_l1)
ax.add_artist(circle_l2)

ax.add_artist(circle_rr1)
ax.add_artist(circle_rr2)
ax.add_artist(circle_rr3)

ax.add_artist(circle_ll1)
ax.add_artist(circle_ll2)
ax.add_artist(circle_ll3)

ax.add_artist(circle_uu1)
ax.add_artist(circle_uu2)
ax.add_artist(circle_uu3)

ax.add_artist(circle_dd1)
ax.add_artist(circle_dd2)
ax.add_artist(circle_dd3)

plt.show()