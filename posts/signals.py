from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Post, Follow, Stream


@receiver(post_save, sender=Post)
def add_post(sender, instance, created, **kwargs):
    if created:
        followers = Follow.objects.filter(following=instance.user)
        for follower in followers:
            stream = Stream(post=instance, user=follower.follower, date=instance.created, following=instance.user)
            stream.save()


# @receiver(post_save, sender=Follow)
# def user_follow(sender, instance, created, **kwargs):
#     if created:
#
#
# @receiver(post_delete, sender=Follow)
# def user_unfollow(sender, instance, created, **kwargs):
#



