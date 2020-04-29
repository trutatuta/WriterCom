from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Publication(models.Model):
    image = models.ImageField(upload_to='images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    book = models.FileField(upload_to='docs/')
    GENRES = (
        ('Fantasy', 'Fantasy'),
        ('Adventure', 'Adventure'),
        ('Mystery', 'Mystery'),
        ('Thriller', 'Thriller'),
        ('Science Fiction', 'Science Fiction'),
    )
    book_genre = models.CharField(max_length = 100, choices = GENRES)
    pub_date = models.DateTimeField()


    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])



    