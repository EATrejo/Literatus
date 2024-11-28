from django.shortcuts import render
from .models import Tertulia



def tertulias_list(request):
    
    tertulias = Tertulia.objects.all()



    context = {
        'tertulias': tertulias,
}
    return render(request, 'tertulias/tertulias_list.html', context)