from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from . forms import ItemForm, StreamForm, StepForm, ActivityForm, ActivityForm2, ActivityForm3, StatusForm, NoteForm, DocumentForm, DoctypeForm, UserGroupForm
from . import models
from accounts.models import Admin
import datetime
from django.core import serializers
from django.contrib.auth.mixins import LoginRequiredMixin 

# Create your views here.

class StreamListView(LoginRequiredMixin, ListView):
    template_name = 'ecm/index.html'
    context_object_name = 'streams'
    model = models.Stream

class EmployeeListView(LoginRequiredMixin, ListView):
    template_name = 'ecm/employees.html'
    context_object_name = 'employees'
    queryset = models.Item.objects.filter(stream__stream ='EMPLOYEE ONBOARDING')

    def get_context_data(self, *args, **kwargs):
        context = super(EmployeeListView,self).get_context_data(*args, **kwargs)
        can = models.Step.objects.filter(stream__stream ='EMPLOYEE ONBOARDING').count()
        stp = models.Activity.objects.filter(stream__stream ='EMPLOYEE ONBOARDING', status__status="Complete").count()
        context['can'] = can
        context['stp'] = stp
        return context

class BranchListView(LoginRequiredMixin, ListView):
    template_name = 'ecm/branches.html'
    context_object_name = 'branches'
    queryset = models.Item.objects.filter(stream__stream ='BRANCH ONBOARDING')

class VendorListView(LoginRequiredMixin, ListView):
    template_name = 'ecm/vendors.html'
    context_object_name = 'vendors'
    queryset = models.Item.objects.filter(stream__stream ='TEST - VENDOR ONBOARDING')


class ItemView(LoginRequiredMixin, ListView):
    template_name = 'ecm/items.html'
    context_object_name = 'items'
    model = models.Item
    ordering = ['-id']

class ItemCreateView(CreateView):
    template_name = 'ecm/item_create.html'
    form_class = ItemForm

    def get_form_kwargs(self):
        kwargs = super(ItemCreateView,self).get_form_kwargs()       
        if self.request.GET.get('stream'):
            kwargs['stream'] = self.request.GET['stream']        
        return kwargs
    
    def get_success_url(self):
        return reverse('ecm:item_details',kwargs={'pk':self.object.pk})
    

class ItemUpdateView(UpdateView):
    model = models.Item
    form_class = ItemForm
    template_name='ecm/item_update.html'

    def get_success_url(self):
        return reverse('ecm:item_details',kwargs={'pk':self.object.pk})


class ItemDeleteView(DeleteView):
    model = models.Item
    success_url = reverse_lazy("ecm:items")

class ItemDetailView(DetailView):
    model = models.Item
    context_object_name = 'item_details'
    template_name='ecm/profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        ste = []
        context['activities'] = models.Activity.objects.filter(item=self.object).order_by('-id')
        context['notes'] = models.Note.objects.filter(item=self.object).order_by('-id')
        context['documents'] = models.Document.objects.filter(item=self.object).order_by('-id')

        for s in models.Step.objects.filter(stream=self.object.stream):
            
            act = models.Activity.objects.filter(step = s, item__pk=self.object.pk).order_by('-id')
            ste.append([s, act])
        
        context['steps'] = ste
        return context

class StreamCreateView(CreateView):
    template_name = 'ecm/stream_create.html'
    form_class = StreamForm
    success_url = reverse_lazy("ecm:stream_create")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        form = StreamForm()
        streams = models.Stream.objects.all().order_by('-id')
        context['streams'] = streams      
        return context

class StreamView(ListView):
    template_name = 'ecm/streams.html'
    model = models.Stream
    context_object_name = 'streams'
    ordering = ['-id']

class StreamUpdateView(UpdateView):
    model = models.Stream
    form_class = StreamForm
    template_name='ecm/stream_update.html'
    success_url = reverse_lazy("ecm:stream_create")

class StreamDeleteView(DeleteView):
    model = models.Stream
    success_url = reverse_lazy("ecm:stream_create")

class StepCreateView(CreateView):
    template_name = 'ecm/step_create.html'
    form_class = StepForm
    success_url = reverse_lazy("ecm:step_create")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        form = StepForm()
        steps = models.Step.objects.all().order_by('-id')
        context['steps'] = steps      
        return context

class StepView(ListView):
    template_name = 'ecm/steps.html'
    model = models.Step
    context_object_name = 'steps'
    ordering = ['-id']

class StepUpdateView(UpdateView):
    model = models.Step
    form_class = StepForm
    template_name='ecm/step_update.html'
    success_url = reverse_lazy("ecm:step_create")

class StepDeleteView(DeleteView):
    model = models.Step
    success_url = reverse_lazy("ecm:step_create")
        
class ActivityCreateView(CreateView):
    template_name = 'ecm/activity_create.html'
    form_class = ActivityForm
    success_url = reverse_lazy("ecm:activities")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        form = ActivityForm()
        if self.request.GET.get('item'):
            item = models.Item.objects.get(pk=self.request.GET['item'])
            context['item'] = item
        if self.request.GET.get('stream'):
            stream = models.Stream.objects.get(pk=self.request.GET['stream'])
            context['stream'] = stream
        if self.request.GET.get('step'):
            step = models.Step.objects.get(pk=self.request.GET['step'])
            context['step'] = step
        return context

    def form_valid(self, form_class):
        if self.request.GET.get('item'):
            item = models.Item.objects.get(pk=self.request.GET['item'])
            form_class.instance.item = item
        if self.request.GET.get('stream'):
            stream = models.Stream.objects.get(pk=self.request.GET['stream'])
            form_class.instance.stream = stream
        if self.request.GET.get('step'):
            step = models.Step.objects.get(pk=self.request.GET['step'])
            form_class.instance.step = step
        return super().form_valid(form_class)

    def get_form_kwargs(self):
        kwargs = super(ActivityCreateView,self).get_form_kwargs()
        if self.request.GET.get('item'):
            kwargs['item'] = self.request.GET['item']
        if self.request.GET.get('stream'):
            kwargs['stream'] = self.request.GET['stream']
        if self.request.GET.get('step'):
            kwargs['step'] = self.request.GET['step']        
        return kwargs    

    def get_success_url(self):
        return reverse('ecm:item_details',kwargs={'pk':self.object.item.pk})

class ActivityCreateView2(CreateView):
    template_name = 'ecm/activity_create2.html'
    form_class = ActivityForm3
    success_url = reverse_lazy("ecm:activities2")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.GET.get('item'):
            context['item'] = self.request.GET.get('item')            
        if self.request.GET.get('stream'):            
            context['stream'] = self.request.GET.get('stream')      
        return context

    def form_valid(self, form_class):
        if self.request.GET.get('item'):
            item = models.Item.objects.get(pk=self.request.GET['item'])
            form_class.instance.item = item
        if self.request.GET.get('stream'):
            stream = models.Stream.objects.get(pk=self.request.GET['stream'])
            form_class.instance.stream = stream        
        return super().form_valid(form_class)

    def get_form_kwargs(self):
        kwargs = super(ActivityCreateView2,self).get_form_kwargs()       
        if self.request.GET.get('stream'):
            kwargs['stream'] = self.request.GET['stream']        
        return kwargs    

    def get_success_url(self):
        return reverse('ecm:item_details',kwargs={'pk':self.object.item.pk})

class ActivityView(ListView):
    template_name = 'ecm/activities.html'
    context_object_name = 'activities'
    model = models.Activity
    ordering = ['-id']

class ActivityUpdateView(UpdateView):
    model = models.Activity
    form_class = ActivityForm
    template_name='ecm/activity_update.html'

    def get_success_url(self):
        return reverse('ecm:item_details',kwargs={'pk':self.object.item.pk})


class ActivityUpdateView2(UpdateView):
    model = models.Activity
    form_class = ActivityForm2
    template_name='ecm/activity_update2.html'

    def get_form_kwargs(self):
        kwargs = super(ActivityUpdateView2,self).get_form_kwargs()
        if self.request.GET.get('stream'):
            kwargs['stream'] = self.request.GET['stream']
        if self.request.GET.get('step'):
            kwargs['step'] = self.request.GET['step']
        return kwargs

    def get_success_url(self):
        return reverse('ecm:item_details',kwargs={'pk':self.object.item.pk})



class ActivityDeleteView(DeleteView):
    model = models.Activity
    success_url = reverse_lazy("ecm:activities")

    def get_success_url(self):
        return reverse('ecm:item_details',kwargs={'pk':self.object.item.pk})

class StatusCreateView(CreateView):
    template_name = 'ecm/status_create.html'
    form_class = StatusForm
    success_url = reverse_lazy("ecm:status_create")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        form = StatusForm()
        statuss = models.Status.objects.all().order_by('-id')
        context['statuss'] = statuss      
        return context

class StatusView(ListView):
    template_name = 'ecm/statuss.html'
    model = models.Status
    context_object_name = 'statuss'
    ordering = ['-id']

class StatusUpdateView(UpdateView):
    model = models.Status
    form_class = StatusForm
    template_name='ecm/status_update.html'
    success_url = reverse_lazy("ecm:status_create")

class StatusDeleteView(DeleteView):
    model = models.Status
    success_url = reverse_lazy("ecm:status_create")

class NoteCreateView(CreateView):
    template_name = 'ecm/note_create.html'
    form_class = NoteForm

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

    def get_success_url(self):
        return reverse('ecm:item_details',kwargs={'pk':self.object.item.pk})      

     

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

    def get_success_url(self):
        return reverse('ecm:item_details',kwargs={'pk':self.object.item.pk}) 

class NoteDeleteView(DeleteView):
    model = models.Note

    def get_success_url(self):
        return reverse('ecm:item_details',kwargs={'pk':self.object.item.pk}) 

class DocumentCreateView(CreateView):
    template_name = 'ecm/document_create.html'
    form_class = DocumentForm
    success_url = reverse_lazy("ecm:documents")

    def get_form_kwargs(self):
        kwargs = super(DocumentCreateView,self).get_form_kwargs()
        if self.request.GET.get('item'):
            kwargs['ne'] = self.request.GET['item']
        return kwargs

    def get_success_url(self):
        return reverse('ecm:item_details',kwargs={'pk':self.object.item.pk}) 

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

    def get_success_url(self):
        return reverse('ecm:item_details',kwargs={'pk':self.object.item.pk}) 

class DocumentDeleteView(DeleteView):
    model = models.Document

    def get_success_url(self):
        return reverse('ecm:item_details',kwargs={'pk':self.object.item.pk}) 

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
    report = models.Item.objects.all()
    stream = request.GET.get('stream')
    if stream:
        report = report.filter(stream__stream = stream)
        
        for i in report:
            can = models.Step.objects.filter(stream__stream = stream).count()
            st = models.Activity.objects.filter(item__pk=i.pk, stream__stream=stream)

    return render(request, 'ecm/find_report.html', {'report':report,'stream':stream,})

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

def status_call(request):
    stream = request.GET.get('stream', None)
    obj = models.Stream.objects.get(pk = stream)
    step = models.Step.objects.filter(stream=obj.pk)
    qs = serializers.serialize('json',step)
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

class UserGroupView(CreateView):
    template_name = 'ecm/usergroups_create.html'
    form_class = UserGroupForm
    success_url = reverse_lazy("ecm:usergroups_create")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        form = UserGroupForm()
        usergroups = models.UserGroup.objects.all().order_by('-id')
        context['usergroups'] = usergroups      
        return context


class UserGroupUpdateView(UpdateView):
    model = models.UserGroup
    form_class = UserGroupForm
    template_name='ecm/doctype_update.html'
    success_url = reverse_lazy("ecm:usergroups_create")


class UserGroupDeleteView(DeleteView):
    model = models.UserGroup
    success_url = reverse_lazy("ecm:usergroups_create")