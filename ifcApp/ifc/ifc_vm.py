import asyncio

from PyQt6 import uic, QtWidgets, QtCore
from PyQt6.QtCore import QObject, QTimer, QDateTime
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QPainter, QColor
from async_modbus import AsyncTCPClient

from ifcApp.crep.crep_vm import CrepViewModel
from ifcApp.dataSensors.data_sensors_vm import DataSensorsMainWindow
from ifcApp.dataSensors.settings_data_sensors_vm import SettingsSensors

UI_ifc = "view/ifc/ifc version1.ui"


class WorkerSignals(QObject):
    result = pyqtSignal(str)


class AsyncTcpReciver(QtCore.QObject):
    running = False
    num = None

    # sigOnal = pyqtSignal(str)
    all_signal = []

    def __init__(self, parent=None):
        super(AsyncTcpReciver, self).__init__(parent)

    # method which will execute algorithm in another thread
    def run(self):
        # for elem in range(self.num):
        #     siOn = pyqtSignal(str)
        #     self.all_signal.append(siOn)
        asyncio.run(self.RunRead())

    async def RunRead(self):
        try:
            reader = await asyncio.open_connection('127.0.0.1', 502)

            client = AsyncTCPClient(reader)
        except:
            self.running = False
        while True:
            # await asyncio.wait([read(client,i) for i in range(1,8)])
            try:
                await self.read(client)
            except:
                break

            # await asyncio.sleep(0.5)

            # print(list)

    async def read(self, client):
        # for elem in range(1, self.num+1):
        #     result = await client.read_holding_registers(slave_id=elem, starting_address=0, quantity=1)
        #     print(result)
        # result = []

        for elem in range(len(self.all_signal)):
            # for elem in range(len(self.all_signal)):
            result = await client.read_holding_registers(slave_id=1, starting_address=0, quantity=1)

            self.all_signal[elem].result.emit(str(result[0]))
            # result.append(  await client.read_holding_registers(slave_id=1, starting_address=0, quantity=1))
            # result.append(  await client.read_holding_registers(slave_id=elem+1, starting_address=0, quantity=1))
            # self.all_signal[elem].emit(str(result[0]))

            # self.all_signal[elem].result.emit(str(result[elem][0]))
            # await asyncio.sleep(0.002)
        # print("    ",result)
        # for elem in range(len(self.all_signal)):
        #     print(result[elem][0])

        # self.all_signal.emit(str( await client.read_holding_registers(slave_id=1, starting_address=0, quantity=10)))


class ClickedGraphics(QtWidgets.QFrame):
    clicked = pyqtSignal()

    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)
        self.clicked.emit()


class ButtonForPressureSection(ClickedGraphics):
    def __init__(self, number):
        super().__init__()
        self.id = number
        self.setMaximumHeight(90)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor(200, 0, 0))
        painter.drawRect(0, 60, int(10), -20)
        painter.setBrush(QColor(255, 80, 0, 160))
        painter.drawRect(10, 60, int(10), -40)


class ButtonForSection(ClickedGraphics):
    def __init__(self, number):
        super().__init__()
        self.id = number
        self.setMaximumHeight(90)


class IfcViewModel(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.settings_sensors = SettingsSensors()
        self.data_sensors = DataSensorsMainWindow()
        uic.loadUi(UI_ifc, self)
        self.section_max_lineEdit.setText('12')
        self.thread = QtCore.QThread()
        # create object which will be moved to another thread
        self.AsyncTcpReciver = AsyncTcpReciver()
        self.AsyncTcpReciver.num = int(self.section_max_lineEdit.text())
        self.AsyncTcpReciver.moveToThread(self.thread)
        self.show_time()

        # self.clientRTU= ModbusTcpClient("127.0.0.1", port=502)
        # if self.clientRTU.connected is False:
        #     self.clientRTU = None
        self.show_button()

        self.v_action.triggered.connect(self.checked_action)
        self.zaz_action.triggered.connect(self.checked_action)
        self.pressure_stand1_action.triggered.connect(self.checked_action)
        self.pressure_stand2_action.triggered.connect(self.checked_action)
        self.shield_UGZ_action.triggered.connect(self.checked_action)
        self.shield_UGZ_sensor_approximation_action.triggered.connect(self.checked_action)
        self.shield_UGZ_angle_action.triggered.connect(self.checked_action)
        self.shield_UGZ_shifting_action.triggered.connect(self.checked_action)
        self.shield_UGZ_pressure_action.triggered.connect(self.checked_action)
        self.shield_UGZ_3rasp_abbr_action.triggered.connect(self.checked_action)
        self.top_drawer_action.triggered.connect(self.checked_action)
        self.top_drawer_shifting_action.triggered.connect(self.checked_action)
        self.visor_action.triggered.connect(self.checked_action)
        self.state_overlap_action.triggered.connect(self.checked_action)
        self.height_section_action1.triggered.connect(self.checked_action)
        self.height_section_action2.triggered.connect(self.checked_action)
        self.height_section_action3.triggered.connect(self.checked_action)

        self.show_name_action.triggered.connect(self.show_name_sensors)
        self.change_setting_action.triggered.connect(self.show_settings_sensors)
        self.data_sensors_pushButton.clicked.connect(self.show_data_sensors)

        self.Ok_button.clicked.connect(self.show_button)



    def show_button(self):
        self.make_buttons(
            [self.layout_100, self.layout_400, self.layout_500, self.layout_600,
             self.layout_700, self.layout_800, ])
        self.make_buttons_for_pressure([self.layout_200, self.layout_300])
        # self.make_buttons(self.layout_300)
        # self.make_buttons(self.layout_400)
        # self.make_buttons(self.layout_500)
        # self.make_buttons(self.layout_600)
        # self.make_buttons(self.layout_700)
        # self.make_buttons(self.layout_800)
        # self.make_buttons(self.layout_900)
        # self.make_buttons(self.layout_1000)
        # self.make_buttons(self.layout_1100)
        # self.make_buttons(self.layout_1200)
        # self.make_buttons(self.layout_1300)
        # self.make_buttons(self.layout_1400)
        # self.make_buttons(self.layout_1500)
        # self.make_buttons(self.layout_1600)
        # self.make_buttons(self.layout_1700)

    def make_buttons(self, layout_list):
        for layout in layout_list:
            for i in reversed(range(layout.count())):
                layout.itemAt(i).widget().deleteLater()
        for elem in range(int(self.section_max_lineEdit.text())):
            sigOnal = WorkerSignals()
            self.AsyncTcpReciver.all_signal.append(sigOnal)
            # self.crep = CrepViewModel(btn.id,self.clientRTU)
            self.crep = CrepViewModel(elem + 1)
            self.AsyncTcpReciver.all_signal[-1].result.connect(self.crep.setText1)
            for layout in layout_list:
                btn = ButtonForSection(elem + 1)
                if elem % 2 == 0:
                    btn.setStyleSheet(" background-color: #666666;")
                else:
                    btn.setStyleSheet("background-color: #a0a0a0;")

                btn.clicked.connect(lambda b=self.crep: self.on_clicked(b))
                # btn.clicked.connect(lambda checked, b=self.crep: self.on_clicked(b,checked))

                layout.addWidget(btn)

    def make_buttons_for_pressure(self, layout_list):
        for layout in layout_list:
            for i in reversed(range(layout.count())):
                layout.itemAt(i).widget().deleteLater()
        for elem in range(int(self.section_max_lineEdit.text())):
            sigOnal = WorkerSignals()
            self.AsyncTcpReciver.all_signal.append(sigOnal)
            # self.crep = CrepViewModel(btn.id,self.clientRTU)
            self.crep = CrepViewModel(elem + 1)
            self.AsyncTcpReciver.all_signal[-1].result.connect(self.crep.setText1)
            for layout in layout_list:
                btn = ButtonForPressureSection(elem + 1)
                if elem % 2 == 0:
                    btn.setStyleSheet(" background-color: #666666;")
                else:
                    btn.setStyleSheet("background-color: #a0a0a0;")

                btn.clicked.connect(lambda b=self.crep: self.on_clicked(b))
                # btn.clicked.connect(lambda checked, b=self.crep: self.on_clicked(b,checked))

                layout.addWidget(btn)

    def on_clicked(self, crepWin):
        if crepWin.isVisible():
            crepWin.hide()

        else:
            crepWin.show()

    def show_data_sensors(self):
        self.data_sensors.show()

    def show_settings_sensors(self):
        if self.change_setting_action.isChecked():
            self.settings_sensors.show()
        else:
            self.settings_sensors.close()

    def show_name_sensors(self):
        if self.show_name_action.isChecked():
            self.CP_label.show()
            self.zaz_label.show()
            self.pressure_st1_label.show()
            self.pressure_st2_label.show()
            self.shield_UGZ_label.show()
            self.shield_UGZ_sensor_label.show()
            self.shield_UGZ_angle_label.show()
            self.shield_UGZ_hod_label.show()
            self.shield_UGZ_pressure_label.show()
            self.shield_UGZ_thrust_label.show()
            self.extension_top_label.show()
            self.extension_top_progress_label.show()
            self.koz_label.show()
            self.shifting_state_label.show()
            self.height_section1_label.show()
            self.height_section2_label.show()
            self.height_section3_label.show()

        else:
            self.CP_label.hide()
            self.zaz_label.hide()
            self.pressure_st1_label.hide()
            self.pressure_st2_label.hide()
            self.shield_UGZ_label.hide()
            self.shield_UGZ_sensor_label.hide()
            self.shield_UGZ_angle_label.hide()
            self.shield_UGZ_hod_label.hide()
            self.shield_UGZ_pressure_label.hide()
            self.shield_UGZ_thrust_label.hide()
            self.extension_top_label.hide()
            self.extension_top_progress_label.hide()
            self.koz_label.hide()
            self.shifting_state_label.hide()
            self.height_section1_label.hide()
            self.height_section2_label.hide()
            self.height_section3_label.hide()

    def checked_action(self):
        if self.v_action.isChecked():
            self.groupBox1.show()
        else:
            self.groupBox1.hide()

        if self.zaz_action.isChecked():
            self.groupBox2.show()
        else:
            self.groupBox2.hide()

        if self.pressure_stand1_action.isChecked():
            self.groupBox3.show()
        else:
            self.groupBox3.hide()

        if self.pressure_stand2_action.isChecked():
            self.groupBox4.show()
        else:
            self.groupBox4.hide()

        if self.shield_UGZ_action.isChecked():
            self.groupBox5.show()
        else:
            self.groupBox5.hide()

        if self.shield_UGZ_sensor_approximation_action.isChecked():
            self.groupBox6.show()
        else:
            self.groupBox6.hide()

        if self.shield_UGZ_angle_action.isChecked():
            self.groupBox7.show()

        else:
            self.groupBox7.hide()

        if self.shield_UGZ_shifting_action.isChecked():
            self.groupBox8.show()

        else:
            self.groupBox8.hide()

        if self.shield_UGZ_pressure_action.isChecked():
            self.groupBox9.show()

        else:
            self.groupBox9.hide()

        if self.top_drawer_action.isChecked():
            self.groupBox10.show()

        else:
            self.groupBox10.hide()

        if self.top_drawer_shifting_action.isChecked():
            self.groupBox11.show()

        else:
            self.groupBox11.hide()

        if self.shield_UGZ_3rasp_abbr_action.isChecked():
            self.groupBox12.show()

        else:
            self.groupBox12.hide()

        if self.visor_action.isChecked():
            self.groupBox13.show()

        else:
            self.groupBox13.hide()

        if self.state_overlap_action.isChecked():
            self.groupBox14.show()

        else:
            self.groupBox14.hide()

        if self.state_overlap_action.isChecked():
            self.groupBox14.show()

        else:
            self.groupBox14.hide()

        if self.height_section_action1.isChecked():
            self.groupBox15.show()

        else:
            self.groupBox15.hide()

        if self.height_section_action2.isChecked():
            self.groupBox16.show()

        else:
            self.groupBox16.hide()

        if self.height_section_action3.isChecked():
            self.groupBox17.show()

        else:
            self.groupBox17.hide()

    def show_time(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.show_time)
        self.timer.start(1000)
        time = QDateTime.currentDateTime()
        timeDisplay = time.toString('dd.MM.yyyy HH:mm:ss')
        self.date_time.setText(timeDisplay)
