from django.core.management.base import BaseCommand

from bazaar.models import Bazaar


class Command(BaseCommand):
    help = 'Create new bazaars'

    def handle(self, *args, **kwargs):
        Bazaar.objects.create(user_id=1, bazaar_date='2018-12-01', item_name='Alu', item_weight=3, item_price=75)
        Bazaar.objects.create(user_id=1, bazaar_date='2018-12-01', item_name='Chal', item_weight=5, item_price=500)
        Bazaar.objects.create(user_id=1, bazaar_date='2018-12-01', item_name='Piaj', item_weight=1, item_price=55)

        Bazaar.objects.create(user_id=2, bazaar_date='2018-12-01', item_name='Alu', item_weight=1, item_price=25)
        Bazaar.objects.create(user_id=2, bazaar_date='2018-12-01', item_name='Chal', item_weight=4, item_price=400)
        Bazaar.objects.create(user_id=2, bazaar_date='2018-12-01', item_name='Piaj', item_weight=1, item_price=55)
