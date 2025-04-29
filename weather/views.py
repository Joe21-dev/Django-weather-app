import requests
from django.shortcuts import render
from django.conf import settings

def home(request):
    weather_data = {}
    if request.method == 'POST':
        city = request.POST.get('city')
        if city:
            api_key = settings.WEATHER_API_KEY
            url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=metric&include=current&key={api_key}&contentType=json"
            ##url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric' 
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                current_conditions = data['currentConditions']
                weather_data = {
                'city': city.title(),
                'temperature': current_conditions['temp'],
                'condition': current_conditions['conditions'].title(),
                'humidity': current_conditions['humidity']
            }

            else:
                weather_data['error'] = 'City not found.'
        else:
            weather_data['error'] = 'Please enter a city.'
    return render(request, 'weather/weather.html', {'weather': weather_data})
