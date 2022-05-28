from django.forms import ModelForm
from .models import PlagiarismReport

class ReportForm(ModelForm):
	class Meta:
		model = PlagiarismReport
		fields = '__all__'