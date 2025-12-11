from django.shortcuts import render
def mileage(request):
    km = int(request.POST.get('distance', 0))
    litre = int(request.POST.get('fuel', 0))
    mileage = km / litre if request.method == 'POST' else 0
    print("distance=",km)
    print("fuel=",litre)
    print("mileage=",mileage)
    return render(request, 'mathapp/math.html', {'km': km, 'litre': litre, 'mileage': mileage})
