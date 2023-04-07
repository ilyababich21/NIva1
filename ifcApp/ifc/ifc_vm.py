from datetime import datetime
import asyncio
from PyQt6 import uic, QtWidgets, QtCore
from PyQt6.QtCore import pyqtSignal, pyqtBoundSignal, QObject, QTimer, QDateTime
from PyQt6.QtWidgets import QColorDialog
from pymodbus.client import ModbusSerialClient, ModbusTcpClient
from pymodbus.server import StartTcpServer
from PyQt6.QtGui import QPainter, QColor
from async_modbus import AsyncTCPClient
from ifcApp.crep.crep_vm import CrepViewModel
from ifcApp.dataSensors.data_sensors_vm import DataSensorsMainWindow
from ifcApp.dataSensors.settings_data_sensors_vm import SettingsSensors
import time

from ifcApp.ifc.AsyncMethods.AsyncReciver import AsyncTcpReciver, WorkerSignals
from ifcApp.ifc.ButtonWidgets.ButtonForSecPre import ButtonForPressureSection, ButtonForSection

UI_ifc = "view/ifc/ifc version1.ui"

class IfcViewModel(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.timer = QTimer()

        self.timer.timeout.connect(self.show_time)
        self.timer.start(1000)
        self.settings_sensors = SettingsSensors()
        self.data_sensors = DataSensorsMainWindow()
        uic.loadUi(UI_ifc, self)
        self.section_max_lineEdit.setText('2')
        self.thread = QtCore.QThread()
        self.AsyncTcpReciver = AsyncTcpReciver()
        self.AsyncTcpReciver.num = int(self.section_max_lineEdit.text())
        self.AsyncTcpReciver.moveToThread(self.thread)

        self.show_button()
        self.thread.started.connect(self.AsyncTcpReciver.run)
        self.thread.start()

        self.list_action_show = [self.v_action, self.zaz_action, self.pressure_stand1_action,
                                 self.pressure_stand2_action,
                                 self.shield_UGZ_action, self.shield_UGZ_sensor_approximation_action,
                                 self.shield_UGZ_angle_action, self.shield_UGZ_shifting_action,
                                 self.shield_UGZ_pressure_action, self.shield_UGZ_3rasp_abbr_action,
                                 self.top_drawer_action,
                                 self.top_drawer_shifting_action,
                                 self.visor_action, self.state_overlap_action, self.height_section_action1,
                                 self.height_section_action2, self.height_section_action3]
        print(self.list_action_show)

        for action in self.list_action_show:
            action.triggered.connect(self.checked_action111)

        self.show_name_action.triggered.connect(lambda: self.show_name_sensors(
            [self.CP_label, self.zaz_label, self.pressure_st1_label, self.pressure_st2_label,
             self.shield_UGZ_label, self.shield_UGZ_sensor_label,
             self.shield_UGZ_angle_label, self.shield_UGZ_hod_label, self.shield_UGZ_pressure_label,
             self.shield_UGZ_thrust_label, self.extension_top_label, self.extension_top_progress_label,
             self.koz_label, self.shifting_state_label, self.height_section1_label,
             self.height_section2_label, self.height_section3_label]))
        self.change_setting_action.triggered.connect(self.show_settings_sensors)
        self.data_sensors_pushButton.clicked.connect(self.show_data_sensors)

        self.Ok_button.clicked.connect(self.show_button)

    def show_button(self):
        self.make_buttons(
            [
                self.layout_100, self.layout_200, self.layout_300, self.layout_400, self.layout_500, self.layout_600,
                self.layout_700, self.layout_800,
            ])

    def make_buttons(self, layout_list):
        for layout in layout_list:
            for i in reversed(range(layout.count())):
                layout.itemAt(i).widget().deleteLater()
        for elem in range(int(self.section_max_lineEdit.text())):
            sigOnal = WorkerSignals()
            sigMinet = WorkerSignals()
            self.AsyncTcpReciver.all_signal.append(sigOnal)
            self.AsyncTcpReciver.all_signal2.append(sigMinet)
            self.crep = CrepViewModel(elem + 1)
            self.AsyncTcpReciver.all_signal[-1].result.connect(self.crep.setText1)
            self.AsyncTcpReciver.all_signal2[-1].result.connect(self.crep.setText2)
            for layout in layout_list:
                if layout == self.layout_200 or layout == self.layout_300:
                    btn = ButtonForPressureSection(elem + 1)
                    self.crep.sensors1_lineEdit.textChanged.connect(
                        lambda checked, b=btn, g=self.crep: b.change_rectangle_size(g.show_sensor1_data()))
                    self.crep.sensors2_lineEdit.textChanged.connect(
                        lambda checked, b=btn, g=self.crep: b.change_rectangle_size1(g.show_sensor2_data()))
                else:
                    btn = ButtonForSection(elem + 1)
                if elem % 2 == 0:
                    btn.setStyleSheet(" background-color: #666666;")
                else:
                    btn.setStyleSheet("background-color: #a0a0a0;")

                btn.clicked.connect(lambda b=self.crep: self.on_clicked(b))
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

    def show_name_sensors(self, list_name_sensors):
        if self.show_name_action.isChecked():
            for elem in list_name_sensors:
                elem.show()
        else:
            for elem in list_name_sensors:
                elem.hide()

    def checked_action(self, activon):
        if self.list_action_show[activon].isChecked():
            self.list_action_group_box[activon].show()
        else:
            self.list_action_group_box[activon].hide()

    def checked_action111(self):
        list_action_show = [self.v_action, self.zaz_action, self.pressure_stand1_action, self.pressure_stand2_action,
                            self.shield_UGZ_action, self.shield_UGZ_sensor_approximation_action,
                            self.shield_UGZ_angle_action, self.shield_UGZ_shifting_action,
                            self.shield_UGZ_pressure_action, self.shield_UGZ_3rasp_abbr_action, self.top_drawer_action,
                            self.top_drawer_shifting_action,
                            self.visor_action, self.state_overlap_action, self.height_section_action1,
                            self.height_section_action2, self.height_section_action3]

        list_action_group_box = [self.groupBox1, self.groupBox2, self.groupBox3, self.groupBox4,
                                 self.groupBox5, self.groupBox6,
                                 self.groupBox7, self.groupBox8,
                                 self.groupBox9, self.groupBox10, self.groupBox11,
                                 self.groupBox12,
                                 self.groupBox13, self.groupBox14, self.groupBox15,
                                 self.groupBox16, self.groupBox17]

        for action in range(len(list_action_show)):
            if list_action_show[action].isChecked():
                list_action_group_box[action].show()
            else:
                list_action_group_box[action].hide()

    def show_time(self):
        time = QDateTime.currentDateTime()
        timeDisplay = time.toString('dd.MM.yyyy HH:mm:ss')
        self.date_time.setText(timeDisplay)
