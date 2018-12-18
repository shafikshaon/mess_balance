from django.core.management.base import BaseCommand

from accounts.models import User


class Command(BaseCommand):
    help = 'Create new users'

    def handle(self, *args, **kwargs):
        # User.objects.create_user(username='shafikshaon', email='shafikshaon@gmail.com', password='P@ss1234',
        #                          is_superuser=True, member_from='2018-12-18', user=1)
        User.objects.create_user(username='shafikurrahman', email='shafikurrahman@gmail.com', password='P@ss1234',
                                 is_superuser=True, member_from='2018-12-18')
