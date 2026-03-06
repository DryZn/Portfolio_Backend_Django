from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CategoryViewSet, TagViewSet

router = DefaultRouter()
router.register(r"blog/posts", PostViewSet)
router.register(r"blog/categories", CategoryViewSet)
router.register(r"blog/tags", TagViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
