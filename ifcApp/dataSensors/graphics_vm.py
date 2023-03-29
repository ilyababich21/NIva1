import datetime as dt
import random
import matplotlib.pyplot
import matplotlib.animation as animation


# Create figure for plotting
fig = matplotlib.pyplot.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []


def animate(i, xs, ys):


    temp = round(random.randint(1,60),2)

    xs.append(dt.datetime.now().strftime('%H:%M:%S'))
    ys.append(temp)

    xs = xs[-10:]
    ys = ys[-10:]


    ax.clear()
    ax.plot(xs, ys)

    matplotlib.pyplot.xticks(rotation=45, ha='right')
    matplotlib.pyplot.subplots_adjust(bottom=0.3)
    matplotlib.pyplot.title('datetime')
    matplotlib.pyplot.ylabel('random')


ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
matplotlib.pyplot.show()

