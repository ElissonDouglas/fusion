from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Servicos, Funcionario, Recursos
from .forms import ContatoForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servicos.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        
        context['recursos1'] = Recursos.objects.order_by('?').filter(coluna='coluna1')
        context['recursos2'] = Recursos.objects.order_by('?').filter(coluna='coluna2')
        return context
    
    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)
    
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar o e-mail')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
    


class Error404View(FormView):
    template_name = '404.html'


class Error500View(FormView):
    template_name = '500.html'

