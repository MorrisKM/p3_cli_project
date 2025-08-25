import click
import pprint
from datetime import datetime
from models import Appointment, Doctor, Medical_Record, Patient, session
from crud import add_appointment, add_doctor, add_medical_record, add_patient, get_data_dict, patient_appointments, view_all_names, doctor_appointments

def hospital():
  click.secho('------Welcome to the hospital app-------',blink=True ,bg='white', fg='green', bold= True)
  click.secho('Select Option to Proceed', fg='blue')
  click.secho('  1. Patients \n  2. Doctors \n  3. Appointment', fg='red')

  choice = click.prompt('type here...', type=int)

  if choice not in [1, 2, 3]:
    print('invalid choice! please pick 1 or 2 to continue')
    return hospital()
  
  if choice == 1:
    while True:
      click.secho('-------PATIENTS-------', fg = 'yellow')
      click.secho("  1. Add patient \n  2. View patient's medical data  \n  3. patient's appointments  \n  4. View patients \n  5.add patients medical record", fg='red')
      choice1 = click.prompt('type here...', type=int)

      if choice1 in [1, 2, 3, 4, 5]:
        break
      else:
        print('please enter a valid choice')
        continue
    
    if choice1 == 1:
      click.secho('To add a new patient...', fg= 'yellow')
      while True:
        name = click.prompt('enter name...', type=str)
        contact = click.prompt('enter contact... in 2547... format', type=str)
        if name and len(contact) == 12:
          add_patient(name, contact)
          print('patient added successfully')
          break
        else:
          print('please enter valid data')
          continue


    elif choice1 == 2:
      name = click.prompt('enter patients name for medical data...', type=str)
      medical = get_data_dict(Medical_Record, name)
      pprint.pp(medical) if medical else click.secho('patient has no medical data', fg='red')

    elif choice1 == 3:
      name = click.prompt('enter patients name to see appointments...', type=str)
      appointments = patient_appointments(name)
      if appointments:
        pprint.pp([f'{a.appointment_date} - Doctor ID: {a.doctor_id}, Notes: {a.notes}' for a in appointments])
      else:
        click.secho('patient has no appointments.', fg = 'red')

    elif choice1 == 4:
      names = view_all_names(Patient)
      pprint.pp(names) if names else click.secho('no patient available', fg= 'red')

    elif choice1 == 5:
      while True:
        name = click.prompt('enter patients name...', type= str)
        allergies = click.prompt('does patient have any allergies?', type=str)
        height = click.prompt('input patients height in cm as an integer:', type=int)
        weight = click.prompt('input patients weight in kg as an integer:', type=int)

        patient = session.query(Patient).filter(Patient.name == name).first()

        if patient and allergies and height and weight:
          add_medical_record(patient, allergies, height, weight)
          click.secho('Medical record added successfully', fg='green')
          break
        else:
          click.secho('Invalid data passed or patient not recorded', fg='red')

      
  elif choice == 2:
    while True:
      click.secho('-------DOCTORS-------', fg = 'yellow')
      click.secho("  1. Add doctor \n  2. doctors's appointments  \n  3. View doctors", fg='red')
      choice2 = click.prompt('type here...', type=int)

      if choice2 in [1, 2, 3]:
        break
      else:
        click.secho('please enter a valid choice', fg = 'red')
        continue

    if choice2 == 1:
      click.secho('To add a new doctor...', fg= 'yellow')
      while True:
        name = click.prompt('enter name...', type=str)
        speciality = click.prompt('enter speciality...', type=str)
        contact = click.prompt('enter contact... in 2547... format', type=str)
        if name and len(contact) == 12 and speciality:
          add_doctor(name, speciality, contact)
          click.secho('Doctor added successfully', fg='green')
          break
        else:
          click.secho('please enter valid data', fg = 'red')
          continue

    elif choice2 == 2:
      name = click.prompt('enter doctors name to see appointments...', type=str)
      appointments = doctor_appointments(name)
      if appointments:
        pprint.pp([f'{a.appointment_date} - Patient ID: {a.patient_id}, Notes: {a.notes}' for a in appointments])
      else:
        click.secho('Doctor has no appointments.', fg = 'red')

    elif choice2 == 3:
      names = view_all_names(Doctor)
      pprint.pp(names) if names else click.secho('no doctors available', fg = 'red')

  elif choice == 3:
    while True:
      click.secho('-------APPOINTMENTS-------', fg = 'yellow')
      click.secho("  1. Add appointment \n", fg='red')
      choice3 = click.prompt('type 1 to continue...', type=int)

      if choice3 == 1:
        break
      else:
        click.secho('please enter a valid choice', fg = 'red')
        continue

    if choice3 == 1:
      click.secho('To add a new appointment...', fg= 'yellow')
      while True:
        patient_name = click.prompt('enter patient...', type=Patient)
        doctor_name = click.prompt('enter doctor assigned...', type=Doctor)
        appointment_date_str = click.prompt('enter appointment data yyyy,mm,dd')
        notes = click.prompt('enter notes...', type=str)

        patient = session.query(Patient).filter(Patient.name == patient_name).first()
        doctor = session.query(Doctor).filter(Doctor.name == doctor_name).first()

        try:
          appointment_date = datetime.strptime(appointment_date, '%Y-%m-%d')
        except ValueError:
          click.secho('Invalid date format. use YYYY-MM-DD', fg='red')
          continue

        if patient and doctor and notes:
          add_appointment(doctor, patient, appointment_date, notes)
          click.secho('Appointment added successfully.', fg='green')
          break
        else:
          click.secho('Invalid data or patient/doctor not found.', fg='red')
          continue

if __name__ == '__main__':
  hospital()
