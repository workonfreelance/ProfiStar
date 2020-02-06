from django.db import models
from django.urls import reverse
from django.conf import settings

# class Form(models.Model):
#     login = models.CharField(max_length=25)
#     Email = models.CharField(max_length=25)
#     file = models.FileField()



class Tag(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Job(models.Model):
    def get_absolute_url(self):
        return reverse('employ:deteil',
                       args=[self.link])

    CHOICES = (
        ("active", 'Активный'),
        ("stop", 'Остановлен'),
        ("in_work", 'В разработке'),)

    shot_name = models.CharField(max_length=25, verbose_name="Краткое название")
    name = models.TextField(max_length=50, verbose_name="Название вакансии")
    shot_body = models.CharField(max_length=50, verbose_name="Краткое описание")
    body = models.TextField(max_length=500, verbose_name="Описание")
    tags = models.ManyToManyField(Tag, verbose_name="Теги")
    link = models.CharField(max_length=25, unique=True, verbose_name="Сылка",default="")
    status = models.CharField(choices=CHOICES, default="in_work", max_length=25, verbose_name="Статус")

    def __str__(self):
        text = str(self.id)+ " - " + self.shot_name
        return text

    class Meta:
        ordering = ('-id',)

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=25)

    def __str__(self):
        return str(self.user)

class UserComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    def __str__(self):
        return str(self.user)


