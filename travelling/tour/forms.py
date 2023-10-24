from django import forms
from . import models

class TourForm(forms.ModelForm):
    class Meta:
        model = models.Tour
        fields = '__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.ReviewTour
        fields = '__all__'