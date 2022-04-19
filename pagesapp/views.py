from django.shortcuts import render
from django.views.generic import TemplateView

class homepageView(TemplateView):
    template_name = "pages.html"

class aboutpageView(TemplateView):
    template_name = "about.html"


