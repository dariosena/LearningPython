import math

v0 = 5
g = 9.81
yc = 0.2

t1 = (v0 - math.sqrt(v0**2 - 2 * g * yc)) / g
t2 = (v0 + math.sqrt(v0**2 - 2 * g * yc)) / g

print('At t = {} s and {} s, the height is {} m.'.format(t1, t2, yc))
