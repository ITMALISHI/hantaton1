from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path('event/<slug:event_slug>', show_event, name="event"),
    path('registration/', registration, name='reg'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('onTakeoff/', takeoff, name='takeoff'),
    path('faq/', faq, name='faq'),
    path('forma/', forma, name='forma')
]