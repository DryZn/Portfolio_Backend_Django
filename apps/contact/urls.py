from django.urls import path
from .views import ContactMessageViewSet

urlpatterns = [
    path("contact/", ContactMessageViewSet.as_view({"post": "create"}), name="contact"),
]
