from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()
metadata = Base.metadata

engine = create_engine('sqlite:///database.db')
session = sessionmaker(bind=engine)()

class Appointment(Base):
  __tablename__ = "appointments"

  id = Column(Integer, primary_key=True)
  doctor_id = Column(Integer, ForeignKey('doctors.id'))
  patient_id = Column(Integer, ForeignKey('patients.id'))
  appointment_date = Column(DateTime)
  notes = Column(String)
  created_at = Column(DateTime, default=func.now())

  doctor = relationship('Doctor', backref= 'appointments')
  patient = relationship('Patient', backref= 'appointments')


class Doctor(Base):
  __tablename__ = 'doctors'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  speciality = Column(String)
  contact = Column(Integer)
  created_at = Column(DateTime, default=func.now())


class Patient(Base):
  __tablename__ = 'patients'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  contact = Column(Integer)
  created_at = Column(DateTime, default=func.now())


class Medical_Record(Base):
  __tablename__ = 'medical_records'

  id = Column(Integer, primary_key=True)
  patients_id = Column(Integer, ForeignKey('patients.id'))
  allergies = Column(String)
  height = Column(Integer)
  weight = Column(Integer)
  updated_at = Column(DateTime, default= func.now())

  patient = relationship('Patient', backref='medical_records')