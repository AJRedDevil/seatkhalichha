from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from seatkhalichha.decorators import is_superuser
from .forms import CarpoolCreationForm, CarpoolEditForm, CarpoolViewForm, CarpoolRequestCreateForm
from .handler import CarpoolManager
import logging
# Init Logger
logger = logging.getLogger(__name__)

# Create your views here.


@login_required
def createCarpool(request):
    user = request.user

    if request.method == "GET":
        carpool_form = CarpoolCreationForm()
        return render(request, 'create_carpool.html', locals())
    if request.method == "POST":
        logger.debug(request.POST)
        carpool_form = CarpoolCreationForm(request.POST)
        if carpool_form.is_valid():
            carpool_data = carpool_form.save(commit=False)
            carpool_data.driver = user
            carpool_data.save()
            return redirect('home')
        if carpool_form.errors:
            logger.debug("Form has errors, %s ", carpool_form.errors)
            return render(request, 'create_carpool.html', locals())


@login_required
def viewCarpool(request, carpool_id):
    user = request.user
    cm = CarpoolManager()
    carpool = cm.getCarpoolDetails(carpool_id)
    if carpool.driver != user:
        carpool_form = CarpoolViewForm(instance=carpool)
        return render(request, 'carpool_details_rider.html', locals())
    carpool_form = CarpoolEditForm(instance=carpool)
    if request.method == "POST":
        if carpool.driver == user:
            logger.debug(request.POST)
            carpool_form = CarpoolEditForm(request.POST, instance=carpool)
            if carpool_form.is_valid():
                carpool_form.save()
                return redirect('listAllCarpools')
        return redirect('listAllCarpools')

        if carpool_form.errors:
            logger.debug("Form has errors, %s ", carpool_form.errors)
            return render(request, 'carpool_details.html', locals())

        return render(request, 'carpool_details.html', locals())

    return render(request, 'carpool_details.html', locals())


@login_required
def listAllCarpools(request):
    """lists all available carpools"""
    user = request.user
    ##Acquire all the current open jobs related to the user
    from apps.carpools.handler import CarpoolManager
    cm = CarpoolManager()
    # carpools = [x for x in cm.getAllCarpools() if x.driver != user]
    carpools = cm.getAllCarpools()
    return render(request, 'list_carpools.html', locals())


@login_required
def requestCarpool(request, carpool_id):
    """
    request for a carpool
    """
    user = request.user
    cm = CarpoolManager()
    carpool = cm.getCarpoolDetails(carpool_id)
    carpoolreq_form = CarpoolRequestCreateForm()
    # you cannot request for your own carpool
    if carpool.driver == user:
        return redirect('home')

    if user in [x.rider for x in carpool.requests.all()]:
        return redirect('home')

    if request.method == "POST":
        carpoolreq_form = CarpoolRequestCreateForm(request.POST)
        if carpoolreq_form.is_valid():
            carpoolreq_data = carpoolreq_form.save(commit=False)
            carpoolreq_data.carpool = carpool
            carpoolreq_data.rider = user
            carpoolreq_data.save()
            return redirect('listAllCarpools')

        if carpoolreq_form.errors:
            logger.debug("Form has errors, %s ", carpoolreq_form.errors)
            return render(request, 'request_carpool.html', locals())

        return render(request, 'request_carpool.html', locals())

    return render(request, 'request_carpool.html', locals())
