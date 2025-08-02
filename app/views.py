from django.shortcuts import render
import requests 
# Create your views here.

def index(request):

    city= request.GET.get('city', 'bangalore')
    api_key="12275acb77446e1742a43128239f5fb4"

    api_url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    print(api_url)
    api=requests.get(api_url).json()
    temperature=api['main']['temp']
    contry=api['sys']['country']
    city=api['name']
    return render(requests,'index.html', {'temperature':temperature, 'contry':contry,'City':city})
