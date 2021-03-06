"""metroservices URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path
from orderapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index_page),
    path('login/', views.Login),
    path('accounts/',include('django.contrib.auth.urls')),
    path('signup/', views.signup_view),
    path('home/', views.show_view),
    path('logout/', views.Logout),
    path('insert/', views.insert_view),
    url(r'^delete/(?P<id>\d+)/$', views.delete_view),
    url(r'^update/(?P<id>\d+)/$', views.update_view),
    path('sendmail/', views.mail_send_view),

]
