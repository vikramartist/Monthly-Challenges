from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
monthly_challenges = {
    "January": "Learn web development",
    "February": "learn react as a front end framework",
    "March": "Learn backend programming either python/ java",
    "April": "Learn backend frameworks like Django",
    "May": "Do some projects of the same using full stack knowledge",
    "June": "Learn datastructures",
    "July": "Learn algorithms",
    "August": "Practice",
    "September": "Practice",
    "October": "Practice",
    "November": "Attend Interviews",
    "December": "Attend Interviews"
}


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if (month < 0 or month > len(months)):
        return HttpResponseNotFound("Error, the month can be only between 1 and 12")
    redirect = months[month-1]
    redirect_path = reverse('month-challenge', args=[redirect])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge = monthly_challenges[month.title()]
        return render(request, "challenges/challenge.html", {'month': challenge, 'title': month})
    except:
        return Http404()


def home(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {'months': months})
