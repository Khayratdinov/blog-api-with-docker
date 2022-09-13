

from django.db.models.aggregates import Count
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
# ============================================================================ #
from rest_framework.decorators import action, permission_classes as view_permission_classes
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework import status
from rest_framework.permissions import  IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet, GenericViewSet
# ============================================================================ #
from apps.common.permissions import IsSuperUserOrAuthorOrReadOnly, IsSuperUserOrReadOnly

from apps.post.models import Category, Blog
from apps.post.api.serializers  import CategorySerializer, BlogSerializer,  CategoryDetailSerializer
from apps.post.pagination import DefaultPagination




# ============================================================================ #
#                                     BLOG                                     #
# ============================================================================ #



class BlogViewSet(ModelViewSet):

    serializer_class = BlogSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['created_at',]
    pagination_class = DefaultPagination


    def get_queryset(self):
        return Blog.objects.select_related_object('category')

    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE']:
            return [IsSuperUserOrAuthorOrReadOnly()]
        return [IsAuthenticatedOrReadOnly()]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)





class BlogListByAuthor(ListAPIView):
    serializer_class = BlogSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['data_pub',]
    pagination_class = DefaultPagination

    def get_queryset(self):
        return Blog.objects.filter(author__username=self.kwargs['username'])

    




# ============================================================================ #
#                                   CATEGORY                                   #
# ============================================================================ #


class CategoryDetail(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.active()
    serializer_class = CategoryDetailSerializer
    permission_classes = [IsSuperUserOrReadOnly,]



# ============================================================================ #
#                                   OLD CODE                                   #
# ============================================================================ #



# ============================================================================ #
#                                   CATEGORY                                   #
# ============================================================================ #

# ============================== FUNCTION VIEWS ============================== #


# @api_view(['GET', 'POST'])
# def category_list(request):
#     if request.method == 'GET':
#         category = Category.objects.annotate(blogs_count=Count('blogs')).all()
#         serializer = CategorySerializer(category, many=True, context={'request': request})
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = CategorySerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'PUT', 'DELETE'])
# def category_detail(request, pk):
#     category = Category.objects.get(id=pk)

#     if request.method == 'GET':
#         serializers = CategoryDetailSerializer(category)
        
#         return Response(serializers.data)

#     elif request.method == 'PUT':
#         serializers = CategoryDetailSerializer(category, data=request.data)
#         serializers.is_valid(raise_exception=True)
#         serializers.save()
#         return Response(serializers.data)

#     elif request.method == 'DELETE':
#         if category.blogs.count() > 0:
#             return Response({'error': 'Categoryga bogliq bloglar borligi sabab buni oshira olmaysiz'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# ============================================================================ #
#                                     BLOG                                     #
# ============================================================================ #

# class BlogList(ListCreateAPIView):
#     """
#     GET:
#         Barcha mavjud bloglar royxatini qaytaradi.
    
#     POST:
#          Royxattan otkan foydalanuvshi Blog yarata oladi

#     """
    
#     serializer_class = BlogSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly,]
#     filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
#     search_fields = ['title', 'description']
#     ordering_fields = ['data_pub',]
#     pagination_class = DefaultPagination

#     def get_queryset(self):
#         return Blog.objects.select_related_object('category')

#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)



# class BlogDetail(RetrieveUpdateDestroyAPIView):
#     serializer_class = BlogSerializer
#     permission_classes = [IsSuperUserOrAuthorOrReadOnly,]

#     def get_queryset(self):
#         return Blog.objects.select_related_object('category')