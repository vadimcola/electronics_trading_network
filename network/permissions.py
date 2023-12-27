from rest_framework.permissions import BasePermission


class UpdateDebtPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        if view.action in ['update', 'partial_update'] and 'debt' in request.data:
            return False
        return True
