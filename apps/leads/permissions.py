from rest_framework import permissions

class IsCompanyAdminOrManager(permissions.BasePermission):
    """
    Company Admin yoki Manager o'z kompaniyasidagi leadlarni boshqarishi mumkin
    """

    def has_object_permission(self, request, view, obj):
        if request.user.role == "SUPER_ADMIN":
            return True
        if obj.company != request.user.company:
            return False
        if request.user.role in ["COMPANY_ADMIN", "MANAGER"]:
            return True
        return False
