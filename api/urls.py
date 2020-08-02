from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'brews', views.BrewViewSet)
router.register(r'updates', views.UpdateViewSet)

urlpatterns = [
  path('', include(router.urls)),
  path('auth/', include('rest_auth.urls')),
]

