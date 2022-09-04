

from django.db.models.aggregates import Count
# ============================================================================ #
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework import status
from rest_framework.permissions import IsAdminOrReadOnly, IsAuthenticatedOrReadOnly
# ============================================================================ #
from .models import Category, Blog
from .serializers  import CategorySerializer, BlogSerializer,  CategoryDetailSerializer
from .permissions import IsOwnerOrReadOnly




# ============================================================================ #
#                                     BLOG                                     #
# ============================================================================ #


class BlogList(ListCreateAPIView):
    
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class BlogDetail(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsOwnerOrReadOnly,]



class BlogListByAuthor(ListAPIView):
    serializer_class = BlogSerializer

    def get_queryset(self):
        return Blog.objects.filter(author__username=self.kwargs['username'])



# ============================================================================ #
#                                   CATEGORY                                   #
# ============================================================================ #


# ================================ CLASS VIEWS =============================== #


class CategoryDetail(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    permission_classes = [IsAdminOrReadOnly,]




# ============================== FUNCTION VIEWS ============================== #


@api_view(['GET', 'POST'])
def category_list(request):
    if request.method == 'GET':
        category = Category.objects.annotate(blogs_count=Count('blogs')).all()
        serializer = CategorySerializer(category, many=True, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, pk):
    category = Category.objects.get(id=pk)

    if request.method == 'GET':
        serializers = CategoryDetailSerializer(category)
        return Response(serializers.data)

    elif request.method == 'PUT':
        serializers = CategoryDetailSerializer(category, data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)

    elif request.method == 'DELETE':
        if category.blogs.count() > 0:
            return Response({'error': 'Categoryga bogliq bloglar borligi sabab buni oshira olmaysiz'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




