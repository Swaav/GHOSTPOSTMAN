from django.utils import timezone
from ghostpost.models import GhostPost
from ghostpost.forms import GhostAdd
from django.shortcuts import render, HttpResponseRedirect, reverse

def index(request):
    html = 'index.html'

    ghostposts = GhostPost.objects.all()

    return render(request, html, {'data': ghostposts})

def GhostPost_view(request):
    html = "ghost_add.html"
    if request.method == 'POST':
        form = GhostAdd(request.POST)
        if form.is_valid():

            data = form.cleaned_data

            GhostPost.objects.create(
                ghostTitle='That Saiyan',
                body='Had a powerLevel over 9000',
                is_boast=True,
                post_date=timezone.now()
                )

        return render(request,'thanks.html')
    else:
        form = GhostAdd()
        return render(request, html, {'form': form})