import sys
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.QtWidgets import QWidget, QHeaderView, QCheckBox, QLabel, QPushButton
from PyQt5.QtWidgets import QLineEdit, QDialog
import functions


class ErrorPage(QDialog):
    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):
        # Set the window title
        self.setWindowTitle('Error Page')

        # Create a layout
        layout = QVBoxLayout()

        # Create a label for the error message
        error_message = QLabel('An error has occurred. Please try again later.', self)
        error_message.setStyleSheet("font-size: 16px; color: red;")
        layout.addWidget(error_message)

        # Create a close button
        close_button = QPushButton('Close', self)
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)

        # Set the layout to the widget
        self.setLayout(layout)

        # Set the window size
        self.resize(300, 150)

        # Center the window
        self.setGeometry(100, 100, 300, 150)


class SendRepoGui(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle('Login Window')

        self.setGeometry(100, 100, 300, 250)



        # Create layout

        loginLayout = QVBoxLayout()



        # Username field

        self.username_label = QLabel('Username:')

        self.username_input = QLineEdit()

        loginLayout.addWidget(self.username_label)

        loginLayout.addWidget(self.username_input)



        # Password field

        self.password_label = QLabel('Password:')

        self.password_input = QLineEdit()

        self.password_input.setEchoMode(QLineEdit.Password)  # Hide password input

        loginLayout.addWidget(self.password_label)

        loginLayout.addWidget(self.password_input)



        # Hostname field

        self.hostname_label = QLabel('Hostname or IP:')

        self.hostname_input = QLineEdit()

        loginLayout.addWidget(self.hostname_label)

        loginLayout.addWidget(self.hostname_input)



        # Login button

        self.login_button = QPushButton('Upload')

        #self.login_button.clicked.connect(self.handle_send) # This will be send button and send handle

        resulttest = self.login_button.clicked.connect(lambda: functions.send_repo_info(self.hostname_input.text(), self.username_input.text(),self.password_input.text()))
        print(f"resulttest is: {resulttest}")

        loginLayout.addWidget(self.login_button)



        # Cancel button

        self.cancel_button = QPushButton('Cancel')

        self.cancel_button.clicked.connect(self.close)  # Close the window

        loginLayout.addWidget(self.cancel_button)



        # Set the layout for the window

        self.setLayout(loginLayout)

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
        return ApplicationStatus,CoreDumps,GeniewareLogs,OSLogs,SystemLogs
        #return status

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
        selectedstatus =[]
        for i in range(len(self.dateslist)):
            status.append(self.cbs[i].isChecked())
        #print(status)
        return status

class UserCredentials(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle('Login Window')

        self.setGeometry(100, 100, 300, 250)



        # Create layout

        loginLayout = QVBoxLayout()



        # Username field

        self.username_label = QLabel('Username:')

        self.username_input = QLineEdit()

        loginLayout.addWidget(self.username_label)

        loginLayout.addWidget(self.username_input)



        # Password field

        self.password_label = QLabel('Password:')

        self.password_input = QLineEdit()

        self.password_input.setEchoMode(QLineEdit.Password)  # Hide password input

        loginLayout.addWidget(self.password_label)

        loginLayout.addWidget(self.password_input)



        # Hostname field

        self.hostname_label = QLabel('Hostname or IP:')

        self.hostname_input = QLineEdit()

        loginLayout.addWidget(self.hostname_label)

        loginLayout.addWidget(self.hostname_input)



        # Login button

        self.login_button = QPushButton('Upload')

        #self.login_button.clicked.connect(self.handle_send) # This will be send button and send handle

        resulttest = self.login_button.clicked.connect(lambda: functions.upload_directory_via_scp(self.hostname_input.text(), self.username_input.text(),self.password_input.text()))
        #print(resulttest)

        loginLayout.addWidget(self.login_button)



        # Cancel button

        self.cancel_button = QPushButton('Cancel')

        self.cancel_button.clicked.connect(self.close)  # Close the window

        loginLayout.addWidget(self.cancel_button)



        # Set the layout for the window

        self.setLayout(loginLayout)


"""class Buttons():
    def __init__(self):
        super().__init__()

    def Download(self):
        print("Hello world")
        nodes = Table.nodes
        for i in range(len(Table.nodes)):
            print("a")
        #logs = Checkboxes.submitstatus()
        #dates = 
#for i in range(len(nodes)):
        #    download.clicked.connect(functions.downloadLog(
        #types_table[i].submitstatus(),dates_boxes[i].submitstatus(),nodes[i]))"""


#Node listi ayri fonksiyondan alip bu node listteki nodelari tek  tek parametre olarakalip
#Sonra bunlari checkbox olusturacak fonksiyona gonderip checkboxelari ilgili nodelarda listelemek


class Table(QWidget):
    def __init__(self):
        super().__init__()

        #Setting window title
        self.setWindowTitle('Log Management')

        #Setting Row Names
        nodes = functions.ListNodes()
        #print(type(nodes))

        #Creating array for checkbox status
        #Logs = [] # Application,CoreDumps,Genieware Logs, OS Logs, System Logs
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
        #Creating empty lists to which logs for which nodes
        types_table=[]
        # Creating Log Types Checkboxes
        for row  in range(len(nodes)):
            column=2 #Dates column
            types_table.append(Checkboxes())# Types table i types_boxes yap
            self.LogCopy.setCellWidget(row,column,types_table[row])
            # Connecting the Logs checkboxes
            types_table[row].Application.clicked.connect(types_table[row].submitstatus)
            types_table[row].CoreDumps.clicked.connect(types_table[row].submitstatus)
            types_table[row].GeniewareLogs.clicked.connect(types_table[row].submitstatus)
            types_table[row].OSLogs.clicked.connect(types_table[row].submitstatus)
            types_table[row].SystemLogs.clicked.connect(types_table[row].submitstatus)


        #Creating Dates CheckBoxes
        #Creating empty list to define dates checkboxes for every node
        dates_boxes=[]
        for row in range(len(nodes)):
            column=1 #Dates column
            dates_boxes.append(DateListCB(nodes[row]))
            #print(nodes[row])
            self.LogCopy.setCellWidget(row,column,dates_boxes[row])
            #Connecting the Dates checkboxes
            #for i in range(len(dates_boxes[row].dateslist)):
            #    dates_boxes[row].cbs[i].clicked.connect(dates_boxes[row].submitstatus)
            #print(f"cbs is: {dates_boxes[row].submitstatus()}")
        #print(dates_boxes[0].cbs[0].isChecked())
        #Making rows large enough to  fit everything in
        for i in range(len(nodes)):
            self.LogCopy.setRowHeight(i,200)
        self.LogCopy.setColumnWidth(2,270)

        download = QPushButton('Download',self) #Download Button #functions
        upload = QPushButton('Upload',self) # Upload Button
        send_repo = QPushButton('Send Repo Information File',self)
        #sendrepoinf = QPushButton('Send Repo Information',self)
        #sendtomachine = QPushButton('')
        #Connecting download button to download function

        download.clicked.connect(lambda: self.Download(types_table,dates_boxes,nodes))
        
        #Connecting upload button to upload function
        upload.clicked.connect(lambda: self.Upload())

        #Cennectind send_repo button to send_repo_info function
        send_repo.clicked.connect(lambda: self.SendRepoInfo())
        #for i in range(len(nodes)):
            #print(nodes[i])
            #download.clicked.connect(lambda i=i: functions.downloadLog(types_table[i].submitstatus(),dates_boxes[i].submitstatus(),nodes[i]))
            #for k in range(3):
            #    print(i,k, types_table[i].submitstatus()[k])
            #print(type())
        #print (type(types_table[0].submitstatus()))
        #print(nodes[0])
        #Testing part
        #print(Checkboxes().submitstatus())
         

        # Set layout
        layout = QVBoxLayout()    
        layout.addWidget(self.LogCopy)
        layout.addWidget(download)
        layout.addWidget(upload)
        layout.addWidget(send_repo)
        self.setLayout(layout)

    def Download(self,types_table,dates_boxes,nodes):
        #print(dates_boxes[0].dateslist)
        for i in range(len(nodes)):
            functions.downloadLog(types_table[i].submitstatus(),dates_boxes[i].submitstatus(),dates_boxes[i].dateslist,nodes[i])
        #for i in range(len(nodes)):
        #    logs.append(lambda: types_table[i].submitstatus())
    def Upload(self):
        #loginwindow =  UserCredentials.initUI()
        loginwindow = UserCredentials()
        loginwindow.resize(100,100)
        loginwindow.exec_()
        #print("Uploaded   Test")
    def SendRepoInfo(self):
        loginwindow = SendRepoGui()
        loginwindow.resize(100,100)
        loginwindow.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Table()
    window.resize(600, 300)  # Resize the window
    window.show()
    sys.exit(app.exec_())