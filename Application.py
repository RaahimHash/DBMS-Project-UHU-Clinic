# Importing essential modules
from PyQt6 import QtWidgets, uic, QtCore 
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHeaderView
from bcrypt import hashpw, checkpw, gensalt # hashing
import sys
import pyodbc
import qdarktheme

# server = 'DESKTOP-HT3NB74
server = 'DESKTOP-F3QE491\IBAD' 
database = 'Final_Final_Project'  
use_windows_authentication = True 

connection = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;')
cursor = connection.cursor()

class UI(QtWidgets.QMainWindow):
    def __init__(self):
        super(UI, self).__init__() 
        uic.loadUi('Screens\Login Screen.ui', self) 
        self.setWindowTitle("DBClinic")

        # Fixes the screen and Disables Maximize Button
        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)

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
        if self.typeCombo.currentText() == 'Doctor':
            self.usernameCombo.clear()
            cursor.execute("""
                            select FirstName + ' ' + LastName as UserName from Users
                            where TypeID in (
				            select TypeID from Types
				            where type = 'Doctor')""")

        elif self.typeCombo.currentText() == 'Receptionist':
            self.usernameCombo.clear()
            cursor.execute("""
                            select FirstName + ' ' + LastName as UserName from Users
                            where TypeID in (
				            select TypeID from Types
				            where type = 'Receptionist')""")

        elif self.typeCombo.currentText() == 'Nurse':
            self.usernameCombo.clear()
            cursor.execute("""
                            select FirstName + ' ' + LastName as UserName from Users
                            where TypeID in (
				            select TypeID from Types
				            where type = 'Nurse')""")

        elif self.typeCombo.currentText() == 'Technician':
            self.usernameCombo.clear()
            cursor.execute("""
                            select FirstName + ' ' + LastName as UserName from Users
                            where TypeID in (
				            select TypeID from Types
				            where type = 'Technician')""")

        elif self.typeCombo.currentText() == 'Administrator':
            self.usernameCombo.clear()
            cursor.execute("""
                            select FirstName + ' ' + LastName as UserName from Users
                            where TypeID in (
				            select TypeID from Types
				            where type = 'Administrator')""")


        for i in cursor.fetchall():
            self.usernameCombo.addItems(i)

        self.usernameCombo.setCurrentIndex(0)

    def signin(self):
        # cursor.execute(  f'select password from Users where FirstName + ' ' + LastName =  {self.usernameCombo.currentText()} and typeID = ( select typeID from Types where Type = {self.typeCombo.currentText()})')
        #print(cursor.fetchall())
        cursor.execute("select Password from Users where FirstName + ' ' + LastName = '" + str(self.usernameCombo.currentText()) + "'" )#+ " and TypeID = ( select typeID from Types where Type ='" + str(self.typeCombo.currentText()) + "'" )

        # print(self.passwordLine.text() , str(cursor.fetchall()[0][0]))
        currentUser = self.usernameCombo.currentText()
        if checkpw(self.passwordLine.text().encode('utf-8'),str(cursor.fetchall()[0][0]).encode('utf-8')): # and it matches the password of the user whose username is selected in the usernameCombo
            if self.typeCombo.currentText() == "Receptionist":
                self.receptionistscreen = ReceptionistMainMenu()
                self.receptionistscreen.show()
                self.close()

            elif self.typeCombo.currentText() == "Doctor":
                self.doctorscreen = DoctorMainMenu(currentUser)
                self.doctorscreen.show()
                self.close()

            elif self.typeCombo.currentText() == "Nurse":
                self.nursescreen = NurseMainMenu()
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

        # Fixes the screen and Disables Maximize Button
        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)
        

        
        cursor.execute("""
                    select FirstName + ' ' + LastName as UserName from Users
                    where TypeID in (
                    select TypeID from Types
                    where type = 'Doctor')""")
                    
        self.comboDoctor.addItems(('',))
        for i in cursor.fetchall():
            self.comboDoctor.addItems(i)
        
        self.comboDoctor.setCurrentIndex(0)
        
        self.populateWaitlist()
        self.pushAdd.clicked.connect(self.addPatient)
        self.pushSearch.clicked.connect(self.searchPatient)
        self.pushBook.clicked.connect(self.bookAppointment)
        self.pushClear.clicked.connect(self.clearSearch)
        self.pushSearchWaitlist.clicked.connect(self.searchWaitlist)
        self.pushClearFilters.clicked.connect(self.populateWaitlist)
        self.pushCancel.clicked.connect(self.cancelAppointment)
        self.pushRefreshWaitlist.clicked.connect(self.searchWaitlist) # connected here cos it should just redo the query with the same filters
        # self.pushClose.clicked.connect(self.close)
        self.pushLogOut.clicked.connect(self.relog)

    def addPatient(self):
        self.addPatientWindow = AddPatient() # calling a constructor which has the real AddPatient function
        self.addPatientWindow.show()

    def searchPatient(self):
        self.tablewidgetSearch.clearContents()
        self.tablewidgetSearch.setRowCount(0)
        # populate tablewidgetSearch with the results that contain lineMR and linePhone
        # cursor.execute(f"SELECT MR, FirstName + ' ' + LastName as Name, PhoneNum FROM PatientInfo where MR = {str(self.lineMR.text())} and PhoneNum like '{str(self.linePhone.text())}%'")

        if str(self.lineMR.text()).strip() ==  '':
            # print("hello")
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
            Name = self.tablewidgetSearch.item(row,1).text()
            Phone = self.tablewidgetSearch.item(row,2).text()

            self.bookAppointmentWindow = BookAppointment(Name,Phone)
            self.bookAppointmentWindow.show()

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

    def searchWaitlist(self):
        # populate tablewidgetWaitlist with the results that match Doctor and Date
        self.tablewidgetWaitlist.clearContents()
        self.tablewidgetWaitlist.setRowCount(0)

        if self.comboDoctor.currentText().strip() == '':
            cursor.execute(f"SELECT P.MR, P.FirstName + ' ' + P.LastName as Patient, U.FirstName + ' ' + U.LastName as Doctor, R.RoomName, A.Date FROM Appointments A, Users U, PatientInfo P, Doctors D, Rooms R, Status S WHERE A.MR = P.MR AND A.DoctorID = U.UserID AND A.DoctorID = D.DoctorID AND D.RoomID = R.RoomID AND A.Date = '{self.dateEdit.text()}' AND A.StatusID = S.StatusID AND S.Status = 'Upcoming' ORDER BY A.Date ASC")
        else:
            cursor.execute(f"SELECT P.MR, P.FirstName + ' ' + P.LastName as Patient, U.FirstName + ' ' + U.LastName, R.RoomName, A.Date FROM Appointments A, Users U, PatientInfo P, Doctors D, Rooms R, Status S WHERE A.MR = P.MR AND A.DoctorID = U.UserID AND A.DoctorID = D.DoctorID AND D.RoomID = R.RoomID AND A.Date = '{self.dateEdit.text()}' AND U.FirstName + ' ' + U.LastName = '{self.comboDoctor.currentText()}' AND A.StatusID = S.StatusID AND S.Status = 'Upcoming' ORDER BY A.Date ASC")

        # Fetch all rows and populate the table
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.tablewidgetWaitlist.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.tablewidgetWaitlist.setItem(row_index, col_index, item)

    def populateWaitlist(self):
        # repopulate with all upcoming appointments
        self.tablewidgetWaitlist.clearContents()
        self.tablewidgetWaitlist.setRowCount(0)

        cursor.execute("SELECT P.MR, P.FirstName + ' ' + P.LastName as Patient, U.FirstName + ' ' + U.LastName as Doctor, R.RoomName, A.Date FROM Appointments A, Users U, PatientInfo P, Doctors D, Rooms R, Status S WHERE A.MR = P.MR AND A.DoctorID = U.UserID AND A.DoctorID = D.DoctorID AND D.RoomID = R.RoomID AND DATEPART(DY, A.Date) >= DATEPART(DY,GETDATE()) AND A.StatusID = S.StatusID AND S.Status = 'Upcoming' ORDER BY A.Date ASC")

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
                # NEEDS TO BE EDITED WITH THE TURN NUMBER SO IT DOESN'T DELETE MULTIPLE APPOINTMENTS
                cursor.execute (f'''
                DELETE FROM Appointments 
                WHERE MR = {int(self.tablewidgetWaitlist.item(row,0).text())} AND Date = '{self.tablewidgetWaitlist.item(row,4).text()}'
                ''')
                connection.commit()

            self.tablewidgetWaitlist.setCurrentCell(-1,-1)

        else:
            self.ErrorWindow = QtWidgets.QMessageBox()
            self.ErrorWindow.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            self.ErrorWindow.setText("Please select an appointment to cancel.")
            self.ErrorWindow.setWindowTitle("Please select an appointment.")
            self.ErrorWindow.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            self.ErrorWindow.exec()

    def relog(self):
        self.confirmation = QtWidgets.QMessageBox.warning(self, "Confirmation Box", "Are you sure you want to log out?", QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)

        if self.confirmation == QtWidgets.QMessageBox.StandardButton.Yes:
            self.loginScreen = UI()
            self.loginScreen.show()
            self.close()
        else:
            pass




class BookAppointment(QtWidgets.QMainWindow):
    
    def __init__(self, Name, Phone):
        super(BookAppointment, self).__init__()
        uic.loadUi("Screens\Receptionist AddAppointment.ui",self)
        self.setWindowTitle("Book Appointment")

        # Fixes the screen and Disables Maximize Button
        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)
        
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

        firstName = Name.split()[0]
        lastName = Name.split()[-1]

        self.lineFirstName.setDisabled(True)
        self.lineFirstName.setText(firstName) # first name of the patient whose row was selected in the search tablewidget, comes from query or just accessing the tablewidget
        self.lineLastName.setDisabled(True)
        self.lineLastName.setText(lastName) # last name of the patient whose row was selected in the search tablewidget, comes from query or just accessing the tablewidget
        self.linePhone.setDisabled(True)
        self.linePhone.setText(Phone) # phone of the patient whose row was selected in the search tablewidget, comes from query or just accessing the tablewidget

        self.populateSpecialization()
        self.populateDoctor()
        self.showAmount()
        self.comboSpecialization.currentIndexChanged.connect(self.populateDoctor)
        self.comboDoctor.currentIndexChanged.connect(self.showAmount)

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
        # print(self.comboDoctor.currentText())
        cursor.execute(f"SELECT ConsultationCost FROM Doctors WHERE DoctorID IN (SELECT UserID FROM Users WHERE FirstName + ' ' + LastName = '{self.comboDoctor.currentText()}')")
        # print(cursor.fetchall())
        fetched = cursor.fetchall()
        if fetched != []:
            self.lineAmount.setText(str(fetched[0][0]))
        else:
            self.lineAmount.setText('None')

    def confirmAppointment(self):
        # insert into appointments table if there is no existing appointment at the given date and time
        self.close()

class AddPatient(QtWidgets.QMainWindow):
    def __init__(self):
        super(AddPatient, self).__init__()
        uic.loadUi("Screens\Receptionist AddPatient.ui",self)
        self.setWindowTitle("Add Patient")

        # Fixes the screen and Disables Maximize Button
        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)
        
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

        # Fixes the screen and Disables Maximize Button
        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)
        
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
        
        # Fixes the screen and Disables Maximize Button
        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)
        
        self.pushUpdate.clicked.connect(self.updatePatient)
        self.pushCancel.clicked.connect(self.close)

    def updatePatient(self):
        # update the patient's info in the database
        self.close()


class NurseMainMenu(QtWidgets.QMainWindow):

    def __init__(self):
        super(NurseMainMenu, self).__init__()
        uic.loadUi("Screens\\Nurse MainMenu.ui",self)
        self.setWindowTitle("Nurse View")
        
        # Fixes the screen and Disables Maximize Button
        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)
        
        self.lineDoctorAssigned.setDisabled(True)
        self.lineDoctorAssigned.setText("John Doe") # name of the doctor the nurse is assigned to, comes from query
        self.lineRoomAssigned.setDisabled(True)
        self.lineRoomAssigned.setText("1") # room number of the doctor the nurse is assigned to, comes from query
        self.lineMR.setDisabled(True)
        self.lineMR.setText("123456") # MR of the the patient that has an ongoing appointment with the doctor, comes from query
        self.lineName.setDisabled(True)
        self.lineName.setText("Jane Doe") # name of the the patient that has an ongoing appointment with the doctor, comes from query
        
        self.pushAddSymptom.clicked.connect(self.addSymptom)
        self.pushRemoveSymptom.clicked.connect(self.removeSymptom)
        self.pushUpdateStatus.clicked.connect(self.updateStatus)
        self.pushLogOut.clicked.connect(self.relog)
        self.pushClose.clicked.connect(self.close)

    def addSymptom(self):
        # add the selected symptom from comboSymptoms to the listwidgetSymptoms if it doesn't already exist
        pass

    def removeSymptom(self):
        row = self.listwidgetSymptoms.currentRow()

        if row != -1:
            # remove the selected symptom from listwidgetSymptoms
            self.listwidgetSymptoms.takeItem(row)
            self.listwidgetSymptoms.setCurrentRow(-1)

    def updateStatus(self):
        # update the status of the patient in the database and update lineMR and lineName with the next patient's info
        pass

    def relog(self):
        self.confirmation = QtWidgets.QMessageBox.warning(self, "Confirmation Box", "Are you sure you want to log out?", QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)

        if self.confirmation == QtWidgets.QMessageBox.StandardButton.Yes:
            self.loginScreen = UI()
            self.loginScreen.show()
            self.close()
        else:
            pass


class DoctorMainMenu(QtWidgets.QMainWindow):

    def __init__(self, currentUser):
        super(DoctorMainMenu, self).__init__()
        uic.loadUi("Screens\Doctor MainMenu.ui",self)
        self.setWindowTitle("Doctor View")
        
        # Fixes the screen and Disables Maximize Button
        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)
        
        currentUser = currentUser.split()
        cursor.execute(f"select FirstName,LastName from Users where UserID in (select NurseID from Doctors where DoctorID in(select UserID from Users where FirstName = '{currentUser[0]}' and LastName = '{currentUser[1]}'))")
        self.lineNurseAssigned.setDisabled(True)
        self.lineNurseAssigned.setText(" ".join(cursor.fetchall()[0]))
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
        
        # Fixes the screen and Disables Maximize Button
        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)
        
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
        
        # Fixes the screen and Disables Maximize Button
        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)
        
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
            
            # Fixes the screen and Disables Maximize Button
            self.width = self.frameGeometry().width()
            self.height = self.frameGeometry().height()
            self.setFixedSize(self.width, self.height)
            
            self.lineName.setDisabled(True)
            self.lineName.setText("John Doe") # name of the the patient that whose row was selected in the search tablewidget, comes from query or just accessing the tablewidget
            self.linePhone.setDisabled(True)
            self.linePhone.setText("12345689") # phone of the the patient that whose row was selected in the search tablewidget, comes from query or just accessing the tablewidget
            self.lineCNIC.setDisabled(True)
            self.lineCNIC.setText("1234567890123") # CNIC of the the patient that whose row was selected in the search tablewidget, comes from query or just accessing the tablewidget
            self.lineDOB.setDisabled(True)
            self.lineDOB.setText("2000-01-01") # DOB of the the patient that whose row was selected in the search tablewidget, comes from query or just accessing the tablewidget
            self.lineAge.setDisabled(True)
            self.lineAge.setText("21") # age of the the patient that whose row was selected in the search tablewidget, comes from query or just accessing the tablewidget
            self.lineGender.setDisabled(True)
            self.lineGender.setText("Male") # gender of the the patient that whose row was selected in the search tablewidget, comes from query or just accessing the tablewidget
            self.lineAddress.setDisabled(True)
            self.lineAddress.setText("123 Street, 123 City") # address of the the patient that whose row was selected in the search tablewidget, comes from query or just accessing the tablewidget
            self.listwidgetSymptoms.setDisabled(True)
            self.listwidgetSymptoms.addItems(["Cough", "Fever"]) # symptoms of the the patient that whose row was selected in the search tablewidget, comes from query or just accessing the tablewidget

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
        
        # Fixes the screen and Disables Maximize Button
        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)

        cursor.execute("select type from Types where TypeID != 4")
        for i in cursor.fetchall():
            self.comboType.addItems(i)
        
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

    def searchUser(self):
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


    def clearSearchFilters(self):
        self.tablewidgetSearch.clearContents()
        # repopulate with all users

    def updateUser(self):
        row = self.tablewidgetSearch.currentRow()
        type = self.comboType.currentText()
        
        if row != -1:

            firstName = self.tablewidgetSearch.item(row,0).text()
            lastName = self.tablewidgetSearch.item(row,1).text()

            if type == "Technician":
                self.updateTechnicianWindow = UpdateTechnician(firstName, lastName)
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

            self.tablewidgetSearch.setCurrentCell(-1,-1)

        else:
            self.ErrorWindow = QtWidgets.QMessageBox()
            self.ErrorWindow.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            self.ErrorWindow.setText("Please select a User")
            self.ErrorWindow.setWindowTitle("Please select a User")
            self.ErrorWindow.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            self.ErrorWindow.exec()

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
        
        # Fixes the screen and Disables Maximize Button
        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)
        
        self.pushAdd.clicked.connect(self.addTechnician)
        self.pushCancel.clicked.connect(self.close)

    def addTechnician(self):
        # insert into users table
        self.close()


class AddReceptionist(QtWidgets.QMainWindow):
        
    def __init__(self):
        super(AddReceptionist, self).__init__()
        uic.loadUi("Screens\Admin AddReceptionist.ui",self)
        self.setWindowTitle("Add Receptionist")
        
        # Fixes the screen and Disables Maximize Button
        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)
        
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
        
        # Fixes the screen and Disables Maximize Button
        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)
        
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
        
        # Fixes the screen and Disables Maximize Button
        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)
        
        self.pushAdd.clicked.connect(self.addDoctor)
        self.pushCancel.clicked.connect(self.close)

    def addDoctor(self):
        # insert into users table
        self.close()


class UpdateTechnician(QtWidgets.QMainWindow):

    def __init__(self, firstName, lastName):
        super(UpdateTechnician, self).__init__()
        uic.loadUi("Screens\Admin UpdateTechnician.ui",self)
        self.setWindowTitle("Update Technician")
        
        # Fixes the screen and Disables Maximize Button
        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)
        
        self.fN = firstName; self.lN = lastName

        self.lineFirstName.setText(self.fN)
        self.lineLastName.setText(self.lN)

        self.pushUpdate.clicked.connect(self.updateTechnician)
        self.pushCancel.clicked.connect(self.close)

    def updateTechnician(self):
        cursor.execute(f"update Users set FirstName = '{self.lineFirstName.text()}', LastName = '{self.lineLastName.text()}' where FirstName = '{self.fN}' and LastName = '{self.lN}'")
        connection.commit()
        self.close()


class UpdateReceptionist(QtWidgets.QMainWindow):

    def __init__(self):
        super(UpdateReceptionist, self).__init__()
        uic.loadUi("Screens\Admin UpdateReceptionist.ui",self)
        self.setWindowTitle("Update Receptionist")
        
        # Fixes the screen and Disables Maximize Button
        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)
        
        self.pushUpdate.clicked.connect(self.updateReceptionist)
        self.pushCancel.clicked.connect(self.close)

    def updateReceptionist(self):
        # update the receptionist's info in the database
        self.close()


class UpdateNurse(QtWidgets.QMainWindow):

    def __init__(self, row):
        super(UpdateNurse, self).__init__()
        uic.loadUi("Screens\Admin UpdateNurse.ui",self)
        self.setWindowTitle("Update Nurse")
        # print(self.row)
        # Fixes the screen and Disables Maximize Button
        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)
        
        self.pushUpdate.clicked.connect(self.updateNurse)
        self.pushCancel.clicked.connect(self.close)

    def updateNurse(self):
        print(self.lineFirstName.text())
        print(self.lineLastName.text())
        self.close()


class UpdateDoctor(QtWidgets.QMainWindow):

    def __init__(self):
        super(UpdateDoctor, self).__init__()
        uic.loadUi("Screens\Admin UpdateDoctor.ui",self)
        self.setWindowTitle("Update Doctor")
        
        # Fixes the screen and Disables Maximize Button
        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setFixedSize(self.width, self.height)
        
        self.pushUpdate.clicked.connect(self.updateDoctor)
        self.pushCancel.clicked.connect(self.close)

    def updateDoctor(self):
        # update the doctor's info in the database
        self.close()

app = QtWidgets.QApplication(sys.argv) 

# qdarktheme.setup_theme()

window = UI() 
window.show()


app.exec() 