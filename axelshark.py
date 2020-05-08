# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from threading import Thread, Event
from time import sleep
import psutil, logging, core, pickle

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1094, 771)
        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Filters = QtWidgets.QTextEdit(self.centralwidget)
        self.Filters.setGeometry(QtCore.QRect(20, 50, 831, 31))
        self.Filters.setObjectName("Filters")
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(980, 50, 88, 31))
        self.searchButton.setObjectName("searchButton")
        self.Packets = QtWidgets.QTableWidget(self.centralwidget)
        self.Packets.setGeometry(QtCore.QRect(20, 90, 1051, 251))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Packets.sizePolicy().hasHeightForWidth())
        self.Packets.setSizePolicy(sizePolicy)
        self.Packets.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Packets.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Packets.setLineWidth(1)
        self.Packets.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.Packets.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.Packets.setAlternatingRowColors(False)
        self.Packets.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.Packets.setRowCount(0)
        self.Packets.setColumnCount(6)
        self.Packets.setObjectName("Packets")
        item = QtWidgets.QTableWidgetItem()
        self.Packets.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Packets.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Packets.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Packets.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Packets.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Packets.setHorizontalHeaderItem(5, item)
        self.Packets.horizontalHeader().setCascadingSectionResizes(False)
        self.Packets.horizontalHeader().setDefaultSectionSize(160)
        self.Packets.horizontalHeader().setMinimumSectionSize(23)
        self.Packets.horizontalHeader().setSortIndicatorShown(False)
        self.Packets.horizontalHeader().setStretchLastSection(True)
        self.Packets.verticalHeader().setStretchLastSection(True)
        self.packetInfo = QtWidgets.QTreeWidget(self.centralwidget)
        self.packetInfo.setGeometry(QtCore.QRect(20, 360, 1051, 191))
        self.packetInfo.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.packetInfo.setAlternatingRowColors(False)
        self.packetInfo.setObjectName("packetInfo")
        item_0 = QtWidgets.QTreeWidgetItem(self.packetInfo)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.packetInfo)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.packetInfo)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.packetHex = QtWidgets.QTextBrowser(self.centralwidget)
        self.packetHex.setGeometry(QtCore.QRect(20, 570, 1051, 131))
        self.packetHex.setObjectName("packetHex")
        self.packetHex.setFont(font)
        self.interfaceLabel = QtWidgets.QLabel(self.centralwidget)
        self.interfaceLabel.setGeometry(QtCore.QRect(20, 10, 131, 31))
        font.setPointSize(12)
        self.interfaceLabel.setFont(font)
        self.interfaceLabel.setObjectName("interfaceLabel")
        self.interfacesList = QtWidgets.QComboBox(self.centralwidget)
        self.interfacesList.setGeometry(QtCore.QRect(160, 10, 801, 31))
        self.interfacesList.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.interfacesList.setAutoFillBackground(False)
        self.interfacesList.setObjectName("interfacesList")
        interfaces = psutil.net_if_addrs()
        interfaces = list(interfaces.keys())
        self.interfacesList.addItems(interfaces)
        self.captureButton = QtWidgets.QPushButton(self.centralwidget)
        self.captureButton.setGeometry(QtCore.QRect(980, 10, 88, 31))
        self.captureButton.setObjectName("captureButton")
        self.clearFiltersButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearFiltersButton.setGeometry(QtCore.QRect(870, 50, 91, 31))
        self.clearFiltersButton.setObjectName("clearFiltersButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1094, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuCapture = QtWidgets.QMenu(self.menubar)
        self.menuCapture.setObjectName("menuCapture")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuFilters = QtWidgets.QMenu(self.menubar)
        self.menuFilters.setObjectName("menuFilters")
        self.menuFilter_by_type = QtWidgets.QMenu(self.menuFilters)
        self.menuFilter_by_type.setObjectName("menuFilter_by_type")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow) #
        self.actionNew.setObjectName("actionNew")      #
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionStart_Capture = QtWidgets.QAction(MainWindow)
        self.actionStart_Capture.setObjectName("actionStart_Capture")
        self.actionStop_Capture = QtWidgets.QAction(MainWindow)
        self.actionStop_Capture.setObjectName("actionStop_Capture")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionInstructions = QtWidgets.QAction(MainWindow)
        self.actionInstructions.setObjectName("actionInstructions")
        self.actionUDP = QtWidgets.QAction(MainWindow)
        self.actionUDP.setCheckable(True)
        self.actionUDP.setObjectName("actionUDP")
        self.actionTCP = QtWidgets.QAction(MainWindow)
        self.actionTCP.setCheckable(True)
        self.actionTCP.setObjectName("actionTCP")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menuCapture.addAction(self.actionStart_Capture)
        self.menuCapture.addAction(self.actionStop_Capture)
        self.menuAbout.addAction(self.actionInstructions)
        self.menuAbout.addAction(self.actionAbout)
        self.menuFilter_by_type.addAction(self.actionUDP)
        self.menuFilter_by_type.addAction(self.actionTCP)
        self.menuFilters.addAction(self.menuFilter_by_type.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuCapture.menuAction())
        self.menubar.addAction(self.menuFilters.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        logging.basicConfig(filename="sniffer.log", format='%(asctime)s %(message)s', filemode='a') 
        self.logger=logging.getLogger() 
        self.logger.setLevel(logging.DEBUG)
        self.logger.info('Interface started!')
        
        self.actionNew.triggered.connect(self.new_btn_clicked)
        self.actionOpen.triggered.connect(self.file_open)
        self.actionSave.triggered.connect(self.file_save)
        self.actionAbout.triggered.connect(self.about_btn_clicked)
        self.actionInstructions.triggered.connect(self.instructions_btn_clicked)
        self.actionExit.triggered.connect(sys.exit)
        self.actionStart_Capture.triggered.connect(self.capture_btn_clicked)
        self.actionStop_Capture.triggered.connect(self.capture_btn_clicked)
        self.captureButton.clicked.connect(self.capture_btn_clicked)
        self.clearFiltersButton.clicked.connect(self.displayData)

        self.Packets.cellClicked.connect(self.cell_clicked)
        self.searchButton.clicked.connect(self.search_btn_clicked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Axel Shark"))
        self.Filters.setPlaceholderText(_translate("MainWindow", "Filters"))
        self.searchButton.setText(_translate("MainWindow", "Apply"))
        item = self.Packets.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Time"))
        item = self.Packets.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Source"))
        item = self.Packets.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Destination"))
        item = self.Packets.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Protocol"))
        item = self.Packets.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Length"))
        item = self.Packets.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Info"))
        __sortingEnabled = self.packetInfo.isSortingEnabled()
        self.packetInfo.setSortingEnabled(False)
        self.packetInfo.topLevelItem(0).setText(0, _translate("MainWindow", "Ethernet Header"))
        self.packetInfo.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "Packet Data"))
        self.packetInfo.topLevelItem(1).setText(0, _translate("MainWindow", "IP Header"))
        self.packetInfo.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "Packet Data"))
        self.packetInfo.topLevelItem(2).setText(0, _translate("MainWindow", "Transmission Protocol Data"))
        self.packetInfo.topLevelItem(2).child(0).setText(0, _translate("MainWindow", "Packet Data"))
        self.packetInfo.setSortingEnabled(__sortingEnabled)
        self.interfaceLabel.setText(_translate("MainWindow", "Choose Interface:"))
        self.interfacesList.setStatusTip(_translate("MainWindow", "Choose Interface for packets capture"))
        self.interfacesList.setItemText(0, _translate("MainWindow", "Select Interface for Capturing Packets"))
        self.captureButton.setText(_translate("MainWindow", "Capture"))
        self.clearFiltersButton.setText(_translate("MainWindow", "Clear"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuCapture.setTitle(_translate("MainWindow", "Capture"))
        self.menuAbout.setTitle(_translate("MainWindow", "Help"))
        self.menuFilters.setTitle(_translate("MainWindow", "Filters"))
        self.menuFilter_by_type.setTitle(_translate("MainWindow", "Filter by type"))
        self.actionNew.setText(_translate("MainWindow", "New"))  #
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Saves a file"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Alt+F4"))
        self.actionStart_Capture.setText(_translate("MainWindow", "Start Capture"))
        self.actionStop_Capture.setText(_translate("MainWindow", "Stop Capture"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionInstructions.setText(_translate("MainWindow", "Documentation"))
        self.actionUDP.setText(_translate("MainWindow", "UDP"))
        self.actionTCP.setText(_translate("MainWindow", "TCP"))

    #########################################################################################################################
    ############################## Functions, Event handlers, thread and signal slot connectors #############################
    
    ## Global variables ##
    original_data = []
    current_row = 0
    
    
    def file_save(self):
        name,_ = QtWidgets.QFileDialog.getSaveFileName()
        if name:
            pickle.dump(self.original_data, open(name, "wb"))

    def file_open(self):
        name,_ = QtWidgets.QFileDialog.getOpenFileName()
        if name:
            self.original_data = pickle.load(open(name, "rb"))
            self.displayData()
    
    def new_btn_clicked(self):
        while (self.Packets.rowCount() > 0):
            self.Packets.removeRow(0)
        self.original_data = []
        self.current_row = 0
        self.packetHex.clear()
        self.packetInfo.topLevelItem(0).child(0).setText(0, "Packet Data")

    def about_btn_clicked(self):
        self.msg = QtWidgets.QMessageBox()
        self.msg.setIcon(QtWidgets.QMessageBox.Information)
        self.msg.setWindowTitle("About Developer")
        self.msg.setText("Axel Shark developed solely by yatish609@github \nThis tool is open-source for modifications under GPL-2.0 License.\nWe do not support or endorse any kind of illegal activities.")
        self.msg.exec_()

    def instructions_btn_clicked(self):
        self.msg = QtWidgets.QMessageBox()
        self.msg.setIcon(QtWidgets.QMessageBox.Information)
        self.msg.setWindowTitle("Documentation")
        self.msg.setText("Full documentation can be found at yatish609@github")
        self.msg.exec_()
    
    def cell_clicked(self,row,column):
        self.packetHex.clear()
        self.packetHex.setText(self.original_data[row][6])
        self.packetInfo.topLevelItem(0).child(0).setText(0, self.original_data[row][7])

    def search_btn_clicked(self):
        if(self.Packets.rowCount()>0):
            if(self.Filters.toPlainText()==""):
                self.msg = QtWidgets.QMessageBox()
                self.msg.setIcon(QtWidgets.QMessageBox.Critical)
                self.msg.setWindowTitle("Missing input")
                self.msg.setText("No filter entered!")
                self.msg.exec_()
            else:
                search_filter = self.Filters.toPlainText()
                row_index_list = []
                count = 0
                for i in self.original_data:
                    if search_filter in i:
                        row_index_list.append(count)
                    count = count + 1
                self.displayFilter(row_index_list,self.original_data)
        else:
            self.msg = QtWidgets.QMessageBox()
            self.msg.setIcon(QtWidgets.QMessageBox.Critical)
            self.msg.setWindowTitle("No data!")
            self.msg.setText("Start a capture to apply filters.")
            self.msg.exec_()

    def storeData(self,Data):
        self.original_data.append(Data)
        self.addRowData(Data)

    def clearTableData(self):
        while (self.Packets.rowCount() > 0):
            self.Packets.removeRow(0)

    def clearData(self):
        self.original_data = []

    def clearCurrentRows(self):
        self.current_row = 0

    def displayData(self):
        self.Filters.clear()
        if(self.Packets.rowCount()>0):
            self.clearTableData()
            self.clearCurrentRows()
        for i in self.original_data:
            self.addRowData(i)

    def displayFilter(self,FilterList,DataList):
        self.clearTableData()
        self.clearCurrentRows()
        for i in FilterList:
            self.addRowData(DataList[i])

    def addRowData(self,packetData):
        self.Packets.insertRow(self.current_row)
        column_number = 0
        for s in packetData:
            if(column_number==6):
                column_number = column_number + 1
                break
            self.Packets.setItem(self.current_row,column_number,QtWidgets.QTableWidgetItem(s))
            column_number = column_number + 1
        self.current_row = self.current_row + 1

    capture_btn_state = 'Capture'
    def capture_btn_clicked(self):
        if(self.capture_btn_state=='Capture'):
            interface_chosen = str(self.interfacesList.currentText())
            try:
                if(interface_chosen=='Select Interface for Capturing Packets'):
                    self.msg = QtWidgets.QMessageBox()
                    self.msg.setIcon(QtWidgets.QMessageBox.Critical)
                    self.msg.setWindowTitle("Interface error!")
                    self.msg.setText("Not a valid capture interface! \nPlease choose a valid interface.")
                    self.msg.exec_()
                else:
                    self.captureButton.setStyleSheet("background-color: red ; border:none")
                    self.capture_btn_state = 'Stop'
                    self.captureButton.setText("Stop")
                    self.Thread = core.SnifferThread(interface_chosen)
                    self.Thread.connection.connect(self.storeData)
                    self.Thread.start()

            except:
                self.logger.error('Wrong interface selected!')
                self.captureButton.disconnect()
        else:
            self.captureButton.setStyleSheet("")
            self.Thread.stop()
            self.captureButton.setText("Capture")
            self.capture_btn_state = 'Capture'
             

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
