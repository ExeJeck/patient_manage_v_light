from django.shortcuts import render


def registration(request):
    return render(request, 'user/registration.html')