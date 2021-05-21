from django.http import HttpResponse
from django.views.generic import ListView, CreateView

from dup.models import Website
from dup.forms import WebsiteForm

# Create your views here.
class HomeView(ListView):
    model = Website
    template_name = "home.html"
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = WebsiteForm()
        return context


class WebsiteCreateView(CreateView):
    model = Website
