from django.urls import path

from django101.tasks.views import show_bare_minimum_view, show_all_tasks

urlpatterns = (
    path("", show_bare_minimum_view),
    path("all/", show_all_tasks),
)