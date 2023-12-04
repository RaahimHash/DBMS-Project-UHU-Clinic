
select * from Users
select * from Types
select * from Doctors


select FirstName + ' ' + LastName as UserName from Users
where TypeID in (
				select TypeID from Types
				where type = 'Doctor')


insert into Users
values('Salman','Qureshi', 1234)

select TypeID from Types




/*insert into Doctors
values
	((select UserID from users where typeid in 
			((select TypeID from Types
			where type = 'Doctor'))),
			(select SpecializationID from Specialization
			where Specialization = 'Cardiology'),
			(select RoomID from Rooms
			where RoomName ='H-507'),
			(2000))*/

set identity_insert Doctors on
insert into Doctors(DoctorID, SpecializationID, NurseID, RoomID, ConsultationCost)
values (35,7, 36, 15,1400)

select FirstName + ' '+ LastName as DocName from Users where UserID in

(select DoctorID from Doctors
where ConsultationCost between 1000 and 2000)

insert into Users
values('Hania','Kashif', 9821,5)
select * from Users
where TypeID =5

delete from Users
where UserID>=9

select * from users


select * from users
where TypeID in (select typeid from types)




set identity_insert PatientInfo on
INSERT INTO patientInfo (FirstName, LastName, PhoneNum, DateOfBirth,GenderID, CNIC, Age, Address)
VALUES
    ('John', 'Doe', '123-456-7890', '1985-05-15', 1,'123-45-6789', 37, '123 Main Street, Cityville'),
    ('Jane', 'Smith', '987-654-3210', '1990-12-10', 2, '987-65-4321', 31, '456 Oak Avenue, Townsville'),
    ('Michael', 'Johnson', '555-123-4567', '1978-08-22',3, '555-12-3456', 44, '789 Pine Road, Villagetown'),
    ('Emily', 'Davis', '222-333-4444', '1982-04-05', 3,'222-33-4444', 40, '567 Maple Lane, Hamlet City'),
    ('Robert', 'White', '777-888-9999', '1995-11-28',1, '777-88-9999', 26, '890 Cedar Street, Riverside');

select * from Gender
select * from Doctors
select * from Specialization
select * from Rooms
select * from Users
select * from Types
select * from PatientInfo


SELECT MR, FirstName + ' ' + LastName as Name, PhoneNum FROM PatientInfo
where MR = 1 and PhoneNum like '1%'
	



select Genders from Gender where genderId in (select GenderID from PatientInfo)

select FirstName, LastName, PhoneNum, CNIC, DateOfBirth, Age, (select Genders from Gender where genderId in (select GenderID from PatientInfo)),Address from PatientInfo
select * from Gender
select * from PatientInfo

delete from PatientInfo
where mr = 8

select FirstName + ' ' + LastName as UserName from Users where UserID IN (SELECT DoctorID FROM Doctors WHERE SpecializationID = (SELECT SpecializationID FROM Specialization WHERE Specialization = 'Cardiology'))
Select * from users
SELECT ConsultationCost FROM Doctors WHERE DoctorID IN (SELECT UserID FROM Users WHERE FirstName + ' ' + LastName = 'Eman Fatima')
SELECT GETDATE() 
SELECT DATEPART(day,GETDATE()), DATEPART(month,GETDATE()), DATEPART(year,GETDATE())

select * from Specialization
select * from Users

select * from Appointments
select * from AppointmentSymptoms
select * from Symptoms