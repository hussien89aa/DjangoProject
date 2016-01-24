"""managmentstudio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
    #from sellingportal.views import Index,Home,Details
      #url(r'^$',Index,name='index'),
    #url(r'^home/$',Home,name='home'),
    # url(r'^details/(?P<student_id>[a-zA-Z-0-9-.-_/]+)',Details,name='details'),
     #url(r'^details/(?P<student_id>[0-9]+)/$',Details,name='details'),
     #url(r'^(?P<student_id>[0-9]+)/details/$', Details, name='details'),
"""
from django.conf.urls import url
from django.contrib import admin
from sellingportal.views import Index,Student,StudentDegree,Register
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',Index,name='index'),
    url(r'^student/$',Student,name='student'),
    url(r'^degree/(?P<student_id>[0-9]+)/$',StudentDegree,name='degree'),
    url(r'^register/$',Register,name='register'),

]
