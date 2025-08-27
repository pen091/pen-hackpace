from django.shortcuts import render, get_object_or_404
from .models import Topic

def index(request):
    # Group topics by category for display
    categories = {
        'PROG': Topic.objects.filter(category='PROG'),
        'EMB': Topic.objects.filter(category='EMB'),
        'LIN': Topic.objects.filter(category='LIN'),
        'ADM': Topic.objects.filter(category='ADM'),
    }
    
    return render(request, 'hackspace_app/index.html', {'categories': categories})

def topic_detail(request, slug):
    topic = get_object_or_404(Topic, slug=slug)
    return render(request, 'hackspace_app/topic_detail.html', {'topic': topic})
