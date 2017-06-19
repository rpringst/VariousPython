import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

f = plt.Figure(figsize=(5, 4), dpi=100)
a = f.add_subplot(111)
x = np.arange(-10, 10, 0.005)

root = Tk.Tk()
root.wm_title("Plotting in Tk with Matplotlib")
t1 = Tk.Toplevel(root)
f1=Tk.Frame(t1)

timestring = Tk.StringVar()
timestring.set('t = 0')
l = Tk.Label(f1, textvariable = timestring, height=25, width=75)
l.pack()
f1.pack()
t1.geometry("%dx%d+%d+%d" % (100,100,300,300))

def animate(i):
    timestring.set('t = ' + '{:04.2f}'.format(i))
    line.set_ydata((np.exp(-0.5*x**2)*np.cos(0.5*i) + 2*x*np.exp(-0.5*x**2)*np.cos(1.5*i))**2) # update the data
    root.update_idletasks()
    return line,

line, = a.plot(x, (np.exp(-0.5*x**2) + 2*x*np.exp(-0.5*x**2))**2)
a.axis([-10,10,0,4])

# a tk.DrawingArea
canvas = FigureCanvasTkAgg(f, master=root)
canvas.show()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

toolbar = NavigationToolbar2TkAgg(canvas, root)
toolbar.update()
canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

ani = animation.FuncAnimation(f, animate, np.arange(1, 200, 0.01), interval=1, blit=False)

def on_key_event(event):
    print('you pressed %s' % event.key)
    key_press_handler(event, canvas, toolbar)

canvas.mpl_connect('key_press_event', on_key_event)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

button = Tk.Button(master=root, text='Quit', command=_quit)
button.pack(side=Tk.BOTTOM)

Tk.mainloop()
