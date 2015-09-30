

from apps.users.models import UserProfile
from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
import uuid

# Create your models here.
# Job Statuses
STATUS_SELECTION = (
    ('0', 'Active'),
    ('1', 'Expired'),
)

REQUEST_STATUS = (
    ('0', 'Pending'),
    ('1', 'Accepted'),
    ('2', 'Rejected'),
)

VEHICLE_TYPE = (
    ('0', 'Bike'),
    ('1', 'Car'),
    ('2', 'Van'),
)

# Returns a hash that is used as identifier for jobs


def getUniqueUUID():
    uniqueID = ''.join(str(uuid.uuid4()).split('-'))
    return uniqueID


class Carpools(models.Model):
    """
    The carpool model
    """
    # reference id for jobs
    # not the primary key though
    carpoolref = models.CharField(
        _('carpoolref'),
        max_length=100, unique=True, default=getUniqueUUID)
    driver = models.ForeignKey(
        UserProfile,
        related_name='carpool_driver'
    )
    status = models.CharField(
        _('status'),
        max_length=1,
        choices=STATUS_SELECTION,
        default='0',)
    creation_date = models.DateTimeField(
        _('creation_date'),
        default=timezone.now
    )
    vehicle_type = models.CharField(
        _('vehicle_type'),
        max_length=1,
        choices=VEHICLE_TYPE,
        default='0',)
    occupancy = models.IntegerField(_('Seats'), max_length=10, default=1)
    # jobs that are deleted or are to be purged would have this flag
    # set as true, no data would be permanently removed
    ishidden = models.BooleanField(_('ishidden'), default=False)
    remarks = models.TextField(_('remarks'), blank=True)
    # location / coordinates of the exact jobsite
    route = models.TextField(_('route'), blank=False)
    start_datetime= models.DateTimeField(
        _('Available from'),
        default=timezone.now
        )
    end_datetime= models.DateTimeField(
        _('Available till'),
        default='',
        )

    # objects = models.GeoManager()

    def __unicode__(self):
        return str(self.carpoolref)

        #Overriding
    def save(self, *args, **kwargs):
        # set a unique ID for each jobs
        if self.carpoolref == '':
            self.carpoolref = ''.join(str(uuid.uuid4()).split('-'))

        # if no location is provided while creating the job
        # user the customer's default home location
        # if self.location == '' or self.location is None:
        #     self.location = self.customer.primary_contact_person.address_coordinates

        super(Carpools, self).save(*args, **kwargs)


class Carpool_Requests(models.Model):
    """
    The carpool request model
    """
    # reference id for jobs
    # not the primary key though
    carpoolreqref = models.CharField(
        _('carpoolreqref'),
        max_length=100, unique=True, default=getUniqueUUID)
    carpool = models.ForeignKey(
        Carpools,
        related_name='requests'
    )
    rider = models.ForeignKey(
        UserProfile,
        related_name='carpool_rider'
    )
    status = models.CharField(
        _('status'),
        max_length=1,
        choices=REQUEST_STATUS,
        default='0',)
    creation_date = models.DateTimeField(
        _('creation_date'),
        default=timezone.now
    )
    # occupancy = models.IntegerField(_('occupancy'), max_length=10, default=1)
    # jobs that are deleted or are to be purged would have this flag
    # set as true, no data would be permanently removed
    ishidden = models.BooleanField(_('ishidden'), default=False)
    message = models.TextField(_('Message to the owner of the carpool!'), blank=False)
    # objects = models.GeoManager()

    def __unicode__(self):
        return str(self.carpoolreqref)

        #Overriding
    def save(self, *args, **kwargs):
        # set a unique ID for each jobs
        if self.carpoolreqref == '':
            self.carpoolreqref = ''.join(str(uuid.uuid4()).split('-'))

        super(Carpool_Requests, self).save(*args, **kwargs)

