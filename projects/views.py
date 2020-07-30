from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dt

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def project_of_day(request):
	date = dt.date.today()
	return render(request, 'all_projects/today-project.html', {"date": date,})

def past_projects(request, past_date):
	try:
		date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

	except valueError:
		raise Http404()
		assertFalse

	if date == dt.date.today():
		return redirect(project_of_day)

	return render(request, 'all_projects/past-project.html', {"date": date})
