from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class JobPost(models.Model):
    uniq_id = models.CharField(max_length=200,unique=True,null=True,blank=True)
    company	= models.CharField(max_length=200,null=True,blank=True)
    education = models.CharField(max_length=2000,null=True,blank=True)	
    experience = models.CharField(max_length=600,null=True,blank=True)
    industry = models.CharField(max_length=700,null=True,blank=True)
    jobdescription = models.CharField(max_length=2000,null=True,blank=True)
    jobid = models.CharField(max_length=200,null=True,blank=True)
    joblocation_address = models.CharField(max_length=200,null=True,blank=True)
    jobtitle = models.CharField(max_length=200,null=True,blank=True)
    numberofpositions = models.CharField(max_length=200,null=True,blank=True)
    payrate	= models.CharField(max_length=200,null=True,blank=True)
    postdate = models.CharField(max_length=200,null=True,blank=True)
    site_name = models.CharField(max_length=200,null=True,blank=True)
    skills = models.CharField(max_length=200,null=True,blank=True)

    class Meta:
        managed = True
        db_table = 'job_post'


class JobApply(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    jobid = models.ForeignKey(JobPost,on_delete=models.CASCADE)

    class Meta:
        managed=True
        db_table = 'job_applied'
        
    