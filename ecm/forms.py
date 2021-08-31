from .models import Item, Stream, Step, Activity, Status, Note, Document, Doctype, UserGroup
from django.forms import ModelForm, Form
from django import forms
from django.contrib.auth.models import User
import datetime

class ItemForm(ModelForm):
    class Meta:
        model= Item
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        stream = None
        if 'stream' in kwargs:
            stream = kwargs.pop("stream")
        
        super(ItemForm, self).__init__(*args, **kwargs)
        if stream:
            self.fields['stream'].queryset =  Stream.objects.filter(stream = stream)
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
        exclude = ['item','stream','step','added_by']
        # fields = '__all__'
        widgets = {
            'date':forms.DateInput(attrs={'type':'date'})
        }

    def __init__(self, *args, **kwargs):
        item = None
        stream = None
        step = None
        if 'item' in kwargs:
            item = kwargs.pop("item")
        if 'stream' in kwargs:
            stream = kwargs.pop("stream")
        if 'step' in kwargs:
            step = kwargs.pop("step")
    
        super(ActivityForm, self).__init__(*args, **kwargs)
        # if item:
        #     self.fields['item'].queryset =  Item.objects.filter(pk = item)
        # if stream:
        #     self.fields['stream'].queryset =  Stream.objects.filter(stream = stream)
        # if step:
        #     self.fields['step'].queryset =  Step.objects.filter(step = step)
        if step:
            self.fields['status'].queryset =  Status.objects.filter(stream__pk=stream, step__pk=step)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})


class ActivityForm2(ModelForm):
    class Meta:
        model= Activity
        exclude = ['item','stream','step','added_by']
        widgets = {
            'date':forms.DateInput(attrs={'type':'date'})
        }

    def __init__(self, *args, **kwargs):
        stream = None
        step = None
        if 'stream' in kwargs:
            stream = kwargs.pop("stream")
        if 'step' in kwargs:
            step = kwargs.pop("step")
        
        super(ActivityForm2, self).__init__(*args, **kwargs)
        if stream:
            self.fields['status'].queryset =  Status.objects.filter(stream__pk = stream, step__pk=step)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})

class ActivityForm3(ModelForm):
    class Meta:
        model= Activity
        exclude = ['item','stream','added_by']
        widgets = {
            'date':forms.DateInput(attrs={'type':'date'})
        }

    def __init__(self, *args, **kwargs):
        stream = None
        if 'stream' in kwargs:
            stream = kwargs.pop("stream")
        
        super(ActivityForm3, self).__init__(*args, **kwargs)
        if stream:
            self.fields['step'].queryset =  Step.objects.filter(stream__pk = stream)
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
         ne = None
         if 'ne' in kwargs:
            ne = kwargs.pop("ne")
         super(NoteForm, self).__init__(*args, **kwargs)
         if ne:
            self.fields['item'].queryset =  Item.objects.filter(pk = ne)
         for field in self.fields:
             self.fields[field].widget.attrs.update({'class':'form-control'})

class DocumentForm(ModelForm):
    class Meta:
        model= Document
        fields = '__all__'

    def __init__(self, *args, **kwargs):
         ne = None
         if 'ne' in kwargs:
            ne = kwargs.pop("ne")
         super(DocumentForm, self).__init__(*args, **kwargs)
         if ne:
            self.fields['item'].queryset =  Item.objects.filter(pk = ne)
         for field in self.fields:
             self.fields[field].widget.attrs.update({'class':'form-control'})


class DoctypeForm(ModelForm):
    class Meta:
        model= Doctype
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})

class UserGroupForm(ModelForm):
    class Meta:
        model= UserGroup
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})

