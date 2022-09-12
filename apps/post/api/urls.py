from django.urls import path, include
# ============================================================================ #
from rest_framework_nested import routers
# ============================================================================ #
from apps.post.api import views

router = routers.DefaultRouter()

router.register(r'blog', views.BlogViewSet, basename='blog')





urlpatterns = [

    path('author-blogs/<str:username>/', views.BlogListByAuthor.as_view()),


    path('category-with-class/<int:pk>/', views.CategoryDetail.as_view()),
    path('category-with-function/', views.category_list),
    path('category-with-function/<int:pk>/', views.category_detail),

    
]

urlpatterns  += router.urls