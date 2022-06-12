import unittest

from models.booking import Booking

class TestBooking(unittest.TestCase):
    def setUp(self):
        self.booking = Booking("moath", "Crossfit", 3)


    def test_booking_has_member(self):
        self.assertEqual("moath", self.booking.member)  

    def test_booking_has_course(self):
        self.assertEqual("Crossfit", self.booking.course)


    def test_booking_has_id(self):
        self.assertEqual(3, self.booking.id)          