from django.urls import path

from .views import *

urlpatterns = [
    path('',IndexView.as_view(),name = 'index'),
    path('aboutus/',AboutUsView.as_view(),name = 'about'),

]