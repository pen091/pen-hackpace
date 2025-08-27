from django.db import models
from django.urls import reverse

class Topic(models.Model):
    TOPIC_CATEGORIES = [
        ('PROG', 'Programming'),
        ('EMB', 'Embedded'),
        ('LIN', 'Linux'),
        ('ADM', 'Administration'),
    ]
    
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=4, choices=TOPIC_CATEGORIES)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('topic_detail', kwargs={'slug': self.slug})
