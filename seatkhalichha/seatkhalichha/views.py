from django.shortcuts import render, redirect


def index(request):
    """
    Returns Index Page
    """
    user = request.user
    if user.is_authenticated():
        return redirect('home')
    return render(request, 'homepage.html', locals())


def about(request):
    """
    Returns about Page
    """
    user = request.user
    return render(request, 'about.html', locals())
