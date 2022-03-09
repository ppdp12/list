from django.shortcuts import render
from . models import Place,Name
def demo1(request):
    obj=Place.objects.all()
    run=Name.objects.all()
    return  render(request,"index.html",{'result':obj,'do':run})


