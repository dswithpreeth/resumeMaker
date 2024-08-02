from django.shortcuts import render
from .models import Profile
from django.http import HttpResponse
from django.template import loader
from io import BytesIO
from xhtml2pdf  import pisa

# Specify the path to the wkhtmltopdf executable
def accept(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        phone = request.POST.get("phone", "")
        email = request.POST.get("email", "")
        degree = request.POST.get("degree", "")
        skills = request.POST.get("skills", "")
        projects = request.POST.get("projects", "")
        experience = request.POST.get("experience", "")

        profile = Profile(name=name, phone=phone, email=email, degree=degree, skills=skills)
        profile.save()

    return render(request, "accept.html")


def resume(request, id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template("resume.html")
    return render(request, "resume.html", {'user_profile': user_profile})
