import matplotlib as mpl
#from czifile import CziFile
mpl.use('Agg')
import sys
import matplotlib.animation as animation
import numpy as np
from pylab import *
import matplotlib.patches as patches
import matplotlib.gridspec as gridspec
import pylab as pl
import glob

dpi = 300

def ani_frame(img, name2save):

    totframes = float( img.shape[0] - 1 )/100.

    fig, ax = plt.subplots(1, 1, figsize=(4,3.5) )

    ax.axis('off')
    ax.set_aspect('equal')
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    time_text = ax.text(800, 2200, 'Time: 25s')

    im = ax.imshow( img[0,:,:] , cmap='jet', vmin=500, vmax=1900, interpolation='nearest')

    tight_layout()

    def update_img(n):
        print "\r %4.1f%%" % ( n / totframes ) ,
        sys.stdout.flush()

        IMG = img[n,:,:]

        im.set_data( IMG )

        time_text.set_text('Time: ' + str(n+28) +'s' )
        return im

    legend(loc=0)
    ani = animation.FuncAnimation(fig, update_img, img.shape[0], interval=5)
    writer = animation.writers['ffmpeg'](fps=30)
    print 'Now saving to ', name2save
    ani.save(name2save, writer=writer, dpi=dpi )
    return


filename = 'NAME OF THE FILE'
print 'Processing: ', filename
data = np.load(filename)
print data.shape, data.max(), data.min()
img = data[0,28:,0,:,:,0]

ani_frame(img, 'WTHAECs_24sInterval_10min_repl1.mp4')

print 'Done.'
