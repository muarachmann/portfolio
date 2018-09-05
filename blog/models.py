from django.db import models
from django.utils import timezone


# Create your models here.

#here , we create the post model fot our blog

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) #getting the author of post from users table
    title = models.CharField(max_length=300) #getting the title of the post
    model_pic= models.ImageField(upload_to = 'blog/images', default='blog/images/already.png')
    body = models.TextField() #getting the body of the post
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
