from django.shortcuts import render, get_object_or_404
from . import models


def pr_lan_view(request):
    lan_value = models.pr_lan.objects.all()
    return render(request, 'pr_lan.html', {'lan_key': lan_value})


def pr_lan_detail_view(request, id):
    lang_id = get_object_or_404(models.pr_lan, id=id)
    return render(request, 'pr_lan_detail.html', {'lan_key': lang_id})
