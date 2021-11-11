from django.urls import path
from . import views
from django.utils.translation import gettext as _

app_name = 'lang'

urlpatterns = [
    path('', views.home, name='home'),
    path(_('item/'), views.item, name='item'),
]
