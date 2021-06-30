from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def index(request):
    socialize = [
        {
            'title': 'This is our First Hangouts'
        },
        {
            'title': 'This is our Second Hangouts'
        }
    ]
    return render(request, 'socialize/index.html', {
        #'show_socialize': False,
        'show_socialize': True,
        'socialize': socialize
    })
#   return HttpResponse('Hello django!')

