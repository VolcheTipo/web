from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username

class Profile(models.Model):
    user=models.OneToOneField(CustomUser, null=True, on_delete=models.CASCADE)
    bio=models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    facebook = models.CharField(max_length=50, null=True, blank=True)
    twitter = models.CharField(max_length=50, null=True, blank=True)
    instagram = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return str(self.user)

class Post(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=50)
    photo = models.ImageField()
    date = models.DateTimeField()
    text = models.CharField(max_length=50)

    def str(self):
        return f'{self.title}'
        # return f'Новость:{self.title}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'



class LikesP(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='likes')



class CommentsP(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=1000)


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.title
    class Meta:
        db_table = "myapp_image"

class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

