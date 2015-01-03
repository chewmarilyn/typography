from django.db import models


class TypeImage(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    image = models.ImageField()
    priority = models.IntegerField(default=0)


class UserImage(models.Model):
    added = models.DateTimeField(auto_now=True, auto_now_add=True)
    image = models.ImageField()

    @classmethod
    def store_image(cls, image_file):
        image = cls.objects.create(image=image_file)
        return {
            'url': image.image.url,
            'height': image.image.height,
            'width': image.image.width
        }
