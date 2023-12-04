select * from Doctors

begin tran
insert into Doctors
values ()
rollback
select * from Doctors

begin tran
insert into Doctors (SpecializationID, NurseID, RoomID, ConsultationCost)
values
	((select UserID from users where typeid in 
			((select TypeID from Types
			where type = 'Doctor'))),
			(select SpecializationID from Specialization
			where Specialization = 'Orthopedics'),
			(),
			(select RoomID from Rooms
			where RoomName ='W-243'),
			(1000))

--doctor insert query
insert into Doctors(DoctorID,SpecializationID ,NurseID, RoomID, ConsultationCost)
values(25,3,18,5,2100)  
select * from Doctors
select * from Users
select * from Appointments
select * from Specialization
rollback

--doctor update query
update Doctors
set RoomID = 7
where DoctorID= 27
select * from Doctors  

--update user
update Users
set TypeID = 5
where UserID =36
select * from Users

--delete query
delete from Doctors
where DoctorID = 12
select * from Doctors

select UserID from users where typeid in 
			((select TypeID from Types
			where type = 'Doctor'))

select * from users
select * from Specialization
select * from Rooms

-- query for inserting a user
begin tran
insert into Users (FirstName, LastName, Password, TypeID)
values ('Adnan', 'Ahmed', '4142',(select TypeID from Types
			where type = 'Doctor'))
select * from Users where TypeID =2
--select * from Types
rollback



--updating password:
begin tran
update Users
set Password = '1415'
where UserID = '20'
select * from Users
rollback

--query for inserting a room
begin tran
insert into Rooms (RoomName)
values ('E-220')
select * from Rooms
rollback
--ROOMS:
/*H-507
W-243 done
N-219 done
C-200 done
E-100
E-215
W-111
C-109
W-110
W-300
N-220 - 11*/ 


--query for inserting a nurse
begin tran
insert into Nurse (RoomName)
values ('N-220')
select * from 
rollback

--doctor: type id = 2
-- receptionist: type id =1
-- nurse: type id = 5
-- technician = 3
-- admin: 4
-- date stpred as year month day
SELECT * FROM Appointments WHERE DATEPART(DY, DATE) >= DATEPART(DY,GETDATE())
SELECT * FROM PatientInfo

SELECT P.FirstName + ' ' + P.LastName as Patient, P.MR, U.FirstName + ' ' + U.LastName as Doctor, R.RoomName, A.Date FROM Appointments A, Users U, PatientInfo P, Doctors D, Rooms R WHERE A.MR = P.MR AND A.DoctorID = U.UserID AND A.DoctorID = D.DoctorID AND D.RoomID = R.RoomID AND A.Date = '{self.dateEdit.text()}' AND A.StatusID = S.StatusID AND S.Status = 'Upcoming' ORDER BY A.Date ASC
begin tran
INSERT INTO Appointments(MR, DoctorID, Date, StatusID)
VALUES (15, 12, '2023-12-13', 1)
commit
rollback

SELECT P.MR, P.FirstName + ' ' + P.LastName as Patient, U.FirstName + ' ' + U.LastName as Doctor, R.RoomName, A.Date FROM Appointments A, Users U, PatientInfo P, Doctors D, Rooms R, Status S WHERE A.MR = P.MR AND A.DoctorID = U.UserID AND A.DoctorID = D.DoctorID AND D.RoomID = R.RoomID AND DATEPART(DY, A.Date) >= DATEPART(DY,GETDATE()) AND A.StatusID = S.StatusID AND S.Status = 'Upcoming' ORDER BY A.Date ASC
begin tran
DELETE FROM Appointments WHERE MR = 15 AND Date = '2023-12-13'
rollback