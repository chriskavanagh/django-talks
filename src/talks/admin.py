from django.contrib import admin
from .models import TalkList

# Register your models here.
class TalkListAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'text', 'timestamp')
    
    class Meta:
        model = TalkList
    
    
admin.site.register(TalkList, TalkListAdmin)
