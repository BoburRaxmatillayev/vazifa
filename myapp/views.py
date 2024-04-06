from django.shortcuts import render
from django.http import HttpResponse #new


def main(request):
    return render(request,"index.html")

def main1(request):
    return render(request,"main.html")

def main2(request):
    return render(request,"qwerty.html")

def main4(request):
    return render(request,"asdfg.html")

