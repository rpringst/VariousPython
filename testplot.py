from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import Tkinter as Tk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

root = Tk.Tk()
t1 = Tk.Toplevel(root)

f = Tk.Frame(root)
label = Tk.Label(f,text="Superposition State").pack()
f1 = Tk.Frame(t1)
t1.geometry("%dx%d+%d+%d" % (75,20,400,300))

timestring = Tk.StringVar()
timestring.set('t = 0')
l = Tk.Label(f1, textvariable = timestring)

l.pack()
f1.pack()

x = np.arange(-6, 6, 0.005)

def animate(i):
    timestring.set('t = ' + '{:05.3f}'.format(i))
    #line.set_ydata(((1/(4*np.pi))**(1/4))*((np.exp(-0.5*x**2)*np.cos(0.5*i) + 2*x*np.exp(-0.5*x**2)*np.cos(1.5*i))**2))
    line.set_ydata((((4*np.pi)**(-0.25))*(2*x)*np.exp(-0.5*(x**2))+((4*np.pi)**(-0.25))*np.exp(-0.5*(x**2)))**2)
    return line,

fig = plt.Figure()
canvas = FigureCanvasTkAgg(fig, master=f)
tkwidget = canvas.get_tk_widget()
tkwidget.pack()

ax = fig.add_subplot(111)
line, = ax.plot(x, (np.exp(-0.5*x**2) + 2*x*np.exp(-0.5*x**2))**2)
ax.axis([-6,6,0,5])

f.pack()

ani = animation.FuncAnimation(fig, animate, np.arange(0, 200, 0.01), interval=5, blit=False)

root.mainloop()
