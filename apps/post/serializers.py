from .models import Post, Category
from rest_framework import serializers
        
class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ['title', 'subTitle']
    
    
class PostSerializer(serializers.ModelSerializer):
  
  class Meta:    
    model = Post
    fields = ["title", "description", "content", "category"]
    extra_kwargs = {'category': {'read_only': True}}
    
  def get_title_category(self, category):
    if category:
      title = category.title
    return title
  
  def get_category(self, category):
    if category:
      return self.category