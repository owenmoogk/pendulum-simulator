import data
import matplotlib.pyplot as plt


def initGraph():
    global figure, line1, line2, ax
    x = data.data["x"]
    y = data.data["y"]
    figure, ax = plt.subplots()
    line1, = ax.plot(x, y)
    line2, = ax.plot(x, y)

    ax.set_ylabel('Energy')
    ax.set_xlabel("Time")
    ax.set_title('Potential vs Kinetic Energy')
    
    ax.set_ylim(-0.1, 3)
    # for time angle
    ax.set_xlim(0, 350)

def updateGraph(tick):
    global figure, line1, line2, ax
    # line1.set_xdata(data.data["ticks"])
    # line1.set_ydata(data.data["velocity"])

    # line2.set_xdata(data.data["ticks"])
    # line2.set_ydata(data.data["acceleration"])

    line1.set_xdata(data.data["ticks"])
    line1.set_ydata(data.data["potential"])

    line2.set_xdata(data.data["ticks"])
    line2.set_ydata(data.data["kinetic"])


    figure.canvas.draw()
    figure.canvas.flush_events()
