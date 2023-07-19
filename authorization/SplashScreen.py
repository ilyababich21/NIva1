from PyQt6.QtGui import QPainter
from PyQt6.QtWidgets import QWidget


class QexSplashScreen(QWidget):

    def __init__(self, movie):
        super().__init__()
        self.movie = movie



    def paintEvent(self, event):
        super().paintEvent(event)

        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.movie.currentFrame())