# UHU Clinic Database Management System

## Overview

This repository contains our project for the Database Management Systems course (Fall 2023) at UHU Clinic. 
The system comprises a backend implemented using MS SQL and Python with pyodbc, and a frontend developed through QT Designer.

## Setup Instructions

Step 1: Database Creation

- Open SQL Server and create a new database named `project`.

- Run the Database Creation Script provided as a whole query.

- The database 'project' should now be created and populated with dummy data.

Step 2: Install Required Packages

- Make sure to install the following Python packages using pip:

```bash
pip install pyqtdarktheme
pip install bcrypt
```

Step 3: Configuration

- Open the Application.py file.

- Locate the variable named server and enter your SQL Server name.

Step 4: Run the Application

## Dependencies

MS SQL: Database management system used for the backend.

Python: Programming language used for the backend implementation.

pyodbc: Python library for connecting to SQL Server.

PyQtDarkTheme: PyQt theme for a visually appealing frontend.

bcrypt: Python library for password hashing.
