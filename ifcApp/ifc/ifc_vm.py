from PyQt6 import uic, QtWidgets, QtCore
from PyQt6.QtCore import QTimer, QDateTime

from ifcApp.crep.crep_vm import CrepViewModel
from ifcApp.dataSensors.data_sensors_vm import DataSensorsMainWindow
from ifcApp.dataSensors.settings_data_sensors_vm import SettingsSensors
from ifcApp.ifc.AsyncMethods.AsyncReciver import AsyncTcpReciver, WorkerSignals
from ifcApp.ifc.ButtonWidgets.ButtonForSecPre import ButtonForPressureSection
from ifcApp.ifc.mainMenu.global_param import GlobalParam
from ifcApp.ifc.mainMenu.main_menu_vm import MainMenu

UI_ifc = "view/ifc/ifc version1.ui"


class IfcViewModel(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.timer = QTimer()

        self.timer.timeout.connect(self.show_time)
        self.timer.start(1000)
        self.settings_sensors = SettingsSensors()
        self.data_sensors = DataSensorsMainWindow()
        self.global_param = GlobalParam()
        self.main_menu = MainMenu()
        uic.loadUi(UI_ifc, self)
        self.list_all_crep = []
        self.thread = QtCore.QThread()
        self.AsyncTcpReciver = AsyncTcpReciver()
        self.AsyncTcpReciver.moveToThread(self.thread)
        self.thread.started.connect(self.AsyncTcpReciver.run)

        self.show_button()
        self.thread.start()

        self.list_action_show = [self.v_action, self.zaz_action, self.pressure_stand1_action,
                                 self.pressure_stand2_action, self.shield_UGZ_action,
                                 self.shield_UGZ_sensor_approximation_action, self.height_section_action3,
                                 self.shield_UGZ_angle_action, self.shield_UGZ_shifting_action,
                                 self.shield_UGZ_pressure_action, self.shield_UGZ_3rasp_abbr_action,
                                 self.top_drawer_action, self.top_drawer_shifting_action,
                                 self.visor_action, self.state_overlap_action,
                                 self.height_section_action1, self.height_section_action2]

        for action in self.list_action_show:
            action.triggered.connect(self.checked_action_for_sensors)

        self.show_name_action.triggered.connect(lambda: self.show_name_sensors(
            [self.CP_label, self.zaz_label, self.pressure_st1_label, self.pressure_st2_label,
             self.shield_UGZ_label, self.shield_UGZ_sensor_label,
             self.shield_UGZ_angle_label, self.shield_UGZ_hod_label, self.shield_UGZ_pressure_label,
             self.shield_UGZ_thrust_label, self.extension_top_label, self.extension_top_progress_label,
             self.koz_label, self.shifting_state_label, self.height_section1_label,
             self.height_section2_label, self.height_section3_label]))

        self.change_setting_action.triggered.connect(self.show_settings_sensors)

        self.data_sensors_pushButton.clicked.connect(lambda: self.data_sensors.show())

        self.Ok_button.clicked.connect(self.remaster_creps)
        self.menu_pushButton.clicked.connect(lambda: self.main_menu.show())

        self.list_label_min_values = [self.min_value_position_label, self.min_value_clearance_label,
                                      self.min_value_pressure1_label, self.min_value_pressure2_label,
                                      self.min_value_shield_label, self.min_value_shield_UGZ_label,
                                      self.min_value_shield_UGZ_angle_label, self.min_value_shield_hod_label,
                                      self.min_value_shield_UGZ_pressure_label, self.min_value_shield_UGZ_thrust_label,
                                      self.min_value_extension_top_label, self.min_value_extension_top_progress_label,
                                      self.min_value_koz_label, self.min_value_shifting_state_label,
                                      self.min_value_height_section1_label]
        row_in_query = 0
        for min_value_label in range(len(self.list_label_min_values)):
            self.list_label_min_values[min_value_label].setText(
                f"{self.global_param.query_in_global_param_table[row_in_query].min_value}")
            row_in_query += 1

        self.list_label_max_values = [self.max_value_pasition_label, self.max_value_clearance_label,
                                      self.max_value_pressure1_label, self.max_value_pressure2_label,
                                      self.max_value_shield_label, self.max_value_shield_UGZ_label,
                                      self.max_value_shield_UGZ_angle_label, self.max_value_shield_hod_label,
                                      self.max_value_shield_UGZ_pressure_label, self.max_value_shield_UGZ_thrust_label,
                                      self.max_value_extension_top_label, self.max_value_extension_top_progress_label,
                                      self.max_value_koz_label, self.max_value_shifting_state_label,
                                      self.max_value_height_section1_label]
        row_in_query = 0
        for max_value_label in range(len(self.list_label_max_values)):
            self.list_label_max_values[max_value_label].setText(
                f"{self.global_param.query_in_global_param_table[row_in_query].max_value}")
            row_in_query += 1

    def remaster_creps(self):
        self.AsyncTcpReciver.all_signal.clear()

        self.show_button()

    def show_button(self):
        self.make_buttons(
            [
                self.layout_100, self.layout_200, self.layout_300, self.layout_400, self.layout_500, self.layout_600,
                self.layout_700, self.layout_800, self.layout_900, self.layout_1000, self.layout_1100, self.layout_1200,
                self.layout_1300,
                self.layout_1400, self.layout_1500
                # , self.layout_1600, self.layout_1700
            ])

    def make_buttons(self, layout_list):
        self.cleaner_layouts(layout_list)
        print("heeee")
        for elem in range(int(self.section_max_lineEdit.text())):
            self.list_all_crep.append(CrepViewModel(elem + 1))
            self.setting_async_reciver()
            self.create_button_layout_list(layout_list, elem)

    def setting_async_reciver(self):
        sigOnal1 = WorkerSignals()
        sigOnal1.result.connect(self.list_all_crep[-1].setText1)
        self.AsyncTcpReciver.all_signal.append(sigOnal1)
        # print(self.AsyncTcpReciver.all_signal)

    def create_button_layout_list(self, layout_list, elem):

        for one_layout in range(len(layout_list)):
            btn = ButtonForPressureSection(elem + 1)
            btn.coefficient = btn.height() / int(self.global_param.list_max_value[one_layout])
            self.list_all_crep[-1].list_sensors_lineEdit[one_layout].textChanged.connect(
                lambda checked, lt=one_layout, b=btn, g=self.list_all_crep[-1]: b.change_rectangle_size(
                    g.show_sensor1_data(g.list_sensors_lineEdit[lt])))
            self.list_all_crep[-1].list_sensors_lineEdit[one_layout].textChanged.connect(
                lambda ch, b=btn: b.change_color())

            if elem % 2 == 0:
                btn.setStyleSheet(" background-color: #e9e9e9;")
            else:
                btn.setStyleSheet("background-color: #a0a0a0;")
            # btn.change_color()
            btn.setMaximumWidth(int(btn.width() / (0.35 * int(self.section_max_lineEdit.text()))))
            btn.setToolTip(f"Hello i am button number {elem + 1},{one_layout + 1}")
            btn.setWhatsThis("Whatafuck")
            btn.clicked.connect(lambda b=self.list_all_crep[-1]: self.show_window_crep(b))
            layout_list[one_layout].addWidget(btn)
            # print(btn.size())
            # layout.addWidget(btn)
            # print(btn.size())

    def cleaner_layouts(self, layout_list):
        self.list_all_crep.clear()

        for layout in layout_list:
            for i in reversed(range(layout.count())):
                layout.itemAt(i).widget().deleteLater()

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

    def checked_action_for_sensors(self):
        list_action_show = [self.v_action, self.zaz_action, self.pressure_stand1_action,
                            self.pressure_stand2_action, self.shield_UGZ_action,
                            self.shield_UGZ_angle_action, self.shield_UGZ_shifting_action,
                            self.shield_UGZ_pressure_action, self.shield_UGZ_3rasp_abbr_action,
                            self.top_drawer_action, self.top_drawer_shifting_action,
                            self.visor_action, self.state_overlap_action,
                            self.height_section_action1, self.height_section_action2,
                            self.height_section_action3, self.shield_UGZ_sensor_approximation_action]

        list_action_group_box = [self.groupBox1, self.groupBox2,
                                 self.groupBox3, self.groupBox4,
                                 self.groupBox5, self.groupBox6,
                                 self.groupBox7, self.groupBox8,
                                 self.groupBox9, self.groupBox10,
                                 self.groupBox11, self.groupBox12,
                                 self.groupBox13, self.groupBox14,
                                 self.groupBox15, self.groupBox16, self.groupBox17]

        for action in range(len(list_action_show)):
            if list_action_show[action].isChecked():
                list_action_group_box[action].show()
            else:
                list_action_group_box[action].hide()

    def show_time(self):
        time = QDateTime.currentDateTime()
        timeDisplay = time.toString('dd.MM.yyyy HH:mm:ss')
        self.date_time.setText(timeDisplay)
