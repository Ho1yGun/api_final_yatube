from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user == obj.author)