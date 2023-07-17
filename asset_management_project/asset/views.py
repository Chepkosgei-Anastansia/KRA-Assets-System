from django.shortcuts import render

# Create your views here.
def storeHome(request):

    return render(request, "store/storeSummary.html")

