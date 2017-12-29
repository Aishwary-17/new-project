from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^categories/$', views.categories, name='categories'),
    url(r'^about/$', views.about, name='about'),
    url(r'^stories/$', views.stories, name='stories'),
    url(r'^sports/$', views.sports, name='sports'),
    url(r'^economics/$', views.economics, name='economics'),
    url(r'^health/$', views.health, name='health'),
    url(r'^market/$', views.market, name='market'),
    url(r'^politics/$', views.politics, name='politics'),
    url(r'^science/$', views.science, name='science'),
    url(r'^technology/$', views.technology, name='technology'),
    url(r'^cryptocurrency/$', views.cryptocurrency, name='cryptocurrency'),
    url(r'^stocks/$', views.stocks, name='stocks'),
    url(r'^change/$', views.change, name='change'),
    url(r'^news/$', views.NewsListView.as_view(), name='news'),
    url(r'^news/(?P<pk>\d+)$', views.NewsDetailView.as_view(), name='news-detail'),
]


'''
url(r'^categories/(?P<anystring>\w+)/$', views.CategoriesListVeiw.as_Veiw(), name='any_string'),
url(r'^categories/$', views.categories, name='categories'),
url(r'^categories/(?P<query_string>\w+)/$', views.query_categories, name='query_string'),
'''
