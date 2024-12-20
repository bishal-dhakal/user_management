from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.shortcuts import render

User = get_user_model()


def create_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        role = request.POST["role"]

        user = User.objects.create_user(username=username, password=password, role=role)

        # Add the user to the corresponding group
        group = Group.objects.get(name=role)
        user.groups.add(group)
        user.save()

        return HttpResponse(f"User {username} created with role {role}")

    return render(request, "create_user.html")


class DoctorDashboardView(APIView):
    permission_classes = [IsAuthenticated, IsDcotor]

    def get(self, request):
        return Reponse({"message": "Welcome Doctor"})
