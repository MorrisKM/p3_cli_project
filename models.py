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

  doctor = relationship('Doctor', back_populates= 'appointments')
  patient = relationship('Patient', back_populates= 'appointments')


class Doctor(Base):
  __tablename__ = 'doctors'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  speciality = Column(String)
  contact = Column(String)
  created_at = Column(DateTime, default=func.now())

  appointments = relationship('Appointment', back_populates='doctor')


class Patient(Base):
  __tablename__ = 'patients'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  contact = Column(String)
  created_at = Column(DateTime, default=func.now())

  appointments = relationship('Appointment', back_populates='patient')
  medical_record = relationship('Medical_Record', back_populates='patient', uselist=False)


class Medical_Record(Base):
  __tablename__ = 'medical_records'

  id = Column(Integer, primary_key=True)
  patient_id = Column(Integer, ForeignKey('patients.id'))
  allergies = Column(String)
  height = Column(Integer)
  weight = Column(Integer)
  updated_at = Column(DateTime, default= func.now())

  patient = relationship('Patient', back_populates='medical_records')