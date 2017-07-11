from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from .models import Course, Lesson
from .forms import CourseForm, LessonForm

from django.contrib.auth.decorators import login_required


# Create your views here.


def courses_list(request):
    courses = Course.objects.order_by('name')
    return render(request, 'courses/courses_list.html', {'courses': courses})


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    lessons = Lesson.objects.filter(course=pk).order_by('order')
    return render(request, 'courses/course_detail.html', {'course': course, 'lessons': lessons})


@login_required
def course_new(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if (form.is_valid()):
            form = form.save()
            return redirect('courses:course_detail', pk=form.pk)
    else:
        form = CourseForm()
    return render(request, 'courses/course_edit.html', {'form': form})


@login_required
def course_edit(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if (form.is_valid()):
            course = form.save()
            return redirect('courses:course_detail', pk=pk)
    else:
        form = CourseForm(instance=course)
    return render(request, 'courses/course_edit.html', {'form': form})


@login_required
def course_remove(request, pk):
    course = get_object_or_404(Course, pk=pk)
    course.delete()
    return redirect('courses:courses_list')


@login_required
def add_lesson_to_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.course = course
            lesson.save()
            messages.success(request, "Урок " + lesson.subject + " был успешно добавлен")
            return redirect('courses:course_detail', pk=pk)
    else:
        form = LessonForm()
    return render(request, 'courses/add_lesson_to_course.html', {'form': form})


@login_required
def lesson_edit(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    if request.method == "POST":
        form = LessonForm(request.POST, instance=lesson)
        if form.is_valid():
            lesson = form.save()
            return redirect('courses:course_detail', pk=lesson.course.pk)
    else:
        form = LessonForm(instance=lesson)
    return render(request, 'courses/add_lesson_to_course.html', {'form': form})

@login_required
def lesson_remove(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    course = lesson.course.pk
    lesson.delete()
    return redirect('courses:course_detail', pk=course)