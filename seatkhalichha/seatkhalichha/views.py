from django.shortcuts import render, redirect


def index(request):
    """
    Returns Index Page
    """
    user = request.user
    if user.is_authenticated():
        return redirect('home')
    return render(request, 'index.html', locals())
