"""pylab inline"""
import matplotlib
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

N = 100
x_offset = 37
y_offset = 50
x_factor = 5
y_factor = 4
ax = plt.gca()
fig = plt.gcf()
img = mpimg.imread('Monster_1.png')
for x in range(N + 1):
    ax.axhline(x*x_factor+x_offset, lw=1, color='k', zorder=10)
    ax.axvline(x*y_factor+y_offset, lw=1, color='k', zorder=10)
    print(x*y_factor+y_offset)
implot = ax.imshow(img)

# N = 100
# # make an empty data set
# data = np.ones((N, N)) * np.nan
# for j in range(5)[::-1]:
#     data[N//2 - j : N//2 + j +1, N//2 - j : N//2 + j +1] = j
# # make a figure + axes
# fig, ax = plt.subplots(1, 1, tight_layout=True)
# # make color map
# my_cmap = matplotlib.colors.ListedColormap(['r', 'g', 'b'])
# # set the 'bad' values (nan) to be white and transparent
# my_cmap.set_bad(color='w', alpha=0)
# # draw the grid
# for x in range(N + 1):
#     ax.axhline(x, lw=1, color='k', zorder=5)
#     ax.axvline(x, lw=1, color='k', zorder=5)
#
# implot = ax.imshow(img)
# ax.imshow((0,), interpolation='none', cmap=my_cmap, extent=[0, N, 0, N], zorder=0)


def onclick(event):
    if event.xdata != None and event.ydata != None:
        print(event.xdata, event.ydata)


cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()