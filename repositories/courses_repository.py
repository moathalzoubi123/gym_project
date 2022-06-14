from db.run_sql import run_sql
from models.course import Course
from models.member import Member



def save(course):
    sql = """INSERT INTO courses( name, start_date, end_date, time, duration, capacity, active) 
     VALUES ( %s,%s,%s,%s,%s,%s,%s ) RETURNING id"""
    values = [course.name, course.start_date, course.end_date, course.time ,course.duration, course.capacity, course.active] 
    results = run_sql( sql, values )
    course.id = results[0]['id']
    return course 


def select_all():
    courses = []

    sql = "SELECT * FROM courses"
    results = run_sql(sql)
    for row in results:
        course = Course(row['name'],row['start_date'],row['end_date'],row['time'], row['duration'], row['capacity'],row['active'],row['id'])
        courses.append(course)
    return courses 


def select(id):
    course = None
    sql = "SELECT * FROM courses WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        course = Course(result['name'],result['start_date'],result['end_date'],result['time'], result['duration'], result['capacity'],result['active'],result['id'])
    return course  


def update(course):
    sql = "UPDATE courses SET (name, start_date, end_date, time, duration, capacity, active) = (%s,%s,%s,%s,%s,%s,%s) WHERE id = %s"
    values = [course.name, course.start_date, course.end_date, course.time ,course.duration, course.capacity, course.active, course.id] 
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM courses"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM courses WHERE id = %s"
    values = [id]
    run_sql(sql, values)    


def members(course):
    
    course_members = [] 

    sql = """ SELECT members.* FROM members
        INNER JOIN bookings
        ON bookings.member_id = members.id
        WHERE bookings.course_id = %s;
     """    
    values = [course.id] 
    results = run_sql(sql,values)
    for row in results:
     member= Member(row['name'],row['age'],row['membership'],row['active'], row['id'])   
     course_members.append(member)
    return course_members      