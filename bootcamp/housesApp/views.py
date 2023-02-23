from django.shortcuts import render
from .models import houseListingModel

# Create your views here.
"""
CRUD - Create, Read, Update, Delete, listing all element
"""
def houseListings(request):
    # select = from houseListing
    listings = houseListingModel.objects.all()
    context = {
        "listings" : listings,
    
    }
    return render(request, 'listings.html', context)

def retrieveDetails(request, pk):
    #Get house by id
    specific_house =  houseListingModel.objects.get(id = pk)
    context = {
        "specific" : specific_house
    }
    return render(request, 'details.html', context)
