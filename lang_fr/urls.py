from django.urls import path
from . import views

app_name = 'lang_fr'
urlpatterns = [
    path('french/', views.french, name='french')
]