from django.contrib import admin


# Disable Site admins
from django.contrib.sites.models import Site

admin.site.unregister(Site)


# Disable Auth admins
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
User = get_user_model()

admin.site.unregister(User)
admin.site.unregister(Group)


# Disable Mezzanine admins
from mezzanine.conf.models import Setting
from django.contrib.comments.models import Comment

admin.site.unregister(Setting)
admin.site.unregister(Comment)


# Patch the Page get_absolute_url
from mezzanine.pages.models import Page
from widgy.contrib.widgy_mezzanine import get_widgypage_model
from subdomains.utils import reverse
try:
    from urllib.parse import urljoin
except ImportError:     # Python 2
    from urlparse import urljoin


WidgyPage = get_widgypage_model()


def page_get_absolute_url(self):
    slug = self.slug
    if self.content_model == "link":
        # Ensure the URL is absolute.
        slug = urljoin('/', slug)
        return slug
    if slug == "/":
        return reverse("home", subdomain='demo')
    else:
        return reverse("page", subdomain='demo', kwargs={"slug": slug})

WidgyPage.get_absolute_url = Page.get_absolute_url = page_get_absolute_url
