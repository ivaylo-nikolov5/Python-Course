from django.urls import path

from departments_app.departments.views import show_departments

urlpatterns = (
    path('', show_departments),
    path('<department_id>/', show_departments),
    path('int/<int:department_id>/', show_departments),
)