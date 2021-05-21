from django.urls import path


from dup.views import HomeView, WebsiteCreateView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("website/create", WebsiteCreateView.as_view(), name="website_create"),
]
