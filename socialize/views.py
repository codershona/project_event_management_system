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

def socializes_details(request, socializes_slug):
    print(socializes_slug)
    selected_socialize = {
        'title': 'Here First Party',
        'description': 'This is another first Socialize party!!'
        }
    return render(request, 'socialize/socializes-details.html', {
        'socialize_title': selected_socialize['title'],
        'socialize_description': selected_socialize['description']
    })
