import sys
from PyQt6 import uic, QtCore, QtWidgets
from matplotlib import  pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.pyplot import figure
from sqlalchemy.orm import Session
from ifcApp.graphics.graphics_model import Graphics
from serviceApp.service.service_model import engine
from matplotlib.figure import Figure

UI = "view/sensors/graphic.ui"



class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)


class GraphicsWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(GraphicsWindow, self).__init__(*args, **kwargs)

        uic.loadUi(UI, self)
        self.sc = MplCanvas()
        self.x =[]
        self.y = []
        toolbar = NavigationToolbar(self.sc, self)
        self.vLayout.addWidget(toolbar)
        self.vLayout.addWidget(self.sc)


        # Setup a timer to trigger the redraw by calling update_plot.
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()
    def update_plot(self):
        with Session(autoflush=False, bind=engine) as db:
            oneRow = db.query(Graphics).all()
            for p in oneRow:
                self.y.append(p.sensors)
                self.x.append(p.datetime)


        self.x = self.x[-4:]

        self.y = self.y[-4:]
        self.sc.ax.cla()
        self.sc.ax.plot(self.x, self.y)
        self.sc.ax.set_title('datetime')
        # self.sc.ax.plt.xticks(rotation=45, ha='right')
        # plt.xticks(rotation=45, ha='right')
        # plt.subplots_adjust(bottom=0.3)
        # plt.ylabel('random')
        self.sc.ax.grid()


        # Trigger the canvas to update and redraw.
        self.sc.draw()





#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     w = MainWindow()
#     w.show()
#     app.exec()
