DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS courses;

CREATE TABLE members (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  age INT,
  membership VARCHAR(255),
  active BOOLEAN
);

CREATE TABLE courses (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  start_date DATE, 
  end_date DATE,
  time TIME, 
  duration INT, 
  capacity INT,
  active BOOLEAN
);

CREATE TABLE bookings (
  id SERIAL PRIMARY KEY,
  member_id INT REFERENCES members(id) ON DELETE CASCADE , 
  course_id INT REFERENCES courses(id) ON DELETE CASCADE 
);

