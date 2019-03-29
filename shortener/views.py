from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .models import Address
from .forms import AddressForm


def main(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            # TODO with commit=False it crashes. How to handle it?
            # if form.shorten_address():
            # AttributeError: 'AddressForm' object has no attribute 'shorten_address'
            if form.shorten_address():
                form.shorten_address()
                form.save()
                return redirect('details', shortened=form.shortened)
            else:
                form.delete()
                form = AddressForm(request.GET)
                return render(request, 'shortener/main.html', {'form': form})

    elif request.method == 'GET':
        form = AddressForm()
    return render(request, 'shortener/main.html', {'form': form})


def present_shortened_address(request, shortened):
    shortened_address = get_object_or_404(Address, shortened=shortened)  # accessing corresponding url of short in DB
    response = f"http://127.0.0.1:8000/{shortened_address.shortened}"
    return render(request, 'shortener/details.html', {'shortened': response})


def redirect_to_original_address(request, shortened):
    response = get_object_or_404(Address, shortened=shortened)
    return HttpResponseRedirect(response.get_original_address())
