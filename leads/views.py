from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead

# Create your views here.
def index(request):
    return render(request, 'index.html')




def leads_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads,
    }
    return render(request, 'leads/leads_list.html', context)

def lead_detail(request, pk):
    lead = Lead.objects.get(pk=pk)
    context = {
        "lead": lead,
    }
    return render(request, 'leads/lead_detail.html', context)