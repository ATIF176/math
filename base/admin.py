from django.contrib import admin
from .models import *

# Register your models here.
class MeetupAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('type',)}

admin.site.register(Class)
admin.site.register(Content, MeetupAdmin)
admin.site.register(Quiz)
admin.site.register(MCQ)
admin.site.register(Exercise)