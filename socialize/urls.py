from django.urls import path
from . import views

urlpatterns = [
    path('socialize/', views.index), # our-domain.com/socialize
    path('socialize/<slug:socializes_slug>', views.socializes_details), # our-domain.com/socialize/<dynamic-path-segment>a-second-socialize
    # path('#')
]

