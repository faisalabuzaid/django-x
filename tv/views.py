from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Tv


class TvListView(ListView):
    template_name = "tv/tv-list.html"
    model = Tv


class TvDetailView(DetailView):
    template_name = "tv/tv-detail.html"
    model = Tv


class TvCreateView(CreateView):
    template_name = "tv/tv-create.html"
    model = Tv
    fields = ['brand','size','purchaser']


class TvUpdateView(UpdateView):
    template_name = "tv/tv-update.html"
    model = Tv
    fields = ['brand','size']


class TvDeleteView(DeleteView):
    template_name = "tv/tv-delete.html"
    model = Tv
    success_url = reverse_lazy("tv_list")