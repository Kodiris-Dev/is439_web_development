"""ezekielPrototype URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from django.views.generic import RedirectView, TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(
        pattern_name='home_urlpattern',
        permanent=False
    )),
    path('home/',
         TemplateView.as_view(
             template_name='app_info/home.html'),
         name='home_urlpattern'
         ),
    path('login/',
         LoginView.as_view(template_name='app_info/login.html'),
         name='login_urlpattern'
         ),
    path('logout/',
         LogoutView.as_view(),
         name='logout_urlpattern'
         ),
    path('', include('app_info.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
