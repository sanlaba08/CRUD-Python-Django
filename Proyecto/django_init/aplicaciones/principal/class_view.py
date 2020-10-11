from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy
from .forms import personaForm
from .models import Persona

class PersonaList(ListView):
    model = Persona
    template_name = 'index.html'

class PersonaCreate(CreateView):
    model = Persona
    form_class = personaForm
    template_name = 'crearPersona.html'
    success_url = reverse_lazy('index')

class PersonaUpdate(UpdateView):
    model = Persona
    form_class = personaForm
    template_name = 'crearPersona.html'
    success_url = reverse_lazy('index')

class PersonaDelete(DeleteView):
    model = Persona
    template_name = 'verificacion.html'
    success_url = reverse_lazy('index')
