from django.db.models import Q
from django.shortcuts import render

from django.views.generic import TemplateView, ListView

from .models import Food


class HomePageView(TemplateView):
    template_name = 'home.html'


class SearchResultsView(ListView):
    model = Food
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Food.objects.filter(
            Q(name__icontains=query) | Q(restaurant__icontains=query)
        )
        return object_list
