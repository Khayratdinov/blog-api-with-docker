from django.urls import path, include

# ============================================================================ #
from rest_framework_nested import routers

# ============================================================================ #
from project.apps.post.api import views


router = routers.DefaultRouter()
router.register(r"", views.BlogViewSet, basename="blog")


urlpatterns = [
    path("author/<str:username>/", views.BlogListByAuthor.as_view()),
    path("category/<int:pk>/", views.CategoryDetail.as_view()),
]

urlpatterns += router.urls
