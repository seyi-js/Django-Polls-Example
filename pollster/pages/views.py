from django.shortcuts import render

# Create your views here.
# Render Landing Page
def index(request):
    return render(request, 'pages/index.html')