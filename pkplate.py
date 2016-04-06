import matplotlib as mpl
import matplotlib.pyplot as plt

INC = .3937
FS = [i * INC for i in [8, 6]]

mpl.rcParams['font.size'] = 12
mpl.rcParams['figure.figsize'] = FS

'''
Параметр labelsize принимает значения:
"xx-small", "x-small", "small", "medium", "large", "x-large",
"xx-large" или число - размер шрифта
'''
mpl.rcParams['axes.labelsize'] = 'medium'

'''
Параметр labelweight принимает значения:
"ultralight", "light", "normal", "regular", "book", "medium",
"roman", "semibold", "demibold", "demi", "bold", "heavy",
"extra bold", "black" или число 0..1000
'''
mpl.rcParams['axes.labelweight'] = 'semibold'

def plate(x, y, ymax):
    fig = plt.gcf()
    ax = fig.gca()
    ax.set_position([.19, .22, (.93 - .2), (.93 - .22)])
    plt.bar(x, y, width=.2, color='black')
    plt.axis((0, 14, 0, ymax))
    plt.xlabel('pK')
    plt.ylabel('q')
    plt.show()

pkNi = [5.5, 6.7, 6.9, 8.3, 10, 10.1, 12.5, 12.6]
qNi = [.25, .01, .01, .04, .02, .05, .14, .5]

pkPd = [1.9, 4.2, 6.5, 8.3, 12.0]
qPd = [.47, .01, .01, .02, .44]

plate(pkNi, qNi, .6)
