import pdb
from models.course import Course
from models.member import Member
from models.booking import Booking

import repositories.courses_repository as courses_repository
import repositories.members_repository as members_repository
import repositories.booking_repository as booking_repository



member_1 = Member('Moath', 27, 'standerd', True)
member_2 = Member('Adam', 20, 'premium', True)
member_3 = Member('John', 30, 'standerd', False)
member_4 = Member('Liam', 25, 'premium', True)

members_repository.save(member_1)
members_repository.save(member_2)
members_repository.save(member_3)
members_repository.save(member_4)

members_repository.select_all()

course_1 = Course('Crossfit', '2022-08-08', '2022-10-07', '10:30:00', 1, 14, True)
course_2 = Course('Zumba', '2022-09-11', '2022-11-05', '14:10:00', 1, 14, False)
course_3 = Course('Yoga', '2022-07-20', '2022-09-17', '20:40:00', 1, 14, True)

courses_repository.save(course_1)
courses_repository.save(course_2)
courses_repository.save(course_3)

courses_repository.select_all() 

booking_1 = Booking(member_1 , course_3)
booking_2 = Booking(member_3 , course_2)
booking_3 = Booking(member_2 , course_1)
booking_4 = Booking(member_2 , course_3)
booking_5 = Booking(member_1 , course_2)
booking_6 = Booking(member_3 , course_1)
booking_7 = Booking(member_4 , course_2)

booking_repository.save(booking_1)
booking_repository.save(booking_2)
booking_repository.save(booking_3)
booking_repository.save(booking_4)
booking_repository.save(booking_5)
booking_repository.save(booking_6)
booking_repository.save(booking_7)

pdb.set_trace() 