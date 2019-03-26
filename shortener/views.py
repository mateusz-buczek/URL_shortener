from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    return HttpResponse('Url shortener main page')

# TODO view returning shortened address - decide path: by number in DB or shortened url name?
# TODO view redirecting to original url when shortened address requested 
