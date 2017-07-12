from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.contrib import messages
from django.core.mail import mail_admins
from .models import Feedback
from .forms import FeedbackForm
from mysite import settings

import datetime


class FeedbackView(generic.CreateView):
    model = Feedback
    template_name = 'feedbacks/feedback.html'
    form_class = FeedbackForm
    success_url = '#'

    def form_valid(self, form):
        if (form.is_valid()):
            feedback = form.save()
            mail_admins(
                feedback.subject,
                feedback.message + '\n' + datetime.datetime.__str__(feedback.create_date) + '\n' +
                feedback.from_email,

            )
            messages.success(self.request, "Thank you for your feedback! We will keep in touch with you very soon!")
        return super(FeedbackView, self).form_valid(form)
