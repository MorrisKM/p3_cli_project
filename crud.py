from models import Appointment, Doctor, Medical_Record, Patient, session

#handle db data
def to_dict(obj):
  if obj is None:
    return None
  return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}

#add doctor
def add_doctor(name, speciality, contact):
  doctor = Doctor(name = name, speciality = speciality, contact = contact)
  session.add(doctor)
  session.commit()

#view doctors appointments
def doctor_appointments(name):
  doctor = session.query(Doctor).filter(Doctor.name == name).first()
  return doctor.appointments if doctor else []

#add patient
def add_patient(name, contact):
  patient = Patient(name = name, contact = contact)
  session.add(patient)
  session.commit()

#view patients medical data
def get_data_dict(cls, name):
  record = session.query(cls).filter(cls.name == name).first()
  return to_dict(record)

#view patients appointments
def patient_appointments(name):
  patient = session.query(Patient).filter(Patient.name == name).first()
  return patient.appointments if patient else []

#all patients or doctors
def view_all_names(cls):
  names = session.query(cls.name).all()
  return [name_tuple[0] for name_tuple in names]

#add medical records
def add_medical_record(patient_id, allergies, height, weight):
  medical_record = Medical_Record(
    patient_id = patient_id, 
    allergies = allergies, 
    height = height, 
    weight = weight
  )
  session.add(medical_record)
  session.commit()

#add appointment
def add_appointment(doctor, patient, appointment_date, notes):
  appointment = Appointment(
    doctor = doctor, 
    patient = patient, 
    appointment_date = appointment_date, 
    notes = notes
  )
  session.add(appointment)
  session.commit()