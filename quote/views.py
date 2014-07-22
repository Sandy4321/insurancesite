from django.shortcuts import render, render_to_response
from django.template import RequestContext
from quote.forms import QuoteForm

# Create your views here.
def index(request):
    
    form = QuoteForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        
    return render_to_response('index.html',
                              locals(),
                              context_instance=RequestContext(request))