from django.db import models

from django.conf import settings
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


class Post(models.Model):
    title            = models.CharField(max_length=200, blank=False, null=False)
    body             = models.TextField(blank=False)
    image            = models.ImageField(upload_to=upload_img_name, null=True)
    author           = models.ForeignKey(to="users.User", on_delete=models.CASCADE)
    slug             = models.SlugField(unique=True, null=True, blank=True)
    date_published   = models.DateTimeField(auto_now_add=True) # can be modified
    date_created     = models.DateTimeField(auto_now=True)


    def __str__(self):
        if self.slug:
            return self.slug
        return self.title
    # def get_absolute_url(self):
    #     return reverse('blog:detail', kwargs={'slug': self.slug})


    # def save(self, *args, **kwargs):  # new
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     return super().save(*args, **kwargs)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.author.username + '-' + self.title)
        super(Post, self).save(*args, **kwargs)


# Delete image when post is deleted
@receiver(post_delete, sender=Post)
def submit_delete(sender, instance, **kwargs):
    instance.image.delete(False)

# @receiver(post_save, sender=Post)
# def post_slugify(sender, instance=None, created=False, **kwargs):
#     if created:
#         instance.slug = slugify('title')


# def pre_save_post_receiver(sender, instance, *args, **kwargs):

#         print("")
#         print(instance.author.username)
#         print(sender.author.username)
#         print("")
#         instance.slug = slugify(instance.author.username + '-' + instance.title)

# pre_save.connect(pre_save_post_receiver, sender=Post)


# what if I do it like this?
# @receiver(post_save, sender=Post)
# def post_slugify(sender, instance, **kwargs):
#     # if not instance.slug:
#         print("What~!!!!!!!!!!!!!!!!")
#         print(instance.author.username)
#         print(sender.author.username)
#         print("")
#         instance.slug = slugify(instance.author.username + '-' + instance.title)

# @receiver(post_save, sender=Post)
# def post_slugify(sender, instance=None, created=False, **kwargs):
#     if created:
#         instance.slug = slugify('title')
