"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from Hello import views
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from mysite import settings
from django.views.generic import TemplateView
from django.conf.urls.static import static

urlpatterns = [
    #url(r'^users/(?P<q>\d+)/$', views.all_questions, name='your_name_here'),
    url('openapi/', TemplateView.as_view(template_name="index2.html")),
    path('family/<path:m>/create/', views.make),
    path('family/<path:m>/',  views.redirect, name='archive'),
    path('api_documentation/',views.schema_view),
    #path('hello-world-13/', include('Hello.urls')),
    path('admin/', admin.site.urls),
    path('register/', views.register),
    path('', views.index),
    path('try/', views.tryq),
    #path('show/', views.show),
    path('create/', views.create),
    path('swagger/c', views.swagger),
    path('all_questions/', views.all_questions),
    #url('login/',views.login_view,name="login"),
    #url(r'^client/(?P<slug>[\w.@+-]+)/$', views.IndexClientView.as_view(), name='indexClient'),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.STATIC_URL)
