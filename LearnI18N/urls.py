from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path
from django.views.i18n import JavaScriptCatalog

from home.views import home_view

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', home_view, name='index'),
    path("jsi18n/", JavaScriptCatalog.as_view(), name="javascript-catalog"),
)
