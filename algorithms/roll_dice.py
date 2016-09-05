from collections import Counter
import matplotlib.pyplot as plt
% matplotlib
import random

def roll():
  return random.randint(1,6) + random.randint(1,6)
n = input()

counter = Counter( roll() for roll_ in range(n) )

for i, j in counter.iteritems():
  print '%2d: %.3f' % (i, float(j / float(n)) )



plt.bar(counter.keys(), counter.values(), width=1, color='b')
plt.show()
