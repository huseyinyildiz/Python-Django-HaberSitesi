from ckeditor.widgets import CKEditorWidget
from django.db import models

# Create your models here.
from django.forms import ModelForm, TextInput, Select, FileInput

from news.models import New


class ContentForm(ModelForm):
    class Meta:
        model = New
        fields = ['category','title','keywords','description','image','detail','slug']
        widgets = {
            'title' : TextInput(attrs={'class':'input','placeholder':'başlık'}),
            'slug' : TextInput(attrs={'class':'input','placeholder':'slug'}),
            'keywords' : TextInput(attrs={'class':'input','placeholder':'keywords'}),
            'description' : TextInput(attrs={'class':'input','placeholder':'description'}),
            'category' : Select(attrs={'class':'input','placeholder':'category'}),
            'image' : FileInput(attrs={'class':'input','placeholder':'image'}),
            'detail' : CKEditorWidget(),
        }