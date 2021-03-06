from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .models import Address
from .forms import AddressForm


# TODO implement generic views
def main(request):  # view of main page
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            if address.shorten_address():
                address.shorten_address()
                address.save()
                return redirect('details', shortened=address.shortened)

            elif address.shorten_address() == False:
                pass
    else:
        form = AddressForm()
    return render(request, 'shortener/main.html', {'form': form})


def present_shortened_address(request, shortened):  # view presenting shortened address
    return render(request, 'shortener/details.html', {'shortened': shortened})


def redirect_to_original_address(request, shortened):  # redirecting to original URL
    response = get_object_or_404(Address, shortened=shortened)
    return HttpResponseRedirect(response.get_original_address())
