from rest_framework import permissions

class IsCompanyUser(permissions.BasePermission):
    """
    Faqat o‘z kompaniyasi ma’lumotlarini ko‘rishi mumkin
    """
    def has_object_permission(self, request, view, obj):
        if request.user.role == "SUPER_ADMIN":
            return True
        return getattr(obj, "company", None) == request.user.company
