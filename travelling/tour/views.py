from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models
from . import models, forms

def tour_view(request):
    tour_value = models.Tour.objects.all()
    return render(request, 'tour.html', {'tour_key': tour_value})


def tour_detail_view(request, id):
    tour_id = get_object_or_404(models.Tour, id=id)
    return render(request, 'tour_detail.html', {'tour_key': tour_id})

def createTourPostView(request):
    method = request.method
    if method == "POST":
        form = forms.TourForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Successfully added')
    else:
        form = forms.TourForm()
    return render(request, 'create_post_tour.html', {'form': form})

def tour_delete_view(request):
    tour_value = models.Tour.objects.all()
    return render(request, 'tour_list.html', {'tour_key': tour_value})

def tour_drop_view(request, id):
    tour_id = get_object_or_404(models.Tour, id=id)
    tour_id.delete()
    return HttpResponse('Successfully deleted')




def createTourView(request):
    method = request.method
    if method == 'POST':
        form = forms.TourForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Comment added successfully</h1>')

    else:
        form = forms.ReviewForm()

    return render(request, 'create_review.html', {'form': form})
