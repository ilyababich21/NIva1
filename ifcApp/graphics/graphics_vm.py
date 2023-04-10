import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication
from matplotlib import animation, pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from sqlalchemy.orm import  Session
from ifcApp.graphics.graphics_model import Graphics
from serviceApp.service.service_model import engine

UI = "graphic.ui"



class MplCanvas(FigureCanvasQTAgg):

    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1,1,1)

        super(MplCanvas, self).__init__(self.fig)
class GraphicsWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(GraphicsWindow, self).__init__(*args, **kwargs)
        uic.loadUi(UI, self)
        self.sc = MplCanvas()

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar(self.sc, self)
        self.vLayout.addWidget(toolbar)
        self.vLayout.addWidget(self.sc)
        xs = []
        ys = []

        def animate(i, xs, ys):
            with Session(autoflush=False, bind=engine) as db:
                oneRow = db.query(Graphics).all()
            for p in oneRow:
                xs.append(p.datetime)
                ys.append(p.sensors)
                print(p.datetime)

            xs = xs[-15:]
            ys = ys[-15:]

            self.sc.ax.clear()
            self.sc.ax.plot(xs, ys)
            self.sc.ax.grid()
            plt.xticks(rotation=45, ha='right')
            plt.subplots_adjust(bottom=0.3)
            plt.title('datetime')
            plt.ylabel('random')

        self.ani = animation.FuncAnimation(self.sc.fig, animate, fargs=(xs, ys), interval=1000)






if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = GraphicsWindow()
    w.show()
    app.exec()
