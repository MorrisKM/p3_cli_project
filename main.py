import click
import pprint
from datetime import datetime
from models import Appointment, Doctor, Medical_Record, Patient
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
      click.secho("  1. Add patient \n  2. View patient's medical data  \n  3. patient's appointments  \n  4. View patients", fg='red')
      choice1 = click.prompt('type here...', type=int)

      if choice1 in [1, 2, 3, 4]:
        break
      else:
        print('please enter a valid choice')
        continue
    
    if choice1 == 1:
      click.secho('To add a new patient...', fg= 'yellow')
      while True:
        name = click.prompt('enter name...', type=str)
        contact = click.prompt('enter contact... in 2547... format', type=int)
        if name and len(contact) == 12:
          add_patient(name, contact)
          break
        else:
          print('please enter valid data')
          continue

    elif choice1 == 2:
      name = click.prompt('enter patients name for medical data...', type=str)
      medical = get_data_dict(Medical_Record, name)
      pprint.pp(medical) if medical else print('patient has no medical data')

    elif choice1 == 3:
      name = click.prompt('enter patients name to see appointments...', type=str)
      appointments = patient_appointments(name)
      pprint.pp(appointments) if appointments else print('patient has no appointments')

    elif choice1 == 4:
      names = view_all_names(Patient)
      pprint.pp([name for name in names]) if names else print('no patient available')

      
  elif choice == 2:
    while True:
      click.secho('-------DOCTORS-------', fg = 'yellow')
      click.secho("  1. Add doctor \n  2. doctors's appointments  \n  3. View doctors", fg='red')
      choice2 = click.prompt('type here...', type=int)

      if choice2 in [1, 2, 3]:
        break
      else:
        print('please enter a valid choice')
        continue

    if choice2 == 1:
      click.secho('To add a new doctor...', fg= 'yellow')
      while True:
        name = click.prompt('enter name...', type=str)
        speciality = click.prompt('enter speciality...', type=str)
        contact = click.prompt('enter contact... in 2547... format', type=int)
        if name and len(contact) == 12 and speciality:
          add_doctor(name, speciality, contact)
          break
        else:
          print('please enter valid data')
          continue

    elif choice2 == 2:
      name = click.prompt('enter doctors name to see appointments...', type=str)
      appointments = doctor_appointments(name)
      pprint.pp(appointments) if appointments else print('doctor has no appointments')

    elif choice2 == 3:
      names = view_all_names(Doctor)
      pprint.pp([name for name in names]) if names else print('no doctors available')

  elif choice == 3:
    while True:
      click.secho('-------APPOINTMENTS-------', fg = 'yellow')
      click.secho("  1. Add appointment \n  2. remove appointments", fg='red')
      choice3 = click.prompt('type here...', type=int)

      if choice3 in [1, 2, 3]:
        break
      else:
        print('please enter a valid choice')
        continue

    if choice3 == 1:
      click.secho('To add a new appointment...', fg= 'yellow')
      while True:
        patient = click.prompt('enter patient...', type=Patient)
        doctor = click.prompt('enter doctor assigned...', type=Doctor)
        appointment_date = click.prompt('enter appointment data yyyy,mm,dd')
        notes = click.prompt('enter issue...', type=str)
        if isinstance(patient, Patient) and isinstance(doctor, Doctor) and notes and appointment_date:
          add_appointment(doctor, patient, datetime(appointment_date), notes)
          break
        else:
          print('please enter valid data')
          continue


hospital()