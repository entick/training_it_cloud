from django.shortcuts import render, get_object_or_404
from .models import Coach
from courses.models import Course


# Create your views here.


def coach_detail(request, pk):
    coach = get_object_or_404(Coach, pk=pk)
    coursesc = Course.objects.filter(coach=coach)
    coursesa = Course.objects.filter(assistant=coach)
    return render(request, 'coaches/coach_detail.html', {'coach': coach, 'coursesc': coursesc, 'coursesa': coursesa})
