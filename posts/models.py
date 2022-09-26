from django.db import models
import uuid
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

from accounts.models import Profile
User = get_user_model()


def user_directory_path(instance, filename):
    """Формируем путь к картинке"""
    # файл будет загружен в MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Tag(models.Model):
    title = models.CharField(max_length=75)
    slug = models.SlugField(max_length=75, unique_for_date='created')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def get_absolute_url(self):
        return reverse('tags', args=[self.slug])

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


# class PostFileContent(models.Model):
#     user = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name='content_owner'
#     )
#     file = models.FileField(upload_to=user_directory_path)


class Post(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # contents = models.ManyToManyField(
    #     PostFileContent,
    #     related_name='contents'
    # )
    picture = models.ImageField(upload_to='picture/%Y/%m/%d')
    description = models.TextField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)
    tags = models.ManyToManyField(Tag, related_name='tags', blank=True)
    favorites = models.ManyToManyField(Profile, blank=True)
    liked = models.ManyToManyField(User, blank=True, related_name='like')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def get_absolute_url(self):
        return reverse('', args=[self.pk])

    def __str__(self):
        return f'Post by: {self.user.username}'


class Follow(models.Model):
    follower = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        related_name='follower'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        related_name='following'
    )

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'


class Stream(models.Model):
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='stream_following'
    )
    post = models.ForeignKey(
        Post,
        null=True,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    date = models.DateTimeField()
