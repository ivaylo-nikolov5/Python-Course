from unittest import TestCase, main
from student.project.student import Student


class StudentTest(TestCase):
    def setUp(self) -> None:
        self.student = Student("Test", {"course": ["course notes", "more notes"]})
        self.student_without_courses = Student("Student without courses", {})

    def test_constructor_without_none_courses(self):
        student_name = self.student.name
        student_courses = self.student.courses
        self.assertEqual("Test", student_name)
        self.assertEqual({"course": ["course notes", "more notes"]}, student_courses)

    def test_constructor_with_none_courses(self):
        student_name = self.student_without_courses.name
        student_courses = self.student_without_courses.courses

        self.assertEqual("Student without courses", student_name)
        self.assertEqual({}, student_courses)

    def test_enroll_method_with_already_added_course(self):
        result = self.student.enroll("course", "more_notes")
        expected = "Course already added. Notes have been updated."
        self.assertEqual(expected, result)

    def test_enroll_method_with_Y_and_empty_space_add_course_notes(self):
        result_with_y = self.student.enroll("notes", "more_notes", "Y")
        result_with_empty_space = self.student.enroll("more notes", "more notes")

        expected = "Course and course notes have been added."

        self.assertEqual(expected, result_with_y)
        self.assertEqual(expected, result_with_empty_space)

    def test_enroll_method_adding_a_course_without_notes(self):
        result = self.student.enroll("notes", "no notes", "N")
        expected = "Course has been added."

        self.assertEqual([], self.student.courses["notes"])
        self.assertEqual(expected, result)

    def test_add_notes_method_with_correct_course_info(self):
        expected = "Notes have been updated"
        result = self.student.add_notes("course", "some more notes")

        self.assertEqual(expected, result)

    def test_add_notes_method_with_wrong_course_info(self):
        expected = "Cannot add notes. Course not found."
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("non existing course", "correct notes")

        self.assertEqual(expected, str(ex.exception))

    def test_leave_course_method_with_correct_course_info(self):
        expected = "Course has been removed"
        result = self.student.leave_course("course")

        self.assertEqual(expected, result)

    def test_leave_course_method_with_wrong_course_info(self):
        expected = "Cannot remove course. Course not found."

        with self.assertRaises(Exception) as ex:
            self.student.leave_course("non existing course")

        self.assertEqual(expected, str(ex.exception))

if __name__ == '__main__':
    main()
