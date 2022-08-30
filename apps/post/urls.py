from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.BlogList.as_view()),
    path('blogs/<int:pk>/', views.BlogDetail.as_view()),


    path('category-with-class/<int:pk>/', views.CategoryDetail.as_view()),
    path('category-with-function/', views.category_list),
    path('category-with-function/<int:pk>/', views.category_detail),
    
]