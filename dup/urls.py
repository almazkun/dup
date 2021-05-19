from django.urls import path


from dup.views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]
