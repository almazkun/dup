from django.urls import reverse_lazy
from django.views.generic import CreateView

from dup.models import Website

# Create your views here.
class HomeView(CreateView):
    model = Website
    template_name = "home.html"
    fields = [
        "url",
    ]
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["websites"] = Website.objects.all().order_by("-created_on")
        return context
