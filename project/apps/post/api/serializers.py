from unicodedata import category
from rest_framework import serializers
from ..models import Category, Blog
# ============================================================================ #

# ============================== BLOGSERIALIZER ============================== #
class BlogSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    category = serializers.StringRelatedField()
    class Meta:
        model = Blog
        fields = ['id', 'title', 'description', 'body', 'author', 'images', 'category', 'created_at', 'updated_at']



# ============================ CATEGORY SERIALZIER =========================== #
class CategorySerializer(serializers.ModelSerializer):
    
    blogs_count = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Category
        fields = ['id', 'title', 'sub_title', 'created_at', 'blogs_count' ]

class CategoryDetailSerializer(serializers.ModelSerializer):

    blogs = BlogSerializer(many=True, read_only=True)
    blogs_count = serializers.IntegerField(read_only=True)
  
    class Meta:
        model = Category
        fields = ['id', 'title', 'sub_title', 'created_at', 'blogs', 'blogs_count']