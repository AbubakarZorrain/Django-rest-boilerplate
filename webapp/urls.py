from django.urls import include, path
from rest_framework import routers
from .views import myModelList

router = routers.DefaultRouter()
router.register(r'model', myModelList, basename='model')
# Wire up our API using automatic URL routing.
urlpatterns = [
    path('', include(router.urls)),
]