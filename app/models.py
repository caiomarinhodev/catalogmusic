from django.db import models


# Create your models here.

# Create your models here.
class TimeStamped(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)


class Artist(TimeStamped):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.name)

    def __unicode__(self):
        return "{}".format(self.name)


class Music(TimeStamped):
    artist = models.ForeignKey(Artist, blank=True, null=True,
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)
    chords = models.TextField(blank=True, null=True)
    cifraclub_chords_url = models.URLField(blank=True, null=True)
    original_tone = models.CharField(max_length=255, blank=True, null=True)
    band_tone = models.CharField(max_length=255, blank=True, null=True)
    bpm = models.CharField(max_length=255, blank=True, null=True)
    bar_length = models.CharField(max_length=255, blank=True, null=True)
    youtube_id = models.CharField(max_length=255, blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.title)

    def __unicode__(self):
        return "{}".format(self.title)
