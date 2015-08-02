from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.
class TestTalkManager(models.Manager):
	def get_queryset(self):
		return super(TestTalkManager, self).get_queryset().filter(title='Test')


class TalkList(models.Model):
	author = models.ForeignKey(User, related_name='lists')
	title = models.CharField(max_length=50)
	text = models.TextField(max_length=1024)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('talk_detail', kwargs={'pk': self.pk})

	objects = models.Manager()
	test_objects = TestTalkManager()




