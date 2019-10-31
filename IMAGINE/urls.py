"""IMAGINE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from price.admin import admin_site
from django.urls import path, include
from price import urls
from django.conf import settings
from django.conf.urls.static import static
from contact.views import ContactListView
from django.contrib import admin

urlpatterns = [
    
    path('admin/', admin_site.urls),
    path('price/', include('price.urls')),
    path('', include('portfolio.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')), 
    path('contact/', ContactListView.as_view(), name='contact'),
    path('adminauth/', admin.site.urls )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )