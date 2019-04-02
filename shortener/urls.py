from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),  # main page view
    path('<shortened>/details/', views.present_shortened_address, name='details'),  # presenting short
    path('<shortened>/', views.redirect_to_original_address, name='redirect'),  # redirection to original URL
]