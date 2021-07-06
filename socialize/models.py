from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=350)

    def __str__(self):
        return f'{self.name} ({self.address})'

class Group(models.Model):
    group_name = models.CharField(max_length=290)

    def __str__(self):
        return f'{self.group_name}'

class Contributor(models.Model):
    email_address = models.EmailField(unique=True)
    phone_number = models.IntegerField(blank=True)

    def __str__(self):
        return f'{self.email_address} ({self.phone_number})'


class Socialize(models.Model):
    title = models.CharField(max_length=2000)
    supervisor_email = models.EmailField()
    date = models.DateField()
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    group_name = models.CharField(max_length=290)
    contributor = models.ManyToManyField(Contributor, blank=True, null=True)

    def __str__(self):
        return f'{self.title} - {self.slug}'

