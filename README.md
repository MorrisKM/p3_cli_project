# Hospital Management CLI Application

This is a command-line hospital management application built using Python, Click for the CLI interface, and SQLAlchemy ORM for database management. Alembic is used for database migrations.

## Features
- Manage Patients and their Medical Records
- Manage Doctors and their Specialties
- Schedule and view Appointments for Patients and Doctors
- Interactive CLI menu for easy navigation and data entry

## Requirements
- Python 3.8.13
- Click library for CLI prompts and menus
- SQLAlchemy for ORM and SQLite database connection
- Alembic for database migrations and version control

## Installation
1. Clone the repository or copy the source code files.
2. Install dependencies:
3. Initialize the database and apply migrations:


## Running the Application
Run the main application script to start the interactive hospital CLI:

Follow the on-screen prompts to add/view Patients, Doctors, Medical Records, and Appointments.

## Project Structure
- `main.py`: Contains the command-line interface logic using Click to interact with users.
- `models.py`: Defines SQLAlchemy ORM models for Patient, Doctor, Appointment, and Medical_Record with relationships.
- `crud.py`: CRUD operations used by the CLI to interact with the database.
- `alembic/`: Contains Alembic migration scripts and configuration to manage database schema changes.
- `database.db`: SQLite database file created by SQLAlchemy.

## Database Models Overview
- **Patient**: Stores patient information and has one-to-many relationship with `Appointment` and one-to-one with `Medical_Record`.
- **Doctor**: Stores doctor information and has one-to-many relationship with `Appointment`.
- **Appointment**: Links patients and doctors with appointment date, notes, and timestamps.
- **Medical_Record**: Stores detailed medical information per patient.

## Alembic Usage
This project uses Alembic to handle database migrations:
- To create a new migration after model changes:
- To apply migrations to update the database:


## Notes
- Ensure patient contact numbers are in the "2547XXXXXXXX" format (12 characters).
- Appointment dates must be entered in `YYYY-MM-DD` format.
- The CLI uses input validation and prompts to guide the user through operations.
- Relationships between models use SQLAlchemy's `back_populates` to synchronize linked records.

## Author
Munene Morris

## License
This project is open-source.
