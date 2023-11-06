import matplotlib.pyplot as plt
import settings

def initGraph():
    global figure, line1, line2, line3, ax
    x = data["x"]
    y = data["y"]
    figure, ax = plt.subplots()
    line1, = ax.plot(x, y)
    line2, = ax.plot(x, y)
    line3, = ax.plot(x, y)

    ax.set_ylabel('Energy (J)')
    ax.set_xlabel("Time")
    ax.set_title('Potential vs Kinetic Energy')
    
    ax.set_ylim(-0.1, 20)
    # for time angle
    ax.set_xlim(0, 50)

def updateGraph():
    global figure, line1, line2, ax
    # line1.set_xdata(data["ticks"])
    # line1.set_ydata(data["velocity"])

    # line2.set_xdata(data["ticks"])
    # line2.set_ydata(data["acceleration"])

    line1.set_xdata(data["time"])
    line1.set_ydata(data["potential"])

    line2.set_xdata(data["time"])
    line2.set_ydata(data["kinetic"])

    line3.set_xdata(data["time"])
    line3.set_ydata(data["energy"])


    figure.canvas.draw()
    figure.canvas.flush_events()

data = {
    "x": [],
    "y": [],
    "angle": [],
    "time": [],
    "velocity": [],
    "acceleration": [],
    "ticks": [],
    "potential": [],
    "kinetic": [],
    "energy": [],
}

def logData(pendulum, timeElapsed):
    data["x"].append(pendulum.nodeX - pendulum.originX)
    data["y"].append(-(pendulum.nodeY - pendulum.originY))
    data["angle"].append(pendulum.angle)
    data["time"].append(timeElapsed)
    data["velocity"].append(pendulum.angularVelocity)
    data["acceleration"].append(pendulum.angularAcceleration)

    # mgh
    data["potential"].append((pendulum.originY+ settings.length - pendulum.nodeY) * settings.pixelToMeter * settings.mass * settings.gravity)

    # mv^2 / 2
    data["kinetic"].append(0.5 * settings.mass * (pendulum.angularVelocity**2))

    data["energy"].append(0.5 * settings.mass * (pendulum.angularVelocity**2) + (pendulum.originY+ settings.length - pendulum.nodeY) * settings.pixelToMeter * settings.mass * settings.gravity)