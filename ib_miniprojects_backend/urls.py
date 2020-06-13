"""ib_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
import os


api = []

apps = list(settings.SWAGGER_UTILS['APPS'].keys())
apps += getattr(settings, 'THIRD_PARTY_SWAGGER_APPS', [])

for app_name in apps:
    try:
        api.append(url(r'^' + app_name + '/', include(app_name + '.build.urls')))
    except ImportError:
        pass


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api)),
]

urlpatterns += [
    url(r'^swagger/', include('django_swagger_utils.urls', namespace='swagger_ui')),
    url(r'^accounts/', include('django_swagger_utils.auth_urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^fine-uploader/', include('django_fine_uploader_s3.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf import settings

if settings.DEBUG:
    urlpatterns += [
        url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    ]
