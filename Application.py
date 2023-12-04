# Importing essential modules
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHeaderView
import sys
import pyodbc

<<<<<<< Updated upstream
server = 'DESKTOP-HT3NB74' 
=======
# server = 'DESKTOP-HT3NB74 # Eman
server = 'DESKTOP-F3QE491\IBAD' # Ibad
# server = 'DESKTOP-QNMUBSC\DBSFALL23' # Raahim Laptop
# server = 'DESKTOP-D0D9STF\DBSFALL2023' # Raahim PC
>>>>>>> Stashed changes
database = 'Final_Final_Project'  
use_windows_authentication = True 

connection = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;')
cursor = connection.cursor()

class UI(QtWidgets.QMainWindow):
    ids = []
    def __init__(self):
        super(UI, self).__init__() 
        uic.loadUi('Screens\Login Screen.ui', self) 
        self.setWindowTitle("DBClinic")
<<<<<<< Updated upstream
=======
        
        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)
>>>>>>> Stashed changes

        self.populateType()
        self.populateUsername()
        self.typeCombo.activated.connect(self.populateUsername)
        self.signinButton.clicked.connect(self.signin)

    def populateType(self):
        # populate typeCombo with the types of users
        cursor.execute("select type from Types")
        for i in cursor.fetchall():
            self.typeCombo.addItems(i)

    def populateUsername(self):
<<<<<<< Updated upstream

=======
        self.ids.clear()
>>>>>>> Stashed changes
        if self.typeCombo.currentText() == 'Doctor':
            self.usernameCombo.clear()
            cursor.execute("""
                            select FirstName + ' ' + LastName as UserName, UserID from Users
                            where TypeID in (
				            select TypeID from Types
				            where type = 'Doctor')""")

        elif self.typeCombo.currentText() == 'Receptionist':
            self.usernameCombo.clear()
            cursor.execute("""
                            select FirstName + ' ' + LastName as UserName, UserID from Users
                            where TypeID in (
				            select TypeID from Types
				            where type = 'Receptionist')""")

        elif self.typeCombo.currentText() == 'Nurse':
            self.usernameCombo.clear()
            cursor.execute("""
                            select FirstName + ' ' + LastName as UserName, UserID from Users
                            where TypeID in (
				            select TypeID from Types
				            where type = 'Nurse')""")

        elif self.typeCombo.currentText() == 'Technician':
            self.usernameCombo.clear()
            cursor.execute("""
                            select FirstName + ' ' + LastName as UserName, UserID from Users
                            where TypeID in (
				            select TypeID from Types
				            where type = 'Technician')""")

        elif self.typeCombo.currentText() == 'Administrator':
            self.usernameCombo.clear()
            cursor.execute("""
                            select FirstName + ' ' + LastName as UserName, UserID from Users
                            where TypeID in (
				            select TypeID from Types
				            where type = 'Administrator')""")


        for i in cursor.fetchall():
            self.usernameCombo.addItems(i[0:1])
            self.ids.append(i[1])
        
        self.usernameCombo.setCurrentIndex(0)

    def signin(self):
<<<<<<< Updated upstream
        # cursor.execute(  f'select password from Users where FirstName + ' ' + LastName =  {self.usernameCombo.currentText()} and typeID = ( select typeID from Types where Type = {self.typeCombo.currentText()})')
        #print(cursor.fetchall())

        cursor.execute("select Password from Users where FirstName + ' ' + LastName = '" + str(self.usernameCombo.currentText()) + "'" )#+ " and TypeID = ( select typeID from Types where Type ='" + str(self.typeCombo.currentText()) + "'" )
        # print(self.passwordLine.text() , str(cursor.fetchall()[0][0]))
        if self.passwordLine.text() == str(cursor.fetchall()[0][0]) : # and it matches the password of the user whose username is selected in the usernameCombo
=======
        
        cursor.execute("select Password from Users where FirstName + ' ' + LastName = '" + str(self.usernameCombo.currentText()) + "'" )

        # currentUser = self.usernameCombo.currentText()
        if checkpw(self.passwordLine.text().encode('utf-8'),str(cursor.fetchall()[0][0]).encode('utf-8')): # and it matches the password of the user whose username is selected in the usernameCombo

>>>>>>> Stashed changes
            if self.typeCombo.currentText() == "Receptionist":
                self.receptionistscreen = ReceptionistMainMenu()
                self.receptionistscreen.show()
                self.close()

            elif self.typeCombo.currentText() == "Doctor":
<<<<<<< Updated upstream
                self.doctorscreen = DoctorMainMenu()
=======
                id = self.ids[self.usernameCombo.currentIndex()]
                self.doctorscreen = DoctorMainMenu(id)
>>>>>>> Stashed changes
                self.doctorscreen.show()
                self.close()

            elif self.typeCombo.currentText() == "Nurse":
                id = self.ids[self.usernameCombo.currentIndex()]
                print(id)
                self.nursescreen = NurseMainMenu(id)
                self.nursescreen.show()
                self.close()

            elif self.typeCombo.currentText() == "Administrator":
                self.adminscreen = AdminMainMenu()
                self.adminscreen.show()
                self.close()

            elif self.typeCombo.currentText() == "Technician":
                self.technicianscreen = TechnicianMainMenu()
                self.technicianscreen.show()
                self.close()
        else: 
            self.ErrorWindow = QtWidgets.QMessageBox()
            self.ErrorWindow.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            self.ErrorWindow.setText("Incorrect Password! Try again.")
            self.ErrorWindow.setWindowTitle("Incorrect Password")
            self.ErrorWindow.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            self.ErrorWindow.exec()
            self.passwordLine.clear()

class ReceptionistMainMenu(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(ReceptionistMainMenu, self).__init__()
        uic.loadUi("Screens\Receptionist MainMenu.ui",self)
        self.setWindowTitle("Receptionist View")
<<<<<<< Updated upstream
=======

        # Fixes the screen and Disables Maximize Button
        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)
>>>>>>> Stashed changes
        
        cursor.execute("""
                    select FirstName + ' ' + LastName as UserName from Users
                    where TypeID in (
                    select TypeID from Types
                    where type = 'Doctor')
                    """)
                    
        self.comboDoctor.addItems(('',))
        for i in cursor.fetchall():
            self.comboDoctor.addItems(i)
        
        self.comboDoctor.setCurrentIndex(0)
        self.dateEdit.setMinimumDate(QDate.currentDate())
        self.dateEdit.setDisabled(True)
        self.tablewidgetSearch.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers) # make table widgets read only
        self.tablewidgetWaitlist.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        
        self.populateWaitlist()
        self.pushAdd.clicked.connect(self.addPatient)
        self.pushSearch.clicked.connect(self.searchPatient)
        self.pushBook.clicked.connect(self.bookAppointment)
        self.pushClear.clicked.connect(self.clearSearch)
        self.pushClearFilters.clicked.connect(self.populateWaitlist)
        self.pushCancel.clicked.connect(self.cancelAppointment)
        self.comboDoctor.currentIndexChanged.connect(self.searchWaitlist)
        self.dateEdit.dateChanged.connect(self.searchWaitlist)
        self.checkDate.stateChanged.connect(self.toggleDateEdit)
        self.pushLogOut.clicked.connect(self.relog)

    def addPatient(self):
        self.addPatientWindow = AddPatient() # calling a constructor which has the real AddPatient function
        self.addPatientWindow.show()

    def searchPatient(self):
        self.tablewidgetSearch.clearContents()
        self.tablewidgetSearch.setRowCount(0)
        # populate tablewidgetSearch with the results that contain lineMR and linePhone
<<<<<<< Updated upstream
        # cursor.execute(f"SELECT MR, FirstName + ' ' + LastName as Name, PhoneNum FROM PatientInfo where MR = {str(self.lineMR.text())} and PhoneNum like '{str(self.linePhone.text())}%'")
=======
>>>>>>> Stashed changes

        if str(self.lineMR.text()).strip() ==  '':
            cursor.execute(f"SELECT MR, FirstName + ' ' + LastName as Name, PhoneNum FROM PatientInfo where PhoneNum like '%{str(self.linePhone.text())}%'")
        
        else:
            cursor.execute(f"SELECT MR, FirstName + ' ' + LastName as Name, PhoneNum FROM PatientInfo where MR = {str(self.lineMR.text())} and PhoneNum like '%{str(self.linePhone.text())}%'")

	
	# Fetch all rows and populate the table
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.tablewidgetSearch.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.tablewidgetSearch.setItem(row_index, col_index, item)

        # Adjust content display
        # header = self.tablewidgetSearch.horizontalHeader()
        # header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        # header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        # header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)

    def bookAppointment(self):
        row = self.tablewidgetSearch.currentRow()
        
        if row != -1:
            MR = self.tablewidgetSearch.item(row,0).text()
            Name = self.tablewidgetSearch.item(row,1).text()

            self.bookAppointmentWindow = BookAppointment(Name,MR)
            self.bookAppointmentWindow.show()
            
            # refresh the waitlist tablewidget when appointment window closes
            self.bookAppointmentWindow.closeEvent = self.searchWaitlist

        else:
            self.ErrorWindow = QtWidgets.QMessageBox()
            self.ErrorWindow.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            self.ErrorWindow.setText("Please select a patient to book appointment.")
            self.ErrorWindow.setWindowTitle("Please select a patient.")
            self.ErrorWindow.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            self.ErrorWindow.exec()

    def clearSearch(self):
        self.tablewidgetSearch.clearContents()
        self.tablewidgetSearch.setRowCount(0)

    def searchWaitlist(self, event = None):
        # populate tablewidgetWaitlist with the results that match Doctor and Date
        self.tablewidgetWaitlist.clearContents()
        self.tablewidgetWaitlist.setRowCount(0)

        date = self.dateEdit.date().toString("yyyy-MM-dd")

        if self.comboDoctor.currentText().strip() == '' and self.checkDate.isChecked() == False:
            cursor.execute("SELECT P.MR, P.FirstName + ' ' + P.LastName as Patient, U.FirstName + ' ' + U.LastName as Doctor, R.RoomName, A.Date, A.TurnNum FROM Appointments A, Users U, PatientInfo P, Doctors D, Rooms R, Status S WHERE A.MR = P.MR AND A.DoctorID = U.UserID AND A.DoctorID = D.DoctorID AND D.RoomID = R.RoomID AND DATEPART(DY, A.Date) >= DATEPART(DY,GETDATE()) AND A.StatusID = S.StatusID AND S.Status = 'Upcoming' ORDER BY A.Date ASC")

        elif self.comboDoctor.currentText().strip() == '' and self.checkDate.isChecked() == True:
            cursor.execute(f"SELECT P.MR, P.FirstName + ' ' + P.LastName as Patient, U.FirstName + ' ' + U.LastName as Doctor, R.RoomName, A.Date, A.TurnNum FROM Appointments A, Users U, PatientInfo P, Doctors D, Rooms R, Status S WHERE A.MR = P.MR AND A.DoctorID = U.UserID AND A.DoctorID = D.DoctorID AND D.RoomID = R.RoomID AND A.Date = '{date}' AND A.StatusID = S.StatusID AND S.Status = 'Upcoming' ORDER BY A.Date ASC")

        elif self.comboDoctor.currentText().strip() != '' and self.checkDate.isChecked() == False:
            cursor.execute(f"SELECT P.MR, P.FirstName + ' ' + P.LastName as Patient, U.FirstName + ' ' + U.LastName, R.RoomName, A.Date, A.TurnNum FROM Appointments A, Users U, PatientInfo P, Doctors D, Rooms R, Status S WHERE A.MR = P.MR AND A.DoctorID = U.UserID AND A.DoctorID = D.DoctorID AND D.RoomID = R.RoomID AND U.FirstName + ' ' + U.LastName = '{self.comboDoctor.currentText()}' AND A.StatusID = S.StatusID AND S.Status = 'Upcoming' ORDER BY A.Date ASC")

        else:
            cursor.execute(f"SELECT P.MR, P.FirstName + ' ' + P.LastName as Patient, U.FirstName + ' ' + U.LastName, R.RoomName, A.Date, A.TurnNum FROM Appointments A, Users U, PatientInfo P, Doctors D, Rooms R, Status S WHERE A.MR = P.MR AND A.DoctorID = U.UserID AND A.DoctorID = D.DoctorID AND D.RoomID = R.RoomID AND A.Date = '{date}' AND U.FirstName + ' ' + U.LastName = '{self.comboDoctor.currentText()}' AND A.StatusID = S.StatusID AND S.Status = 'Upcoming' ORDER BY A.Date ASC")

        # Fetch all rows and populate the table
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.tablewidgetWaitlist.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.tablewidgetWaitlist.setItem(row_index, col_index, item)

    def populateWaitlist(self):
        # repopulate with all upcoming appointments
        self.comboDoctor.setCurrentIndex(0)
        self.checkDate.setChecked(False)
        self.dateEdit.setDate(QDate.currentDate())
        self.tablewidgetWaitlist.clearContents()
        self.tablewidgetWaitlist.setRowCount(0)

        cursor.execute("SELECT P.MR, P.FirstName + ' ' + P.LastName as Patient, U.FirstName + ' ' + U.LastName as Doctor, R.RoomName, A.Date, A.TurnNum FROM Appointments A, Users U, PatientInfo P, Doctors D, Rooms R, Status S WHERE A.MR = P.MR AND A.DoctorID = U.UserID AND A.DoctorID = D.DoctorID AND D.RoomID = R.RoomID AND DATEPART(DY, A.Date) >= DATEPART(DY,GETDATE()) AND A.StatusID = S.StatusID AND S.Status = 'Upcoming' ORDER BY A.Date ASC")

        # Fetch all rows and populate the table
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.tablewidgetWaitlist.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.tablewidgetWaitlist.setItem(row_index, col_index, item)

    def cancelAppointment(self):

        row = self.tablewidgetWaitlist.currentRow()

        if row != -1:
            self.confirmation = QtWidgets.QMessageBox.warning(self, "Confirmation Box", "Are you sure you want to delete this appointment?", QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)

            if self.confirmation == QtWidgets.QMessageBox.StandardButton.Yes:
                # delete the selected row in tablewidgetWaitlist from the appointments table and repopulate tablewidgetWaitlist
<<<<<<< Updated upstream
                # NEEDS TO BE EDITED WITH THE TURN NUMBER SO IT DOESN'T DELETE MULTIPLE APPOINTMENTS
                cursor.execute (f'''
                DELETE FROM Appointments 
                WHERE MR = {int(self.tablewidgetWaitlist.item(row,0).text())} AND Date = '{self.tablewidgetWaitlist.item(row,4).text()}'
                ''')
=======
                cursor.execute(f"SELECT AppointmentID FROM Appointments WHERE MR = '{self.tablewidgetWaitlist.item(row,0).text()}' AND Date = '{self.tablewidgetWaitlist.item(row,4).text()}' AND TurnNum = {int(self.tablewidgetWaitlist.item(row,5).text())}")
                appointmentID = cursor.fetchall()[0][0]

                # cursor.execute (f'''
                # DELETE FROM Appointments 
                # WHERE MR = {int(self.tablewidgetWaitlist.item(row,0).text())} AND Date = '{self.tablewidgetWaitlist.item(row,4).text()}' AND TurnNum = {int(self.tablewidgetWaitlist.item(row,5).text())}
                # ''')
                cursor.execute(f"DELETE FROM Invoices WHERE AppointmentID = {appointmentID}")
                cursor.execute(f"DELETE FROM Appointments WHERE AppointmentID = {appointmentID}")
>>>>>>> Stashed changes
                connection.commit()

                self.searchWaitlist()

            self.tablewidgetWaitlist.setCurrentCell(-1,-1)

        else:
            self.ErrorWindow = QtWidgets.QMessageBox()
            self.ErrorWindow.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            self.ErrorWindow.setText("Please select an appointment to cancel.")
            self.ErrorWindow.setWindowTitle("Please select an appointment.")
            self.ErrorWindow.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            self.ErrorWindow.exec()

    def toggleDateEdit(self):
        self.dateEdit.setDisabled(not self.checkDate.isChecked())
        self.searchWaitlist()

    def relog(self):
        self.confirmation = QtWidgets.QMessageBox.warning(self, "Confirmation Box", "Are you sure you want to log out?", QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)

        if self.confirmation == QtWidgets.QMessageBox.StandardButton.Yes:
            self.loginScreen = UI()
            self.loginScreen.show()
            self.close()
        else:
            pass


class BookAppointment(QtWidgets.QMainWindow):
    
    def __init__(self, Name, MR):
        super(BookAppointment, self).__init__()
        uic.loadUi("Screens\Receptionist AddAppointment.ui",self)
        self.setWindowTitle("Book Appointment")

<<<<<<< Updated upstream
        # selected_row=self.tablewidgetSearch.currentRow()
        # if selected_row>=0: 
        #     MrNum=self.tablewidgetSearch.item(selected_row,0).text()
        #     patientName=self.tablewidgetSearch.item(selected_row,1).text()
        #     patientPhone=self.tablewidgetSearch.item(selected_row,2).text()
        #     print(selected_row,MrNum, patientName,patientPhone)
            # book_type=self.tablewidgetSearch.item(selected_row,3).text()
            # book_issue=eval(self.tablewidgetSearch.item(selected_row,4).text())

            # self.view_Form=BookAppointment(MrNum, patientName,patientPhone)
            # self.view_Form.show()
=======
        # Fixes the screen and Disables Maximize Button
        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)
>>>>>>> Stashed changes

        firstName = Name.split()[0]
        lastName = Name.split()[-1]

        self.lineFirstName.setDisabled(True)
        self.lineFirstName.setText(firstName) # first name of the patient whose row was selected in the search tablewidget, comes from query or just accessing the tablewidget
        self.lineLastName.setDisabled(True)
        self.lineLastName.setText(lastName) # last name of the patient whose row was selected in the search tablewidget, comes from query or just accessing the tablewidget
        self.lineMR.setDisabled(True)
        self.lineMR.setText(MR) # phone of the patient whose row was selected in the search tablewidget, comes from query or just accessing the tablewidget
        self.linePatientTurn.setDisabled(True)
        self.lineCurrentPatient.setDisabled(True)
        self.dateEditAppointment.setMinimumDate(QDate.currentDate())
        

        self.populateSpecialization()
        self.populateDoctor()
        self.showAmount()
        self.showPatientTurn()
        self.comboSpecialization.currentIndexChanged.connect(self.populateDoctor)
        self.comboDoctor.currentIndexChanged.connect(self.showAmount)
        self.dateEditAppointment.dateChanged.connect(self.showPatientTurn)

        cursor.execute("SELECT DATEPART(day,GETDATE()), DATEPART(month,GETDATE()), DATEPART(year,GETDATE())")
        date = cursor.fetchall()
        self.lineInvoiceDate.setDisabled(True) # current date, use GETDATE() query
        self.lineInvoiceDate.setText(str(date[0][0]) + '-' + str(date[0][1]) + '-' + str(date[0][2]))
        self.lineAmount.setDisabled(True) # consultation cost of the selected doctor, comes from query

        self.pushConfirm.clicked.connect(self.confirmAppointment)
        self.pushCancel.clicked.connect(self.close)

    def populateSpecialization(self):
        # populate the combobox with the specializations
        cursor.execute("select specialization from Specialization")
        for i in cursor.fetchall():
            self.comboSpecialization.addItems(i)

        self.comboSpecialization.setCurrentIndex(0)

    def populateDoctor(self):
        # populate the combobox with the doctors of the selected specialization
        self.comboDoctor.clear()
        cursor.execute(f"select FirstName + ' ' + LastName as UserName from Users where UserID IN (SELECT DoctorID FROM Doctors WHERE SpecializationID = (SELECT SpecializationID FROM Specialization WHERE Specialization = '{self.comboSpecialization.currentText()}'))")
        
        for i in cursor.fetchall():
            self.comboDoctor.addItems(i)

        self.comboDoctor.setCurrentIndex(0)

    def showAmount(self):
        cursor.execute(f"SELECT ConsultationCost FROM Doctors WHERE DoctorID IN (SELECT UserID FROM Users WHERE FirstName + ' ' + LastName = '{self.comboDoctor.currentText()}')")
        fetched = cursor.fetchall()
        if fetched != []:
            self.lineAmount.setText(str(fetched[0][0]))
        else:
            self.lineAmount.setText('None')

        self.showPatientTurn()

    def showPatientTurn(self):
        date = self.dateEditAppointment.date().toString("yyyy-MM-dd") # not working by putting this in fstring

        cursor.execute(f"SELECT MAX(TurnNum) FROM Appointments WHERE DoctorID IN (SELECT UserID FROM Users WHERE FirstName + ' ' + LastName = '{self.comboDoctor.currentText()}') AND Date = '{date}'")
        fetched = cursor.fetchall()
        if fetched != [] and fetched[0][0] != None:
            self.linePatientTurn.setText(str(fetched[0][0]+1))
        else:
            self.linePatientTurn.setText('1')

        self.showCurrentTurn()

    def showCurrentTurn(self):
        date = self.dateEditAppointment.date().toString("yyyy-MM-dd")

        cursor.execute(f"SELECT TurnNum FROM Appointments WHERE DoctorID IN (SELECT UserID FROM Users WHERE FirstName + ' ' + LastName = '{self.comboDoctor.currentText()}') AND Date = '{date}' AND StatusID IN (SELECT StatusID FROM Status WHERE Status = 'Ongoing')")
        fetched = cursor.fetchall()
        if fetched != []:
            self.lineCurrentPatient.setText(str(fetched[0][0]))
        else:
            self.lineCurrentPatient.setText('None')

    def confirmAppointment(self):
        
        date = self.dateEditAppointment.date().toString("yyyy-MM-dd")
        cursor.execute(f"SELECT COUNT(*) FROM Appointments WHERE DoctorID IN (SELECT UserID FROM Users WHERE FirstName + ' ' + LastName = '{self.comboDoctor.currentText()}') AND Date = '{date}' AND StatusID IN (SELECT StatusID FROM Status WHERE Status != 'Skipped')")
        fetched = cursor.fetchall()

        if fetched != [] and fetched[0][0] != None:
            appointmentsBooked = int(fetched[0][0])
        else:
            appointmentsBooked = 0

        cursor.execute(f"SELECT NumPatients FROM Doctors WHERE DoctorID IN (SELECT UserID FROM Users WHERE FirstName + ' ' + LastName = '{self.comboDoctor.currentText()}')")
        patientCapacity = int(cursor.fetchall()[0][0])

        if appointmentsBooked >= patientCapacity:
            self.ErrorWindow = QtWidgets.QMessageBox()
            self.ErrorWindow.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            self.ErrorWindow.setText("This doctor is fully booked for this day. Please select another doctor or day.")
            self.ErrorWindow.setWindowTitle("Fully Booked")
            self.ErrorWindow.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            self.ErrorWindow.exec()

        else:
            cursor.execute(f'''
                            INSERT INTO Appointments (MR, DoctorID, Date, TurnNum, StatusID)
                            VALUES ({self.lineMR.text()}, (SELECT UserID FROM Users WHERE FirstName + ' ' + LastName = '{self.comboDoctor.currentText()}'), '{self.dateEditAppointment.text()}', {self.linePatientTurn.text()}, (SELECT StatusID FROM Status WHERE Status = 'Upcoming'))
                            ''')

            cursor.execute(f'''
                            INSERT INTO Invoices  (AppointmentID, Cost, Date, MR)
                            VALUES ((SELECT AppointmentID FROM Appointments WHERE MR = {self.lineMR.text()} AND DoctorID = (SELECT UserID FROM Users WHERE FirstName + ' ' + LastName = '{self.comboDoctor.currentText()}') AND Date = '{self.dateEditAppointment.text()}' AND TurnNum = {self.linePatientTurn.text()}), {self.lineAmount.text()}, '{self.lineInvoiceDate.text()}', {self.lineMR.text()})
                            ''')
            
            connection.commit()

            self.confirmation = QtWidgets.QMessageBox.information(self, "Appointment Booked", "Appointment has been successfully booked!", QtWidgets.QMessageBox.StandardButton.Ok)

            if self.confirmation == QtWidgets.QMessageBox.StandardButton.Ok or self.confirmation == QtWidgets.QMessageBox.StandardButton.Close:
                self.close()

class AddPatient(QtWidgets.QMainWindow):
    def __init__(self):
        super(AddPatient, self).__init__()
        uic.loadUi("Screens\Receptionist AddPatient.ui",self)
        self.setWindowTitle("Add Patient")

        cursor.execute("""
                            select Genders from Gender
                            """)
                        
        for i in cursor.fetchall():
            self.comboGender.addItems(i)
        
        self.pushAdd.clicked.connect(self.addPatient) # for now
        self.pushCancel.clicked.connect(self.close)

    def addPatient(self):
        firstname = self.lineFirstName.text()
        lastname = self.lineLastName.text()
        phone = self.linePhone.text()
        cnic = self.lineCNIC.text()
        datee = "-".join(self.date.text().split('/')[::-1])
        age = self.lineAge.text()
        gender = self.comboGender.currentText()
        street = self.lineStreet.text()
        city = self.lineCity.text()
        address = street+", "+city
        cursor.execute(f"select GenderID from Gender where Genders = '{gender}'")

        new_patient = (firstname, lastname, phone, datee, cursor.fetchall()[0][0], cnic, age, address)

        insertPatient =  f"INSERT INTO patientInfo (FirstName, LastName, PhoneNum, DateOfBirth,GenderID, CNIC, Age, Address) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(insertPatient, new_patient)
        connection.commit()
        self.close()

class TechnicianMainMenu(QtWidgets.QMainWindow):

    def __init__(self):
        super(TechnicianMainMenu, self).__init__()
        uic.loadUi("Screens\Technician MainMenu.ui",self)
        self.setWindowTitle("Technician View")

        self.pushSearch.clicked.connect(self.searchPatient)
        self.pushUpdate.clicked.connect(self.updatePatient)
        self.pushClear.clicked.connect(self.clearSearch)
        self.pushLogOut.clicked.connect(self.relog)

    def searchPatient(self):
        # populate tablewidgetSearch with the results that contain lineMR and linePhone
        pass

    def updatePatient(self):
        row = self.tablewidgetSearch.currentRow()
        
        # if row != -1: # this is the actual condition, the below is just for testing
            # self.editPatientWindow = UpdatePatient()
            # self.editPatientWindow.show()
         
        self.editPatientWindow = UpdatePatient()
        self.editPatientWindow.show()

    def clearSearch(self):
        self.tablewidgetSearch.clearContents()

    def relog(self):
        self.confirmation = QtWidgets.QMessageBox.warning(self, "Confirmation Box", "Are you sure you want to log out?", QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)

        if self.confirmation == QtWidgets.QMessageBox.StandardButton.Yes:
            self.loginScreen = UI()
            self.loginScreen.show()
            self.close()
        else:
            pass


class UpdatePatient(QtWidgets.QMainWindow):

    def __init__(self):
        super(UpdatePatient, self).__init__()
        uic.loadUi("Screens\Technician UpdatePatient.ui",self)
        self.setWindowTitle("Update Patient")

        self.pushUpdate.clicked.connect(self.updatePatient)
        self.pushCancel.clicked.connect(self.close)

    def updatePatient(self):
        # update the patient's info in the database
        self.close()


class NurseMainMenu(QtWidgets.QMainWindow):

    id = -1
    appointmentID = -1

    def __init__(self, nurseID):
        super(NurseMainMenu, self).__init__()
        uic.loadUi("Screens\\Nurse MainMenu.ui",self)   
        self.setWindowTitle("Nurse View")
<<<<<<< Updated upstream
=======
        
        self.id = nurseID 

        # find the doctor assigned to the nurse and respective room
        cursor.execute(f"SELECT FirstName + ' ' + LastName FROM Users WHERE UserID = (SELECT DoctorID FROM Doctors WHERE NurseID = {self.id})")
        fetched = cursor.fetchall()
        if fetched != [] and fetched[0][0] != None: # if the nurse has a doctor
            self.lineDoctorAssigned.setText(str(fetched[0][0]))
            cursor.execute(f"SELECT RoomName FROM Rooms WHERE RoomID = (SELECT RoomID FROM Doctors WHERE DoctorID = (SELECT DoctorID FROM Doctors WHERE NurseID = {self.id}))")
            fetched = cursor.fetchall()
            if fetched != [] and fetched[0][0] != None: # if the doctors room wasn't deleted
                self.lineRoomAssigned.setText(str(fetched[0][0]))
            else:
                self.lineRoomAssigned.setText('None')

        else :
            self.lineDoctorAssigned.setText('None')
            self.lineRoomAssigned.setText('None')            

        # find the ongoing appointment of the doctor assigned to the nurse
        if self.lineDoctorAssigned.text() != 'None':
            cursor.execute(f"SELECT P.MR, P.FirstName + ' ' + P.LastName as Patient, A.AppointmentID FROM Appointments A, Users U, PatientInfo P, Doctors D, Rooms R, Status S WHERE A.MR = P.MR AND A.DoctorID = U.UserID AND A.DoctorID = D.DoctorID AND D.RoomID = R.RoomID AND DATEPART(DY, A.Date) >= DATEPART(DY,GETDATE()) AND A.StatusID = S.StatusID AND S.Status = 'Ongoing' AND D.NurseID = {self.id} ORDER BY A.Date ASC")
            fetched = cursor.fetchall()
            print(fetched)
            if fetched != [] and fetched[0][0] != None:
                self.lineMR.setText(str(fetched[0][0]))
                self.lineName.setText(str(fetched[0][1]))
                self.appointmentID = fetched[0][2]
            else: 
                self.lineMR.setText('None')
                self.lineName.setText('None')
        else: 
            self.lineMR.setText('None')
            self.lineName.setText('None')
>>>>>>> Stashed changes

        self.lineDoctorAssigned.setDisabled(True)
        self.lineRoomAssigned.setDisabled(True)
        self.lineMR.setDisabled(True)
        self.lineName.setDisabled(True)

        if self.lineMR.text() == 'None':
            self.comboSymptoms.setDisabled(True)
            self.pushAddSymptom.setDisabled(True)
            self.pushRemoveSymptom.setDisabled(True)
            self.listwidgetSymptoms.setDisabled(True)
            self.comboStatus.setDisabled(True)
            self.pushUpdateStatus.setText("Next Patient")
        else: 
            self.populateSymptoms()
            self.populateStatus()

        self.populateWaitlist()

        self.pushAddSymptom.clicked.connect(self.addSymptom)
        self.pushRemoveSymptom.clicked.connect(self.removeSymptom)
        self.comboStatus.activated.connect(self.removeEmptyStatus)
        self.pushUpdateStatus.clicked.connect(self.updateStatus)
        self.pushLogOut.clicked.connect(self.relog)

    def populateSymptoms(self):
        # populate comboSymptoms with the symptoms
        cursor.execute("select symptom from Symptoms")
        for i in cursor.fetchall():
            self.comboSymptoms.addItems(i)

    def populateStatus(self):
        # populate comboStatus with the statuses
        self.comboStatus.clear()
        self.comboStatus.addItems(('',))
        cursor.execute("select Status from Status")
        for i in cursor.fetchall():
            if i[0] != 'Ongoing' and i[0] != 'Upcoming':
                self.comboStatus.addItems(i)
        self.pushUpdateStatus.setDisabled(True)

    def removeEmptyStatus(self):
        # remove the empty status from comboStatus
        # list of items in the comboBox
        items = [self.comboStatus.itemText(i) for i in range(self.comboStatus.count())]
        if '' in items:
            self.comboStatus.removeItem(items.index(''))
            self.pushUpdateStatus.setDisabled(False)

    def addSymptom(self):
        # add the selected symptom from comboSymptoms to the listwidgetSymptoms if it doesn't already exist
        if self.comboSymptoms.currentText() not in [self.listwidgetSymptoms.item(i).text() for i in range(self.listwidgetSymptoms.count())]:
            self.listwidgetSymptoms.addItem(self.comboSymptoms.currentText())
            self.listwidgetSymptoms.setCurrentRow(-1)

    def removeSymptom(self):
        row = self.listwidgetSymptoms.currentRow()

        if row != -1:
            # remove the selected symptom from listwidgetSymptoms
            self.listwidgetSymptoms.takeItem(row)
            self.listwidgetSymptoms.setCurrentRow(-1)

    def updateStatus(self):
        # update the status of the patient in the database and update lineMR and lineName with the next patient's info
        # if self.comboStatus.isEnabled() == False:
        pass


    def populateWaitlist(self):
        # repopulate with all upcoming appointments of the doctor assigned to the nurse
        print(self.id)
        cursor.execute(f"SELECT A.AppointmentID, P.MR, P.FirstName + ' ' + P.LastName as Patient, A.Date, A.TurnNum FROM Appointments A, Users U, PatientInfo P, Doctors D, Rooms R, Status S WHERE A.MR = P.MR AND A.DoctorID = U.UserID AND A.DoctorID = D.DoctorID AND D.RoomID = R.RoomID AND DATEPART(DY, A.Date) >= DATEPART(DY,GETDATE()) AND A.StatusID = S.StatusID AND S.Status = 'Upcoming' AND D.NurseID = {self.id} ORDER BY A.Date ASC")

        # Fetch all rows and populate the table
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.tablewidgetUpcoming.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.tablewidgetUpcoming.setItem(row_index, col_index, item)

    def relog(self):
        self.confirmation = QtWidgets.QMessageBox.warning(self, "Confirmation Box", "Are you sure you want to log out?", QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)

        if self.confirmation == QtWidgets.QMessageBox.StandardButton.Yes:
            self.loginScreen = UI()
            self.loginScreen.show()
            self.close()
        else:
            pass


class DoctorMainMenu(QtWidgets.QMainWindow):

<<<<<<< Updated upstream
    def __init__(self):
=======
    def __init__(self, DoctorID):
>>>>>>> Stashed changes
        super(DoctorMainMenu, self).__init__()
        uic.loadUi("Screens\Doctor MainMenu.ui",self)
        self.setWindowTitle("Doctor View")

<<<<<<< Updated upstream
        self.lineNurseAssigned.setDisabled(True)
        self.lineNurseAssigned.setText("Jane Doe") # name of the nurse assigned to the doctor, comes from query
=======
        # Fixes the screen and Disables Maximize Button
        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)

        # currentUser = currentUser.split()
        # cursor.execute(f"select FirstName,LastName from Users where UserID in (select NurseID from Doctors where DoctorID in(select UserID from Users where FirstName = '{currentUser[0]}' and LastName = '{currentUser[1]}'))")

        self.lineNurseAssigned.setDisabled(True)
        # self.lineNurseAssigned.setText(" ".join(cursor.fetchall()[0]))
        self.lineNurseAssigned.setText("Jane Doe")
>>>>>>> Stashed changes
        self.lineMR.setDisabled(True)
        self.lineMR.setText("123456") # MR of the the patient that has an ongoing appointment with the doctor, comes from query
        
        self.pushViewDetails.clicked.connect(self.viewDetails)
        self.pushCompleteAppointment.clicked.connect(self.completeAppointment)
        self.pushViewPastAppointments.clicked.connect(self.viewPastAppointments)
        self.pushLogOut.clicked.connect(self.relog)
        self.pushClose.clicked.connect(self.close)

    def viewDetails(self):
        self.viewDetailsWindow = ViewDetails()
        self.viewDetailsWindow.show()

    def completeAppointment(self):
        # update the status of the patient in the database and update lineMR with the next patient's MR
        self.plaintexteditDiagnosis.clear()
        self.plaintexteditNotes.clear()

    def viewPastAppointments(self):
        self.viewPastAppointmentsWindow = ViewPastAppointments()
        self.viewPastAppointmentsWindow.show()

    def relog(self):
        self.confirmation = QtWidgets.QMessageBox.warning(self, "Confirmation Box", "Are you sure you want to log out?", QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)

        if self.confirmation == QtWidgets.QMessageBox.StandardButton.Yes:
            self.loginScreen = UI()
            self.loginScreen.show()
            self.close()
        else:
            pass


class ViewDetails(QtWidgets.QMainWindow):

    def __init__(self):
        super(ViewDetails, self).__init__()
        uic.loadUi("Screens\Doctor ViewDetails.ui",self)
        self.setWindowTitle("Patient Details")

        self.lineMR.setDisabled(True)
        self.lineMR.setText("123456") # MR of the the patient that has an ongoing appointment with the doctor, comes from query
        self.lineName.setDisabled(True)
        self.lineName.setText("John Doe") # name of the the patient that has an ongoing appointment with the doctor, comes from query
        self.lineAge.setDisabled(True)
        self.lineAge.setText("21") # age of the the patient that has an ongoing appointment with the doctor, comes from query
        self.lineGender.setDisabled(True)
        self.lineGender.setText("Male") # gender of the the patient that has an ongoing appointment with the doctor, comes from query
        self.listwidgetSymptoms.setDisabled(True)
        self.listwidgetSymptoms.addItems(["Cough", "Fever"]) # symptoms of the the patient that has an ongoing appointment with the doctor, comes from query

        self.pushClose.clicked.connect(self.close)


class ViewPastAppointments(QtWidgets.QMainWindow):

    def __init__(self):
        super(ViewPastAppointments, self).__init__()
        uic.loadUi("Screens\Doctor PastAppointments.ui",self)
        self.setWindowTitle("Past Appointments")

        self.pushSearch.clicked.connect(self.searchAppointment)
        self.pushClearFilters.clicked.connect(self.clearSearchFilters)
        self.pushUpdate.clicked.connect(self.updateAppointment)
        self.pushClose.clicked.connect(self.close)

    def searchAppointment(self):
        # populate tablewidgetSearch with the results that match the filters
        pass

    def clearSearchFilters(self):
        self.tablewidgetSearch.clearContents()
        # repopulate with all past appointments

    def updateAppointment(self):
        row = self.tablewidgetSearch.currentRow()
        
        # if row != -1: # this is the actual condition, the below is just for testing
            # self.editAppointmentWindow = UpdateAppointment()
            # self.editAppointmentWindow.show()
         
        self.editAppointmentWindow = UpdateAppointment()
        self.editAppointmentWindow.show()


class UpdateAppointment(QtWidgets.QMainWindow):
    
        def __init__(self):
            super(UpdateAppointment, self).__init__()
            uic.loadUi("Screens\Doctor UpdateAppointment.ui",self)
            self.setWindowTitle("Update Appointment")
    
            self.lineName.setDisabled(True)
            self.lineName.setText("John Doe") 
            self.linePhone.setDisabled(True)
            self.linePhone.setText("12345689") 
            self.lineCNIC.setDisabled(True)
            self.lineCNIC.setText("1234567890123") 
            self.lineDOB.setDisabled(True)
            self.lineDOB.setText("2000-01-01")
            self.lineAge.setDisabled(True)
            self.lineAge.setText("21")
            self.lineGender.setDisabled(True)
            self.lineGender.setText("Male") 
            self.lineAddress.setDisabled(True)
            self.lineAddress.setText("123 Street, 123 City")
            self.listwidgetSymptoms.setDisabled(True)
            self.listwidgetSymptoms.addItems(["Cough", "Fever"])

            self.pushUpdate.clicked.connect(self.updatePatient)
            self.pushCancel.clicked.connect(self.close)

        def updatePatient(self):
            # update the patient's info in the database
            self.close()


class AdminMainMenu(QtWidgets.QMainWindow):

    def __init__(self):
        super(AdminMainMenu, self).__init__()
        uic.loadUi("Screens\Admin MainMenu.ui",self)
        self.setWindowTitle("Admin View")

        self.comboType.addItems(["Technician", "Receptionist", "Nurse", "Doctor"]) # for testing

        self.pushAddUser.clicked.connect(self.addUser)
        self.pushSearch.clicked.connect(self.searchUser)
        self.pushClearFilters.clicked.connect(self.clearSearchFilters)
        self.pushLogOut.clicked.connect(self.relog)
        self.pushUpdateUser.clicked.connect(self.updateUser)
        self.pushRemoveUser.clicked.connect(self.removeUser)
        self.pushClose.clicked.connect(self.close)

    def addUser(self):
        
        if self.comboType.currentText() == "Technician":
            self.addTechnicianWindow = AddTechnician()
            self.addTechnicianWindow.show()

        elif self.comboType.currentText() == "Receptionist":
            self.addReceptionistWindow = AddReceptionist()
            self.addReceptionistWindow.show()

        elif self.comboType.currentText() == "Nurse":
            self.addNurseWindow = AddNurse()
            self.addNurseWindow.show()

        elif self.comboType.currentText() == "Doctor":
            self.addDoctorWindow = AddDoctor()
            self.addDoctorWindow.show()

<<<<<<< Updated upstream
    def searchUser(self):
        # populate tablewidgetSearch with the results that match the filters
        pass
=======
            self.addDoctorWindow.closeEvent = self.searchUser

    def searchUser(self, event = None):
        # print('a')
        self.tablewidgetSearch.clearContents()
        self.tablewidgetSearch.setRowCount(0)

        cursor.execute(f"select FirstName, LastName from Users where FirstName + ' '+ LastName like '%{self.lineName.text()}%' and TypeID in (select TypeID from Types where Type = '{self.comboType.currentText()}')")

        # Fetch all rows and populate the table
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.tablewidgetSearch.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.tablewidgetSearch.setItem(row_index, col_index, item)
        
        # Adjust content display
        header = self.tablewidgetSearch.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
>>>>>>> Stashed changes

    def clearSearchFilters(self):
        self.tablewidgetSearch.clearContents()
        # repopulate with all users

    def updateUser(self):
        row = self.tablewidgetSearch.currentRow()
        type = self.comboType.currentText()

        # if row != -1: # this is the actual condition, the below is just for testing
        if type == "Technician":
            self.updateTechnicianWindow = UpdateTechnician()
            self.updateTechnicianWindow.show()
        elif type == "Receptionist":
            self.updateReceptionistWindow = UpdateReceptionist()
            self.updateReceptionistWindow.show()
        elif type == "Nurse":
            self.updateNurseWindow = UpdateNurse()
            self.updateNurseWindow.show()
        elif type == "Doctor":
            self.updateDoctorWindow = UpdateDoctor()
            self.updateDoctorWindow.show()

    def removeUser(self):
        row = self.tablewidgetSearch.currentRow()

        if row != -1:
            self.confirmation = QtWidgets.QMessageBox.warning(self, "Confirmation Box", "Are you sure you want to delete this user?", QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)

            if self.confirmation == QtWidgets.QMessageBox.StandardButton.Yes:

                # delete the selected row in tablewidgetSearch from the users table and repopulate tablewidgetSearch

                self.tablewidgetSearch.removeRow(row)

            self.tablewidgetSearch.setCurrentCell(-1,-1)

    def relog(self):
        self.confirmation = QtWidgets.QMessageBox.warning(self, "Confirmation Box", "Are you sure you want to log out?", QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)

        if self.confirmation == QtWidgets.QMessageBox.StandardButton.Yes:
            self.loginScreen = UI()
            self.loginScreen.show()
            self.close()
        else:
            pass



class AddTechnician(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(AddTechnician, self).__init__()
        uic.loadUi("Screens\Admin AddTechnician.ui",self)
        self.setWindowTitle("Add Technician")

        self.pushAdd.clicked.connect(self.addTechnician)
        self.pushCancel.clicked.connect(self.close)

    def addTechnician(self):
        # insert into users table
        self.close()

<<<<<<< Updated upstream
=======
        firstname = self.lineFirstName.text()
        lastname = self.lineLastName.text()
        password = hashpw(self.linePassword.text().encode('utf8'), salt).decode('utf8')
        if firstname != '' and lastname != '' and self.linePassword.text() != '':

            new_technician = (firstname, lastname, password, 3)
            insertTechnician  = f"insert into Users (FirstName, LastName, Password, TypeID) values (?, ?, ?, ?)"
            
            cursor.execute(insertTechnician, new_technician)
            connection.commit()

            self.close()
        
        else:
            self.ErrorWindow = QtWidgets.QMessageBox()
            self.ErrorWindow.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            self.ErrorWindow.setText("Please enter all fields correctly!")
            self.ErrorWindow.setWindowTitle("Error!")
            self.ErrorWindow.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            self.ErrorWindow.exec()
>>>>>>> Stashed changes

class AddReceptionist(QtWidgets.QMainWindow):
        
    def __init__(self):
        super(AddReceptionist, self).__init__()
        uic.loadUi("Screens\Admin AddReceptionist.ui",self)
        self.setWindowTitle("Add Receptionist")

        self.pushAdd.clicked.connect(self.addReceptionist)
        self.pushCancel.clicked.connect(self.close)

    def addReceptionist(self):
        # insert into users table
        self.close()


class AddNurse(QtWidgets.QMainWindow):

    def __init__(self):
        super(AddNurse, self).__init__()
        uic.loadUi("Screens\Admin AddNurse.ui",self)
        self.setWindowTitle("Add Nurse")

        self.pushAdd.clicked.connect(self.addNurse)
        self.pushCancel.clicked.connect(self.close)

    def addNurse(self):
        # insert into users table
        self.close()


class AddDoctor(QtWidgets.QMainWindow):

    def __init__(self):
        super(AddDoctor, self).__init__()
        uic.loadUi("Screens\Admin AddDoctor.ui",self)
        self.setWindowTitle("Add Doctor")

        self.pushAdd.clicked.connect(self.addDoctor)
        self.pushCancel.clicked.connect(self.close)

    def addDoctor(self):
        # insert into users table
        self.close()


class UpdateTechnician(QtWidgets.QMainWindow):

    def __init__(self):
        super(UpdateTechnician, self).__init__()
        uic.loadUi("Screens\Admin UpdateTechnician.ui",self)
        self.setWindowTitle("Update Technician")

        self.pushUpdate.clicked.connect(self.updateTechnician)
        self.pushCancel.clicked.connect(self.close)

    def updateTechnician(self):
        # update the technician's info in the database
        self.close()

class UpdateReceptionist(QtWidgets.QMainWindow):

    def __init__(self):
        super(UpdateReceptionist, self).__init__()
        uic.loadUi("Screens\Admin UpdateReceptionist.ui",self)
        self.setWindowTitle("Update Receptionist")

        self.pushUpdate.clicked.connect(self.updateReceptionist)
        self.pushCancel.clicked.connect(self.close)

    def updateReceptionist(self):
        # update the receptionist's info in the database
        self.close()


class UpdateNurse(QtWidgets.QMainWindow):

    def __init__(self):
        super(UpdateNurse, self).__init__()
        uic.loadUi("Screens\Admin UpdateNurse.ui",self)
        self.setWindowTitle("Update Nurse")

        self.pushUpdate.clicked.connect(self.updateNurse)
        self.pushCancel.clicked.connect(self.close)

    def updateNurse(self):
        # update the nurse's info in the database
        self.close()


class UpdateDoctor(QtWidgets.QMainWindow):

    def __init__(self):
        super(UpdateDoctor, self).__init__()
        uic.loadUi("Screens\Admin UpdateDoctor.ui",self)
        self.setWindowTitle("Update Doctor")

        self.pushUpdate.clicked.connect(self.updateDoctor)
        self.pushCancel.clicked.connect(self.close)

    def updateDoctor(self):
        # update the doctor's info in the database
        self.close()



app = QtWidgets.QApplication(sys.argv) 
window = UI() 
window.show()


app.exec() 