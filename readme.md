# 🚤 MRC Booking App

The **Merrimack River Cruises (MRC) Booking App** is a Python application for managing bookings, passengers, vessels, and trips.  
It follows a layered architecture with a **Business Logic Layer (BLL)** and **Data Access Layer (DAL)** for clean separation of concerns.  

---

## 📂 Project Structure

```plaintext

├── main.py                # Entry point
├── bll/                   # Business Logic Layer
│   ├── __init__.py
│   └── mrc_bll.py
├── dal/                   # Data Access Layer
│   ├── __init__.py
│   ├── mrc_dal.py
│   ├── passenger_dal.py
│   ├── trip_dal.py
│   └── vessels_dal.py
├── models/                # Database models
│   ├── __init__.py
│   ├── passengers.py
│   ├── trips.py
│   └── vessels.py
└── README.md
```

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- A database (e.g., MySQL, PostgreSQL)
- mysql-connector-python Python package (`pip install mysql-connector-python`)

## macOS

- Navigate to the project directory
- run `python main.py` (or `python3 main.py`)

## Windows

- Navigate to the project directory 
- run `python main.py`

## Usage

### 1. Starting the Application

Run the application using the command:

`python main.py` or `python3 main.py`

### 2. Enter Database Credentials

You will be prompted to enter the DB host username, password, and DB name

### 3. Navigating the Application

As this is a sample program, the following information from the database will be displayed in the terminal:

- **Total Revenue by Vessel Example**: The application will display the total revenue generated for each vessel.
- **Getting Vessel ID Example**: You will see the Vessel ID for "Sea Breeze" and a request for the ID for a non-existent vessel, an appropriate success/error message will be displayed for both. 
- **Adding Trips Example**: When a trip is successfully added, a confirmation message will appear. Otherwise, the SQL error message will display.
- **Trip Information Table Example**: A table displaying all trip information will be printed to the terminal, showing details such as date, time, vessel, and passenger bookings.


## Future Improvements

Planned enhancements and possible extensions include:


- Dockerization → Containerize the application and database for easier setup and deployment.


- Improved Security → Implement environment-based configuration and encrypted credential storage.

- Advanced Reporting → Add analytics for revenue trends, passenger stats, and vessel utilization.

- Unit Testing → Add automated tests for DAL and BLL functions to ensure reliability.