from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenges_dict = {
    "january": "Do Django for 20 minutes a day.",
    "february": "Practice piano for at least 30 minutes each day.",
    "march": "Walk for at least 30 minutes each day.",
    "april": "Drink at least 3 glasses of water each day.",
    "may": "Brush your teeth twice every day.",
    "june": "Sleep for 8-9 hours every day.",
    "july": "Do at least 15 minutes of yoga each day.",
    "august": "Wake up early each and every day.",
    "september": None,
    "october": "Start a blog and write in it every single day.",
    "november": "Write a poem every day about something that you experiences that day.",
    "december": None
}

# Create your views here.

def index(request):
    months = list(monthly_challenges_dict.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def month_by_num(request, month):
    months = list(monthly_challenges_dict.keys())

    if month > len(months):
        return HttpResponseNotFound("This is an invalid month.")


    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return(HttpResponseRedirect(redirect_path))


def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenges_dict[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
    except:
        raise Http404()
    