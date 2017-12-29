from django.db import models

# Create your models here.
class Genre(models.Model):
    """
    Model representing a News genre (e.g. politics, sports).
    """
    name = models.CharField(max_length=200, help_text="news category (e.g. politics, sports etc.)")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class News(models.Model):
    """
    Model representing a news.
    """
    title = models.CharField(max_length=200)
    #date = models.ForeignKey('date', on_delete=models.SET_NULL, null=True)
    date = models.CharField(max_length=100)
    # Foreign Key used because news can only have one publish date, but on that date we have multiple news
    # date as a string rather than object because it hasn't been declared yet in the file.
    description = models.TextField(max_length=1000, help_text="Enter a brief description of the news")
    link = models.CharField(max_length=100, help_text="hfjhhj")
    #category = models.ManyToManyField(Genre, help_text="Select a genre for this news")
    category = models.CharField(Genre, max_length=100, help_text="Select a genre for this news")
    # ManyToManyField used because genre can contain many news. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title
    
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular news instance.
        """
        return reverse('news-detail', args=[str(self.id)])
 


class Date(models.Model):
    """
    Model representing an Date.
    """
    news_date = models.CharField(max_length=100)
    news_day = models.CharField(max_length=100)
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular date instance.
        """
        return reverse('news-detail', args=[str(self.id)])
    

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.news_date, self.news_day)
