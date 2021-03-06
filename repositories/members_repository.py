from db.run_sql import run_sql
from models.course import Course
from models.member import Member



def save(member):
    sql = "INSERT INTO members( name, age, membership, active ) VALUES ( %s,%s,%s,%s ) RETURNING id"
    values = [member.name, member.age, member.membership, member.active]
    results = run_sql( sql, values )
    member.id = results[0]['id']
    return member 


def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['name'],row['age'],row['membership'],row['active'], row['id'])
        members.append(member)
    return members


def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
     member = Member(result['name'],result['age'],result['membership'],result['active'], result['id'])
    return member   


def update(member):
    sql = "UPDATE members SET (name, age, membership, active) = (%s, %s,%s ,%s) WHERE id = %s"
    values = [member.name, member.age, member.membership, member.active, member.id]
    run_sql(sql, values)    


def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)  

def courses(member):
    
    member_courses = [] 

    sql = """ SELECT courses.* FROM courses
        INNER JOIN bookings
        ON bookings.course_id = courses.id
        WHERE bookings.member_id = %s;
     """    
    values = [member.id] 
    results = run_sql(sql,values)
    for row in results:
        course = Course(row['name'],row['start_date'],row['end_date'],row['time'],row['duration'],row['capacity'],row['active'], row['id'])  
        member_courses.append(course)
    return member_courses    