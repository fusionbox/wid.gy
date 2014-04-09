from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    can_import_Settings = True

    def handle(self, *args, **kwargs):
        User = get_user_model()
        admin_user, created = User.objects.get_or_create(
            username='admin',
        )

        admin_user.is_superuser = True
        admin_user.is_staff = True
        admin_user.set_password('admin')
        admin_user.save()
