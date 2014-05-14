from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from chartapp.models import Chart, TimeStamp
# Create your views here.

def index(request):
    context = RequestContext(request)
    chart = Chart.objects.get(pk=1)
    timestamps = TimeStamp.objects.all()

    context_dict = {'chart':chart, 'timestamps': timestamps}
    return render_to_response('chartapp/index.html', context_dict, context)



