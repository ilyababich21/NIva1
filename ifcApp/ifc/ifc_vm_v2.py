import threading

from PyQt6 import uic, QtWidgets, QtGui, QtCore
from PyQt6.QtCore import QTimer, QDateTime, QSettings
from PyQt6.QtWidgets import QApplication, QTableWidgetItem

from address import resource_path
from ifcApp.countShield.count_shield_vm import CountShieldVM
from ifcApp.crep.crep_vm import CrepViewModel
from ifcApp.dataSensors.data_sensors_vm import DataSensorsMainWindow
from ifcApp.errors.notification_errors import NotificationErrors
from ifcApp.ifc.buttonWidget.button_widget import ButtonForSectionWidget
from ifcApp.ifc.globalParam.global_param import GlobalParam
from ifcApp.ifc.groupboxWidget.groupbox_widget import GroupBoxWidget
from ifcApp.ifc.ifc_model import IfcModel, traversing_directories
from ifcApp.ifc.modbus.asyncMethods.async_ilya import AsyncThread
from ifcApp.ifc.modbus.asyncMethods.async_ilya import WorkerSignals
from ifcApp.ifc.modbus.modbus_connect_vm import ModbusConnectViewModel
from ifcApp.ifc.urod import Urod
from ifcApp.ifc.users.users_in_ifc_vm import UserInIfc
from ifcApp.settingsSensors.settings_sensors_vm import SettingsSensors


UI_ifc = "resources\\view\\ifc\\ifc version1.ui"

class IfcViewModel2(QtWidgets.QMainWindow):
    def __init__(self, load, database):
        super().__init__()
        self.database = database
        uic.loadUi(resource_path(UI_ifc), self)
        self.timer = QTimer()
        self.timer.timeout.connect(self.show_time)
        self.timer.start(1000)
        print("Load ifc")
        self.data_sensors = DataSensorsMainWindow(self.database)
        self.global_param = GlobalParam(self.database)
        self.user_ifc = UserInIfc(self.database)
        self.model = IfcModel()
        self.count_shield = CountShieldVM(self.database)
        self.notification_errors = NotificationErrors()
        self.AsyncTcpReciver = AsyncThread()

        self.list_urods=[]
        self.button_list_signals = []
        self.list_groupbox = []
        self.layout_list_in_groupbox = []
        self.list_all_crep = dict()

        self.list_action_show = {"v_action": self.v_action,
                                 "zaz_action": self.zaz_action,
                                 "pressure_stand1_action": self.pressure_stand1_action,
                                 "pressure_stand2_action": self.pressure_stand2_action,
                                 "shield_UGZ_action": self.shield_UGZ_action,
                                 "shield_UGZ_angle_action": self.shield_UGZ_angle_action,
                                 "shield_UGZ_shifting_action": self.shield_UGZ_shifting_action,
                                 "shield_UGZ_pressure_action": self.shield_UGZ_pressure_action,
                                 "shield_UGZ_3rasp_abbr_action": self.shield_UGZ_3rasp_abbr_action,
                                 "top_drawer_action": self.top_drawer_action,
                                 "top_drawer_shifting_action": self.top_drawer_shifting_action,
                                 "visor_action": self.visor_action,
                                 "state_overlap_action": self.state_overlap_action,
                                 "height_section_action1": self.height_section_action1,
                                 "height_section_action2": self.height_section_action2}

        for setting, object in self.list_action_show.items():
            object.triggered.connect(self.checked_action_for_sensors)
        self.show_name_action.triggered.connect(self.show_name_sensors)
        self.change_setting_action.triggered.connect(self.show_settings_sensors)
        self.data_sensors_pushButton.clicked.connect(lambda: self.data_sensors.show())
        self.notification_errors_pushButton.clicked.connect(lambda: self.show_window(self.notification_errors))
        self.menu_pushButton.clicked.connect(lambda: self.global_param.show())
        self.global_param.save_pushButton.clicked.connect(self.update_global_param)
        self.user_pushbutton.clicked.connect(lambda: self.user_ifc.show())
        self.exit_pushButton.clicked.connect(self.exit_program)
        self.quantity_shield_pushButton.clicked.connect(self.show_count)
        self.connect_modbus_pushButton.clicked.connect(self.show_modbus_ui)


        # FOR create Groupbox and Show BATON
        self.create_groupbox()
        self.load_auth = load
        self.make_buttons()
        self.raise_labels()
        self.AsyncTcpReciver.play_pause = True




        self.loadSettings(self.load_auth.id_user)
        self.checked_action_for_sensors()
        # self.database.check_color_in_database()

        self.model.start()
        self.AsyncTcpReciver.start()

    def make_buttons(self):
        self.cleaner_layouts(self.layout_list_in_groupbox)
        pizda = self.database.get_global_params()
        query_global_param = self.database.get_setting_sensors(self.load_auth.id_user)
        self.count_sh = self.database.get_count_shield()
        for elem in range(self.count_sh):
            self.create_button_layout_list(elem,pizda,query_global_param)
            self.setting_async_receiver()



    def setting_async_receiver(self):
        py_signal = WorkerSignals()
        py_signal.result.connect(self.list_urods[-1].setText)
        self.AsyncTcpReciver.all_signal.append(py_signal)

    def create_button_layout_list(self,  elem,pizda,query_global_param):
        self.button_list_signals.append([])
        for index, row in enumerate(pizda):
            list_color_in_button = [query_global_param[index].color_normal,
                                    query_global_param[index].color_reduced,
                                    query_global_param[index].color_increased]
            self.btn = ButtonForSectionWidget(elem + 1, list_color_in_button)
            self.btn.value = int(row.max_value)
            self.btn.min_normal=int(row.from_normal_value)
            self.btn.max_normal=int(row.to_normal_value)
            self.btn.entry.connect(self.btn.update_color_and_height)
            self.button_list_signals[elem].append(self.btn)
            # self.button_list_signals.append(self.btn)


            if elem % 2 == 0:
                self.btn.setStyleSheet(" background-color: #e9e9e9;")
            else:
                self.btn.setStyleSheet("background-color: #a0a0a0;")
            self.btn.setMaximumWidth(int(self.btn.width() / (0.35 * self.count_sh)))
            self.btn.setToolTip(f"Крепь № {elem + 1}, Датчик {self.groupbox.list_name_for_groupbox[index]}")
            self.btn.clicked.connect(lambda :self.createCrepWin(elem+1))
            self.layout_list_in_groupbox[index].addWidget(self.btn)
        self.list_urods.append(Urod(self.button_list_signals[elem],self.data_sensors,self.list_all_crep,elem))

    def createCrepWin(self,num):
        if self.list_all_crep.get(num):
            # self.list_all_crep.
            self.show_window(self.list_all_crep[num])
            # if not self.list_all_crep[num].isVisible():
                # self.list_all_crep[num].setVisible()
        else:
            self.list_all_crep[num]= CrepViewModel(num, self.database)
            self.list_all_crep[num].stop_signal.connect(lambda:self.list_all_crep.pop(num))

            # кнопка Вправо на 1
            self.list_all_crep[num].right_pushButton.clicked.connect(
                lambda: self.otkritka(1 if num == self.count_sh else num + 1,num))

            # кнопка ВЛЕВО на 1
            self.list_all_crep[num].left_pushButton.clicked.connect(
                lambda: self.otkritka(self.count_sh if num == 1 else num-1,num))

            # Кнопка ВПРАВО на 10
            self.list_all_crep[num].right_x10_pushButton.clicked.connect(
                lambda: self.otkritka(self.count_sh if num >= self.count_sh - 10 else num + 10,num))

            # Кнопка ВЛЕВО на 10
            self.list_all_crep[num].left_x10_pushButton.clicked.connect(
                lambda: self.otkritka(1 if num <= 11 else num - 10,num))

            # КНОПКА ВНАЧАЛО
            self.list_all_crep[num].start_pushButton.clicked.connect(
                lambda: self.otkritka(1,num))

            # КНОПКА ВКОНЕЦ
            self.list_all_crep[num].finish_pushButton.clicked.connect(
                lambda: self.otkritka(self.count_sh,num))






            print(len(self.list_all_crep),"   ",self.list_all_crep.items())


    def otkritka(self,target,num):

        self.list_all_crep[num].hide()
        self.list_all_crep.pop(num)
        self.createCrepWin(target)


    @QtCore.pyqtSlot(list,int)
    def udochka(self,listick,kek):
        for num in range(len(listick)):
            # self.button_list_signals[kek][num].emit(listick[num])
            # self.button_list_signals[kek*15+num].update_color_and_height(listick[num])
            # self.button_list_signals[kek][num].update_color_and_height(listick[num])
            self.data_sensors.tableWidget.setItem(num, kek, QTableWidgetItem(str(listick[num])))
        #
        if self.list_all_crep.get(kek+1):
            self.list_all_crep[kek+1].setText_lineEdit_sensors(listick)


    def raise_labels(self):
        for elem in range(len(self.global_param.list_groupbox)):
            self.global_param.list_groupbox[elem].name_label.raise_()


    def create_groupbox(self):
        # self.layout_list_in_groupbox.clear()
        self.global_param.list_groupbox.clear()
        for index, row in enumerate(self.database.get_global_params()):
            self.groupbox = GroupBoxWidget()
            self.layout_groupbox.addWidget(self.groupbox)
            self.global_param.list_groupbox.append(self.groupbox)
            self.global_param.list_groupbox[index].min_value.setText(str(row.min_value))
            self.global_param.list_groupbox[index].max_value.setText(str(row.max_value))
            self.layout_list_in_groupbox.append(self.groupbox.layoutWidget)
            self.groupbox.name_label.setText(row.name)
            self.groupbox.icon_label.setPixmap(QtGui.QPixmap(self.groupbox.icon_paths[index]))


    def remaster_creps(self):
        self.count_shield.get_and_save_number_from_lineedit()
        self.AsyncTcpReciver.play_pause = False
        self.AsyncTcpReciver.all_signal.clear()
        self.AsyncTcpReciver.brokeSignalsId.clear()
        self.close_crep()
        self.make_buttons()
        self.AsyncTcpReciver.play_pause = True

    def close_crep(self):
        for value in self.list_all_crep.values():
            value.hide()
        print(len(self.list_all_crep))

    def cleaner_layouts(self, layout_list):
        self.list_all_crep.clear()
        self.list_urods.clear()
        self.button_list_signals.clear()
        for layout in layout_list:
            for i in reversed(range(layout.count())):
                layout.itemAt(i).widget().deleteLater()

    def exit_program(self):
        self.thread.running = False
        QApplication.instance().quit()
    def show_window(self, Win):
        if Win.isVisible():
            Win.hide()
        else:
            Win.show()

    def show_count(self):
        self.count_shield.OK_pushButton.clicked.connect(self.remaster_creps)
        self.count_shield.show()

    def show_modbus_ui(self):
        self.modbus_connect = ModbusConnectViewModel(self.database)
        self.modbus_connect.show()
    def show_settings_sensors(self):
        user_id = self.load_auth.id_user
        self.settings_sensors = SettingsSensors(user_id, self.database)
        if self.change_setting_action.isChecked():
            self.settings_sensors.show()
            self.change_setting_action.setChecked(False)

        else:
            self.settings_sensors.close()

    def show_name_sensors(self):
        if self.show_name_action.isChecked():
            for i, row in enumerate(self.global_param.list_groupbox):
                row.name_label.show()
        else:
            for i, row in enumerate(self.global_param.list_groupbox):
                row.name_label.close()


    def checked_action_for_sensors(self):
        for action, object in enumerate(self.list_action_show.values()):
            if object.isChecked():
                self.global_param.list_groupbox[action].show()
            else:
                self.global_param.list_groupbox[action].close()

    def update_global_param(self):
        self.global_param.save_on_clicked_information()
        self.remaster_creps()

    def show_time(self):
        time = QDateTime.currentDateTime()
        timeDisplay = time.toString('dd.MM.yyyy HH:mm:ss')
        self.date_time.setText(timeDisplay)

    def saveSettings(self):
        print(self.settings.fileName())
        for name, action in self.list_action_show.items():
            self.settings.setValue(name, action.isChecked())

    def loadSettings(self, user_id):
        if user_id:
            settings_path = f"settingsForUsers/settings_{user_id}.ini"
            self.settings = QSettings(settings_path, QSettings.Format.IniFormat)
            for name, action in self.list_action_show.items():
                state = self.settings.value(name, defaultValue=False, type=bool)
                action.setChecked(state)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.AsyncTcpReciver.running = False
        self.AsyncTcpReciver.all_signal.clear()
        self.close_crep()
        self.model.running = False
        self.AsyncTcpReciver.join()
        self.model.join()

        traversing_directories()
        threads = threading.enumerate()
        print("Active threads:", threads)
        self.load_auth.load_ui_auth()
        self.load_auth.show()
        self.close()
        self.saveSettings()

    def role_for_miner(self):
        self.menu_pushButton.setEnabled(False)
        # for action in self.list_action_show.values():
        #     action.setEnabled(False)