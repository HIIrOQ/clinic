from django.urls import path

from . import views
from .views import *


urlpatterns = [
    path('',IndexView.as_view(),name = 'index'),
    path('aboutus/',AboutUsView.as_view(),name = 'about'),
    path('service',ServiceView.as_view(),name = 'service'),
    path('graph',Graph.as_view(),name = 'graph'),
    path('doctor', DoctorListView.as_view(), name='doctor'),
    path('prices', Prices.as_view(), name='prices'),
    path('contact', Contact.as_view(), name='contact'),
    path('service_detail', ServiceDetail.as_view(), name='service_detail'),
    path('doctor_detail', DoctorDetail.as_view(), name='doctor_detail'),
    path('send_email/', SendEmailView.as_view(), name='send_email')

]