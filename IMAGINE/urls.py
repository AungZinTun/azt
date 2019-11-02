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
from django.conf.urls import handler404, handler500

def page_not_found(request):
    response=render_to_response('404.html', context_instance=RequestContext(request))
    response.status_code=404
    return response

urlpatterns = [
    
    path('admin/', admin_site.urls),
    path('price/', include('price.urls')),
    path('', include('portfolio.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')), 
    path('contact/', ContactListView.as_view(), name='contact'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
hadnler404=page_not_found


