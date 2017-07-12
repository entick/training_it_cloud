from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.CourseListView.as_view(), name='courses_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.CourseDetailView.as_view(), name='course_detail'),
    url(r'^new$', views.CourseCreateView.as_view(), name='course_new'),
    url(r'^(?P<pk>[0-9]+)/edit$', views.course_edit, name='course_edit'),
    url(r'^(?P<pk>\d+)/lesson$', views.add_lesson_to_course, name='add_lesson_to_course'),
    url(r'^(?P<pk>\d+)/remove$', views.course_remove, name='course_remove'),
    url(r'^lessons/(?P<pk>\d+)/edit$', views.lesson_edit, name='lesson_edit'),
    url(r'^lessons/(?P<pk>\d+)/remove$', views.lesson_remove, name='lesson_remove'),

]
