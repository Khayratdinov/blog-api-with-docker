from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=20, null=True, blank=True)
    subTitle = models.CharField(max_length=10, null=True, blank=True)
    
    
class Post(models.Model):
    title = models.CharField(max_length=20, null=True, blank=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    content = models.TextField(max_length=100, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='post')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['created_at']
        
    def __str__(self):
        return self.title