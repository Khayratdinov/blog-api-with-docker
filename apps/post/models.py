from django.db import models
# ============================================================================ #
from apps.users.models import User 
from apps.common.models import TimeStampedUUIDModel


# ================================= CATEGORY ================================= #

class Category(TimeStampedUUIDModel):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title


# =================================== BLOG =================================== #

class Blog(TimeStampedUUIDModel):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")
    images = models.ImageField(upload_to="media", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, related_name="blogs")

    def __str__(self):
        return self.title