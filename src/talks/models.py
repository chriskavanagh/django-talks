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
    
    
    
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    gender = models.CharField(max_length=4)
    location = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.user.username
        
        
        
@receiver(post_save, sender=User)
def create_profile(sender, created, instance, **kwargs):
    if created:
        user_profile = UserProfile.objects.get_or_create(user=instance)[0]
        user_profile.save()