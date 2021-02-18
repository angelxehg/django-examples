from django.shortcuts import render
from django.urls import path

def index_view(request):
    """
    Vista de landing page
    """
    return render(request, 'index.html')

urlpatterns = [
    path('', view=index_view, name='index_view'),
]
