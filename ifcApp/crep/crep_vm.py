from PyQt6 import QtCore
from PyQt6 import uic, QtWidgets
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QGraphicsScene, QGraphicsView

from ifcApp.dataSensors.data_sensors_vm import DataSensorsSection

UI_crep = "view/ifc/ifc_crep.ui"


class ClickedGraphics(QGraphicsView):
    clicked = pyqtSignal()

    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)

        self.clicked.emit()


class CreateGraphicScene(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        scene = QGraphicsScene()
        scene.setSceneRect(+10, -10, self.width() - 41, self.height())
        self.pixmap = QPixmap("image/sensors/sparaw.png")
        self.arrow = scene.addPixmap(self.pixmap)
        self.arrow.setTransformOriginPoint(38, 11)
        self.arrow.setRotation(-5)
        self.graphicsView = ClickedGraphics()
        self.graphicsView.setStyleSheet("background-image:url(image/sensors/sensors.png);\n"
                                        "background-repeat:no-repeat;\n"
                                        "background-position: center;")
        self.graphicsView.setScene(scene)
        self.graphicsView.clicked.connect(lambda: print('Console'))

    def valuechange(self, lineEdit):
        angel = lineEdit.text()
        if angel == '':
            angel = 0
        else:
            angel = int(angel)
        self.arrow.setRotation((angel * 2 - 5))
        print(angel)


class Changer(QtCore.QThread):
    dat1 = QtCore.pyqtSignal(str)
    dat2 = QtCore.pyqtSignal(str)
    dat3 = QtCore.pyqtSignal(str)
    clientRTU = None
    # clientRTU = ModbusTcpClient("127.0.0.1",502)
    SlaveID = None

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

        self.running = False

    text = ['', '', '']

    def run(self):
        self.running = True

        while self.running == True:
            if self.clientRTU:
                try:
                    self.text = self.clientRTU.read_holding_registers\
                        (address=0, count=3, slave=self.SlaveID).registers
                    print(self.text)
                # except serial.SerialException as e:
                #     print(e)
                #     self.text = ['','','']
                except:

                    self.text = ['', '', '']

            # else:
            #     self.text += str(
            #         clientTCP.read_holding_registers
            #         (int(addressssio), int(countio), int(Slavik)).registers[0])
            # self.text += '\n'
            self.dat1.emit(str(self.text[0]))
            self.dat2.emit(str(self.text[1]))
            self.dat3.emit(str(self.text[2]))

            QtCore.QThread.msleep(1000)

    #     self.running = True
    #     asyncio.run(self.get_var_modbus())
    #     # loop = asyncio.get_event_loop()
    #     # loop.create_task(self.get_var_modbus(loop))
    #     # loop.run_forever()
    #
    # async def get_var_modbus(self):
    #     self.client = await AsyncModbusSerialClient(port="COM9", baudrate=9600)
    #
    #     while True:
    #         if self.client:
    #             self.text = str(
    #                 await self.client.read_holding_registers(0,1, unit=1).registers[0])
    #         self.text += '\n'
    #         self.nextValueOfText.emit(self.text)
    #         await QtCore.QThread.msleep(1000)


class CrepViewModel(QtWidgets.QMainWindow):
    def __init__(self, num, clientRTU):
        super().__init__()

        uic.loadUi(UI_crep, self)

        speed = CreateGraphicScene(self)
        self.gridLayout1.addWidget(speed.graphicsView)
        self.sensors1_lineEdit.textChanged.connect\
            (lambda: speed.valuechange(self.sensors1_lineEdit))

        speed2 = CreateGraphicScene(self)
        self.gridLayout2.addWidget(speed2.graphicsView)
        self.sensors2_lineEdit.textChanged.connect(lambda: speed2.valuechange(self.sensors2_lineEdit))

        speed3 = CreateGraphicScene(self)
        self.gridLayout3.addWidget(speed3.graphicsView)
        self.sensors3_lineEdit.textChanged.connect(lambda: speed3.valuechange(self.sensors3_lineEdit))

        self.data_sensors_section = DataSensorsSection()
        self.num_crep.setText(str(num))
        self.control_pushButton.clicked.connect(self.show_data_sensors_section)

        self.tracker = Changer()
        self.tracker.clientRTU = clientRTU
        self.tracker.SlaveID = num
        self.tracker.dat1.connect(self.setText1)
        self.tracker.dat2.connect(self.setText2)
        self.tracker.dat3.connect(self.setText3)
        self.tracker.start()

    # def closeEvent(self, event):  # Вызывается при закрытии окна
    #     self.hide()  # Скрываем окно
    #     self.tracker.running = False  # Изменяем флаг выполнения
    #     self.tracker.wait(1000)  # Даем время, чтобы закончить
    #     event.accept()  # Закрываем окно

    def show_data_sensors_section(self):
        self.data_sensors_section.show()

    @QtCore.pyqtSlot(str)
    def setText1(self, string):
        self.sensors1_lineEdit.setText(string)

    @QtCore.pyqtSlot(str)
    def setText2(self, string):
        self.sensors2_lineEdit.setText(string)

    #
    @QtCore.pyqtSlot(str)
    def setText3(self, string):
        self.sensors3_lineEdit.setText(string)
