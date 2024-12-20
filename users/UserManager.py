from django.contrib.auth.models import Group, UserManager


class CustomUserManager(UserManager):
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        """
        Override the default create_superuser method to set the role of superuser.
        """
        extra_fields.setdefault("role", "1")  # Set default role to 'Other' (3)
        user = super().create_superuser(username, email, password, **extra_fields)
        self.assign_group(user, is_superuser=True)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("role", 3)
        user = super().create_user(username, email, password, **extra_fields)
        self.assign_group(user)
        return user

    def assign_group(self, user, is_superuser=False):
        if is_superuser:
            group_name = "Admin"
        else:
            if user.role == 2:
                group_name = "Doctor"
            elif user.role == 3:
                group_name = "Nurse"
            else:
                group_name = "Nurse"

        group, created = Group.objects.get_or_create(name=group_name)
        user.groups.add(group)
        user.save()

