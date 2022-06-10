from db.run_sql import run_sql
from models.booking import Booking
import repositories.courses_repository as courses_repository 
import repositories.members_repository as members_repository 




def save(booking):
    sql = "INSERT INTO bookings ( member_id, course_id) VALUES ( %s, %s) RETURNING id"
    values = [booking.member.id, booking.course.id]
    results = run_sql( sql, values )
    booking.id = results[0]['id']
    return booking


def select_all():
    bookings = []

    sql = "SELECT * FROM bookings"
    results = run_sql(sql)

    for row in results:
        member = members_repository.select(row['member_id'])
        course = courses_repository.select(row['course_id'])
        booking = Booking(member, course,row['id'])
        bookings.append(booking)
    return bookings


def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)    