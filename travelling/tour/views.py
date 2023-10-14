from django.shortcuts import render, get_object_or_404
from . import models

def tour_view(request):
    tour_value = models.Tour.objects.all()
    return render(request, 'tour.html', {'tour_key': tour_value})


def tour_detail_view(request, id):
    tour_id = get_object_or_404(models.Tour, id=id)
    return render(request, 'tour_detail.html', {'tour_key': tour_id})
