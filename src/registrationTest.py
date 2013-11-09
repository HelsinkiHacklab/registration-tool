#!/usr/bin/env python
# Unit Test for registration module

import unittest
import registration

class RegistrationUnitTests(unittest.TestCase):
    def test_registration(self):
        course=registration.Course("Test course")
        self.assert_(registration.register(course,"test@example.com"), 'Registration should be successfull')
        self.assert_("test@example.com" in course.members.keys(), 'email is added to members')
        self.assertEqual(course.members["test@example.com"], "unconfirmed", 'but it should be unconfirmed')

if '__main__' == __name__:
    unittest.main()
