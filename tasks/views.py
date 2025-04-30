from django.shortcuts import render
from django.views.generic import ListView
from .models import Task, Category
from django.views.generic import DetailView
from django.views.generic import CreateView
from .models import Task
from django.urls import reverse_lazy

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    
    def get_queryset(self):
        queryset = Task.objects.all()
        category_filter = self.request.GET.get('category')
        search_query = self.request.GET.get('search')
        
        if category_filter:
            queryset = queryset.filter(category__id=category_filter)
        
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)
        
        return queryset
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'

class TaskCreateView(CreateView):
    model = Task
    template_name = 'tasks/task_create.html'
    fields = ['title', 'description', 'category']
    success_url = reverse_lazy('task_list')
