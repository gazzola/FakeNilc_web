from django.urls import path

from . import views

app_name = 'classifier'

urlpatterns = [
	path('ajax/check/', views.check, name='check'),
    path('', views.classif, name='classif'),
    path('about', views.about, name='about')
]