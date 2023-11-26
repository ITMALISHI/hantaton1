from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from .forms import myUserCreationForm
from django.contrib.auth.models import Group
from django.db.models import Q, Count

from .models import *

def index(request):

    categories = Category.objects.all()
    selected_categor = request.POST.getlist("categor_for_select")
    print(selected_categor)
    if selected_categor == []:
        events = Event.objects.all()
    else:
        events = Event.objects.filter(eventcategory__idCategory__in=selected_categor).annotate(num_genres=Count('eventcategory')).filter(num_genres=len(selected_categor))
    context = {
        'categories': categories,
        "events": events,
    }
    return render(request, context=context, template_name='growplace/index.html')

def show_event(request, event_slug):
    button_flag = 'false'
    event = get_object_or_404(Event, slug=event_slug)
    organizers = EventOrganizer.objects.filter(idEvent=event.pk)
    tags = EventCategory.objects.filter(idEvent=event)
    if request.user.is_anonymous:
        button_flag = 'anon'
    elif UserEvent.objects.filter(idEvent_id=event, idUser=request.user).exists():
        button_flag = 'true'
    else:
        if request.POST:
            UserEvent.objects.create(idEvent=event, idUser=request.user)
    content = {
        'tags': tags,
        'event': event,
        'organizers': organizers,
        'button_off': button_flag
    }
    return render(request, 'growplace/mero.html', context=content)

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'growplace/Enter.html'


class LogoutUser(LogoutView):
    next_page = "/"



def registration(request):
    if request.method == 'POST':
        form = myUserCreationForm(request.POST)
        if form.is_valid():
            organiser = request.POST.getlist('org_box')
            form.save()
            # получаем имя пользователя и пароль из формы
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            # выполняем аутентификацию
            user = authenticate(username=username, password=password)
            if organiser[0] == 'on':
                group = Group.objects.get(name='Organizer')
                group.user_set.add(user)
            else:
                group = Group.objects.get(name='ITshnik')
                group.user_set.add(user)
            print(organiser)
            login(request, user)
            return redirect('/')
    else:
        form = myUserCreationForm()
    return render(request, 'growplace/registration.html', {'form': form})
@login_required()
def takeoff(request):
    user_events = UserEvent.objects.filter(idUser=request.user)
    return render(request, 'growplace/onVzlet.html', {'events': user_events})

def faq(requests):
    return render(requests, 'growplace/FAQ.html', context=None)

@login_required()
def forma(requests):
    return render(requests, 'growplace/forma.html', context=None)