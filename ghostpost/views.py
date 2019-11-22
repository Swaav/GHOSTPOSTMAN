from django.utils import timezone
from ghostpost.models import GhostPost
from ghostpost.forms import GhostAdd
from django.shortcuts import render, HttpResponseRedirect, reverse
sort = True

def sort(request):
    global sort
    sort = not sort
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def index(request):
    html = 'index.html'
    if sort == True:
        ghostposts = GhostPost.objects.all().order_by('post_date')
    else:
        ghostposts = GhostPost.objects.all().order_by('totalvotes')
    return render(request, html, {'data': ghostposts})

def GhostPost_view(request):
    html = "ghost_add.html"
    if request.method == 'POST':
        form = GhostAdd(request.POST)
        if form.is_valid():

            data = form.cleaned_data

            GhostPost.objects.create(
                ghostTitle=data['ghostTitle'],
                body=data['body'],
                is_boast=data['is_boast'],
                post_date=timezone.now()
                )

        return render(request,'thanks.html')
    else:
        form = GhostAdd()
        return render(request, html, {'form': form})


def boast(request):
    html = 'index.html'
    if sort == True:
        ghostposts = GhostPost.objects.filter(is_boast=True).order_by('post_date')
    else:
        ghostposts = GhostPost.objects.filter(is_boast=True).order_by('totalvotes')
    return render(request, html, {'data': ghostposts})
    




def roast(request):
    html = 'index.html'
    if sort == True:
        ghostposts = GhostPost.objects.filter(is_boast=False).order_by('post_date')
    else:
        ghostposts = GhostPost.objects.filter(is_boast=False).order_by('totalvotes')
    return render(request, html, {'data': ghostposts})


def upvotes(request, id):
    try:
        ghostposts = GhostPost.objects.get(id=id)

    except GhostPosts.DoesNotExist():
       return HttpResponseRedirect(reverse('homepage'))
    
    ghostposts.goodvote+=1
    ghostposts.totalvotes+=1
    ghostposts.save()
    return HttpResponseRedirect(reverse('homepage'))




def downvotes(request, id):
    try:
        ghostposts = GhostPost.objects.get(id=id)

    except GhostPosts.DoesNotExist():
        return HttpResponseRedirect(reverse('homepage'))

    ghostposts.badvote-=1
    ghostposts.totalvotes-=1
    ghostposts.save()
    return HttpResponseRedirect(reverse('homepage'))






