"""
URL configuration for designhunt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from authorization import views as authorization_views
from create_portfolio import views as create_portfolio_views
from designers import views as designers
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', authorization_views.authorization, name = 'authorization'),
    path('registration/', authorization_views.registration, name='registration'),
    path('designers/', designers.designers, name='designers'),
    path('logout/', authorization_views.logout_view, name='logout'),
    path('admin/', admin.site.urls),
    path('create_portfolio/', create_portfolio_views.create_portfolio, name='create_portfolio'),
    path('accounts/', include('allauth.urls')),
    path('', include('portfolio.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)