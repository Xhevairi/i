
from django.contrib import admin
from django.conf import settings

# i18n before include
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include, re_path
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path(_('admin/'), admin.site.urls),
    path('', include('lang_fr.urls', namespace='lang_fr'))
]
# adding i18n
urlpatterns += i18n_patterns(
    path('', include('lang.urls', namespace='lang')),
    # path('', include('lang_fr.urls', namespace='lang_fr')),
)

# adding rossetta
if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]