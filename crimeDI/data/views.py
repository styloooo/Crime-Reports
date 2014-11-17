from django.shortcuts import render
from crimeDI.data.models import Incident

# Create your views here.
def index(request):
	all_incidents = Incident.objects.all()

	return render('index.html', {'incidents':all_incidents})