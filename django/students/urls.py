from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.students_list, name='students_list'),
    url(r'^(?P<pk>[0-9]+)$', views.student_details, name='student_detail'),
    url(r'^new/$', views.student_new, name='student_new'),
    url(r'^(?P<pk>[0-9]+)/edit/$',views.student_edit, name='student_edit'),
    url(r'^(?P<pk>[0-9]+)/remove/$',views.student_remove, name='student_remove'),
]
