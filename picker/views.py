from django.shortcuts import render
from .forms import BasicSearchForm
from django.contrib import messages
from django.views.generic.edit import FormView

class SearchView(FormView):
    template_name = 'picker/basic-search.html'
    form_class = BasicSearchForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        results = form.get_catalog()
        if results.get('status', 'success') == 'fail':
        	msg = results.get('error', {}).get('message', '')
        	messages.error(self.request, msg)
        return render(
        	self.request,
        	self.template_name,
        	self.get_context_data(
        		art=results.get('object', {})))
