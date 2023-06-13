from django.db import models
from django.db.models.query import QuerySet
from ..users.models import User
from ..posts.models import Post

import uuid

# Create your models here.

class Comment(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.PROTECT)
    post = models.ForeignKey(to=Post, on_delete=models.PROTECT)

    public_id = models.UUIDField(db_index=True, unique=True, default=uuid.uuid4, editable=False)
    content = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)

    comments = models.Manager()


    def __str__(self):
        return self.author.name
