from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = {
            "title",
            "traveled_at",
            "grade",
            "companion",
            "content",            
            "image",
        }