from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import Course, Lesson
from coaches.models import Coach
from django.contrib.auth.models import User

import datetime


def course_create(coach=None, assistant=None):
    course = Course.objects.create(
        name='Course',
        short_description='Course description',
        description='1',
        coach=coach,
        assistant=assistant,
    )
    return course


def coach_create(username=None):
    coach = Coach.objects.create(
        pk=1,
        user=User.objects.create(username=username),
        date_of_bitrh=datetime.date.today(),
    )

    def lesson_create(course=None):
        lesson = Lesson.objects.create(
            subject='Lesson',
            description='Lesson description',
            order=1,
            course=course,
        )
        return lesson

    class CoursesListTest(TestCase):
        def test_courses_list_response(self):
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)

        def test_courses_list_content(self):
            response = self.client.get('/')
            self.assertIn(b'PyCloud', response.content)

        def test_courses_list_with_5_courses(self):
            coach = coach_create(1)
            for i in range(5):
                course = course_create(coach, coach)
            self.assertEqual(Course.objects.all().count(), 5)

        def test_courses_list_empty(self):
            coach = coach_create(1)
            course = course_create(coach, coach)
            Course.objects.filter(id=1).delete()
            self.assertEqual(Course.objects.all().count(), 0)

        def test_courses_list_context(self):
            response = self.client.get('/')
            self.assertContains(response, 'index.html')

    class CoursesDetailTest(TestCase):
        def test_course_detail_response(self):
            coach = coach_create(1)
            course = course_create(coach, coach)
            response = self.client.get('/course/1/')
            self.assertEqual(response.status_code, 200)

        def test_course_detail_render(self):
            coach = coach_create(1)
            course = course_create(coach, coach)
            response = self.client.get('/course/1/')
            self.assertTemplateUsed(response, 'courses/course_detail.html')

        def test_course_detail_create_lesson(self):
            coach = coach_create(1)
            course = course_create(coach, coach)
            lesson = lesson_create(course=course)
            self.assertEqual(Lesson.objects.all().count(), 1)

        def test_course_detail_context(self):
            coach = coach_create(1)
            course = course_create(coach, coach)
            response = self.client.get('/course/1/')
            self.assertContains(response, course.name)

        def test_course_detail_not_exist(self):
            response = self.client.get('/course/1/')
            self.assertEqual(response.status_code, 404)
