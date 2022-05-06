from django.urls import path
from django.views import generic
from . import views

urlpatterns = [
    path("", views.JobList.as_view(), name="jobs"),
    path("job/<int:pk>/", views.JobDetail.as_view(), name="job"),
    path("job/create/", views.JobCreate.as_view(), name="job_create"),
    path("job/delete/<int:pk>", views.JobDelete.as_view(), name="job_delete"),
    path("job/update/<int:pk>", views.JobUpdate.as_view(), name="job_update"),
    path("job/<int:pk>/create", views.ShiftCreate.as_view(), name="shift_create"),
    path("job/<int:job_pk>/delete/<int:pk>", views.ShiftDelete.as_view(), name="shift_delete"),
    path("job/<int:job_pk>/update/<int:pk>", views.ShiftUpdate.as_view(), name="shift_update"),
]
