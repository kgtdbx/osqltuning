from django.db import models
from django.forms import ModelForm

class DbConnections(models.Model):
	conname = models.CharField("Connection Name", max_length=40)
	hostname = models.CharField("Hostname or IP", max_length=100)
	username = models.CharField("Username to connect", max_length=30)
	password = models.CharField(max_length=100)
	servicename = models.CharField("Oracle ServiceName", max_length=100)

	def __unicode__(self):
		return self.conname
	      
class DbConnectionsForm(ModelForm):
    class Meta:
        model = DbConnections
        fields = ['conname', 'hostname', 'username','password','servicename']
