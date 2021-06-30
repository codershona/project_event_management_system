from django.urls import path
from . import views

urlpatterns = [
    path('socialize/', views.index) # our-domain.com/socialize
]

