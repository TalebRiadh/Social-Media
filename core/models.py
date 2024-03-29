from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime



User = get_user_model()
# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_img = models.ImageField(upload_to='profile_images', default='blank-profile.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    class Meta:
        ordering = ('-created_at', )
    def __str__(self):
        return self.user


class LikePost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)



class FollowersCount(models.Model):
    follower = models.ForeignKey(Profile,related_name="follower", on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

