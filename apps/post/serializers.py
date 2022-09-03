from rest_framework import serializers
from .models import Category, Blog
# ============================================================================ #

# ============================== BLOGSERIALIZER ============================== #
class BlogSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Blog
        fields = ['id', 'title', 'description', 'body', 'author', 'images', 'category', 'data_pub', 'last_update']



# ============================ CATEGORY SERIALZIER =========================== #
class CategorySerializer(serializers.ModelSerializer):
    
    blogs_count = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Category
        fields = ['id', 'title', 'sub_title', 'data_pub', 'blogs_count' ]

class CategoryDetailSerializer(serializers.ModelSerializer):

    blogs = BlogSerializer(many=True, read_only=True)
    blogs_count = serializers.IntegerField(read_only=True)
  
    class Meta:
        model = Category
        fields = ['id', 'title', 'sub_title', 'data_pub', 'blogs', 'blogs_count']