from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def index(request):
    socialize = [
        {
            'title': 'This is our First Hangouts',
            'location': 'Gotland Amusement Park',
            'group_name': 'Baby-doll',
            'slug': 'x-first-hangouts'
        },
        {
            'title': 'This is our Second Hangouts',
            'location': 'Malmo Sea beach',
            'group_name': 'Charming-Prince',
            'slug': 'x-second-hangouts'
        }
    ]
    return render(request, 'socialize/index.html', {
        #'show_socialize': False,
        'show_socialize': True,
        'socialize': socialize
    })
#   return HttpResponse('Hello django!')

