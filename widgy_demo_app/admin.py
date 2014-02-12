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
