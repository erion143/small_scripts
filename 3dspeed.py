from myparser import parser
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

filtr1 = (lambda line: '(АРД)' in line)
rep1 = [(r'%Pd/C(АРД)', ''),
        ('---', '0'),
        ('alkaly', '2'),
        ('acid', '1')]

filtr2 = (lambda line: 'Al2O3' in line)
rep2 = [(r'%Pd/2%C/Al2O3', '')] + rep1[1:]

res1 = parser("c.txt",
              (float, float, float, float, float),
              filt=filtr1,
              replacement=rep1,
              )

res2 = parser("c.txt",
              (float, float, float, float, float),
              filt=filtr2,
              replacement=rep2,
              )


cat1, nature1, s, order, speed1 = res1
cat2, nature2, s, order, speed2 = res2
fig = plt.gcf()
ax = fig.gca(projection='3d')
surf = ax.scatter(cat1, nature1, speed1, c='b')
surf1 = ax.scatter(cat2, nature2, speed2, c='r')
plt.show()
