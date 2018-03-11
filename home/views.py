from django.shortcuts import render
from django.views.generic import TemplateView
from django.template.loader import get_template
from django.shortcuts import render_to_response
# Create your views here.




def index(request):
    return render(request, "index.html",{'page':' Page'})
