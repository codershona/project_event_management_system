from django.shortcuts import render, redirect

from .models import Socialize, Contributor
from .forms import RegistrationForm
# from django.http import HttpResponse

# Create your views here.

def index(request):
    socialize = Socialize.objects.all()
    return render(request, 'socialize/index.html', {
        #'show_socialize': False,
        # 'show_socialize': True,
        'socialize': socialize
    })
#   return HttpResponse('Hello django!')

def socializes_details(request, socializes_slug):
    # print(socializes_slug)
    try:
      selected_socialize = Socialize.objects.get(slug=socializes_slug)
      if request.method == 'GET':
        # selected_socialize = Socialize.objects.get(slug=socializes_slug)
        registration_form = RegistrationForm()
        # return render(request, 'socialize/socializes-details.html', {
        # 'socialize_found': True,
        # 'socialize': selected_socialize,
        # 'form': registration_form
        #  'form': registration_form
        # 'socialize_title': selected_socialize['title'],
        # Using dot notation in this method
        # 'socialize_title': selected_socialize.title,
        # 'socialize_description': selected_socialize['description']
        # 'socialize_description': selected_socialize.description
    #    })
      else:
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
         # contributor = registration_form.save()
           user_email = registration_form.cleaned_data['email_address']
           user_phone = registration_form.cleaned_data['phone_number']
           contributor,_ = Contributor.objects.get_or_create(email_address=user_email, phone_number=user_phone)
           selected_socialize.contributor.add(contributor)
           return redirect('registration_complete', socializes_slug=socializes_slug)


      return render(request, 'socialize/socializes-details.html', {
            'socialize_found': True,
            'socialize': selected_socialize,
            'form': registration_form
        })

    except Exception as exc:
        print(exc)
        return render(request, 'socialize/socializes-details.html', {
            'socialize_found': False
        })

def registration_complete(request, socializes_slug):
  socialize = Socialize.objects.get(slug=socializes_slug)
  return render(request, 'socialize/registration-complete.html', {
        'supervisor_email': socialize.supervisor_email
    })