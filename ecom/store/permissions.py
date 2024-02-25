from rest_framework import permissions

class IsOwnerORReadOnly(permissions.BasePermission):
    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user == obj.owner


class IsVendorORReadOnly(permissions.BasePermission):
    def has_permission(self,request,view):
        if request.method in ["POST","PUT","DELETE","PATCH"]:
            return request.user.groups.filter(name="vendor").exists()
        return True
