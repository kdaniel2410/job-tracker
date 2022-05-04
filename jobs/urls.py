from django.urls import path
from django.views import generic
from . import views

urlpatterns = [
    path("", views.JobList.as_view(), name="jobs"),
    path("job/<int:pk>/", views.JobDetail.as_view(), name="job"),
    path("job/create/", views.JobCreate.as_view(), name="job_create"),
    path("job/<int:pk>/create", views.ShiftCreate.as_view(), name="shift_create"),
    path("shift/delete/<int:pk>", views.ShiftDelete.as_view(), name="shift_delete"),
    path("shift/update/<int:pk>", views.ShiftUpdate.as_view(), name="shift_update"),
]