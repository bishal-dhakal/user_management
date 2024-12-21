from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .permissions import IsDoctor


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
    permission_classes = [IsAuthenticated, IsDoctor]

    def get(self, request):
        return Response({"message": "Welcome Doctor"})
