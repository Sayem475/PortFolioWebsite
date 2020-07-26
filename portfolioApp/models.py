from django.db import models

# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()

    def __str__(self):
        return self.title


class Skills(models.Model):
    skill = models.CharField(max_length=50)

    def __str__(self):
        return self.skill


class Portfolio(models.Model):
    image = models.ImageField(upload_to='images', default='', blank=True)
    image_title = models.CharField(max_length=100)

    def __str__(self):
        return self.image_title

class PortfolioImages(models.Model):
    portfolio = models.ForeignKey( Portfolio, default=None, on_delete= models.CASCADE)
    image = models.ImageField(upload_to ='images')

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    msg = models.CharField(max_length=30)
    timeStamp = models.DateTimeField(auto_now_add=True, blank= True)

    def __str__(self):
        return 'Message from ' + self.name + ' - ' + self.email

    
 