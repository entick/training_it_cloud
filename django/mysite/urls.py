from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.contrib.auth import views as viewsdj
from feedbacks import views as fviews

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^post/', include('blog.urls', namespace="posts"), name='posts'),
    url(r'^polls/', include('polls.urls', namespace="polls"), name='polls'),
    url(r'^login/$', viewsdj.login, name='login'),
    url(r'^logout/$', viewsdj.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^$', views.home, name='home'),
    url(r'^course/', include('courses.urls', namespace="courses"), name='course'),
    url(r'^students/', include('students.urls', namespace="students"), name='student'),
    url(r'^quadratic/$', include('quadratic.urls', namespace="quadratic"), name='quadratic'),
    url(r'^coaches/', include('coaches.urls', namespace="coaches"), name='coaches'),
    url(r'^feedback/$', fviews.FeedbackView.as_view(), name="feedback"),
]
