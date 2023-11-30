from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import get_user_model
from .models import *

User = get_user_model()


class HomeTemplateView(View):
    template_name = 'index.html'
    context = {}

    def get(self, request):
        todos = Todo.objects.filter(owner_id=request.user.id)
        todo_data = []
        for index, value in enumerate(todos):
            value.index = index + 1
            todo_data.append(value)
        self.context.update({'todos': todo_data})
        return render(request, self.template_name, self.context)

    def post(self, request):
        todo_id = request.POST.get('todo_id')
        Todo.objects.get(pk=todo_id).delete()
        return redirect('/todo')


class TodoTemplateView(View):
    template_name = 'todo.html'
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        text = request.POST.get('text')
        expires_at = request.POST.get('expires_at')
        owner = request.user.id

        todo = Todo.objects.create(
            text=text,
            expires_at=expires_at,
            owner_id=owner
        )
        todo.save()
        return redirect('/todo')