from .models import Item,Comment
from django import forms

class ItemForm(forms.ModelForm):
          class Meta:
                  model=Item
                  fields=['name','desc']

class CommentForm(forms.ModelForm):
          class Meta:
                  model=Comment
                  fields=['cmt']