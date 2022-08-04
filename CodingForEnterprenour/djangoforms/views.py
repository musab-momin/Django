from django.shortcuts import render
from django.views import View
from django.views.generic.base import ContextMixin
from django.views.generic import CreateView
from djangoforms.forms import SearchForm, NormalForm, CarModelForm
from djangoforms.models import Car
from django.contrib import messages

# Create your views here.
class SearchFormView(ContextMixin, View):
    def get(self, request):
        context = self.get_context_data()
        context['title'] = 'Django Search Form'
        search_form = SearchForm()
        context['form'] = search_form
        return render(request, template_name='djangoforms/searchform.html', context=context)


class NormalFormView(ContextMixin, View):  
    def get(self, request):
        context = self.get_context_data()
        form = NormalForm()
        context['form'] = form
        context['title'] = 'Normal Form'
        return render(request, 'djangoforms/normalform.html', context=context)

    def post(self, request):
        form = NormalForm(request.POST)
        context = self.get_context_data()
        context['title'] = 'Normal Form'
        context['form'] = form
        
        if form.is_valid():
            print(form.cleaned_data)
        return render(request, 'djangoforms/normalform.html', context=context)
    
    
class ModelFormView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'djangoforms/postmodelform.html'
    success_url = "/djangoforms/modelform" 
    
    
    def get_context_data(self, **kwargs):
        context = super(ModelFormView, self).get_context_data(**kwargs)
        context['title'] = 'Post Modal Form'
        print(f'''
                ModelFormView context {context}
              ''')
        
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'New Car is published')
        return super(ModelFormView, self).form_valid(form)