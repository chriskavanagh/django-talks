from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class TestTalkManager(models.Manager):
	def get_queryset(self):
		return super(TestTalkManager, self).get_queryset().filter(title='Test')
        


class TalkList(models.Model):
	author = models.ForeignKey(User, related_name='lists')    #settings.AUTH_USER_MODEL
	title = models.CharField(max_length=50)
	text = models.TextField(max_length=1024)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('talk_detail', kwargs={'pk': self.pk})

	objects = models.Manager()
	test_objects = TestTalkManager()
    
    
    
class Comment(models.Model):
	talk = models.ForeignKey(TalkList, related_name='comments')
	title = models.CharField(max_length=50)
	text = models.TextField(max_length=1024)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
        
	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('view_comment', kwargs={'pk': self.pk})

	# def get_absolute_url(self):
	# 	return reverse('view_comment', kwargs={'pk': self.talk.pk, 'pk': self.pk})        
    
    
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')    # user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile')
    gender = models.CharField(max_length=4)
    location = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.user.username
        
    # access Profile attributes in Templates like this: {{ user.profile.location }}
        
        
## -------------------Signals------------------- ##        
        
# Signal that creates a profile for each user, when a new User is created.
@receiver(post_save, sender=User)
def create_profile(sender, created, instance, **kwargs):    
    if created:                                             
        profile = UserProfile.objects.get_or_create(user=instance)[0]
        profile.save()
        
        
# sender: the User model class
# created: a boolean indicating if a new User has been created
# instance: the User instance being saved