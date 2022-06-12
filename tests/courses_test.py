import unittest

from models.course import Course, free_space

class TestCourse(unittest.TestCase):
    def setUp(self):
        self.course = Course("Crossfit", "2022-09-06" ,"2022-11-13", "14:10", 1, 20, True, 8) 


    def test_course_has_name(self):
        self.assertEqual("Crossfit", self.course.name)  


    def test_course_has_start_date(self):
        self.assertEqual("2022-09-06", self.course.start_date)   


    def test_course_has_end_date(self):
        self.assertEqual("2022-11-13", self.course.end_date)   


    def test_course_has_time(self):
        self.assertEqual("14:10", self.course.time)  


    def test_course_has_duration(self):
        self.assertEqual(1, self.course.duration) 


    def test_course_has_capacity(self):
        self.assertEqual(20, self.course.capacity)    


    def test_course_status(self):
        self.assertEqual(True, self.course.active)    


    def test_course_has_id(self):
        self.assertEqual(8, self.course.id)  

    def test_free_space(self):
        free_space(self.course)
        self.assertEqual(19, self.course.capacity)     