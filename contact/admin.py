from django.contrib import admin
from price.admin import admin_site
# Register your models here.
from .models import Contact

admin_site.register(Contact)