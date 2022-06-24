from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
from .models import City
from .forms import CityForm,RegisterForm



# Create your views here.

def index(request):
	url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=7fe68d95a3bb236f241fbfa9c5978a5b'
	if request.method == 'POST':
		form = CityForm(request.POST)
		form.save()
	form = CityForm()
	cities = City.objects.all()
	weather_data = []
	for city in cities:
		r = requests.get(url.format(city)).json()

		city_weather = {
			'city': city.name,
			'id':city.id,
			'temperature': r['main']['temp'],
			'humidity': r['main']['humidity'],
			'description': r['weather'][0]['description'],
			'icon': r['weather'][0]['icon'],
		}
		weather_data.append(city_weather)

	context = {'weather_data': weather_data, 'form': form}
	return render(request, 'weather.html', context)


def delete_city(request, city_id):
	City.objects.get(id=city_id).delete()
	return redirect('weatherhome')


def register(response):
	if response.method == "POST":
		form = RegisterForm(response.POST)
		if form.is_valid():
			form.save()

		return redirect("login")
	else:
		form = RegisterForm()

	return render(response, "registration/register.html", {"form": form})