from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
import jsonfield
import uuid

# Create your models here.

# Returns a hash that is used as identifier for jobs


def getUniqueUUID():
    uniqueID = ''.join(str(uuid.uuid4()).split('-'))
    return uniqueID


class Collectors(models.Model):
    """
    The collector model
    """
    # reference id for jobs
    # not the primary key though
    sourceref = models.CharField(
        _('sourceref'),
        max_length=100, unique=True, default=getUniqueUUID)
    name = models.CharField(
        _('name'),
        max_length=100, unique=True)

    def __unicode__(self):
        return str(self.sourceref)

        #Overriding
    def save(self, *args, **kwargs):
        # set a unique ID for each jobs
        if self.sourceref == '':
            self.sourceref = ''.join(str(uuid.uuid4()).split('-'))

        super(Collectors, self).save(*args, **kwargs)


class Collector_Contents(models.Model):
    """Models for Collector_Contents"""

    source = models.ForeignKey(Collectors)
    identifier = models.CharField(_('identifier'), max_length=254, unique=True)
    permalink = models.URLField(_('permalink'), unique=True)
    shortlink = models.URLField(_('shortlink'), unique=True)
    content = jsonfield.JSONField(
        _('content'),
        blank=False
    )
    is_loaded = models.BooleanField(_('is_loaded'), default=False)

    def save(self, *args, **kwargs):
        super(Collector_Contents, self).save(*args, **kwargs)
