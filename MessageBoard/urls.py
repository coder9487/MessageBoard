"""
URL configuration for MessageBoard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    #path('account/', include('django.contrib.auth.urls')),
    path('intro/', include('intro.urls')),
    path('', include('login.urls')),
    path('', include('logout.urls')),
    path('admin/', admin.site.urls),
    path('login/', include('login.urls')),
    path('', include('message_board.urls')),
    path('login/', include('message_board.urls')),
]
