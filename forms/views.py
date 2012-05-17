#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView

from forms import RegistrationForm

# Create your views here.


class ParticipationView(FormView):
    template_name = 'form.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('thank_you')

    def form_valid(self, form):
        form.save()
        return super(ParticipationView, self).form_valid(form)


def thanks(request):
    return HttpResponse('thank you')

