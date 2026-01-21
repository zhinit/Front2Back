from rest_framework.routers import DefaultRouter
from posts.api.urls import post_router
from django.urls import path, include

router = DefaultRouter
# posts
router.registery.extend(post_router.registery)

urlpatterns = [path("", include(router.urls))]
