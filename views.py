from django.shortcuts import render
from django.views.generic import TemplateView
from .models import club

# Create your views here.
class ClubChartview(TemplateView):
	template_name = 'clubs/charts.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["qs"] = club.objects.all()
		return context