from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('<shortened>/details/', views.present_shortened_address, name='details'),
    path('<shortened>/', views.redirect_to_original_address, name='redirect'),
]