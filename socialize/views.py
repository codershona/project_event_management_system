from django.shortcuts import render

from .models import Socialize
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
     return render(request, 'socialize/socializes-details.html', {
        'socialize_found': True,
        # 'socialize_title': selected_socialize['title'],
        # Using dot notation in this method
        'socialize_title': selected_socialize.title,
        # 'socialize_description': selected_socialize['description']
        'socialize_description': selected_socialize.description
    })
    except Exception as exc:
        return render(request, 'socialize/socializes-details.html', {
            'socialize_found': False
        }) 
