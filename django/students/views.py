from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.views import generic
from django.core.urlresolvers import reverse_lazy

from courses.models import Course
from .models import Student
from .forms import StudentForm

from django.contrib.auth.decorators import login_required


# Create your views here.

class StudentLstView(generic.ListView):
    template_name = 'students/students_list.html'
    context_object_name = 'students'

    def get_queryset(self):
        pk = self.request.GET.get('course_id', '-1')
        if '-' in pk or pk is not int:
            students = Student.objects.all().order_by('name')
        else:
            course = get_object_or_404(Course, pk=pk)
            students = Student.objects.filter(courses=course).order_by('name')
        paginator = Paginator(students, 2)
        page = self.request.GET.get('page')
        try:
            students_page = paginator.page(page)
        except PageNotAnInteger:
            students_page = paginator.page(1)
        except EmptyPage:
            students_page = paginator.page(paginator.num_pages)
        return students_page


class StudentDetailView(generic.DetailView):
    model = Student
    template_name = 'students/student_detail.html'

    def get_queryset(self):
        return Student.objects.filter()


class StudentCreateView(generic.CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_edit.html'
    success_url = reverse_lazy('students_list')

    def get_initial(self):
        course_id = self.request.GET.get('course_id', '-1')
        if '-' in course_id or course_id == '':
            return super(StudentCreateView, self).get_initial()
        else:
            course = get_object_or_404(Course, pk=course_id)
            return {
                'courses': [course]
            }

    def form_valid(self, form):
        if form.is_valid():
            student = form.save(commit=True)
            messages.success(self.request,
                             message='Студент {0} был успешно добавлен.'.format(student))
            self.success_url = self.request.GET.get('next', self.success_url)
        return super(StudentCreateView, self).form_valid(form)


class StudentUpdateView(generic.UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_edit.html'
    success_url = reverse_lazy('students_list')

    def get_initial(self):
        course_id = self.request.GET.get('course_id', '-1')
        if '-' in course_id or course_id == '':
            return super(StudentUpdateView, self).get_initial()
        else:
            course = get_object_or_404(Course, pk=course_id)
            return {
                'courses': [course]
            }

    def form_valid(self, form):
        if form.is_valid():
            student = form.save(commit=True)
            messages.success(self.request,
                             message='Студент {0} был успешно обновлен.'.format(student))
            self.success_url = self.request.GET.get('next', self.success_url)
        return super(StudentUpdateView, self).form_valid(form)


class StudentDeleteView(generic.DeleteView):
    model = Student
    success_url = reverse_lazy('students_list')

    def get_success_url(self):
        return self.request.GET.get('next', self.success_url)

    def delete(self, request, *args, **kwargs):
        res = super(StudentDeleteView, self).delete(request, *args, **kwargs)
        messages.success(self.request, 'Студент {0} успешно удален'.format(
            self.object))
        return res


def students_list(request):
    pk = request.GET.get('course_id', '-1')
    if '-' in pk or pk == '':
        students = Student.objects.all().order_by('name')
    else:
        course = get_object_or_404(Course, pk=pk)
        students = Student.objects.filter(courses=course).order_by('name')
    paginator = Paginator(students, 2)
    page = request.GET.get('page')
    try:
        students_page = paginator.page(page)
    except PageNotAnInteger:
        students_page = paginator.page(1)
    except EmptyPage:
        students_page = paginator.page(paginator.num_pages)
    return render(request, 'students/students_list.html', {'students': students_page})


def student_details(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})


@login_required
def student_new(request):
    if (request.method == "POST"):
        form = StudentForm(request.POST)
        if (form.is_valid()):
            student = form.save()
            name = student.name
            surname = student.surname
            next = request.POST.get('next', '/')
            messages.success(request, "Студент " + name + " " + surname + " был успешно добавлен")
            return HttpResponseRedirect(next)
    else:
        course_id = request.GET.get('course_id', '-1')
        if '-' in course_id or course_id == '':
            form = StudentForm()
        else:
            course = get_object_or_404(Course, pk=course_id)
            form = StudentForm(initial={'courses': [course]})
    return render(request, 'students/student_edit.html', {'form': form})


@login_required
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if (request.method == "POST"):
        form = StudentForm(request.POST, instance=student)
        if (form.is_valid()):
            student = form.save()
            name = student.name
            surname = student.surname
            next = request.POST.get('next', '/')
            messages.success(request, "Студент " + name + " " + surname + " был успешно удален")
            return HttpResponseRedirect(next)
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_edit.html', {'form': form})


@login_required
def student_remove(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if (request.method == "POST"):
        name = student.name
        surname = student.surname
        student.delete()
        next = request.GET.get('next', '/')
        messages.success(request, "Студент " + name + " " + surname + " был успешно удален")
        return HttpResponseRedirect(next)
    else:
        name = student.name
        surname = student.surname
    return render(request, 'students/student_confirm_delete.html', {'name': name, 'surname': surname, 'pk': pk})
