import unittest

from models.member import Member

class TestMember(unittest.TestCase):
    def setUp(self):
        self.member = Member("moath", 27 ,"standerd", True, 4) 


    def test_member_has_name(self):
            self.assertEqual("moath", self.member.name) 

    def test_member_has_age(self):
        self.assertEqual(27, self.member.age)     

    def test_member_has_membership(self):
        self.assertEqual("standerd", self.member.membership)    

    def test_member_status(self):
        self.assertEqual(True, self.member.active)    


    def test_member_has_id(self):
        self.assertEqual( 4 , self.member.id)    