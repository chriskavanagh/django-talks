from __future__ import absolute_import
from django.db import models
from talks.models import TalkList
from django.conf import settings
#from django.contrib.auth.models import User
from django.core.urlresolvers import reverse



# Create your models here.
class Comment(models.Model):
	talk = models.ManyToManyField(TalkList, related_name='comments')
	title = models.CharField(max_length=50)
	text = models.TextField(max_length=1024)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('comment_detail', kwargs={'pk': self.pk})
        
        
