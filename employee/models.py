from django.db import models

# Create your models here.
RELIGION =(
			("Islam","Islam"),
    		("Christian","Christian"),
		    ("Catholic","Catholic"),
		    ("Kong Hu Cu","Kong Hu Cu"),
		    ("Hindu","Hindu"),
            ("Buddha","Buddha"),
	        ("Other","Other"),
		)

MARITAL =(
			("Single","Single"),
    		("Married","Married"),
	        ("Widowed","Widowed"),
	        ("Widower","Widower"),
		    ("Divorced","Divorced"),
		    ("Other","Other"),
		)
GENDER = (
	("Male","Male"),
	("Female","Female"),
	("Other","Other"),
)


class Position(models.Model):
	name              = models.CharField(max_length=50, unique=True)
	base_salary       = models.DecimalField(max_digits=12,decimal_places=2)
	transport         = models.DecimalField(max_digits=10,decimal_places=2)
	family_incentive  = models.DecimalField(max_digits=10,decimal_places=2)
	bpjs_cut          = models.DecimalField(max_digits=2,decimal_places=2,default=0.04)
	take_home_pay     = models.DecimalField(max_digits=12,decimal_places=2)
	
	def __str__(self):
		return "{}".format(self.name)
	

class Employee(models.Model):
	name 		= models.CharField(max_length=50)
	gender		= models.CharField(max_length=50,choices=GENDER,default='Male')
	position	= models.ForeignKey('Position',on_delete=models.CASCADE, related_name="position_employee")
	address 	= models.TextField()
	religion    = models.CharField(max_length=10,choices=RELIGION,default='Islam')
	marital     = models.CharField(max_length=20,choices=MARITAL,default='Single')
	email       = models.EmailField()
	phone       = models.CharField(max_length=15)
	
	def __str__(self):
		return "{}".format(self.name)