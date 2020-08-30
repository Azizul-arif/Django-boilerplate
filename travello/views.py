from django.shortcuts import render
from . models import Destination

# Create your views here.
def index(request):
    # dest1=Destination()
    # dest1.name='Mumbai'
    # dest1.desc='The city that never sleep'
    # dest1.price=700
    # dest1.img='destination_1.jpg'
    # dest1.offer=False
    # dest2=Destination()
    # dest2.name='Dhaka'
    # dest2.desc='it’s at the center of national government, trade and culture.'
    # dest2.price=800
    # dest2.img='destination_2.jpg'
    # dest2.offer=False
    # dest3=Destination()
    # dest3.name='Ho chi Minh'
    # dest3.desc='Ho Chi Minh City (Vietnamese: Thành phố Hồ Chí Minh).'
    # dest3.price=600
    # dest3.img='destination_3.jpg'
    # dest3.offer=True
    # dests=[dest1,dest2,dest3]
    dests=Destination.objects.all()
    return render (request,'index.html',{'dests':dests})