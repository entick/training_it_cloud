from django.shortcuts import render
from .forms import QuadraticForm
from cmath import sqrt


# Create your views here.


def quadratic_evaluate(request):
    if (request.method == "POST"):
        form = QuadraticForm(request.POST)
        if (form.is_valid()):
            quadratic = form.save(commit=False)
            a = quadratic.a
            b = quadratic.b
            c = quadratic.c
            if (a!=0):
                d = (b ** 2) - (4 * a * c)
                sol1 = (-b - sqrt(d)) / (2 * a)
                sol2 = (-b + sqrt(d)) / (2 * a)
            else:
                d='division by zero'
                sol1 = 'division by zero'
                sol2 = 'division by zero'
            var = {'d': d, 'sol1': sol1, 'sol2': sol2}
            return render(request, "quadratic/quadratic_eval.html", {'form': form, 'var': var})
    else:
        form = QuadraticForm()
    return render(request, "quadratic/quadratic_eval.html", {'form': form})
