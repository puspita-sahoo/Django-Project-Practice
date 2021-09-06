from django.shortcuts import render


def msg_page(request):
    
    return render(request,"msg.html")


def newsfeed_page(request):
    return render(request,"newsfeed.html")


def profile_page(request):
    return render(request,"profile.html")






