from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Profile(models.Model):
    id_user = models.OneToOneField(User, on_delete=models.CASCADE)
    patronymic = models.CharField(max_length=50, null=True, blank=True)
    age = models.DateField()
    tel_number = models.CharField(max_length=20, null=True, blank=True)
    photo = models.ImageField(upload_to='images/user_photo/', null=True, blank=True)

    def __str__(self):
        return self.id_user.username

    def get_photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return "/media/images/user_photo/user.jpg"

class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

class CategoryDescription(models.Model):
    idCategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.idCategory.category

class Event(models.Model):
    name = models.CharField(max_length=100)
    datetimefield = models.DateTimeField()
    description = models.CharField(max_length=750, blank=True, null=True)
    loc = models.CharField(max_length=100)
    imagefield = models.ImageField(upload_to='images/events/', null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_photo_url(self):
        if self.imagefield and hasattr(self.imagefield, 'url'):
            return self.imagefield.url
        else:
            return "/media/images/user_photo/user.jpg"

    def get_absolute_url(self):
        return reverse("event", kwargs={'event_slug': self.slug})

class EventOrganizer(models.Model):
    idEvent = models.ForeignKey(Event, on_delete=models.CASCADE)
    idOrganizer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.idEvent.name

class EventCategory(models.Model):
    idEvent = models.ForeignKey(Event, on_delete=models.CASCADE)
    idCategory = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.idEvent.name

class UserCategory(models.Model):
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    idCategory = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.idUser.username

class UserEvent(models.Model):
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    idEvent = models.ForeignKey(Event, on_delete=models.CASCADE)
    passed = models.BooleanField(default=False)



