from dataclasses import dataclass
from datetime import date
from enum import Enum


@dataclass
class SimpleUser:
    full_name: str
    email: str
    current_address: str
    permanent_address: str


class Hobby(Enum):
    sports = 'Sports'
    reading = 'Reading'
    music = 'Music'


class Gender(Enum):
    male = 'Male'
    female = 'Female'
    other = 'Other'


@dataclass
class User:
    first_name: str
    last_name: str
    user_email: str
    gender: Gender
    user_number: str
    date_of_birth: date
    subjects: tuple[str, ...]
    hobbies: tuple[Hobby, ...]
    picture: str
    current_address: str
    state: str
    city: str


vika = User(
    first_name='Viktoriia',
    last_name='Lav',
    user_email='newuser@gmail.com',
    gender=Gender.female,
    user_number='8800222334',
    date_of_birth=date(1993, 5, 17),
    subjects=('Chemistry',),
    hobbies=(Hobby.sports, Hobby.reading),
    picture='photo.png',
    current_address='144 Broadway, suit 12',
    state='NCR',
    city='Gurgaon',
)

simple_vika = SimpleUser(
    full_name='Viktoriia Lav',
    email='newuser@gmail.com',
    current_address='144 Broadway, suit 12',
    permanent_address='55 Ocean Drive, suit 234'
)
