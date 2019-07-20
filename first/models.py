from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    author = models.CharField(max_length=10) #charfield는 길에 제한 넣어야함.textfield는 상관없음
    message = models.TextField()

    #python manage.py makemigrations
    #python manage.py migrate
