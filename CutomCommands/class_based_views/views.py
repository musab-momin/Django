from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .forms import ContactForm, StudentForm

from .models import Student

#this is for list view
from django.views.generic import ListView

#this is detail view
from django.views.generic.detail import DetailView

#this is formview
from django.views.generic.edit import FormView


# Create your views here.
class IndexView(View):
    def get(self, request):
        form = ContactForm()
        context = {'mssg': 'I am learning class based view', 'form': form}
        return render(request, 'class_based_views/index.html', context)

    def post(self, request):
        print('This is hit')
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['name']
        context = {'name': data}
        return render(request, 'class_based_views/index.html', context)


class Parameter(View):
    def get(self, request, id):
        print('''
        This is not working me | This is not working for me |
        This is nor 
        ''')
        return HttpResponse(f'This is not okay {id}')


#From here I am using ListView it comes under Generic views it is not from BaseView
class StudentView(ListView):
    # model = Student     #list view comes with default template nameing convention but u can override that
    # ordering = ['roll']

    #cutom template nameing
    model = Student
    template_name = 'class_based_views/student.html'
    context_object_name = 'students'

    #if you want to perform any query on your data you can use this mehtod this will auto called 
    #by django
    # def get_queryset(self):
    #     return Student.objects.filter(course='Python')



#this is detail view we use this to display a single object from the table to template
class StudentDetailView(DetailView):
    model = Student
    template_name = 'class_based_views/single_student.html'
    context_object_name = 'single_student'



#this is form view
class AddStudentFormView(FormView):
    template_name = 'class_based_views/add_student.html'
    form_class = StudentForm





