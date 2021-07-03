from django.urls import path
from . import views

urlpatterns = [
    path('socialize/', views.index, name='all_socialize'), # our-domain.com/socialize
    path('socialize/<slug:socializes_slug>', views.socializes_details, name='socializes-details'), # our-domain.com/socialize/<dynamic-path-segment>a-second-socialize
    # path('#')


#   path('<slug:socializes_slug>/success', views.confirm_registration, name='confirm-registration'),
#   path('<slug:socializes_slug>', views.socializes_details, name='socializes-detail'), # our-domain.com/meetups/<dynamic-path-segment>
]

