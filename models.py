from django.db import models

# Create your models here.
class Menu(models.Model):
	menu_name = models.CharField(max_length=100)
	pub_date = models.DateTimeField('Available time')
	def __str__(self):
	    return self.menu_name

class Choice(models.Model):
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE)
    classfication = models.CharField(max_length=200,default='snoopy')
    classfication_desc = models.CharField(max_length=200,default='water')
    def __str__(self):
        return self.classfication

class achievement(models.Model):
	#这行有问题，如何加入联合主键
	choice = models.ForeignKey(Choice,Menu)
	goal = models.CharField(max_length=200,default='none')
	time_start = models.DateField('Begins')
	time_end = models.DateField('End')
	extrainfo = models.CharField(max_length=200,default='none')
	def __str__(self):
		return self.goal
