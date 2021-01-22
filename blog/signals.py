from django.db.models import signals
from django.dispatch import receiver
from .models import Post


#also we have post-save action
@receiver(signals.pre_save, sender=Post)
def post_pre_save(sender, instance, raw, using, update_fields, **kwargs):
    instance.title = "{} {}".format(instance.title, "elham")