from django.dispatch import receiver
from django.db.models.signals import post_save

from news.models import News


@receiver(post_save, sender=News)
def order_item_post_save(sender, instance: News, created, *args, **kwargs):
    if created:
        category = instance.category
        category.rating += 1
        category.save()