import sys
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.QtWidgets import QWidget, QHeaderView, QCheckBox, QLabel, QPushButton
import functions
class Checkboxes(QWidget):
    def __init__(self):
        super().__init__()

        #Creating checkboxes for logs
        self.Application = QCheckBox('Application Logs')
        self.CoreDumps = QCheckBox('Core Dumps')
        self.GeniewareLogs = QCheckBox('Genieware Logs')
        self.OSLogs = QCheckBox('OS Logs')
        self.SystemLogs = QCheckBox('System Logs')


        boxlayout = QVBoxLayout()
        boxlayout.addWidget(self.Application)
        boxlayout.addWidget(self.CoreDumps)
        boxlayout.addWidget(self.GeniewareLogs)
        boxlayout.addWidget(self.OSLogs)
        boxlayout.addWidget(self.SystemLogs)
        self.setLayout(boxlayout)

    def submitstatus(self):
        ApplicationStatus = self.Application.isChecked()
        CoreDumps = self.CoreDumps.isChecked()
        GeniewareLogs = self.GeniewareLogs.isChecked()
        OSLogs = self.OSLogs.isChecked()
        SystemLogs = self.SystemLogs.isChecked()
        #print(ApplicationStatus,CoreDumps,GeniewareLogs,OSLogs,SystemLogs)
        return ApplicationStatus,CoreDumps,GeniewareLogs,OSLogs,SystemLogs

class DateListCB(QWidget):
    def __init__(self,node):
        super().__init__()

        boxlayoutdate = QVBoxLayout()

        #Creating checkboxes for dates
        self.dateslist=functions.ListDates(node)
        #creating checkboxes list
        self.cbs = [] # stands for checkboxes
        for i in range(len(self.dateslist)):
            checkbox = QCheckBox(self.dateslist[i])
            self.cbs.append(checkbox)
            #setattr(self, f'Date{i}',  QCheckBox(dateslist[i]))
            boxlayoutdate.addWidget(self.cbs[i])
        self.setLayout(boxlayoutdate)

    def submitstatus(self):
        status = []
        for i in self.dateslist:
            print(i)

class Buttons():
    def __init__(self):
        super().__init__()

    def Download(self):
        logs = Checkboxes.submitstatus()
        #dates = 

#Node listi ayri fonksiyondan alip bu node listteki nodelari tek  tek parametre olarakalip
#Sonra bunlari checkbox olusturacak fonksiyona gonderip checkboxelari ilgili nodelarda listelemek


class Table(QWidget):
    def __init__(self):
        super().__init__()

        #Setting window title
        self.setWindowTitle('Log Management')

        #Setting Row Names
        nodes = functions.ListNodes()

        #Creating array for checkbox status
        Logs = [] # Application,CoreDumps,Genieware Logs, OS Logs, System Logs
        #Dates = []

        #Create a QTableWidget
        self.LogCopy = QTableWidget()
        self.LogCopy.setColumnCount(3)
        self.LogCopy.setRowCount(len(nodes))
        
        #print(len(nodes))
        self.LogCopy.setVerticalHeaderLabels(nodes)

        # Setting Column Names
        self.LogCopy.setHorizontalHeaderLabels(['Nodes','Dates','Types'])

        #Making CheckBoxes

        # Creating Log Types Checkboxes
        for row  in range(len(nodes)):
            column=2 #Dates column
            types_table = Checkboxes() # Types table i types_boxes yap
            self.LogCopy.setCellWidget(row,column,types_table)
            # Connecting the Logs checkboxes
            types_table.Application.clicked.connect(types_table.submitstatus)
            types_table.CoreDumps.clicked.connect(types_table.submitstatus)
            types_table.GeniewareLogs.clicked.connect(types_table.submitstatus)
            types_table.OSLogs.clicked.connect(types_table.submitstatus)
            types_table.SystemLogs.clicked.connect(types_table.submitstatus)
        #Creating Dates CheckBoxes
        for row in range(len(nodes)):
            column=1 #Dates column
            dates_boxes = DateListCB(nodes[row])
            #print(nodes[row])
            self.LogCopy.setCellWidget(row,column,dates_boxes)
            #Connecting the Dates checkboxes
            for i in range(len(dates_boxes.dateslist)):
                dates_boxes.cbs[i].clicked.connect(dates_boxes.submitstatus)

        
        
        #Making rows large enough to  fit everything in
        for i in range(len(nodes)):
            self.LogCopy.setRowHeight(i,200)
        self.LogCopy.setColumnWidth(2,270)

        download = QPushButton('Download',self) #functions
        #sendrepoinf = QPushButton('Send Repo Information',self)
        #sendtomachine = QPushButton('')

        #download.clicked.connect("give the class and function here")

        #Testing part
        #print(Checkboxes().submitstatus())
         

        # Set layout
        layout = QVBoxLayout()    
        layout.addWidget(self.LogCopy)
        layout.addWidget(download)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Table()
    window.resize(600, 300)  # Resize the window
    window.show()
    sys.exit(app.exec_())