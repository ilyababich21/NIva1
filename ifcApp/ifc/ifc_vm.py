from PyQt6 import uic, QtWidgets, QtGui
from PyQt6.QtCore import QTimer, QDateTime, QThread
from PyQt6.QtWidgets import QApplication, QTableWidgetItem

from ifcApp.countShield.count_shield_vm import CountShieldVM
from ifcApp.crep.crep_vm import CrepViewModel
from ifcApp.dataSensors.data_sensors_vm import DataSensorsMainWindow
from ifcApp.dataSensors.settings_data_sensors_vm import SettingsSensors
from ifcApp.errors.notification_errors import NotificationErrors
from ifcApp.ifc.asyncMethods.async_ilya import AsyncThread
from ifcApp.ifc.asyncMethods.async_receiver import WorkerSignals
from ifcApp.ifc.buttonWidget.button_widget import ButtonForSectionWidget
from ifcApp.ifc.groupboxWidget.groupbox_widget import GroupBoxWidget
from ifcApp.ifc.ifc_model import IfcModel
from ifcApp.ifc.globalParam.global_param import GlobalParam
from ifcApp.ifc.users.users_in_ifc_vm import UserInIfc
from ifcApp.ifc.ifc_model import traversing_directories

UI_ifc = "resources/view/ifc/ifc version1.ui"


class User:
    def __init__(self, log):
        super().__init__()
        self.login = log


class IfcViewModel(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.timer = QTimer()
        self.timer.timeout.connect(self.show_time)
        self.timer.start(1000)
        print("Load ifc")
        self.settings_sensors = SettingsSensors()
        self.data_sensors = DataSensorsMainWindow()
        self.global_param = GlobalParam()
        self.user_ifc = UserInIfc()
        self.thread = QThread()
        self.model = IfcModel()
        self.count_shield = CountShieldVM()
        self.notification_errors = NotificationErrors()
        self.AsyncTcpReciver = AsyncThread()

        uic.loadUi(UI_ifc, self)

        self.list_groupbox = []
        self.layout_list_in_groupbox = []
        self.list_all_crep = []

        self.AsyncTcpReciver.moveToThread(self.thread)
        self.thread.started.connect(self.AsyncTcpReciver.run)
        self.create_groupbox(self.layout_groupbox)
        self.show_button()
        self.thread.start()
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
        self.menu_pushButton.clicked.connect(lambda: self.global_param.show())
        self.global_param.save_pushButton.clicked.connect(self.update_global_param)
        self.user_pushbutton.clicked.connect(lambda: self.user_ifc.show())
        self.exit_pushButton.clicked.connect(self.exit_program)
        self.quantity_shield_pushButton.clicked.connect(self.show_count)
        self.driver_pushButton.clicked.connect(lambda: print("Привет!"))

    def exit_program(self):
        self.pan_ui.add_user_in_layout( User("ig"))
        # self.thread.running = False
        # QApplication.instance().quit()

    def show_count(self):
        self.count_shield.OK_pushButton.clicked.connect(self.remaster_creps)
        self.count_shield.show()

    def create_groupbox(self, layout):
        self.global_param.list_groupbox.clear()
        for index, row in enumerate(self.model.get_global_param()):
            self.groupbox = GroupBoxWidget()
            layout.addWidget(self.groupbox)
            self.global_param.list_groupbox.append(self.groupbox)
            self.global_param.list_groupbox[index].min_value.setText(f"{row.min_value}")
            self.global_param.list_groupbox[index].max_value.setText(f"{row.max_value}")
            self.layout_list_in_groupbox.append(self.groupbox.layoutWidget)
            self.groupbox.name_label.setText(self.groupbox.list_name_for_groupbox[index])
            self.groupbox.icon_label.setPixmap(QtGui.QPixmap(self.groupbox.icon_paths[index]))

    def show_button(self):
        self.make_buttons(self.layout_list_in_groupbox)
        self.AsyncTcpReciver.play_pause = True

        for elem in range(len(self.global_param.list_groupbox)):
            self.global_param.list_groupbox[elem].name_label.raise_()

    def make_buttons(self, layout_list):
        self.cleaner_layouts(layout_list)
        for elem in range(self.count_shield.model.get_count_shield()):
            self.list_all_crep.append(CrepViewModel(elem + 1))
            self.setting_async_receiver()
            self.create_button_layout_list(layout_list, elem)

    def cleaner_layouts(self, layout_list):
        self.list_all_crep.clear()
        for layout in layout_list:
            for i in reversed(range(layout.count())):
                layout.itemAt(i).widget().deleteLater()

    def setting_async_receiver(self):
        py_signal = WorkerSignals()
        py_signal.result.connect(self.list_all_crep[-1].setText_lineEdit_sensors)
        self.AsyncTcpReciver.all_signal.append(py_signal)

    def create_button_layout_list(self, layout_list, elem):
        for index, row in enumerate(self.model.get_global_param()):
            self.btn = ButtonForSectionWidget(elem + 1)
            self.btn.value = int(row.max_value)
            self.list_all_crep[-1].list_sensors_lineEdit[index].textChanged.connect(
                lambda checked, lt=index, b=self.btn, g=self.list_all_crep[-1],
                       from_normal_value=int(row.from_normal_value),
                       to_normal_value=int(row.to_normal_value):
                b.update_color_and_height(
                    g.show_sensor_data(g.list_sensors_lineEdit[lt]), self.notification_errors.textEdit,
                    from_normal_value, to_normal_value, self.groupbox.list_name_for_groupbox[lt], elem + 1,
                    self.notification_errors_pushButton))

            self.list_all_crep[-1].list_sensors_lineEdit[index].textChanged.connect(
                lambda checked, e=elem, i=index, g=self.list_all_crep[-1]:
                self.data_sensors.all_values.setItem(i, e, QTableWidgetItem(
                    g.show_sensor_data(g.list_sensors_lineEdit[i]))))

            if len(self.list_all_crep) % 2 == 0:
                self.btn.setStyleSheet(" background-color: #e9e9e9;")
            else:
                self.btn.setStyleSheet("background-color: #a0a0a0;")
            self.btn.setMaximumWidth(int(self.btn.width() / (0.35 * self.count_shield.model.get_count_shield())))
            self.btn.setToolTip(f"Крепь № {elem + 1}, Датчик {self.groupbox.list_name_for_groupbox[index]}")
            self.btn.clicked.connect(lambda current_crep=self.list_all_crep[-1]: self.show_window_crep(current_crep))
            layout_list[index].addWidget(self.btn)
        self.working_with_button_crep(elem)

    def working_with_button_crep(self, elem):
        self.list_all_crep[-1].right_pushButton.clicked.connect(
            lambda: self.open_next_crep(self.list_all_crep[elem if elem == len(self.list_all_crep) - 1 else elem + 1]))
        self.list_all_crep[-1].left_pushButton.clicked.connect(
            lambda: self.open_next_crep(
                self.list_all_crep[len(self.list_all_crep) - 2 if elem == len(self.list_all_crep) - 1 else elem - 1]))
        self.list_all_crep[-1].right_x10_pushButton.clicked.connect(
            lambda: self.open_next_crep(self.list_all_crep[elem if elem == len(self.list_all_crep) - 1 else elem + 10]))
        self.list_all_crep[-1].left_x10_pushButton.clicked.connect(
            lambda: self.open_next_crep(self.list_all_crep[elem if elem == len(self.list_all_crep) - 1 else elem - 10]))
        self.list_all_crep[-1].start_pushButton.clicked.connect(
            lambda: self.open_next_crep(self.list_all_crep[0]))
        self.list_all_crep[-1].finish_pushButton.clicked.connect(
            lambda: self.open_next_crep(self.list_all_crep[-1]))

    def open_next_crep(self, elem):
        for i in range(len(self.list_all_crep)):
            self.list_all_crep[i].close()
        self.show_window_crep(elem)

    def remaster_creps(self):
        self.count_shield.get_and_save_number_from_lineedit()
        self.AsyncTcpReciver.play_pause = False
        self.AsyncTcpReciver.all_signal.clear()
        self.AsyncTcpReciver.brokeSignalsId.clear()
        self.show_button()

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
            for i, row in enumerate(self.global_param.list_groupbox):
                row.name_label.show()
        else:
            for i, row in enumerate(self.global_param.list_groupbox):
                row.name_label.close()

    def checked_action_for_sensors(self):
        for action, _ in enumerate(self.list_action_show):
            if self.list_action_show[action].isChecked():
                self.global_param.list_groupbox[action].show()
            else:
                self.global_param.list_groupbox[action].close()

    def show_time(self):
        time = QDateTime.currentDateTime()
        timeDisplay = time.toString('dd.MM.yyyy HH:mm:ss')
        self.date_time.setText(timeDisplay)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.thread.running = False
        self.AsyncTcpReciver.play_pause = False
        self.AsyncTcpReciver.client.close()
        traversing_directories()
        self.close()

    def update_global_param(self):
        self.global_param.save_on_clicked_information()
        self.remaster_creps()

    def role_for_miner(self):
        self.menu_pushButton.setEnabled(False)
        for action in self.list_action_show:
            action.setEnabled(False)
