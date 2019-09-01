from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user trying to update own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.method == request.user.id