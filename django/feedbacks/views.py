from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.contrib import messages
from django.core.mail import mail_admins
from .models import Feedback
from .forms import FeedbackForm
from mysite import settings

import sendgrid
import os
from sendgrid.helpers.mail import *


class FeedbackView(generic.CreateView):
    model = Feedback
    template_name = 'feedbacks/feedback.html'
    form_class = FeedbackForm
    success_url = '#'

    def form_valid(self, form):
        if (form.is_valid()):
            feedback = form.save()
            sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
            from_email = Email("root@localhost")
            to_email = Email(settings.ADMINS)
            subject = 'PyCloud ' + form.subject
            content = Content("text/plain", form.message+'\n'+form.from_email)
            mail = Mail(from_email, subject, to_email, content)
            response = sg.client.mail.send.post(request_body=mail.get())
            messages.success(self.request, "Thank you for your feedback! We will keep in touch with you very soon!")
        return super(FeedbackView, self).form_valid(form)
