from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver

from .permissions import GROUP_PERMISSIONS, PERMISSIONS


@receiver(post_migrate)
def create_roles_and_permission(sender, **kwargs):
    # Iterate through each role in GROUP_PERMISSIONS
    for role, permission_ids in GROUP_PERMISSIONS.items():
        # Get or create the group for this role
        group, created = Group.objects.get_or_create(name=role)

        # Fetch the permission names using the permission_ids from the PERMISSIONS dictionary
        permission_names = [
            PERMISSIONS[str(permission_id)] for permission_id in permission_ids
        ]

        # Retrieve permissions based on the permission names
        permissions = Permission.objects.filter(codename__in=permission_names)

        # Set the permissions to the group
        group.permissions.set(permissions)
        group.save()