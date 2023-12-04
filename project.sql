USE [master]
GO
/****** Object:  Database [project]    Script Date: 05-Dec-23 4:27:19 AM ******/
CREATE DATABASE [project]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'project', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.IBAD\MSSQL\DATA\project.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'project_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.IBAD\MSSQL\DATA\project_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT, LEDGER = OFF
GO
ALTER DATABASE [project] SET COMPATIBILITY_LEVEL = 160
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [project].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [project] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [project] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [project] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [project] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [project] SET ARITHABORT OFF 
GO
ALTER DATABASE [project] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [project] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [project] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [project] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [project] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [project] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [project] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [project] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [project] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [project] SET  DISABLE_BROKER 
GO
ALTER DATABASE [project] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [project] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [project] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [project] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [project] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [project] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [project] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [project] SET RECOVERY FULL 
GO
ALTER DATABASE [project] SET  MULTI_USER 
GO
ALTER DATABASE [project] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [project] SET DB_CHAINING OFF 
GO
ALTER DATABASE [project] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [project] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [project] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [project] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
EXEC sys.sp_db_vardecimal_storage_format N'project', N'ON'
GO
ALTER DATABASE [project] SET QUERY_STORE = ON
GO
ALTER DATABASE [project] SET QUERY_STORE (OPERATION_MODE = READ_WRITE, CLEANUP_POLICY = (STALE_QUERY_THRESHOLD_DAYS = 30), DATA_FLUSH_INTERVAL_SECONDS = 900, INTERVAL_LENGTH_MINUTES = 60, MAX_STORAGE_SIZE_MB = 1000, QUERY_CAPTURE_MODE = AUTO, SIZE_BASED_CLEANUP_MODE = AUTO, MAX_PLANS_PER_QUERY = 200, WAIT_STATS_CAPTURE_MODE = ON)
GO
USE [project]
GO
/****** Object:  Table [dbo].[Appointments]    Script Date: 05-Dec-23 4:27:19 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Appointments](
	[AppointmentID] [int] IDENTITY(1,1) NOT NULL,
	[MR] [int] NOT NULL,
	[DoctorID] [int] NULL,
	[Date] [date] NOT NULL,
	[StatusID] [int] NOT NULL,
	[TurnNum] [int] NULL,
PRIMARY KEY CLUSTERED 
(
	[AppointmentID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[AppointmentSymptoms]    Script Date: 05-Dec-23 4:27:19 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[AppointmentSymptoms](
	[AppointmentID] [int] IDENTITY(1,1) NOT NULL,
	[SymptomID] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[AppointmentID] ASC,
	[SymptomID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Diagnoses]    Script Date: 05-Dec-23 4:27:19 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Diagnoses](
	[AppointmentID] [int] NOT NULL,
	[Diagnosis] [varchar](255) NOT NULL,
	[Notes] [varchar](255) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[AppointmentID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Doctors]    Script Date: 05-Dec-23 4:27:19 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Doctors](
	[DoctorID] [int] NOT NULL,
	[SpecializationID] [int] NOT NULL,
	[NurseID] [int] NULL,
	[RoomID] [int] NULL,
	[ConsultationCost] [float] NOT NULL,
	[NumPatients] [int] NULL,
PRIMARY KEY CLUSTERED 
(
	[DoctorID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Gender]    Script Date: 05-Dec-23 4:27:19 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Gender](
	[GenderID] [int] IDENTITY(1,1) NOT NULL,
	[Genders] [varchar](255) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[GenderID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Invoices]    Script Date: 05-Dec-23 4:27:19 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Invoices](
	[InvoiceID] [int] IDENTITY(1,1) NOT NULL,
	[AppointmentID] [int] NOT NULL,
	[Cost] [float] NOT NULL,
	[Date] [date] NOT NULL,
	[MR] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[InvoiceID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[PatientInfo]    Script Date: 05-Dec-23 4:27:19 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[PatientInfo](
	[PatientID] [int] IDENTITY(1,1) NOT NULL,
	[FirstName] [varchar](255) NOT NULL,
	[LastName] [varchar](255) NOT NULL,
	[PhoneNum] [varchar](255) NOT NULL,
	[DateOfBirth] [date] NOT NULL,
	[GenderID] [int] NOT NULL,
	[CNIC] [varchar](255) NOT NULL,
	[Age] [int] NULL,
	[Address] [varchar](255) NOT NULL,
	[MR] [varchar](255) NULL,
PRIMARY KEY CLUSTERED 
(
	[PatientID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Rooms]    Script Date: 05-Dec-23 4:27:19 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Rooms](
	[RoomID] [int] IDENTITY(1,1) NOT NULL,
	[RoomName] [varchar](255) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[RoomID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Specialization]    Script Date: 05-Dec-23 4:27:19 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Specialization](
	[SpecializationID] [int] IDENTITY(1,1) NOT NULL,
	[Specialization] [varchar](255) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[SpecializationID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Status]    Script Date: 05-Dec-23 4:27:19 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Status](
	[StatusID] [int] IDENTITY(1,1) NOT NULL,
	[Status] [varchar](255) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[StatusID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Symptoms]    Script Date: 05-Dec-23 4:27:19 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Symptoms](
	[SymptomsID] [int] IDENTITY(1,1) NOT NULL,
	[Symptom] [varchar](255) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[SymptomsID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Types]    Script Date: 05-Dec-23 4:27:19 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Types](
	[TypeID] [int] IDENTITY(1,1) NOT NULL,
	[Type] [varchar](255) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[TypeID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Users]    Script Date: 05-Dec-23 4:27:19 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Users](
	[UserID] [int] IDENTITY(1,1) NOT NULL,
	[FirstName] [varchar](255) NOT NULL,
	[LastName] [varchar](255) NOT NULL,
	[Password] [varchar](255) NOT NULL,
	[TypeID] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[UserID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
SET IDENTITY_INSERT [dbo].[Appointments] ON 
GO
INSERT [dbo].[Appointments] ([AppointmentID], [MR], [DoctorID], [Date], [StatusID], [TurnNum]) VALUES (7, 22, 12, CAST(N'2023-12-05' AS Date), 1, 2)
GO
INSERT [dbo].[Appointments] ([AppointmentID], [MR], [DoctorID], [Date], [StatusID], [TurnNum]) VALUES (9, 15, 27, CAST(N'2023-12-04' AS Date), 1, 1)
GO
INSERT [dbo].[Appointments] ([AppointmentID], [MR], [DoctorID], [Date], [StatusID], [TurnNum]) VALUES (10, 15, 8, CAST(N'2023-12-05' AS Date), 3, 1)
GO
INSERT [dbo].[Appointments] ([AppointmentID], [MR], [DoctorID], [Date], [StatusID], [TurnNum]) VALUES (11, 15, 12, CAST(N'2023-12-05' AS Date), 1, 3)
GO
INSERT [dbo].[Appointments] ([AppointmentID], [MR], [DoctorID], [Date], [StatusID], [TurnNum]) VALUES (12, 17, 8, CAST(N'2023-12-06' AS Date), 1, 1)
GO
INSERT [dbo].[Appointments] ([AppointmentID], [MR], [DoctorID], [Date], [StatusID], [TurnNum]) VALUES (13, 19, 8, CAST(N'2023-12-20' AS Date), 1, 1)
GO
INSERT [dbo].[Appointments] ([AppointmentID], [MR], [DoctorID], [Date], [StatusID], [TurnNum]) VALUES (14, 20, 8, CAST(N'2023-12-05' AS Date), 1, 2)
GO
SET IDENTITY_INSERT [dbo].[Appointments] OFF
GO
INSERT [dbo].[Doctors] ([DoctorID], [SpecializationID], [NurseID], [RoomID], [ConsultationCost], [NumPatients]) VALUES (2, 5, 20, 1, 5000, 2)
GO
INSERT [dbo].[Doctors] ([DoctorID], [SpecializationID], [NurseID], [RoomID], [ConsultationCost], [NumPatients]) VALUES (8, 2, 11, 2, 1000, 4)
GO
INSERT [dbo].[Doctors] ([DoctorID], [SpecializationID], [NurseID], [RoomID], [ConsultationCost], [NumPatients]) VALUES (12, 1, 16, 3, 15000, 4)
GO
INSERT [dbo].[Doctors] ([DoctorID], [SpecializationID], [NurseID], [RoomID], [ConsultationCost], [NumPatients]) VALUES (14, 2, 17, 4, 1300, 2)
GO
INSERT [dbo].[Doctors] ([DoctorID], [SpecializationID], [NurseID], [RoomID], [ConsultationCost], [NumPatients]) VALUES (25, 3, 18, 5, 2100, 5)
GO
INSERT [dbo].[Doctors] ([DoctorID], [SpecializationID], [NurseID], [RoomID], [ConsultationCost], [NumPatients]) VALUES (26, 3, 19, 6, 1500, 2)
GO
INSERT [dbo].[Doctors] ([DoctorID], [SpecializationID], [NurseID], [RoomID], [ConsultationCost], [NumPatients]) VALUES (27, 4, 20, 7, 2300, 3)
GO
INSERT [dbo].[Doctors] ([DoctorID], [SpecializationID], [NurseID], [RoomID], [ConsultationCost], [NumPatients]) VALUES (28, 4, 21, 8, 1100, 4)
GO
INSERT [dbo].[Doctors] ([DoctorID], [SpecializationID], [NurseID], [RoomID], [ConsultationCost], [NumPatients]) VALUES (29, 5, 22, 9, 1200, 6)
GO
INSERT [dbo].[Doctors] ([DoctorID], [SpecializationID], [NurseID], [RoomID], [ConsultationCost], [NumPatients]) VALUES (30, 5, 23, 10, 1500, 5)
GO
INSERT [dbo].[Doctors] ([DoctorID], [SpecializationID], [NurseID], [RoomID], [ConsultationCost], [NumPatients]) VALUES (31, 6, 24, 11, 1600, 6)
GO
INSERT [dbo].[Doctors] ([DoctorID], [SpecializationID], [NurseID], [RoomID], [ConsultationCost], [NumPatients]) VALUES (32, 7, 38, 12, 800, 4)
GO
INSERT [dbo].[Doctors] ([DoctorID], [SpecializationID], [NurseID], [RoomID], [ConsultationCost], [NumPatients]) VALUES (33, 8, 39, 13, 2100, 3)
GO
INSERT [dbo].[Doctors] ([DoctorID], [SpecializationID], [NurseID], [RoomID], [ConsultationCost], [NumPatients]) VALUES (34, 6, 37, 14, 2500, 2)
GO
INSERT [dbo].[Doctors] ([DoctorID], [SpecializationID], [NurseID], [RoomID], [ConsultationCost], [NumPatients]) VALUES (35, 7, 36, 15, 1400, 5)
GO
INSERT [dbo].[Doctors] ([DoctorID], [SpecializationID], [NurseID], [RoomID], [ConsultationCost], [NumPatients]) VALUES (40, 1, 6, 1, 1467, 15)
GO
SET IDENTITY_INSERT [dbo].[Gender] ON 
GO
INSERT [dbo].[Gender] ([GenderID], [Genders]) VALUES (1, N'Male')
GO
INSERT [dbo].[Gender] ([GenderID], [Genders]) VALUES (2, N'Female')
GO
INSERT [dbo].[Gender] ([GenderID], [Genders]) VALUES (3, N'Prefer not to say')
GO
SET IDENTITY_INSERT [dbo].[Gender] OFF
GO
SET IDENTITY_INSERT [dbo].[Invoices] ON 
GO
INSERT [dbo].[Invoices] ([InvoiceID], [AppointmentID], [Cost], [Date], [MR]) VALUES (2, 7, 15000, CAST(N'2023-04-12' AS Date), 22)
GO
INSERT [dbo].[Invoices] ([InvoiceID], [AppointmentID], [Cost], [Date], [MR]) VALUES (4, 9, 2300, CAST(N'2023-04-12' AS Date), 15)
GO
INSERT [dbo].[Invoices] ([InvoiceID], [AppointmentID], [Cost], [Date], [MR]) VALUES (5, 10, 1000, CAST(N'2023-05-12' AS Date), 15)
GO
INSERT [dbo].[Invoices] ([InvoiceID], [AppointmentID], [Cost], [Date], [MR]) VALUES (6, 11, 15000, CAST(N'2023-05-12' AS Date), 15)
GO
INSERT [dbo].[Invoices] ([InvoiceID], [AppointmentID], [Cost], [Date], [MR]) VALUES (7, 12, 1000, CAST(N'2023-05-12' AS Date), 17)
GO
INSERT [dbo].[Invoices] ([InvoiceID], [AppointmentID], [Cost], [Date], [MR]) VALUES (8, 13, 1000, CAST(N'2023-05-12' AS Date), 19)
GO
INSERT [dbo].[Invoices] ([InvoiceID], [AppointmentID], [Cost], [Date], [MR]) VALUES (9, 14, 1000, CAST(N'2023-05-12' AS Date), 20)
GO
SET IDENTITY_INSERT [dbo].[Invoices] OFF
GO
SET IDENTITY_INSERT [dbo].[PatientInfo] ON 
GO
INSERT [dbo].[PatientInfo] ([PatientID], [FirstName], [LastName], [PhoneNum], [DateOfBirth], [GenderID], [CNIC], [Age], [Address], [MR]) VALUES (13, N'John', N'Doe', N'123-456-7890', CAST(N'1985-05-15' AS Date), 1, N'123-45-6789', 38, N'123 Main Street, Cityville', N'13')
GO
INSERT [dbo].[PatientInfo] ([PatientID], [FirstName], [LastName], [PhoneNum], [DateOfBirth], [GenderID], [CNIC], [Age], [Address], [MR]) VALUES (14, N'Jane', N'Smith', N'987-654-3210', CAST(N'1990-12-10' AS Date), 2, N'987-65-4321', 33, N'456 Oak Avenue, Townsville', N'14')
GO
INSERT [dbo].[PatientInfo] ([PatientID], [FirstName], [LastName], [PhoneNum], [DateOfBirth], [GenderID], [CNIC], [Age], [Address], [MR]) VALUES (15, N'Michael', N'Johnson', N'555-123-4567', CAST(N'1978-08-22' AS Date), 3, N'555-12-3456', 45, N'789 Pine Road, Villagetown', N'15')
GO
INSERT [dbo].[PatientInfo] ([PatientID], [FirstName], [LastName], [PhoneNum], [DateOfBirth], [GenderID], [CNIC], [Age], [Address], [MR]) VALUES (16, N'Emily', N'Davis', N'222-333-4444', CAST(N'1982-04-05' AS Date), 3, N'222-33-4444', 41, N'567 Maple Lane, Hamlet City', N'16')
GO
INSERT [dbo].[PatientInfo] ([PatientID], [FirstName], [LastName], [PhoneNum], [DateOfBirth], [GenderID], [CNIC], [Age], [Address], [MR]) VALUES (17, N'Robert', N'White', N'777-888-9999', CAST(N'1995-11-28' AS Date), 1, N'777-88-9999', 28, N'890 Cedar Street, Riverside', N'17')
GO
INSERT [dbo].[PatientInfo] ([PatientID], [FirstName], [LastName], [PhoneNum], [DateOfBirth], [GenderID], [CNIC], [Age], [Address], [MR]) VALUES (18, N'Aina', N'Shakeel', N'0315-9275824', CAST(N'2013-01-01' AS Date), 2, N'42310-62868295-1', 10, N'Dhoraji, Karachi', N'18')
GO
INSERT [dbo].[PatientInfo] ([PatientID], [FirstName], [LastName], [PhoneNum], [DateOfBirth], [GenderID], [CNIC], [Age], [Address], [MR]) VALUES (19, N'John', N'Cena', N'123-321-231', CAST(N'2000-01-01' AS Date), 1, N'42201-153543-5', 23, N'House 43-B, Bahria Town, Lahore', N'19')
GO
INSERT [dbo].[PatientInfo] ([PatientID], [FirstName], [LastName], [PhoneNum], [DateOfBirth], [GenderID], [CNIC], [Age], [Address], [MR]) VALUES (20, N'Maria', N'Adnan', N'123-344-454', CAST(N'2021-01-01' AS Date), 2, N'42201-435354-3', 2, N'Pehlwan Goth, Habib University, Islamabad', N'20')
GO
INSERT [dbo].[PatientInfo] ([PatientID], [FirstName], [LastName], [PhoneNum], [DateOfBirth], [GenderID], [CNIC], [Age], [Address], [MR]) VALUES (21, N'Qurba', N'Mustaque', N'0314-52857295', CAST(N'2004-06-13' AS Date), 2, N'42915-2582959-4', 19, N'Malir Cantt, Karachi', N'21')
GO
INSERT [dbo].[PatientInfo] ([PatientID], [FirstName], [LastName], [PhoneNum], [DateOfBirth], [GenderID], [CNIC], [Age], [Address], [MR]) VALUES (22, N'Qasim ', N'Pasta', N'123-3443-4334', CAST(N'2000-01-01' AS Date), 1, N'42201-324343-3', 23, N'Habib University, Karachi', N'22')
GO
INSERT [dbo].[PatientInfo] ([PatientID], [FirstName], [LastName], [PhoneNum], [DateOfBirth], [GenderID], [CNIC], [Age], [Address], [MR]) VALUES (23, N'Muddasir', N'Ahmed', N'0336-6454584', CAST(N'2004-03-13' AS Date), 1, N'42301-546362-4', 19, N'Kamal Motors, Karachi', N'23')
GO
INSERT [dbo].[PatientInfo] ([PatientID], [FirstName], [LastName], [PhoneNum], [DateOfBirth], [GenderID], [CNIC], [Age], [Address], [MR]) VALUES (25, N'Naeem', N'Ahmed', N'0324-2059215', CAST(N'2004-10-24' AS Date), 1, N'43210-525292-3', 19, N'Multani Park, Karachi', N'25')
GO
INSERT [dbo].[PatientInfo] ([PatientID], [FirstName], [LastName], [PhoneNum], [DateOfBirth], [GenderID], [CNIC], [Age], [Address], [MR]) VALUES (26, N'Ashar', N'Ali', N'0242-4259201', CAST(N'2004-09-23' AS Date), 1, N'43132-5282985-4', 19, N'Habib Public School, Karachi', N'26')
GO
INSERT [dbo].[PatientInfo] ([PatientID], [FirstName], [LastName], [PhoneNum], [DateOfBirth], [GenderID], [CNIC], [Age], [Address], [MR]) VALUES (27, N'Alishba', N'Khalid', N'0425-2592829', CAST(N'2003-09-13' AS Date), 2, N'42752-582975-2', 20, N'Ibrahim Terrace Adam Road, Karachi', N'27')
GO
INSERT [dbo].[PatientInfo] ([PatientID], [FirstName], [LastName], [PhoneNum], [DateOfBirth], [GenderID], [CNIC], [Age], [Address], [MR]) VALUES (28, N'Jibran', N'Sheikh', N'0331 3027668', CAST(N'1999-12-01' AS Date), 3, N'42201-1582347-5', 24, N'House 13-D, Near Potadose, Karachi', N'28')
GO
SET IDENTITY_INSERT [dbo].[PatientInfo] OFF
GO
SET IDENTITY_INSERT [dbo].[Rooms] ON 
GO
INSERT [dbo].[Rooms] ([RoomID], [RoomName]) VALUES (1, N'H-507')
GO
INSERT [dbo].[Rooms] ([RoomID], [RoomName]) VALUES (2, N'W-243')
GO
INSERT [dbo].[Rooms] ([RoomID], [RoomName]) VALUES (3, N'N-219')
GO
INSERT [dbo].[Rooms] ([RoomID], [RoomName]) VALUES (4, N'C-200')
GO
INSERT [dbo].[Rooms] ([RoomID], [RoomName]) VALUES (5, N'E-100')
GO
INSERT [dbo].[Rooms] ([RoomID], [RoomName]) VALUES (6, N'E-215')
GO
INSERT [dbo].[Rooms] ([RoomID], [RoomName]) VALUES (7, N'W-111')
GO
INSERT [dbo].[Rooms] ([RoomID], [RoomName]) VALUES (8, N'C-109')
GO
INSERT [dbo].[Rooms] ([RoomID], [RoomName]) VALUES (9, N'W-110')
GO
INSERT [dbo].[Rooms] ([RoomID], [RoomName]) VALUES (10, N'W-300')
GO
INSERT [dbo].[Rooms] ([RoomID], [RoomName]) VALUES (11, N'N-220')
GO
INSERT [dbo].[Rooms] ([RoomID], [RoomName]) VALUES (12, N'W-234')
GO
INSERT [dbo].[Rooms] ([RoomID], [RoomName]) VALUES (13, N'H-509')
GO
INSERT [dbo].[Rooms] ([RoomID], [RoomName]) VALUES (14, N'E-121')
GO
INSERT [dbo].[Rooms] ([RoomID], [RoomName]) VALUES (15, N'E-012')
GO
INSERT [dbo].[Rooms] ([RoomID], [RoomName]) VALUES (16, N'E-220')
GO
SET IDENTITY_INSERT [dbo].[Rooms] OFF
GO
SET IDENTITY_INSERT [dbo].[Specialization] ON 
GO
INSERT [dbo].[Specialization] ([SpecializationID], [Specialization]) VALUES (1, N'Cardiology')
GO
INSERT [dbo].[Specialization] ([SpecializationID], [Specialization]) VALUES (2, N'Orthopedics')
GO
INSERT [dbo].[Specialization] ([SpecializationID], [Specialization]) VALUES (3, N'Neurology')
GO
INSERT [dbo].[Specialization] ([SpecializationID], [Specialization]) VALUES (4, N'Pediatrics')
GO
INSERT [dbo].[Specialization] ([SpecializationID], [Specialization]) VALUES (5, N'Radiology')
GO
INSERT [dbo].[Specialization] ([SpecializationID], [Specialization]) VALUES (6, N'Dermatology')
GO
INSERT [dbo].[Specialization] ([SpecializationID], [Specialization]) VALUES (7, N'Ophthalmology')
GO
INSERT [dbo].[Specialization] ([SpecializationID], [Specialization]) VALUES (8, N'ENT')
GO
SET IDENTITY_INSERT [dbo].[Specialization] OFF
GO
SET IDENTITY_INSERT [dbo].[Status] ON 
GO
INSERT [dbo].[Status] ([StatusID], [Status]) VALUES (1, N'Upcoming')
GO
INSERT [dbo].[Status] ([StatusID], [Status]) VALUES (2, N'Completed')
GO
INSERT [dbo].[Status] ([StatusID], [Status]) VALUES (3, N'Ongoing')
GO
INSERT [dbo].[Status] ([StatusID], [Status]) VALUES (4, N'Skipped')
GO
SET IDENTITY_INSERT [dbo].[Status] OFF
GO
SET IDENTITY_INSERT [dbo].[Symptoms] ON 
GO
INSERT [dbo].[Symptoms] ([SymptomsID], [Symptom]) VALUES (1, N'Fever')
GO
INSERT [dbo].[Symptoms] ([SymptomsID], [Symptom]) VALUES (2, N'Headache')
GO
INSERT [dbo].[Symptoms] ([SymptomsID], [Symptom]) VALUES (3, N'Fatigue')
GO
INSERT [dbo].[Symptoms] ([SymptomsID], [Symptom]) VALUES (4, N'Cough')
GO
INSERT [dbo].[Symptoms] ([SymptomsID], [Symptom]) VALUES (5, N'Shortness of breath')
GO
INSERT [dbo].[Symptoms] ([SymptomsID], [Symptom]) VALUES (6, N'Sore throat')
GO
INSERT [dbo].[Symptoms] ([SymptomsID], [Symptom]) VALUES (7, N'Muscle aches')
GO
INSERT [dbo].[Symptoms] ([SymptomsID], [Symptom]) VALUES (8, N'Loss of taste or smell')
GO
INSERT [dbo].[Symptoms] ([SymptomsID], [Symptom]) VALUES (9, N'Nausea')
GO
INSERT [dbo].[Symptoms] ([SymptomsID], [Symptom]) VALUES (10, N'Chills')
GO
INSERT [dbo].[Symptoms] ([SymptomsID], [Symptom]) VALUES (11, N'Runny nose')
GO
INSERT [dbo].[Symptoms] ([SymptomsID], [Symptom]) VALUES (12, N'Difficulty sleeping')
GO
INSERT [dbo].[Symptoms] ([SymptomsID], [Symptom]) VALUES (13, N'Joint pain')
GO
INSERT [dbo].[Symptoms] ([SymptomsID], [Symptom]) VALUES (14, N'Dizziness')
GO
INSERT [dbo].[Symptoms] ([SymptomsID], [Symptom]) VALUES (15, N'Stomach pain')
GO
INSERT [dbo].[Symptoms] ([SymptomsID], [Symptom]) VALUES (16, N'Chest pain')
GO
INSERT [dbo].[Symptoms] ([SymptomsID], [Symptom]) VALUES (17, N'Skin rash')
GO
INSERT [dbo].[Symptoms] ([SymptomsID], [Symptom]) VALUES (18, N'Eye redness')
GO
INSERT [dbo].[Symptoms] ([SymptomsID], [Symptom]) VALUES (19, N'Excessive sweating')
GO
SET IDENTITY_INSERT [dbo].[Symptoms] OFF
GO
SET IDENTITY_INSERT [dbo].[Types] ON 
GO
INSERT [dbo].[Types] ([TypeID], [Type]) VALUES (1, N'Receptionist')
GO
INSERT [dbo].[Types] ([TypeID], [Type]) VALUES (2, N'Doctor')
GO
INSERT [dbo].[Types] ([TypeID], [Type]) VALUES (3, N'Technician')
GO
INSERT [dbo].[Types] ([TypeID], [Type]) VALUES (4, N'Administrator')
GO
INSERT [dbo].[Types] ([TypeID], [Type]) VALUES (5, N'Nurse')
GO
SET IDENTITY_INSERT [dbo].[Types] OFF
GO
SET IDENTITY_INSERT [dbo].[Users] ON 
GO
INSERT [dbo].[Users] ([UserID], [FirstName], [LastName], [Password], [TypeID]) VALUES (2, N'Eman', N'Fatima', N'$2b$07$yF2jppWhXNS.mGZal8D3eOCPOja/05v6zILmsPSn1hmsSJYeCnk.e', 2)
GO
INSERT [dbo].[Users] ([UserID], [FirstName], [LastName], [Password], [TypeID]) VALUES (3, N'Raahim', N'Hashmi', N'$2b$07$NOCmNEUzDde8NDVQxOXwzuvJ4t.JBMXgulkHMr04xNlNB2t/pHVXG', 1)
GO
INSERT [dbo].[Users] ([UserID], [FirstName], [LastName], [Password], [TypeID]) VALUES (5, N'Ibad', N'Nadeem', N'$2b$07$NOCmNEUzDde8NDVQxOXwzu6WhYl0r6CslMhloINCfEwQilBUdBNEa', 4)
GO
INSERT [dbo].[Users] ([UserID], [FirstName], [LastName], [Password], [TypeID]) VALUES (6, N'Fakeha', N'Faisal', N'$2b$07$8OFpVeMHQzOaCfsb15tBEu/DCUocSVPXXO0ihN.DvxCi19RPwSVd.', 5)
GO
INSERT [dbo].[Users] ([UserID], [FirstName], [LastName], [Password], [TypeID]) VALUES (7, N'Ali', N'Ahsan', N'$2b$07$8OFpVeMHQzOaCfsb15tBEuc036n3JoKZRGXKVEAafc.h/NHYCt5R2', 3)
GO
INSERT [dbo].[Users] ([UserID], [FirstName], [LastName], [Password], [TypeID]) VALUES (8, N'Shawaiz', N'Khan', N'$2b$07$NOCmNEUzDde8NDVQxOXwzuOA8VicM8K1PdS.O4LgfsCvLlHeuz7Ay', 2)
GO
INSERT [dbo].[Users] ([UserID], [FirstName], [LastName], [Password], [TypeID]) VALUES (11, N'Hania', N'Kashif', N'$2b$07$NOCmNEUzDde8NDVQxOXwzuYlsmneODD7qSgBNYVmu/GkrLyEa9zZi', 5)
GO
INSERT [dbo].[Users] ([UserID], [FirstName], [LastName], [Password], [TypeID]) VALUES (12, N'Waqar', N'Saleem', N'$2b$07$XHPyOVBDYONi/0aMEdPDX.S7Od3Jgx69XMCkIIumSq3WEI1FSxXaK', 2)
GO
INSERT [dbo].[Users] ([UserID], [FirstName], [LastName], [Password], [TypeID]) VALUES (14, N'Ahmed', N'Tariq', N'$2b$07$NOCmNEUzDde8NDVQxOXwzuseoPm5VwDNWH4Jw3LH6G1AL94HedeYq', 2)
GO
INSERT [dbo].[Users] ([UserID], [FirstName], [LastName], [Password], [TypeID]) VALUES (16, N'Shazia', N'Ahmed', N'$2b$07$NOCmNEUzDde8NDVQxOXwzuEG2n4v3fnwkpoashhy9WWUgz92tMjd.', 5)
GO
INSERT [dbo].[Users] ([UserID], [FirstName], [LastName], [Password], [TypeID]) VALUES (17, N'Shumaila', N'Farooq', N'$2b$07$NOCmNEUzDde8NDVQxOXwzu8UzmRK72R1fWFSZ68HHfKGYMp/muVxu', 5)
GO
INSERT [dbo].[Users] ([UserID], [FirstName], [LastName], [Password], [TypeID]) VALUES (18, N'Asma', N'Jawed', N'$2b$07$NOCmNEUzDde8NDVQxOXwzu0DAfYRs8oz3edl3HAdJuOz3B//amMNu', 5)
GO
INSERT [dbo].[Users] ([UserID], [FirstName], [LastName], [Password], [TypeID]) VALUES (19, N'Asjal', N'Usman', N'$2b$07$NOCmNEUzDde8NDVQxOXwzu8quN4Lj8vMNiV379l.EipP/ozqN2/L6', 5)
GO
INSERT [dbo].[Users] ([UserID], [FirstName], [LastName], [Password], [TypeID]) VALUES (20, N'Maimoona', N'Qamal', N'$2b$07$NOCmNEUzDde8NDVQxOXwzuJ/30hO0z4.v7wFALfZXXf6jNSz2yBU2', 5)
GO
INSERT [dbo].[Users] ([UserID], [FirstName], [LastName], [Password], [TypeID]) VALUES (21, N'Hamza', N'Khan', N'$2b$07$NOCmNEUzDde8NDVQxOXwzulnWHp9q.KMaBVrCQaC0ohy8UNBlWdrK', 5)
GO
INSERT [dbo].[Users] ([UserID], [FirstName], [LastName], [Password], [TypeID]) VALUES (22, N'Bismil', N'Faisal', N'$2b$07$NOCmNEUzDde8NDVQxOXwzuDDSTGfrbTe1HGBxJufrEK4vRUNhz0t.', 5)
GO
INSERT [dbo].[Users] ([UserID], [FirstName], [LastName], [Password], [TypeID]) VALUES (23, N'Usama', N'Nadeem', N'$2b$07$NOCmNEUzDde8NDVQxOXwzu9Bl6RN.JsT./ddAtb4cF.VZxJX5ytwu', 5)
GO
INSERT [dbo].[Users] ([UserID], [FirstName], [LastName], [Password], [TypeID]) VALUES (24, N'Bilal', N'Ahsan', N'$2b$07$NOCmNEUzDde8NDVQxOXwzukbQJzBiHy4NvVDIlS7iLZgIN8w2YCdW', 5)
GO
INSERT [dbo].[Users] ([UserID], [FirstName], [LastName], [Password], [TypeID]) VALUES (25, N'Imran', N'Ali', N'$2b$07$NOCmNEUzDde8NDVQxOXwzukewiiG57B0zBk69XDLca0mwh.el9Bd2', 2)
GO
INSERT [dbo].[Users] ([UserID], [FirstName], [LastName], [Password], [TypeID]) VALUES (26, N'Sana', N'Aslam', N'$2b$07$NOCmNEUzDde8NDVQxOXwzu0SWpN5tb6kjuUufWuY0J2PJR0NFvfCq', 2)
GO
INSERT [dbo].[Users] ([UserID], [FirstName], [LastName], [Password], [TypeID]) VALUES (27, N'Fatima', N'Ali', N'$2b$07$NOCmNEUzDde8NDVQxOXwzuPlnuvowtvicB2oS7z.LmHKZz0vMcIiy', 2)
GO
INSERT [dbo].[Users] ([UserID], [FirstName], [LastName], [Password], [TypeID]) VALUES (28, N'Farhan', N'Qureshi', N'$2b$07$NOCmNEUzDde8NDVQxOXwzuN8mTPqHj2O.Pc6TMUsf6B5LMLskMwbm', 2)
GO
INSERT [dbo].[Users] ([UserID], [FirstName], [LastName], [Password], [TypeID]) VALUES (29, N'Nazia', N'Iqbal', N'$2b$07$NOCmNEUzDde8NDVQxOXwzurXM2WnWmL76FQHzgZZmaKkBHh2xU0zW', 2)
GO
INSERT [dbo].[Users] ([UserID], [FirstName], [LastName], [Password], [TypeID]) VALUES (30, N'Sadia', N'Raza', N'$2b$07$NOCmNEUzDde8NDVQxOXwzuyHuOy6NRqSWEDCcL/ZCyD9h.ULcXmj2', 2)
GO
INSERT [dbo].[Users] ([UserID], [FirstName], [LastName], [Password], [TypeID]) VALUES (31, N'Ahmed', N'Siddique', N'$2b$07$NOCmNEUzDde8NDVQxOXwzuEFy.In1w/Qm70VTyqMZ2lGr9bHvjPDW', 2)
GO
INSERT [dbo].[Users] ([UserID], [FirstName], [LastName], [Password], [TypeID]) VALUES (32, N'Ali', N'Raza', N'$2b$07$NOCmNEUzDde8NDVQxOXwzuUpfAOVmbLkayApJQS1Xi2Vk/nyysWe2', 2)
GO
INSERT [dbo].[Users] ([UserID], [FirstName], [LastName], [Password], [TypeID]) VALUES (33, N'Nida', N'Sheikh', N'$2b$07$NOCmNEUzDde8NDVQxOXwzuHlzxdHY0lgZj61ousD3a1iadB6EPIt.', 2)
GO
INSERT [dbo].[Users] ([UserID], [FirstName], [LastName], [Password], [TypeID]) VALUES (34, N'Hira', N'Maliq', N'$2b$07$NOCmNEUzDde8NDVQxOXwzut/VDYPC4vE2JAf9Yw6CXO1dJuHqFD3W', 2)
GO
INSERT [dbo].[Users] ([UserID], [FirstName], [LastName], [Password], [TypeID]) VALUES (35, N'Usman', N'Akhtar', N'$2b$07$NOCmNEUzDde8NDVQxOXwzuVH9g4vgOPhkbJ2CV8hkmcwy.8vJ4ywC', 2)
GO
INSERT [dbo].[Users] ([UserID], [FirstName], [LastName], [Password], [TypeID]) VALUES (36, N'Hassan', N'Rizvi', N'$2b$07$NOCmNEUzDde8NDVQxOXwzuQ/LhrU/WaMEZZURikFyvL02XJTgJl4S', 5)
GO
INSERT [dbo].[Users] ([UserID], [FirstName], [LastName], [Password], [TypeID]) VALUES (37, N'Rabia', N'Abbas', N'$2b$07$NOCmNEUzDde8NDVQxOXwzuRydWMLfVdWx43GX2LUGD1PP0P0XCcsm', 5)
GO
INSERT [dbo].[Users] ([UserID], [FirstName], [LastName], [Password], [TypeID]) VALUES (38, N'Samina', N'Shah', N'$2b$07$NOCmNEUzDde8NDVQxOXwzu5vfAs6/HADUVlmv4.cMvc1NO/G1e3dK', 5)
GO
INSERT [dbo].[Users] ([UserID], [FirstName], [LastName], [Password], [TypeID]) VALUES (39, N'Adnan', N'Ahmed', N'$2b$07$NOCmNEUzDde8NDVQxOXwzuz1IioIgiemkBWaGVl7thId6n4ck52nK', 5)
GO
INSERT [dbo].[Users] ([UserID], [FirstName], [LastName], [Password], [TypeID]) VALUES (40, N'Ben', N'Tennison', N'$2b$07$gRpfq189ktIYEtKA7Qsw6.tKKEWOX0EJtWhkbWNx4ULp6t9AAAfb6', 2)
GO
SET IDENTITY_INSERT [dbo].[Users] OFF
GO
ALTER TABLE [dbo].[Appointments]  WITH CHECK ADD  CONSTRAINT [Appointments_fk0] FOREIGN KEY([MR])
REFERENCES [dbo].[PatientInfo] ([PatientID])
GO
ALTER TABLE [dbo].[Appointments] CHECK CONSTRAINT [Appointments_fk0]
GO
ALTER TABLE [dbo].[Appointments]  WITH CHECK ADD  CONSTRAINT [Appointments_fk2] FOREIGN KEY([StatusID])
REFERENCES [dbo].[Status] ([StatusID])
GO
ALTER TABLE [dbo].[Appointments] CHECK CONSTRAINT [Appointments_fk2]
GO
ALTER TABLE [dbo].[AppointmentSymptoms]  WITH CHECK ADD  CONSTRAINT [AppointmentSymptoms_fk0] FOREIGN KEY([AppointmentID])
REFERENCES [dbo].[Appointments] ([AppointmentID])
GO
ALTER TABLE [dbo].[AppointmentSymptoms] CHECK CONSTRAINT [AppointmentSymptoms_fk0]
GO
ALTER TABLE [dbo].[AppointmentSymptoms]  WITH CHECK ADD  CONSTRAINT [AppointmentSymptoms_fk1] FOREIGN KEY([SymptomID])
REFERENCES [dbo].[Symptoms] ([SymptomsID])
GO
ALTER TABLE [dbo].[AppointmentSymptoms] CHECK CONSTRAINT [AppointmentSymptoms_fk1]
GO
ALTER TABLE [dbo].[Diagnoses]  WITH CHECK ADD  CONSTRAINT [Diagnoses_fk0] FOREIGN KEY([AppointmentID])
REFERENCES [dbo].[Appointments] ([AppointmentID])
GO
ALTER TABLE [dbo].[Diagnoses] CHECK CONSTRAINT [Diagnoses_fk0]
GO
ALTER TABLE [dbo].[Doctors]  WITH CHECK ADD  CONSTRAINT [Doctors_fk0] FOREIGN KEY([DoctorID])
REFERENCES [dbo].[Users] ([UserID])
GO
ALTER TABLE [dbo].[Doctors] CHECK CONSTRAINT [Doctors_fk0]
GO
ALTER TABLE [dbo].[Doctors]  WITH CHECK ADD  CONSTRAINT [Doctors_fk1] FOREIGN KEY([SpecializationID])
REFERENCES [dbo].[Specialization] ([SpecializationID])
GO
ALTER TABLE [dbo].[Doctors] CHECK CONSTRAINT [Doctors_fk1]
GO
ALTER TABLE [dbo].[Doctors]  WITH CHECK ADD  CONSTRAINT [Doctors_fk2] FOREIGN KEY([NurseID])
REFERENCES [dbo].[Users] ([UserID])
GO
ALTER TABLE [dbo].[Doctors] CHECK CONSTRAINT [Doctors_fk2]
GO
ALTER TABLE [dbo].[Doctors]  WITH CHECK ADD  CONSTRAINT [Doctors_fk3] FOREIGN KEY([RoomID])
REFERENCES [dbo].[Rooms] ([RoomID])
GO
ALTER TABLE [dbo].[Doctors] CHECK CONSTRAINT [Doctors_fk3]
GO
ALTER TABLE [dbo].[Invoices]  WITH CHECK ADD  CONSTRAINT [Invoices_fk0] FOREIGN KEY([AppointmentID])
REFERENCES [dbo].[Appointments] ([AppointmentID])
GO
ALTER TABLE [dbo].[Invoices] CHECK CONSTRAINT [Invoices_fk0]
GO
ALTER TABLE [dbo].[Invoices]  WITH CHECK ADD  CONSTRAINT [Invoices_fk1] FOREIGN KEY([MR])
REFERENCES [dbo].[PatientInfo] ([PatientID])
GO
ALTER TABLE [dbo].[Invoices] CHECK CONSTRAINT [Invoices_fk1]
GO
ALTER TABLE [dbo].[PatientInfo]  WITH CHECK ADD  CONSTRAINT [PatientInfo_fk0] FOREIGN KEY([GenderID])
REFERENCES [dbo].[Gender] ([GenderID])
GO
ALTER TABLE [dbo].[PatientInfo] CHECK CONSTRAINT [PatientInfo_fk0]
GO
ALTER TABLE [dbo].[Users]  WITH CHECK ADD  CONSTRAINT [Users_fk0] FOREIGN KEY([TypeID])
REFERENCES [dbo].[Types] ([TypeID])
GO
ALTER TABLE [dbo].[Users] CHECK CONSTRAINT [Users_fk0]
GO
USE [master]
GO
ALTER DATABASE [project] SET  READ_WRITE 
GO
