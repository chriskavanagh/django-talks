from django.db import models
from django.contrib.auth import User
from django.core.urlresolvers import reverse

# Create your models here.
class TalkList(models.Model):
	author = models.ForeignKey(User, related_name='lists')
	title = models.CharField(max_length=50)
	text = models.TextField(max_length=1024)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('comment_detail', kwargs={'pk': self.pk})




