from django.shortcuts import get_object_or_404
from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    def get_object(self):
        obj = get_object_or_404(self.get_queryset())
        self.check_object_permissions(self.request, obj)
        return obj

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
