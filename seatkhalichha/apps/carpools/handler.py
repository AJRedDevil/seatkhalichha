

import logging
import pytz
from datetime import datetime, timedelta
from django.core import serializers
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.utils import timezone

from .models import Carpools, Carpool_Requests

# Init Logger
logger = logging.getLogger(__name__)

def get_listing_startdatetime():
    now = datetime.now()
    now = now - timedelta(minutes=30)
    tzinfo=pytz.timezone('Asia/Kathmandu')
    start_datetime=timezone.make_aware(now, tzinfo)
    return start_datetime


class CarpoolManager(object):
    """docstring for JobManager"""
    def getCarpoolDetails(self, carpool_id):
        """List carpool information"""
        carpool = get_object_or_404(Carpools, carpoolref=carpool_id)
        return carpool

    # def getJobsForHandyman(self, user):
    #     jobs = jobs.objects.filter(handyman!=None)

    def getAllCarpools(self):
        # if user.user_type == 0:
        #     jobs = Jobs.objects.filter()
        # ## If it's a handymen, only show requests which they were assigned to
        # elif user.user_type == 1:
        #     alljobs = Jobs.objects.exclude(handyman=None)
        #     # get the jobs where the handyman is listed
        #     # as the one chosen for the particular work
        #     jobs = [x for x in alljobs if user in x.handyman.all()]
        # ## If it's a customer only show requests that they created
        # elif user.user_type == 2:
        #     jobs=[]
        #     subscribers=Subscriber.objects.filter(primary_contact_person=user)
        #     for subscriber in subscribers:
        #         jobs.extend(Jobs.objects.filter(customer_id=subscriber.id))
        # else:
        #     jobs = []
        carpools = Carpools.objects.filter(ishidden=False, status='0', start_datetime__gt=get_listing_startdatetime())
        # logger.debug("Carpool Details : \n {0}".format(
        #     serializers.serialize('json', carpools))
        # )
        return carpools

    def getRecentCarpools(self):
        # if user.user_type == 0:
        #     jobs = Jobs.objects.filter()
        # ## If it's a handymen, only show requests which they were assigned to
        # elif user.user_type == 1:
        #     alljobs = Jobs.objects.exclude(handyman=None)
        #     # get the jobs where the handyman is listed
        #     # as the one chosen for the particular work
        #     jobs = [x for x in alljobs if user in x.handyman.all()]
        # ## If it's a customer only show requests that they created
        # elif user.user_type == 2:
        #     jobs=[]
        #     subscribers=Subscriber.objects.filter(primary_contact_person=user)
        #     for subscriber in subscribers:
        #         jobs.extend(Jobs.objects.filter(customer_id=subscriber.id))
        # else:
        #     jobs = []
        carpools = Carpools.objects.filter(ishidden=False, start_datetime__gt=get_listing_startdatetime()).order_by('-id')[:20]
        # logger.debug("Carpool Details : \n {0}".format(
        #     serializers.serialize('json', carpools))
        # )
        return carpools

    def getCarpoolsByRoute(self, route):
        carpools = Carpools.objects.filter(ishidden=False, route__istartswith=route, start_datetime__gt=get_listing_startdatetime()) | Carpools.objects.filter(ishidden=False, route__icontains=route, start_datetime__gt=get_listing_startdatetime())
        # logger.debug("Carpool Details : \n {0}".format(
        #     serializers.serialize('json', carpools))
        # )
        return carpools

    def getCarpoolDetailsByRoute(self, route):
        # carpools = Carpools.objects.filter(ishidden=False, route__istartswith=route, end_datetime__gt=timezone.now()) | Carpools.objects.filter(ishidden=False, route__contains=route, end_datetime__gt=timezone.now())
        carpools = Carpools.objects.filter(ishidden=False, route__istartswith=route.split(' ')[0], start_datetime__gt=get_listing_startdatetime()) | Carpools.objects.filter(ishidden=False, route__icontains=route.split(' ')[0], start_datetime__gt=get_listing_startdatetime())


        # carpools = Carpools.objects.filter(ishidden=False, route__istartswith=str(route.split(' ')[0]) | Carpools.objects.filter(ishidden=False, route__contains=str(route.split(' ')[0]), end_datetime__gt=timezone.now())
        # logger.debug("Carpool Details : \n {0}".format(
        #     serializers.serialize('json', carpools))
        # )
        return carpools

class CarpoolReqManager(object):
    """docstring for carpool request manager"""
    def getCarpoolReqDetails(self, carpoolreq_id):
        """List carpool request information"""
        carpoolreq = get_object_or_404(Carpool_Requests, carpoolreqref=carpoolreq_id)
        return carpoolreq

    # def getJobsForHandyman(self, user):
    #     jobs = jobs.objects.filter(handyman!=None)

    def getAllCarpoolReqs(self):
        # if user.user_type == 0:
        #     jobs = Jobs.objects.filter()
        # ## If it's a handymen, only show requests which they were assigned to
        # elif user.user_type == 1:
        #     alljobs = Jobs.objects.exclude(handyman=None)
        #     # get the jobs where the handyman is listed
        #     # as the one chosen for the particular work
        #     jobs = [x for x in alljobs if user in x.handyman.all()]
        # ## If it's a customer only show requests that they created
        # elif user.user_type == 2:
        #     jobs=[]
        #     subscribers=Subscriber.objects.filter(primary_contact_person=user)
        #     for subscriber in subscribers:
        #         jobs.extend(Jobs.objects.filter(customer_id=subscriber.id))
        # else:
        #     jobs = []
        carpoolreqs = Carpool_Requests.objects.filter(ishidden=False)
        # logger.debug("Carpool Details : \n {0}".format(
        #     serializers.serialize('json', carpools))
        # )
        return carpoolreqs

    def getMyCarpoolReqs(self, user):
        carpoolreqs = Carpool_Requests.objects.filter(ishidden=False)
        myrequests = [x for x in carpoolreqs if x.carpool.driver == user]
        # logger.debug("Carpool Details : \n {0}".format(
        #     serializers.serialize('json', carpools))
        # )
        return myrequests
