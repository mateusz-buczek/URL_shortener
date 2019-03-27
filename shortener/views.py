from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .models import Addresses
from .forms import AddressesForm

def main(request):
    form = AddressesForm()
    return render(request, 'shortener/main.html', {'form': form})


def present_shortened_address(request, shortened):
    shortened_address = get_object_or_404(Addresses, shortened=shortened)  # accessing corresponding url of short in DB
    response = f"http://127.0.0.1:8000/{shortened_address.get_shortened()}"
    return render(request, 'shortener/details.html', {'shortened': response})


def redirect_to_original_address(request, shortened):
    response = get_object_or_404(Addresses, shortened=shortened)
    return HttpResponseRedirect(response.get_original())
