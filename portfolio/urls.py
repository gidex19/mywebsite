from django.urls import path
from . import views as portfolio_views

urlpatterns=[
    path('', portfolio_views.home, name = 'home'),
    path('services/', portfolio_views.services, name = 'services'),
    path('portfolio/', portfolio_views.portfolio, name='portfolio'),
    path('contact/', portfolio_views.contact, name='contact'),
]