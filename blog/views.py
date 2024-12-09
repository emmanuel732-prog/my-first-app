from django.shortcuts import render

# Create your views here.

def post_list(request, template_name='blog/post_list.html'):
    return render(request, template_name, {})