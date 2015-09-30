from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from seatkhalichha.decorators import is_superuser

from apps.carpools import handler as cphandler
import simplejson as json
import logging
import re
# Init Logger
logger = logging.getLogger(__name__)
# Create your views here.


def carpoolSearch(request, route=None):
    """
    Searches a carpool for the matching pattern and
    returns a list of matches
    """
    logging.warn(request.GET)

    if 'route' in request.GET:
        querystring = request.GET['route']
        cm = cphandler.CarpoolManager()
        result = cm.getCarpoolsByRoute(querystring)
        data = result.values('id', 'route', 'occupancy')
        data = json.loads(json.dumps(list(data)))
        responsedata = dict(detail=data)
        return HttpResponse(
            json.dumps(responsedata),
            content_type="application/json",
            status=200)

    return redirect('home')


@login_required
def carpoolSearchDetail(request):
    """
    Searches carpools from the route provided
    and lists their detail
    """
    user = request.user
    if request.method == "POST":
        logging.warn(request.POST)
        route = request.POST['route']
        # try:
        #     route = re.findall('\((.*?)\)', route)
        #     logging.warn(route)
        # except Exception:
        #     return redirect('home')
        cm = cphandler.CarpoolManager()
        carpools = cm.getCarpoolDetailsByRoute(route)
        return render(request, 'list_carpools.html', locals())
    return redirect('home')
