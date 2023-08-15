from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from website import forms
from website.models import Slider, Service, Portfolio, Package, Video, WebsiteSettings


class HomeView(TemplateView):
  template_name = 'index.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['sliders'] = Slider.objects.all()
    context['services'] = Service.objects.all()
    context['portfolios'] = Portfolio.objects.all()
    context['packages'] = Package.objects.all()
    context['videos'] = Video.objects.all()
    context['website'] = WebsiteSettings.objects.first()

    return context


class ContactView(View):
    def post(self, request):
        form = forms.ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your data has been successfully saved")
        else:
            messages.error(request, "Invalid data! please try again.")
        return redirect('/')


class SubscriberView(View):
    def post(self, request):
        form = forms.SubscriberForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your data has been successfully saved")
        else:
            messages.error(request, "Invalid data! please try again.")
        return redirect('/')


