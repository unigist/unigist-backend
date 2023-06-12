import uuid
from django.db import models
from django.conf import settings
from django.db.models.query import QuerySet
from django.utils.text import slugify
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.
def upload_img_name(instance, filename):
    file_path = 'blog/{author_id}/{title}-{filename}'.format(
        author_id=instance.author.id,
        title = instance.title,
        filename=filename
    )
    return file_path

class PostPublishedManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(status='P')

class PostDraftManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(status='D')


class Post(models.Model):
    public_id        = models.UUIDField(db_index=True, editable=False, unique=True, default=uuid.uuid4)
    title            = models.CharField(max_length=200, blank=False, null=False)
    body             = models.TextField(blank=False)
    image            = models.ImageField(upload_to=upload_img_name, null=True)
    author           = models.ForeignKey(to="users.User", on_delete=models.CASCADE)
    slug             = models.SlugField(unique=True, null=True, blank=True)
    created          = models.DateTimeField(auto_now_add=True) # can't be modified
    published        = models.DateTimeField(auto_now=True)
    edited           = models.BooleanField(default=False)
    updated          = models.DateTimeField(auto_now=True)
    status           = models.CharField(
        max_length=1, default='D', choices=[('P', ('Published')), ('D', ('Draft'))]
    )

    articles  = models.Manager()
    published = PostPublishedManager()
    draft     = PostDraftManager()

    def __str__(self):
        if self.slug:
            return self.slug
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.author.username + '-' + self.title)
        super(Post, self).save(*args, **kwargs)


# Delete image when post is deleted
@receiver(post_delete, sender=Post)
def submit_delete(sender, instance, **kwargs):
    instance.image.delete(False)
