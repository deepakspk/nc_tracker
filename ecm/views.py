from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.http import HttpResponse
from . forms import ItemForm, StreamForm, StepForm, ActivityForm, StatusForm, NoteForm, DocumentForm, DoctypeForm
from . import models
from accounts.models import Admin
import datetime
from django.core import serializers
from django.contrib.auth.mixins import LoginRequiredMixin 

# Create your views here.
def index(request):
    return render(request,'ecm/index.html')

class ItemView(LoginRequiredMixin, ListView):
    template_name = 'ecm/items.html'
    context_object_name = 'items'
    model = models.Item
    ordering = ['-id']

class ItemCreateView(CreateView):
    template_name = 'ecm/item_create.html'
    form_class = ItemForm
    success_url = reverse_lazy("ecm:items")

class ItemUpdateView(UpdateView):
    model = models.Item
    form_class = ItemForm
    template_name='ecm/item_update.html'
    success_url = reverse_lazy("ecm:items")

class ItemDeleteView(DeleteView):
    model = models.Item
    success_url = reverse_lazy("ecm:items")

class ItemDetailView(DetailView):
    model = models.Item
    context_object_name = 'item_details'
    template_name='ecm/profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['activities'] = models.Activity.objects.filter(item=self.object).order_by('-id')
        context['notes'] = models.Note.objects.filter(item=self.object).order_by('-id')
        context['documents'] = models.Document.objects.filter(item=self.object).order_by('-id')
        return context

class StreamCreateView(CreateView):
    template_name = 'ecm/stream_create.html'
    form_class = StreamForm
    success_url = reverse_lazy("ecm:streams")

class StreamView(ListView):
    template_name = 'ecm/streams.html'
    model = models.Stream
    context_object_name = 'streams'
    ordering = ['-id']

class StreamUpdateView(UpdateView):
    model = models.Stream
    form_class = StreamForm
    template_name='ecm/stream_update.html'
    success_url = reverse_lazy("ecm:streams")

class StreamDeleteView(DeleteView):
    model = models.Stream
    success_url = reverse_lazy("ecm:streams")

class StepCreateView(CreateView):
    template_name = 'ecm/step_create.html'
    form_class = StepForm
    success_url = reverse_lazy("ecm:steps")

class StepView(ListView):
    template_name = 'ecm/steps.html'
    model = models.Step
    context_object_name = 'steps'
    ordering = ['-id']

class StepUpdateView(UpdateView):
    model = models.Step
    form_class = StepForm
    template_name='ecm/step_update.html'
    success_url = reverse_lazy("ecm:steps")

class StepDeleteView(DeleteView):
    model = models.Step
    success_url = reverse_lazy("ecm:streams")
        
class ActivityCreateView(CreateView):
    template_name = 'ecm/activity_create.html'
    form_class = ActivityForm
    success_url = reverse_lazy("ecm:activities")

    def get_form_kwargs(self):
        kwargs = super(ActivityCreateView,self).get_form_kwargs()
        if self.request.GET.get('item'):
            kwargs['ne'] = self.request.GET['item']
        return kwargs

class ActivityView(ListView):
    template_name = 'ecm/activities.html'
    context_object_name = 'activities'
    model = models.Activity
    ordering = ['-id']

class ActivityUpdateView(UpdateView):
    model = models.Activity
    form_class = ActivityForm
    template_name='ecm/activity_update.html'
    success_url = reverse_lazy("ecm:activities")

class ActivityDeleteView(DeleteView):
    model = models.Activity
    success_url = reverse_lazy("ecm:activities")

class StatusCreateView(CreateView):
    template_name = 'ecm/status_create.html'
    form_class = StatusForm
    success_url = reverse_lazy("ecm:statuss")

class StatusView(ListView):
    template_name = 'ecm/statuss.html'
    model = models.Status
    context_object_name = 'statuss'
    ordering = ['-id']

class StatusUpdateView(UpdateView):
    model = models.Status
    form_class = StatusForm
    template_name='ecm/status_update.html'
    success_url = reverse_lazy("ecm:statuss")

class StatusDeleteView(DeleteView):
    model = models.Status
    success_url = reverse_lazy("ecm:statuss")

class NoteCreateView(CreateView):
    template_name = 'ecm/note_create.html'
    form_class = NoteForm
    success_url = reverse_lazy("ecm:notes") 

    def form_valid(self, form_class):
        form_class.instance.date = datetime.date.today()
        emp = Admin.objects.get(user=self.request.user)
        form_class.instance.comment_by = emp
        return super().form_valid(form_class)  
    
    def get_form_kwargs(self):
        kwargs = super(NoteCreateView,self).get_form_kwargs()
        if self.request.GET.get('item'):
            kwargs['ne'] = self.request.GET['item']
        return kwargs

     

class NoteView(ListView):
    template_name = 'ecm/notes.html'
    model = models.Note
    context_object_name = 'notes'
    ordering = ['-id']    

class NoteUpdateView(UpdateView):
    model = models.Note
    form_class = NoteForm
    template_name='ecm/note_update.html'
    success_url = reverse_lazy("ecm:notes")

class NoteDeleteView(DeleteView):
    model = models.Note
    success_url = reverse_lazy("ecm:notes")

class DocumentCreateView(CreateView):
    template_name = 'ecm/document_create.html'
    form_class = DocumentForm
    success_url = reverse_lazy("ecm:documents")

    def get_form_kwargs(self):
        kwargs = super(DocumentCreateView,self).get_form_kwargs()
        if self.request.GET.get('item'):
            kwargs['ne'] = self.request.GET['item']
        return kwargs

class DocumentView(ListView):
    template_name = 'ecm/documents.html'
    model = models.Document
    context_object_name = 'documents'
    ordering = ['-id']

class DocumentUpdateView(UpdateView):
    model = models.Document
    form_class = DocumentForm
    template_name='ecm/document_update.html'
    success_url = reverse_lazy("ecm:documents")

class DocumentDeleteView(DeleteView):
    model = models.Document
    success_url = reverse_lazy("ecm:documents")

class ReportView(ListView):
    template_name = 'ecm/report.html'
    context_object_name = 'report'
    model = models.Stream

    def get_context_data(self, *args, **kwargs):
        context = super(ReportView,self).get_context_data(*args, **kwargs)
        can = models.Stream.objects.all()
        context['can'] = can
        return context

def findReport(request):
    report = models.Activity.objects.all()
    stream = request.GET.get('stream')
    if stream:
        report = report.filter(stream__stream = stream)
    return render(request, 'ecm/find_report.html', {'report':report})

def report_call(request):
    item = request.GET.get('item', None)
    obj = models.Item.objects.get(pk = item)
    stream = models.Stream.objects.filter(pk=obj.stream.pk)
    qs = serializers.serialize('json',stream)
    return HttpResponse(qs)

def report_step(request):
    stream = request.GET.get('stream', None)
    obj = models.Stream.objects.get(pk = stream)
    step = models.Step.objects.filter(stream__pk=obj.pk)
    qs = serializers.serialize('json',step)
    return HttpResponse(qs)

def report_status(request):
    step = request.GET.get('step', None)
    obj = models.Step.objects.get(pk = step)
    status = models.Status.objects.filter(step__pk=obj.pk)
    qs = serializers.serialize('json',status)
    return HttpResponse(qs)


class DoctypeView(CreateView):
    template_name = 'ecm/doctypes.html'
    form_class = DoctypeForm
    success_url = reverse_lazy("ecm:doctypes")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        form = DoctypeForm()
        doctypes = models.Doctype.objects.all().order_by('-id')
        context['doctypes'] = doctypes      
        return context


class DoctypeUpdateView(UpdateView):
    model = models.Doctype
    form_class = DoctypeForm
    template_name='ecm/doctype_update.html'
    success_url = reverse_lazy("ecm:doctypes")


class DoctypeDeleteView(DeleteView):
    model = models.Doctype
    success_url = reverse_lazy("ecm:doctypes")