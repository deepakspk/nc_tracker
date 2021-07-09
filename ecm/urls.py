from django.urls import path
from . import views

app_name = 'ecm'

urlpatterns = [
    path('',views.index, name='index'),
    path('items/',views.ItemView.as_view(),name='items'),
    path('item_create/',views.ItemCreateView.as_view(),name='item_create'),
    path('details/<str:pk>/',views.ItemDetailView.as_view(),name='item_details'),
    path('item/update/<str:pk>/',views.ItemUpdateView.as_view(),name='item_update'),
    path('item/delete/<str:pk>/',views.ItemDeleteView.as_view(),name='item_delete'),

    path('streams/',views.StreamView.as_view(),name='streams'),
    path('stream_create/',views.StreamCreateView.as_view(),name='stream_create'),
    path('stream/update/<str:pk>/',views.StreamUpdateView.as_view(),name='stream_update'),
    path('stream/delete/<str:pk>/',views.StreamDeleteView.as_view(),name='stream_delete'),

    path('steps/',views.StepView.as_view(),name='steps'),
    path('step_create/',views.StepCreateView.as_view(),name='step_create'),
    path('step/update/<str:pk>/',views.StepUpdateView.as_view(),name='step_update'),
    path('step/delete/<str:pk>/',views.StepDeleteView.as_view(),name='step_delete'),

    path('activities/',views.ActivityView.as_view(),name='activities'),
    path('activity_create/',views.ActivityCreateView.as_view(),name='activity_create'),    
    path('activity/update/<str:pk>/',views.ActivityUpdateView.as_view(),name='activity_update'),
    path('activity/delete/<str:pk>/',views.ActivityDeleteView.as_view(),name='activity_delete'),

    path('notes/',views.NoteView.as_view(),name='notes'),    
    path('note_create/',views.NoteCreateView.as_view(),name='note_create'),
    path('note/update/<str:pk>/',views.NoteUpdateView.as_view(),name='note_update'),
    path('note/delete/<str:pk>/',views.NoteDeleteView.as_view(),name='note_delete'),

    path('statuss/',views.StatusView.as_view(),name='statuss'),
    path('status_create/',views.StatusCreateView.as_view(),name='status_create'),
    path('status/update/<str:pk>/',views.StatusUpdateView.as_view(),name='status_update'),
    path('status/delete/<str:pk>/',views.StatusDeleteView.as_view(),name='status_delete'),

    path('documents/',views.DocumentView.as_view(),name='documents'),
    path('document_create/',views.DocumentCreateView.as_view(),name='document_create'),
    path('document/update/<str:pk>/',views.DocumentUpdateView.as_view(),name='document_update'),
    path('document/delete/<str:pk>/',views.DocumentDeleteView.as_view(),name='document_delete'),

    path('report/',views.ReportView.as_view(),name='report'),
    path('find_report/',views.findReport,name='find_report'),

    path('report_call/',views.report_call,name='report_call'),
    path('report_step/',views.report_step,name='report_step'),
    path('report_status/',views.report_status,name='report_status'),
    path('status_call/',views.status_call,name='status_call'),

    path('doctypes/',views.DoctypeView.as_view(),name='doctypes'),
    path('doctype/update/<str:pk>/',views.DoctypeUpdateView.as_view(),name='doctype_update'),
    path('doctype/delete/<str:pk>/',views.DoctypeDeleteView.as_view(),name='doctype_delete'),

    path('usergroups_create/',views.UserGroupView.as_view(),name='usergroups_create'),
    path('usergroup/update/<str:pk>/',views.UserGroupUpdateView.as_view(),name='usergroup_update'),
    path('usergroup/delete/<str:pk>/',views.UserGroupDeleteView.as_view(),name='usergroup_delete'),
]