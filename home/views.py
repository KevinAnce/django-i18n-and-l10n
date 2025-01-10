from django.shortcuts import render

from home.models import Greeting


def home_view(request):
    return render(request, template_name="index.html", context={"greetings": Greeting.objects.all()})
