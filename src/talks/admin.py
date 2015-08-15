from django.contrib import admin
from .models import TalkList, UserProfile, Comment

# Register your models here.
class TalkListAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'text', 'timestamp')
    
    class Meta:
        model = TalkList
        
        
        
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'location')
    
    class Meta:
        model = UserProfile
        
        
        
class CommentAdmin(admin.ModelAdmin):
    list_display = ('talk', 'title', 'text', 'timestamp')
    
    class Meta:
        model = Comment

    
    
admin.site.register(TalkList, TalkListAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Comment, CommentAdmin)
