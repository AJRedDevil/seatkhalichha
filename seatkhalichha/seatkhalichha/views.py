from django.shortcuts import render, redirect
from apps.carpools.handler import CarpoolManager
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt

import logging


def index(request):
    """
    Returns Index Page
    """
    user = request.user
    cm = CarpoolManager()
    carpools = cm.getRecentCarpools()
    if user.is_authenticated():
        return redirect('home')
    return render(request, 'homepage.html', locals())


def about(request):
    """
    Returns about Page
    """
    user = request.user
    return render(request, 'about.html', locals())


@csrf_exempt
@xframe_options_exempt
def fbpost(request):
    """
    facebook endpoint url
    """
    if request.method == "POST":
        logging.warn(request.POST)
        msg = """
        <html>
        <head>
            <title>Seatkhalicha!</title>
        </head>
        <body>
        <a href="http://www.seatkhalicha.com">http://www.seatkhalicha.com</a>
        </body>
        </html>
        """
        return HttpResponse(msg, content_type="text/html")
