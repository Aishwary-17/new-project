from django.shortcuts import render

# Create your views here.

from django.template import context
from .models import News, Date, Genre
import csv
import requests
from bs4 import BeautifulSoup
import re
from django.db.models import Count
def change(request):
    with open('/home/aishwary/newsaggregator/new_news.csv', newline='') as f:
        reader=csv.reader(f)
        for row in reader:
           p=News(title=row[5],date=row[2],description=row[3],link=row[4],category=row[1])
           p.save()

    return render(
        request,
        'change.html',
    ) 
  
def index(request):
    """
    View function for home page of site.
    """  

    # Generate counts of some of the main objects
    num_news=News.objects.all().count()
    # Available news
    num_genre=News.objects.annotate(Count('category', distinct=True))  # The 'all()' is implied by default.
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_news':num_news,'num_category':num_genre},
    )
def stories(request):
    page = requests.get("https://economictimes.indiatimes.com/rssfeedstopstories.cms")
    soup = BeautifulSoup(page.content, 'html.parser')
    total_item=soup.find_all("item")
    title_list=list()
    link_list=list()
    description_list=list()
    date_list=list()
    for i in range(len(total_item)):
        t=total_item[i]
        ftitle = t.find("title").get_text()
        flink = t.find("link").get_text()
        fdate = t.find("pubdate").get_text()
        fdescription = t.find("description").get_text()
        title_list.append(ftitle)
        link_list.append(flink)
        description_list.append(fdescription)
        date_list.append(fdate)
    for i in range(len(description_list)):
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', description_list[i])
        if len(urls):
            link_list[i]=urls[0]
            description_list[i]="none"
        else:
            link_list[i]="https://economictimes.indiatimes.com"
    new_content=News()
    for i in range(len(title_list)):
        new_content=News(title=title_list[i],date=date_list[i],description=description_list[i],link=link_list[i],category="Top Stories")
    total_news=len(title_list)
    return render(
           request,
           'stories.html',
           context={'new_contents':new_content,'total_news':total_news},
    )
def about(request):
    return render(
           request,
           'about.html',
    )

def categories(request):
    return render(
           request,
           'categories_list.html',
    )

def sports(request):
    category_news = News.objects.filter(category="sports")
    category_count = News.objects.filter(category="sports").count()
    return render(
           request,
           'categories.html',
            context={'category_news':category_news,'category_count':category_count,'c':"sports"},
    )
def stocks(request):
    category_news = News.objects.filter(category="stocks")
    category_count = News.objects.filter(category="stocks").count()
    return render(
           request,
           'categories.html',
            context={'category_news':category_news,'category_count':category_count,'c':"stocks"},
    )
def economics(request):
    category_news = News.objects.filter(category="economics")
    category_count = News.objects.filter(category="economics").count()
    return render(
           request,
           'categories.html',
            context={'category_news':category_news,'category_count':category_count,'c':"economics"},
    )
def politics(request):
    category_news = News.objects.filter(category="top_stories")
    category_count = News.objects.filter(category="top_stories").count()
    return render(
           request,
           'categories.html',
            context={'category_news':category_news,'category_count':category_count,'c':"politics"},
    )
def health(request):
    category_news = News.objects.filter(category="health")
    category_count = News.objects.filter(category="health").count()
    return render(
           request,
           'categories.html',
            context={'category_news':category_news,'category_count':category_count,'c':"health"},
    )
def science(request):
    category_news = News.objects.filter(category="science")
    category_count = News.objects.filter(category="science").count()
    return render(
           request,
           'categories.html',
            context={'category_news':category_news,'category_count':category_count,'c':"science"},
    )
def technology(request):
    category_news = News.objects.filter(category="technology")
    category_count = News.objects.filter(category="technology").count()
    return render(
           request,
           'categories.html',
            context={'category_news':category_news,'category_count':category_count,'c':"technology"},
    )
def cryptocurrency(request):
    category_news = News.objects.filter(category="cryptocurrency")
    category_count = News.objects.filter(category="cryptocurrency").count()
    return render(
           request,
           'categories.html',
            context={'category_news':category_news,'category_count':category_count,'c':"cryptocurrency"},
    )
def market(request):
    category_news = News.objects.filter(category="market")
    category_count = News.objects.filter(category="market").count()
    return render(
           request,
           'categories.html',
            context={'category_news':category_news,'category_count':category_count,'c':"market"},
    )


from django.views import generic

class NewsListView(generic.ListView):
    model = News
    paginate_by = 20
class NewsDetailView(generic.DetailView):
    model = News
