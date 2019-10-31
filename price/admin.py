
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
# Register your models here.
from .models import Category, Price

from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
# Register your models here.

class MyAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = ugettext_lazy('AZ Photo')

    # Text to put in each page's <h1> (and above login form).
    site_header = ugettext_lazy('AZ Photo')

    # Text to put at the top of the admin index page.
    index_title = ugettext_lazy('AZ Photo Photography Administration')

admin_site = MyAdminSite()

admin_site.register(Price)