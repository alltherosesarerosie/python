from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models
from . import forms
from django.views import generic

# def tour_view(request):
#     tour_value = models.Tour.objects.all()
#     return render(request, 'tour.html', {'tour_key': tour_value})
class TourView(generic.ListView):
    template_name = 'tour.html'
    queryset = models.Tour.objects.all()

    def get_queryset(self):
        return models.Tour.objects.all()

# def tour_detail_view(request, id):
#     tour_id = get_object_or_404(models.Tour, id=id)
#     return render(request, 'tour_detail.html', {'tour_key': tour_id})
class TourDetailView(generic.DetailView):
    template_name = 'tour_detail.html'

    def get_object(self, **kwargs):
        tour = self.kwargs.get('id')
        return get_object_or_404(models.Tour, id=tour)


# def createTourPostView(request):
#     method = request.method
#     if method == "POST":
#         form = forms.TourForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Successfully added')
#     else:
#         form = forms.TourForm()
#     return render(request, 'create_post_tour.html', {'form': form})

class CreateTourPostView(generic.CreateView):
    template_name = 'create_post_tour.html'
    form_class = forms.TourForm
    queryset = models.Tour.objects.all()
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateTourPostView, self).form_valid(form=form)

# def tour_delete_view(request):
#     tour_value = models.Tour.objects.all()
#     return render(request, 'tour_list.html', {'tour_key': tour_value})

# def tour_drop_view(request, id):
#     tour_id = get_object_or_404(models.Tour, id=id)
#     tour_id.delete()
#     return HttpResponse('Successfully deleted')
class DropTourView(generic.DeleteView):
    template_name = 'confirm_delete.html'
    success_url = '/'

    def get_object(self, **kwargs):
        tour_id = self.kwargs.get('id')
        return get_object_or_404(models.Tour, id=tour_id)



class UpdateTourPostView(generic.UpdateView):
    template_name = 'update_tour.html'
    form_class = forms.TourForm
    success_url = '/'

    def get_object(self, **kwargs):
        tour = self.kwargs.get('id')
        return get_object_or_404(models.Tour, id=tour)

    def form_valid(self, form):
        return super(UpdateTourPostView, self).form_valid(form=form)


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

# кнопка поиска
class SearchTourView(generic.ListView):
    template_name = 'tour.html'
    context_object_name = 'tour'
    paginate_by = 5

    def get_queryset(self):
        return models.Tour.objects.filter(tour_name__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context