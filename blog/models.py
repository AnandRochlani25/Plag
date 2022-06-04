
from django.db import models

# Create your models here.
class PlagiarismReport(models.Model):
    #cohort, unit, sprint, file_name, extension)
    cohort_id=models.CharField(max_length=15)
    unit=models.IntegerField()
    sprint=models.IntegerField()
    filename=models.CharField(max_length=255)
    extension=models.CharField(max_length=10)
    token=models.CharField(max_length=100000)
    def __str__(self):
        return self.cohort_id+' '+str(self.unit)+'  '+str(self.sprint)+' '+' '+self.filename+' '+self.extension+' '+self.token


class PlagiarismRecordU_3(models.Model):
    report=models.ForeignKey(PlagiarismReport,on_delete=models.CASCADE)
    student_1=models.CharField(max_length=15)
    student_2=models.CharField(max_length=15)
    similarity_coeff=models.FloatField()

    def __str__(self):
        return self.student_1+' '+self.student_2+' '+str(self.similarity_coeff)