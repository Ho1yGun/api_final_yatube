from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from api.views import CommentsViewSet, GroupViewSet, PostViewSet, FollowViewSet

router_v1 = routers.DefaultRouter()
router_v1.register('posts', PostViewSet, basename='post')
router_v1.register('groups', GroupViewSet, basename='group')
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentsViewSet,
    basename='comment')
router_v1.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
