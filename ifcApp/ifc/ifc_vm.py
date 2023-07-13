import csv
import os
import time
from multiprocessing import Process

import pandas as pd
from PyQt6 import uic, QtWidgets, QtCore, QtGui
from PyQt6.QtCore import QTimer, QDateTime

from connection_to_db import engine, session
from ifcApp.crep.crep_vm import CrepViewModel
from ifcApp.dataSensors.data_sensors_vm import DataSensorsMainWindow
from ifcApp.dataSensors.settings_data_sensors_vm import SettingsSensors
from ifcApp.errors.notification_errors import NotificationErrors
from ifcApp.ifc.AsyncMethods.AsyncReciver import AsyncTcpReciver, WorkerSignals
from ifcApp.ifc.ButtonWidgets.ButtonForSecPre import ButtonForSectionWidget
from ifcApp.ifc.GroupBox.groupbox_widget import GroupBoxWidget
from ifcApp.ifc.mainMenu.global_param import GlobalParam
from ifcApp.ifc.mainMenu.globalparam_model import GlobalParamTable
from ifcApp.ifc.mainMenu.main_menu_vm import MainMenu
from ifcApp.ifc.users.users_in_ifc_vm import UserInIfc

UI_ifc = "view/ifc/ifc version1.ui"


def DBWriterIter():
    try:
        try:
            for chunk in pd.read_csv("CSV_History\\" + os.listdir('CSV_History')[-1], chunksize=5000):
                chunk.to_sql("sensors", engine, if_exists="append", index=False)
        except:
            print("shit")

        print("prokatilo")
        with open("CSV_History\\data" + str(len(os.listdir('CSV_History')) + 1) + ".csv", "w", newline="") as file:
            writer = csv.DictWriter(file, ["id_dat", "value", "crep_id", "create_date"], restval='Unknown',
                                    extrasaction='ignore')
            writer.writeheader()
    except:
        print('rig')
def DBwrite():
    while True:
        print("hel")
        try:
            print(pd.read_csv("CSV_History\\" + os.listdir('CSV_History')[-1]))
            try:

                time.sleep(20)
            except:
                print("ebanutsa")
        except:
            print("afvvs")
        DBWriterIter()


class IfcViewModel(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.query_global_param_table = session.query(GlobalParamTable).all()
        self.timer = QTimer()
        self.timer.timeout.connect(self.show_time)
        self.timer.start(1000)
        self.settings_sensors = SettingsSensors()
        self.data_sensors = DataSensorsMainWindow()
        self.global_param = GlobalParam()
        self.main_menu = MainMenu()
        self.user_ifc = UserInIfc()
        self.notification_errors = NotificationErrors()
        uic.loadUi(UI_ifc, self)
        self.list_groupbox = []
        self.layout_list_in_groupbox = []
        self.list_name_layout = []
        self.section_max_lineEdit.setText('2')
        self.list_all_crep = []

        for f in os.listdir('CSV_History'):
            os.remove(os.path.join('CSV_History', f))

        self.thread = QtCore.QThread()
        self.AsyncTcpReciver = AsyncTcpReciver()
        self.AsyncTcpReciver.moveToThread(self.thread)
        self.thread.started.connect(self.AsyncTcpReciver.run)
        self.create_groupbox(self.layout_groupbox)
        self.show_button()
        self.thread.start()
        proc = Process(target=DBwrite, daemon=True)
        proc.start()
        self.list_action_show = [self.v_action, self.zaz_action, self.pressure_stand1_action,
                                 self.pressure_stand2_action, self.shield_UGZ_action,
                                 self.shield_UGZ_angle_action, self.shield_UGZ_shifting_action,
                                 self.shield_UGZ_pressure_action, self.shield_UGZ_3rasp_abbr_action,
                                 self.top_drawer_action, self.top_drawer_shifting_action,
                                 self.visor_action, self.state_overlap_action,
                                 self.height_section_action1, self.height_section_action2]

        for action in self.list_action_show:
            action.triggered.connect(self.checked_action_for_sensors)

        self.show_name_action.triggered.connect(self.show_name_sensors)

        self.change_setting_action.triggered.connect(self.show_settings_sensors)

        self.data_sensors_pushButton.clicked.connect(lambda: self.data_sensors.show())
        self.notification_errors_pushButton.clicked.connect(lambda: self.show_window_crep(self.notification_errors))

        self.Ok_button.clicked.connect(self.remaster_creps)
        self.menu_pushButton.clicked.connect(lambda: self.global_param.show())
        self.global_param.save_pushButton.clicked.connect(self.update_global_param)
        self.user_pushbutton.clicked.connect(lambda: self.user_ifc.show())
        # кнопка закрытия приложения
        # self.admin_ui.exit_pushButton.clicked.connect(lambda ch :self.close())
        # print(f"ljh{QCoreApplication.instance()}")


    def create_groupbox(self, layout):
        self.list_groupbox = self.global_param.list_groupbox
        self.list_name_for_groupbox = ["ЦП", "Зазор цлиндра передвижки", "Давление в стойке левая",
                                       "Давление в стойке правая", "Щит УГЗ", "Щит Угз Угол",
                                       "Щит УГЗ ход", "Щит угз давление",
                                       "9", "10", "11", "12", "13", "14", "15"]
        list_icon_for_groupbox = ["image/img tools/conveyor_distance.png", "image/img tools/conveyor_clearance.png",
                                  "image/img tools/prop_pressure_1.png", "image/img tools/prop_pressure_2.png",
                                  "image/img tools/articulated_cantilever_pos.png",
                                  "image/img tools/articulated_cantilever_pos.png",
                                  "image/img tools/articulated_cantilever_switch.png",
                                  "image/img tools/articulated_cantilever_way.png",
                                  "image/img tools/articulated_cantilever_pressure.png",
                                  "image/img tools/articulated_cantilever3.png",
                                  "image/img tools/cantilever.png", "image/img tools/articulated_cantilever_way.png",
                                  "image/img tools/slidebar_pos.png",
                                  "image/img tools/cantilever_state.png", "image/img tools/shield_height_1.png"]
        for elem in range(15):
            self.groupbox = GroupBoxWidget()
            layout.addWidget(self.groupbox)
            self.list_groupbox.append(self.groupbox)
            self.list_groupbox[elem].min_value.setText(
                f"{self.query_global_param_table[elem].min_value}")
            self.list_groupbox[elem].max_value.setText(
                f"{self.query_global_param_table[elem].max_value}")
            self.layout_list_in_groupbox.append(self.groupbox.layoutWidget)
            self.groupbox.name_label.setText(self.list_name_for_groupbox[elem])
            self.list_name_layout.append(self.groupbox.name_label)
            self.groupbox.icon_label.setPixmap(QtGui.QPixmap(list_icon_for_groupbox[elem]))


    def show_button(self):
        self.make_buttons(self.layout_list_in_groupbox)

        for elem in range(len(self.list_groupbox)):
            self.list_groupbox[elem].name_label.raise_()

    def make_buttons(self, layout_list):
        self.cleaner_layouts(layout_list)
        for elem in range(int(self.section_max_lineEdit.text())):
            self.list_all_crep.append(CrepViewModel(elem + 1))
            self.setting_async_reciver()
            # print(self.list_all_crep[-1].show_sensor1_data(self.list_all_crep[-1].list_sensors_lineEdit[1]))
            self.create_button_layout_list(layout_list, elem)

    def cleaner_layouts(self, layout_list):
        self.list_all_crep.clear()
        for layout in layout_list:
            for i in reversed(range(layout.count())):
                layout.itemAt(i).widget().deleteLater()

    def setting_async_reciver(self):
        sigOnal1 = WorkerSignals()
        sigOnal1.result.connect(self.list_all_crep[-1].setText_lineEdit_sensors)
        self.AsyncTcpReciver.all_signal.append(sigOnal1)
        # print(sigOnal1)

    def create_button_layout_list(self, layout_list, elem):
        for one_layout in range(len(layout_list)):
            self.btn = ButtonForSectionWidget(elem + 1)
            self.btn.value = int(self.query_global_param_table[one_layout].max_value)

            self.list_all_crep[-1].list_sensors_lineEdit[one_layout].textChanged.connect(
                lambda checked, lt=one_layout, b=self.btn, g=self.list_all_crep[-1],
                       from_normal_value=int(self.query_global_param_table[one_layout].from_normal_value),
                       to_normal_value=int(self.query_global_param_table[one_layout].to_normal_value):b.ubdateColorAndHeight(
                    g.show_sensor1_data(g.list_sensors_lineEdit[lt]), self.notification_errors.textEdit, from_normal_value,to_normal_value, self.list_name_for_groupbox[lt], elem + 1, self.notification_errors_pushButton)
                )
            if len(self.list_all_crep) % 2 == 0:
                self.btn.setStyleSheet(" background-color: #e9e9e9;")
            else:
                self.btn.setStyleSheet("background-color: #a0a0a0;")
            self.btn.setMaximumWidth(int(self.btn.width() / (0.35 * int(self.section_max_lineEdit.text()))))
            self.btn.setToolTip(f"Крепь № {elem + 1}, Датчик {self.list_name_for_groupbox[one_layout]}")
            self.btn.clicked.connect(lambda list_all_crep=self.list_all_crep[-1]: self.show_window_crep(list_all_crep))
            layout_list[one_layout].addWidget(self.btn)

    def remaster_creps(self):
        # self.AsyncTcpReciver.prec=False
        # # Остановка потока
        # self.thread.quit()
        #
        # # Ожидание завершения потока
        # self.thread.wait(1000)


        print("IZMENA")
        # print(self.AsyncTcpReciver.prec)
        print(self.thread.isRunning())
        print((self.thread.isFinished()))
        self.AsyncTcpReciver.all_signal.clear()
        self.AsyncTcpReciver.brokeSignalsId.clear()
        self.show_button()
        # self.AsyncTcpReciver.prec=True
        self.thread.start()

    def show_window_crep(self, crepWin):
        if crepWin.isVisible():
            crepWin.hide()
        else:
            crepWin.show()

    def show_settings_sensors(self):
        if self.change_setting_action.isChecked():
            self.settings_sensors.show()
        else:
            self.settings_sensors.close()

    def show_name_sensors(self):
        if self.show_name_action.isChecked():
            for elem in self.list_name_layout:
                elem.show()
        else:
            for elem in self.list_name_layout:
                elem.close()

    def checked_action_for_sensors(self):

        for action in range(len(self.list_action_show)):
            if self.list_action_show[action].isChecked():
                self.list_groupbox[action].show()
            else:
                self.list_groupbox[action].close()

    def show_time(self):
        time = QDateTime.currentDateTime()
        timeDisplay = time.toString('dd.MM.yyyy HH:mm:ss')
        self.date_time.setText(timeDisplay)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.AsyncTcpReciver.prec = False

        print("ИДЕТ СОХРАНЕНИЕ....")
        try:
            for chunk in pd.read_csv("CSV_History\\" + os.listdir('CSV_History')[-1], chunksize=5000):
                chunk.to_sql("sensors", engine, if_exists="append", index=False)
        except:
            print("shit")
        print("mission complete")
        super(QtGui,self).closeEvent(a0)

    def update_global_param(self):
        self.global_param.save_on_clicked_information()
        self.remaster_creps()

    def role_for_miner(self):
        self.menu_pushButton.setEnabled(False)
        for action in self.list_action_show:
            action.setEnabled(False)

