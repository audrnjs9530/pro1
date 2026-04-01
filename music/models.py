from django.db import models
from django.conf import settings
from accounts.models import User



class Music(models.Model):
    artist = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='musics',
    )
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    audio_file = models.FileField(upload_to='music/media/')
    cover_image = models.ImageField(upload_to='music/cover/', blank=True, null=True)

    genre = models.CharField(max_length=30)
    play_count = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='liked_musics',
        blank=True,
    )

    @property
    def points(self):
        return self.likes.count() * 3 + self.play_count

    def __str__(self):
        return f"{self.title} - {self.artist.username}"



