from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    abstract = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author)

    def __str__(self):
        return self.title

class ContactInfo(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6)
    age = models.CharField(max_length=3)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name
