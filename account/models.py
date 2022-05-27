from django.db import models
from blog.models import Report
# Create your models here.

class RecordHtml(models.Model):
    report=models.ForeignKey(Report,on_delete=models.CASCADE)
    student_1=models.CharField(max_length=15)
    student_2=models.CharField(max_length=15)
    similarity_code=models.FloatField()
    similarity_ids=models.FloatField()
    similarity_classes=models.FloatField()
    similarity_content=models.FloatField()
    similarity_type=models.FloatField()
    similarity_value=models.FloatField()
    similatity_hrefs=models.FloatField()
    similarity_srcs=models.FloatField()
    similarity_others=models.FloatField()
    
    def __str__(self):
        return self.student_1+' '+self.student_2+' '+str(self.similarity_code)+' '+str(self.similarity_ids)+' '+str(self.similarity_classes)+' '+str(self.similarity_content)+' '+str(self.similarity_type)+' '+str(self.similarity_value)+' '+str(self.similatity_hrefs)+' '+str(self.similarity_srcs)+' '+str(self.similarity_others)


