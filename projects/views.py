from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to Fred Ojures Projects')

def project_of_day(request):
	date = dt.date.today()
	day = convert_dates(date)

	html = f'''
		<html>
			<body>
				<h1> Projet for {day} {date.day} - {date.month} - {date.year} </h1>
			</body>
		</html>
		'''
	return HttpResponse(html)

def convert_dates(dates):
	day_number = dt.date.weekday(dates)

	days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

	#Returning the actual day of the week
	day = days[day_number]
	return day
