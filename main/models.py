from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    text = models.TextField()
    img = models.ImageField(upload_to='news_photo/')
    data = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Aout_us(models.Model):
    title =models.CharField(max_length=255)
    text_1 = models.TextField()
    text_2 = models.TextField()

    def __str__(self):
        return self.title



class Our_teams(models.Model):
    img = models.ImageField(upload_to='teams/')
    name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    twiter = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    telegram = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Adress(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name
