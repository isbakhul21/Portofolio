--cretae tabel

CREATE TABLE [dbo].[DATA_SOURCE_TRAINING_HISTORY](
	[EmployeeID] [smallint] NOT NULL,
	[CourseID] [tinyint] NOT NULL,
	[CourseName] [nvarchar](50) NOT NULL,
	[Rating] [tinyint] NOT NULL,
	[Date_Training] [date] NOT NULL,
	[Achieve_Course_PerDaily] [tinyint] NOT NULL
) ON [PRIMARY]
GO



CREATE TABLE [dbo].[Employee_PT_SAMPLE_INDONESIA](
	[EmployeeID] [smallint] NOT NULL,
	[EmpName] [nvarchar](100) NULL,
	[Birthday] [date] NOT NULL,
	[Province] [nvarchar](500) NULL,
	[City] [nvarchar](500) NULL
) ON [PRIMARY]
GO

--INI ADALAH COMMAND UNTUK MENGECEK
--SELECT * FROM [dbo].[DATA_SOURCE_TRAINING_HISTORY]
--SELECT * FROM [dbo].[Employee_PT_SAMPLE_INDONESIA]
--TRUNCATE TABLE [dbo].[DATA_SOURCE_TRAINING_HISTORY]
--TRUNCATE TABLE [dbo].[Employee_PT_SAMPLE_INDONESIA]