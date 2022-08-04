from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, DetailView, ListView, CreateView, UpdateView, DeleteView
from django.views.generic.base import ContextMixin, TemplateResponseMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy


from classbasedviews.models import Book, author


# class LoginRequiredMixin(obj):   
#     @classmethod
#     def as_view(cls, **kwargs):
#         view = super(LoginRequiredMixin, cls).as_view(**kwargs)
#         return login_required(view)



# Create your views here.
class AboutUsView(TemplateView):
    template_name = "classbasedviews/about.html"
    
    
    def get_context_data(self, **kwargs):
        context = super(AboutUsView, self).get_context_data(**kwargs)
        context['title'] = 'AboutUs'
        context['meta_data'] = 'Welcome Musab'
        return context
    

#this is base view in base view we have to define render function but we can cutomise it by inherting different 
#mixins like TemplateResponseMixin has render_to_response function which we use to pass our context to our template
#since we inherit the TemplateReponseMixin we can pass template from view_as() from url and bcoz of context mixin 
#we get get_context_data function which return us the default context
class BaseView(ContextMixin, TemplateResponseMixin, View):
    def get(self, request):
        context = self.get_context_data()
        context['title'] = 'BaseView'
        context['meta_data'] = 'Welcome To BaseView'
        return self.render_to_response(context)
    
    


class DetailViewOfBooks(DetailView):
    model = Book
    template_name = 'classbasedviews/book_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(DetailViewOfBooks, self).get_context_data(**kwargs)
        context['title'] = 'DetailView'
        return context



class ListViewOfBooks(ListView):
    model = Book
    context_object_name = 'book_lst'
        
    def get_context_data(self, **kwargs):
        context = super(ListViewOfBooks, self).get_context_data(**kwargs)
        context['title'] = 'ListView'
        return context
    

class CreateViewOfBooks(CreateView):
    model = Book
    fields = ['title', 'description']           #instead of fields you can form_class = model_form if you have model form
    template_name = 'classbasedviews/forms.html'
    success_url = "/classbasedviews/createview"     #if you didn't define the successurl by default it will use the absoulte_url method of model class

    
    def get_context_data(self, **kwargs):
        context = super(CreateViewOfBooks, self).get_context_data(**kwargs)
        print(context)
        context['title'] = 'CreateView'
        return context
    
    #use this method to perform some action when form data is valid
    def form_valid(self, form):
        messages.success(self.request, 'New Book is added')
        form.instance.author = author.objects.get(name='Musab Momin')
        return super(CreateViewOfBooks, self).form_valid(form)
    

class UpdateViewOfBooks(UpdateView):
    model = Book
    fields = ['title', 'description']
    template_name = 'classbasedviews/forms.html'
    
    
    def get_context_data(self, **kwargs):
        context = super(UpdateViewOfBooks, self).get_context_data(**kwargs)
        context['title'] = 'UpdateView'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'New Book is added')
        return super(UpdateViewOfBooks, self).form_valid(form)
    

class DeleteViewOfBooks(DeleteView):
    model = Book
    success_url = '/classbasedviews/listview'
    template_name = "classbasedviews/confirm_delete.html"
    
    def get_context_data(self, **kwargs):
        context = super(DeleteViewOfBooks, self).get_context_data(**kwargs)
        context['title'] = 'DeleteViewOfBooks'
        return context
    
    #here we don't use form_valid method to add success message we use delete method to do that
    #we also have success message mixin to do add success message
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Book was deleted successfully.")
        return super(DeleteViewOfBooks, self).delete(request, *args, **kwargs)
    