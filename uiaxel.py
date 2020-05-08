# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from threading import Thread, Event
from time import sleep
import netifaces, logging, core

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1093, 758)
        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.packetInfo = QtWidgets.QTreeWidget(self.centralwidget)
        self.packetInfo.setGeometry(QtCore.QRect(10, 360, 1071, 172))
        self.packetInfo.setFrameShape(QtWidgets.QFrame.Box)
        self.packetInfo.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.packetInfo.setAlternatingRowColors(False)
        self.packetInfo.setObjectName("packetInfo")
        item_0 = QtWidgets.QTreeWidgetItem(self.packetInfo)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.packetInfo)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.packetInfo)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.packetHex = QtWidgets.QTextBrowser(self.centralwidget)
        self.packetHex.setGeometry(QtCore.QRect(10, 540, 1071, 171))
        self.packetHex.setFrameShape(QtWidgets.QFrame.Box)
        self.packetHex.setObjectName("packetHex")
        self.packetsTable = QtWidgets.QTableView(self.centralwidget)
        self.packetsTable.setGeometry(QtCore.QRect(10, 90, 1071, 261))
        self.packetsTable.setFrameShape(QtWidgets.QFrame.Box)
        self.packetsTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.packetsTable.setAlternatingRowColors(True)
        self.packetsTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.packetsTable.setObjectName("packetsTable")
        self.interfaceLabel = QtWidgets.QLabel(self.centralwidget)
        self.interfaceLabel.setGeometry(QtCore.QRect(10, 10, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.interfaceLabel.setFont(font)
        self.interfaceLabel.setObjectName("interfaceLabel")
        self.interfacesList = QtWidgets.QComboBox(self.centralwidget)
        self.interfacesList.setEnabled(True)
        self.interfacesList.setGeometry(QtCore.QRect(100, 10, 881, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.interfacesList.setFont(font)
        self.interfacesList.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.interfacesList.setAutoFillBackground(False)
        self.interfacesList.setObjectName("interfacesList")
        self.interfacesList.addItem("")
        self.captureButton = QtWidgets.QPushButton(self.centralwidget)
        self.captureButton.setGeometry(QtCore.QRect(990, 10, 91, 28))
        self.captureButton.setObjectName("captureButton")
        self.filterBox = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.filterBox.setGeometry(QtCore.QRect(10, 50, 971, 31))
        self.filterBox.setMaximumSize(QtCore.QSize(1033, 96))
        self.filterBox.setFrameShape(QtWidgets.QFrame.Box)
        self.filterBox.setObjectName("filterBox")
        self.applyButton = QtWidgets.QPushButton(self.centralwidget)
        self.applyButton.setGeometry(QtCore.QRect(990, 50, 91, 28))
        self.applyButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.applyButton.setObjectName("applyButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1093, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuCapture = QtWidgets.QMenu(self.menubar)
        self.menuCapture.setObjectName("menuCapture")
        self.menuFilters = QtWidgets.QMenu(self.menubar)
        self.menuFilters.setObjectName("menuFilters")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
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
        self.actionUDP = QtWidgets.QAction(MainWindow)
        self.actionUDP.setCheckable(True)
        self.actionUDP.setObjectName("actionUDP")
        self.actionTCP = QtWidgets.QAction(MainWindow)
        self.actionTCP.setCheckable(True)
        self.actionTCP.setObjectName("actionTCP")
        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menuCapture.addAction(self.actionStart_Capture)
        self.menuCapture.addAction(self.actionStop_Capture)
        self.menuFilters.addAction(self.actionUDP)
        self.menuFilters.addAction(self.actionTCP)
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuCapture.menuAction())
        self.menubar.addAction(self.menuFilters.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ##################################################################################################

        logging.basicConfig(filename="sniffer.log", format='%(asctime)s %(message)s', filemode='a') 
        self.logger=logging.getLogger() 
        self.logger.setLevel(logging.DEBUG)
        self.logger.info('Interface started!')
        
        self.actionNew.triggered.connect(self.new_btn_clicked)
        self.actionSave.triggered.connect(self.file_save)
        self.actionAbout.triggered.connect(self.about_btn_clicked)
        self.actionInstructions.triggered.connect(self.instructions_btn_clicked)
        self.actionExit.triggered.connect(sys.exit)
        self.actionStart_Capture.triggered.connect(self.capture_btn_clicked)
        self.actionStop_Capture.triggered.connect(self.capture_btn_clicked)
        self.captureButton.clicked.connect(self.capture_btn_clicked)
        

        self.Packets.cellClicked.connect(self.cell_clicked)
        self.searchButton.clicked.connect(self.search_btn_clicked)
        ###################################################################################################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.packetInfo.isSortingEnabled()
        self.packetInfo.setSortingEnabled(False)
        self.packetInfo.topLevelItem(0).setText(0, _translate("MainWindow", "IP"))
        self.packetInfo.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "New Subitem"))
        self.packetInfo.topLevelItem(1).setText(0, _translate("MainWindow", "HTTP"))
        self.packetInfo.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "New Subitem"))
        self.packetInfo.topLevelItem(2).setText(0, _translate("MainWindow", "Transmission control protocol"))
        self.packetInfo.topLevelItem(2).child(0).setText(0, _translate("MainWindow", "New Subitem"))
        self.packetInfo.setSortingEnabled(__sortingEnabled)
        self.interfaceLabel.setText(_translate("MainWindow", "Interface:"))
        self.interfacesList.setStatusTip(_translate("MainWindow", "Choose Interface for packets capture"))
        self.interfacesList.setCurrentText(_translate("MainWindow", "Select Interface for Capturing Packets ..."))
        self.interfacesList.setItemText(0, _translate("MainWindow", "Select Interface for Capturing Packets ..."))
        self.captureButton.setText(_translate("MainWindow", "Capture"))
        self.filterBox.setPlaceholderText(_translate("MainWindow", "Apply a display filter ..."))
        self.applyButton.setText(_translate("MainWindow", "Apply"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuCapture.setTitle(_translate("MainWindow", "Capture"))
        self.menuFilters.setTitle(_translate("MainWindow", "Filters"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionStart_Capture.setText(_translate("MainWindow", "Start Capture"))
        self.actionStop_Capture.setText(_translate("MainWindow", "Stop Capture"))
        self.actionUDP.setText(_translate("MainWindow", "UDP"))
        self.actionTCP.setText(_translate("MainWindow", "TCP"))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

    
    
    #########################################################################################################################
    ############################## Functions, Event handlers, thread and signal slot connectors #############################
    
    ## Global variables ##
    packets_Hex = []
    full_data = []
    original_data = []
    current_row = 0
    
    
    def file_save(self):
        name,_ = QtWidgets.QFileDialog.getSaveFileName()
        if name:
            file = open(name,'w')
            text = str(type(name))
            file.write(text)
            file.close()

    def new_btn_clicked(self):
        while (self.Packets.rowCount() > 0):
            self.Packets.removeRow(0)
        self.packets_Hex = []
        self.full_data = []
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
        self.packetHex.setText(self.packets_Hex[row])
        self.packetInfo.topLevelItem(0).child(0).setText(0, self.full_data[row])

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
                filter_items = self.Packets.findItems(search_filter,QtCore.Qt.MatchContains)
                row_index_list = []
                for i in range(0,len(filter_items)):
                    row_index_list.append(self.Packets.row(filter_items[i]))
                while (self.Packets.rowCount() > 0):
                    self.Packets.removeRow(0)
                current_row_2 = 0
                for i in range(0,len(row_index_list)):
                    self.Packets.insertRow(current_row_2)
                    column_number_2 = 0
                    for j in self.original_data[row_index_list[i]]:
                        if(column_number_2 == 6):
                            break
                        self.Packets.setItem(current_row_2,column_number_2,QtWidgets.QTableWidgetItem(j))
                        column_number_2 = column_number_2 + 1
                    current_row_2 = current_row_2 + 1

        else:
            self.msg = QtWidgets.QMessageBox()
            self.msg.setIcon(QtWidgets.QMessageBox.Critical)
            self.msg.setWindowTitle("No data!")
            self.msg.setText("Start a capture to apply filters.")
            self.msg.exec_()


    def addRowData(self,Data):
        self.original_data.append(Data)
        self.Packets.insertRow(self.current_row)
        column_number = 0
        for packet_Data in Data:
            if(column_number==6):
                self.packets_Hex.append(packet_Data)
                column_number = column_number + 1
                continue
            if(column_number==7):
                self.full_data.append(packet_Data)
                break
            self.Packets.setItem(self.current_row,column_number,QtWidgets.QTableWidgetItem(str(packet_Data)))
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
                    self.Thread.connection.connect(self.addRowData)
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
