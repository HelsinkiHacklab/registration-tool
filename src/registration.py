#!/usr/bin/env python
# Registration for a course

class Course:
    """Course which to register"""
    def __init__(self, title):
        self.title = title
        self.members = {}

def register(course,email):
    """register a student for a course"""
    course.members[email] = "unconfirmed"
    return True
