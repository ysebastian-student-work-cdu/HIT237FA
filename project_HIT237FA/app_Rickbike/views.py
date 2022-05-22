from django.shortcuts import render
from app_Rickbike.models import Widget

# Create your views here.
def home(request):
    return render(request, 'app_Rickbike/index.html')


def all_widgets(request):
    result = Widget.objects.order_by("price")

    page_data = {
    'list_widgets': result
    }

    return render(request, "app_Rickbike/all_widgets.html", page_data)

def widget_details (request, wid):

    try:
        result = Widget.objects.get(id=wid)
    except:
        result = None

    page_data = {
    'widget': result

    }

    return render (request, "app_Rickbike/widget_details.html", page_data)
