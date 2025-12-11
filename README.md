# Ex.04 Design a Website for Server Side Processing
## Date:11/12/2025

## AIM:
To create a web page to calculate vehicle mileage and fuel efficiency using server-side scripts.

## FORMULA:
M = D / F
<br> M --> Mileage (in km/l)
<br> D --> Distance Travelled (in km)
<br> F --> Fuel Consumed (in l)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM:
```
views.py
from django.shortcuts import render
def mileage(request):
    km = int(request.POST.get('distance', 0))
    litre = int(request.POST.get('fuel', 0))
    mileage = km / litre if request.method == 'POST' else 0
    print("distance=",km)
    print("fuel=",litre)
    print("mileage=",mileage)
    return render(request, 'mathapp/math.html', {'km': km, 'litre': litre, 'mileage': mileage})


urls.py
from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns = [
    path('', views.mileage, name='mileage'),
]

```


## OUTPUT - SERVER SIDE:
![alt text](<Screenshot (31).png>)

## OUTPUT - WEBPAGE:
![alt text](<Screenshot (30).png>)

## RESULT:
The a web page to calculate vehicle mileage and fuel efficiency using server-side scripts is created successfully.
