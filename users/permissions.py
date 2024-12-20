from rest_framework.permissions import BasePermission


class IsDoctor(BasePermission):
    """
    Custom Permissions to allow only users in the 'Doctor' group.
    """

    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name="Doctor").exists()


class IsNurse(BasePermission):
    """
    Custom Permissions to allow only users in the "Nurse" group.
    """

    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name="Nurse").exists()


PERMISSIONS = {
    "1": "view_patient",
    "2": "change_patient",
    "3": "delete_patient",
    "4": "add_patient",
}

GROUP_PERMISSIONS = {
    "Doctor": [1, 4],
    "Nurse": [1, 2],
}
