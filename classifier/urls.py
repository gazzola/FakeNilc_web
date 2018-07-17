from django.urls import path

from . import views

app_name = 'classifier'

urlpatterns = [
	path('ajax/check/', views.check, name='check'),
    path('', views.index, name='index')
]