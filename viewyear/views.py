from django.shortcuts import render

from django.http import HttpResponse
from .models import MoodOfTheDay
from django.template import loader
from calendar import monthrange


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def get_person(request, person_name, year):
    year_data = MoodOfTheDay.objects.filter(person_name=person_name, year=year)
    month_names = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    month_names_short = ['j', 'f', 'm', 'a', 'm', 'j', 'j', 'a', 's', 'o', 'n', 'd']

    data = []

    for ii in range(12):
        monthly_data = {}
        monthly_data["name"] = month_names[ii]
        monthly_data["name_short"] = month_names_short[ii]
        monthly_data["data"] = []
        for day in range(monthrange(year, ii + 1)[1]):
            monthly_data["data"].append(year_data.filter(month=ii + 1, day=day + 1))

        data.append(monthly_data)

    template = loader.get_template("viewyear/index.html")

    context = {"mood_data": data, "person_name": person_name}
    return HttpResponse(template.render(context, request))


def set_mood(request, person_name, year, month, day, mood):
    # Look up if mood is already set.
    old = MoodOfTheDay.objects.filter(person_name=person_name, year=year, month=month, day=day)
    if len(old) > 0:
        old.delete()

    m = MoodOfTheDay(person_name=person_name, year=year, month=month, day=day, mood=mood)
    m.save()
    return HttpResponse(str(m))
