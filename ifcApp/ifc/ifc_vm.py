from PyQt6 import uic, QtWidgets, QtCore, QtGui
from PyQt6.QtCore import QTimer, QDateTime

from ifcApp.crep.crep_vm import CrepViewModel
from ifcApp.dataSensors.data_sensors_vm import DataSensorsMainWindow
from ifcApp.dataSensors.settings_data_sensors_vm import SettingsSensors
from ifcApp.ifc.AsyncMethods.AsyncReciver import AsyncTcpReciver, WorkerSignals
from ifcApp.ifc.ButtonWidgets.ButtonForSecPre import ButtonForPressureSection
from ifcApp.ifc.GroupBox.groupbox_widget import GroupBox
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

        self.list_groupbox = []
        self.layout_list_in_groupbox = []
        self.list_name_layout = []

        self.list_all_crep = []
        self.thread = QtCore.QThread()
        self.AsyncTcpReciver = AsyncTcpReciver()
        self.AsyncTcpReciver.moveToThread(self.thread)
        self.thread.started.connect(self.AsyncTcpReciver.run)
        self.make_groupbox(self.layout_groupbox)
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

        self.Ok_button.clicked.connect(self.remaster_creps)
        self.menu_pushButton.clicked.connect(lambda: self.main_menu.show())

    def make_groupbox(self, layout):

        list_name_for_groupbox = ["ЦП", "Зазор цлиндра передвижки", "Давление в стойке 1",
                                  "Давление в стойке 2", "Щит УГЗ", "Щит Угз Угол",
                                  "Щит УГЗ ход", "Щит угз давление",
                                  "9", "10", "11", "12", "13", "14", "15", ]
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
                                  "image/img tools/cantilever_state.png", "image/img tools/shield_height_1.png",
                                  "image/img tools/shield_height_2.png"

                                  ]
        for elem in range(15):
            self.groupbox = GroupBox()
            layout.addWidget(self.groupbox)
            self.list_groupbox.append(self.groupbox)
            self.list_groupbox[elem].min_value.setText(
                f"{self.global_param.query_in_global_param_table[elem].min_value}")
            self.list_groupbox[elem].max_value.setText(
                f"{self.global_param.query_in_global_param_table[elem].max_value}")
            self.layout_list_in_groupbox.append(self.groupbox.layoutWidget)
            self.groupbox.name_label.setText(list_name_for_groupbox[elem])
            self.list_name_layout.append(self.groupbox.name_label)
            self.groupbox.icon_label.setPixmap(QtGui.QPixmap(list_icon_for_groupbox[elem]))

    def create_button_layout_list(self, layout_list, elem):
        for one_layout in range(len(layout_list)):
            self.btn = ButtonForPressureSection(elem + 1)
            self.btn.coefficient = int(self.btn.height()) / int(self.global_param.list_max_value[one_layout])
            print(int(self.btn.height()))
            self.list_all_crep[-1].list_sensors_lineEdit[one_layout].textChanged.connect(
                lambda checked, lt=one_layout, b=self.btn, g=self.list_all_crep[-1]: b.change_rectangle_size(
                    g.show_sensor1_data(g.list_sensors_lineEdit[lt])))
            self.list_all_crep[-1].list_sensors_lineEdit[one_layout].textChanged.connect(
                lambda ch, b=self.btn: b.change_color())
            if elem % 2 == 0:
                self.btn.setStyleSheet(" background-color: #e9e9e9;")
            else:
                self.btn.setStyleSheet("background-color: #a0a0a0;")
            self.btn.setMaximumWidth(int(self.btn.width() / (0.35 * int(self.section_max_lineEdit.text()))))
            self.btn.setToolTip(f"Hello i am button number {elem + 1},{one_layout + 1}")
            self.btn.setWhatsThis("Whatafuck")
            self.btn.clicked.connect(lambda b=self.list_all_crep[-1]: self.show_window_crep(b))
            layout_list[one_layout].addWidget(self.btn)

    def make_buttons(self, layout_list):
        self.cleaner_layouts(layout_list)
        print("heeee")
        for elem in range(int(self.section_max_lineEdit.text())):
            self.list_all_crep.append(CrepViewModel(elem + 1))
            self.setting_async_reciver()
            self.create_button_layout_list(layout_list, elem)

    def show_button(self):
        self.make_buttons(self.layout_list_in_groupbox)
        for elem in range(len(self.list_groupbox)):
            self.list_groupbox[elem].name_label.raise_()

    def setting_async_reciver(self):

        sigOnal1 = WorkerSignals()
        sigOnal1.result.connect(self.list_all_crep[-1].setText_lineEdit_sensors)
        self.AsyncTcpReciver.all_signal.append(sigOnal1)

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

    def remaster_creps(self):
        self.AsyncTcpReciver.all_signal.clear()
        self.show_button()
