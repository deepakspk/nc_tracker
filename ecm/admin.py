from django.contrib import admin
from .models import Item, Stream, Step, Activity, Status, Note, Document, Doctype, UserGroup
admin.site.register(Item)
admin.site.register(Stream)
admin.site.register(Step)
admin.site.register(Activity)
admin.site.register(Status)
admin.site.register(Note)
admin.site.register(Document)
admin.site.register(Doctype)
admin.site.register(UserGroup)

# Register your models here.
