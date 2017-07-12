from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.StudentLstView.as_view(), name='students_list'),
    url(r'^(?P<pk>[0-9]+)$', views.StudentDetailView.as_view(), name='student_detail'),
    url(r'^new/$', views.StudentCreateView.as_view(), name='student_new'),
    url(r'^(?P<pk>[0-9]+)/edit/$',views.StudentUpdateView.as_view(), name='student_edit'),
    url(r'^(?P<pk>[0-9]+)/remove/$',views.StudentDeleteView.as_view(), name='student_remove'),
]
