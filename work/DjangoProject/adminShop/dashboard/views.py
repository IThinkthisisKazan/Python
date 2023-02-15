from django.shortcuts import render
import json
from dashboard.models import News

# Create your views here.
def index_page(request):

    all_news = News.objects.all()

    return render(request, 'index.html', {'news_list': all_news})