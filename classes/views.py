from django.shortcuts import render
from .models import Section
from django.db.models import Q
from datetime import time
import re

# Create your views here.
def index(request):
    context = {

    }
    return render(request, 'classes/index.html', context)

def details(request, id):
    classe = Section.objects.get(id=id)
    context = {
        'classe': classe
    }

    return render(request, 'classes/details.html', context)

# Filter by course, number, section, day, and time
def search_terms(query):
    query = query.split()
    results = Section.objects.all()
    foundMatch = False

    for q in query:
        # Day
        if re.match("[MTWThF]+", q):
            results = results.filter(day__icontains = q)
        # Course
        elif len(q) == 3 and q.isalpha():
            results = results.filter(course__icontains = q)
        # Number
        elif len(q) == 3 and q.isdigit():
            results = results.filter(number__icontains = q)
        # Section
        elif re.match("[A-Z]\d\d[A-Z]?", q):
            results = results.filter(section__icontains = q)
        # Time
        elif re.match("\d\d:\d\d", q):
            t = q.split(":")
            t = time(hour = int(t[0]), minute = int(t[1]))
            results = results.filter(starttime__lte = t, endtime__gte = t)
        # Badly formatted
        else:
            results = Section.objects.none()

    return results

def search(request):
    template = 'classes/searches.html'
    query = request.GET.get('q')
    if len(query) == 0:
        results = Section.objects.none()
    else:
        results = search_terms(query)
    context = {
        'classes': results
    }

    return render(request, template, context)
