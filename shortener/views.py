from django.shortcuts import render
from django.http import HttpResponse
from .models import Addresses


def main(request):
    return HttpResponse('Url shortener main page')


def present_shortened_address(request, shortened):
    shortened_address = Addresses.objects.get(shortened__exact=shortened)  # accessing corresponding url of short in DB
    response = f"Your shortened link: http://127.0.0.1:8000/{shortened_address.get_shortened()}"  #TODO make it
    # generating in block content in html with css support
    return HttpResponse(response)

# TODO view returning shortened address - decide path: by number in DB or shortened url name? (after pressing button)
# TODO view redirecting to original url when shortened address requested
