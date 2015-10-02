

import logging
from django.core import serializers
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.utils import timezone

from apps.collectors.models import Collector_Contents

# Init Logger
logger = logging.getLogger(__name__)


class FeedManager(object):
    """docstring for carpool request manager"""
    def getFeedDetails(self, feed_id):
        """List carpool request information"""
        feed = get_object_or_404(Collector_Contents, id=feed_id)
        return feed

    # def getJobsForHandyman(self, user):
    #     jobs = jobs.objects.filter(handyman!=None)

    def getAllFeeds(self):
        feeds = Collector_Contents.objects.filter(is_loaded=False)
        # logger.debug("Carpool Details : \n {0}".format(
        #     serializers.serialize('json', carpools))
        # )
        return feeds
