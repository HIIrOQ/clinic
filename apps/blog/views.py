from django.conf import settings
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, FormView

from .forms import EmailForm
from .models import Doctor


from django.core.mail import send_mail
from django.http import HttpResponseRedirect



class IndexView(FormView) :
    template_name = 'index.html'
    form_class = EmailForm
    success_url = '/'

    def form_valid(self, form):

        subject= form.cleaned_data['subject']
        message = form.cleaned_data['message']
        from_email = settings.DEFAULT_FROM_EMAIL
        to_emails = form.cleaned_data['to_emails']

        send_mail(subject, message, from_email,[to_emails])

        return super().form_valid(form)

class AboutUsView(TemplateView):
    template_name = 'about.html'

class ServiceView(TemplateView):
    template_name = 'service.html'

class Graph(TemplateView):
    template_name = 'graph.html'

# class Doctor(TemplateView):
#     template_name = 'doctor.html'

class Prices(TemplateView):
    template_name = 'prices.html'

class Contact(TemplateView):
    template_name = 'contact.html'

class ServiceDetail(TemplateView):
    template_name = 'service-detail.html'



class DoctorDetail(TemplateView):
    template_name = 'doctor-detail.html'


class DoctorListView(ListView):
    template_name = 'doctor.html'
    model = Doctor
    queryset = Doctor.objects.all()




class SendEmailView(FormView):
    template_name = 'index.html'
    form_class = EmailForm
    success_url = 'contact.html'

    def form_valid(self, form):
        name = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        email = form.cleaned_data['email']
        number = form.cleaned_data['number']
        from_email = settings.DEFAULT_FROM_EMAIL
        to_emails = 'cliclinick@gmail.com'

        send_mail(name,number,email, message, from_email, to_emails)

        return super().form_valid(form)









import smtplib

import os
from email.mime.text import MIMEText

#
# def send_text(message):
#     sender = 'artykovh@gmail.com'
#     to_send = 'artykovh2@gmail.com'
#     gmail = 'kwvh tnih tpia kvrl'
#     password2 = 'kwvh tnih tpia kvrl'
#
#     server = smtplib.SMTP("smtp.gmail.com", 587)
#     server.starttls()
#
#     try:
#         server.login(sender, password2)
#         msg = MIMEText(message)
#         msg['Subject'] = 'Click me'
#         server.sendmail(sender, to_send, msg.as_string())
#
#         return 'message was send'
#     except Exception as _ex:
#         return f'{_ex} check login or pass'
#
#
# def main():
#     message = input('Type message: ')
#     print(send_text(message=message))
#
#
# if __name__ == '__main__':
#     main()