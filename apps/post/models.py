from django.db import models
# ============================================================================ #

# ================================= CATEGORY ================================= #

class Category(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=50, blank=True)
    data_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# =================================== BLOG =================================== #

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    images = models.ImageField(upload_to="media", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, related_name="blogs")
    data_pub = models.DateTimeField(auto_now=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title