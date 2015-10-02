
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from seatkhalichha.decorators import is_superuser
from apps.collectors.forms import FeedViewForm
from apps.carpools.models import Carpools
from apps.collectors.handler import FeedManager
import logging
# Init Logger
logger = logging.getLogger(__name__)
# Create your views here.


@login_required
@is_superuser
def viewFeed(request, feed_id):
    user = request.user
    fm = FeedManager()
    feed = fm.getFeedDetails(feed_id)
    message_clean = unicode(feed.content['message'])
    message = ''.join([unicode(x) for x in message_clean.split("#offer") if x != ''])
    feed_form = FeedViewForm(instance=feed, initial={'content': message})
    if request.method == "POST":
            feed_form = FeedViewForm(request.POST)
            if feed_form.is_valid():
                carpool = Carpools()
                carpool.driver = user
                carpool.vehicle_type = feed_form.cleaned_data['vehicle_type']
                carpool.occupancy = feed_form.cleaned_data['occupancy']
                carpool.tp_url = feed.shortlink
                carpool.start_datetime = feed_form.cleaned_data['pickup_time']
                carpool.route = feed_form.cleaned_data['route']
                carpool.remarks = feed_form.cleaned_data['remarks']
                carpool.save()
                feed.is_loaded = True
                feed.save()
                return redirect('listAllFeeds')

            if feed_form.errors:
                logger.debug("Form has errors, %s ", feed_form.errors)
                return render(request, 'feed_details.html', locals())
    return render(request, 'feed_details.html', locals())


@login_required
@is_superuser
def listAllFeeds(request):
    """lists all available carpools"""
    user = request.user
    ##Acquire all the current open jobs related to the user
    fm = FeedManager()
    # carpools = [x for x in fm.getAllCarpools() if x.driver != user]
    feeds = fm.getAllFeeds()
    return render(request, 'list_feeds.html', locals())
