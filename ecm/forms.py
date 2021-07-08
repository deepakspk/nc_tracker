from .models import Item, Stream, Step, Activity, Status, Note, Document
from django.forms import ModelForm, Form
from django import forms
from django.contrib.auth.models import User
import datetime

class ItemForm(ModelForm):
    class Meta:
        model= Item
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})

class StreamForm(ModelForm):
    class Meta:
        model= Stream
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})

class StepForm(ModelForm):
    class Meta:
        model= Step
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})

class ActivityForm(ModelForm):
    class Meta:
        model= Activity
        fields = '__all__'
        widgets = {
            'date':forms.DateInput(attrs={'type':'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})

class StatusForm(ModelForm):
    class Meta:
        model= Status
        fields = '__all__'        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})


class NoteForm(ModelForm):
    class Meta:
        model= Note
        exclude = ('date','comment_by',)
        widgets = {
            'date':forms.DateInput(attrs={'type':'date'})
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})

class DocumentForm(ModelForm):
    class Meta:
        model= Document
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})