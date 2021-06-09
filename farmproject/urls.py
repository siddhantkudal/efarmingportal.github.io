"""farmproject URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from index import views
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.firstpage),
    path('register/',views.register),
    path('login/',views.login),
    path('homepage/',views.homepage),
    path('search<id>/',views.search),
    path('cart',views.order),
    path('orderlist/',views.orderlist),
    #path('receipt/',views.render_pdf_view),
    path('contactus/',views.contactus),
    path('mys/',include('MYS.urls')),
    path('logout/',views.logout),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
