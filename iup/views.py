from django.http import *
from django.shortcuts import render
from iup.forms import Upload
import Image


def main(request):
	form = Upload()
	if request.method == "POST":
		form = Upload(request.POST, request.FILES)
		if form.is_valid():
			return HttpResponse("SUCCESS NIGGA!")
	return render(request, "upload.html", {"form": form})
