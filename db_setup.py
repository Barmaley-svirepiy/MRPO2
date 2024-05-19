from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

# Association table for many-to-many relationship between Users and Skills
user_skills = Table('user_skills', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('skill_id', Integer, ForeignKey('skills.id'))
)

# Association table for many-to-many relationship between Vacancies and Skills
vacancy_skills = Table('vacancy_skills', Base.metadata,
    Column('vacancy_id', Integer, ForeignKey('vacancies.id')),
    Column('skill_id', Integer, ForeignKey('skills.id'))
)

class UserModel(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    skills = relationship('SkillModel', secondary=user_skills, back_populates='users')

class SkillModel(Base):
    __tablename__ = 'skills'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    users = relationship('UserModel', secondary=user_skills, back_populates='skills')
    vacancies = relationship('VacancyModel', secondary=vacancy_skills, back_populates='skills')

class VacancyModel(Base):
    __tablename__ = 'vacancies'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    salary = Column(Float)
    skills = relationship('SkillModel', secondary=vacancy_skills, back_populates='vacancies')

class SeekerModel(Base):
    __tablename__ = 'seekers'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    vacancy_id = Column(Integer, ForeignKey('vacancies.id'))
    user = relationship('UserModel')
    vacancy = relationship('VacancyModel')

# Database setup
engine = create_engine('sqlite:///jobs.db')
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()