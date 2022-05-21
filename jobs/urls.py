from django.urls import path
from django.views import generic
from . import views

urlpatterns = [
    path("", views.JobList.as_view(), name="job_list"),
    path("job/create/", views.JobCreate.as_view(), name="job_create"),
    path("job/delete/<int:pk>/", views.JobDelete.as_view(), name="job_delete"),
    path("job/update/<int:pk>/", views.JobUpdate.as_view(), name="job_update"),

    path("job/<int:job_pk>/", views.PeriodList.as_view(), name="period_list"),
    path("job/<int:job_pk>/period/create/", views.PeriodCreate.as_view(), name="period_create"),
    path("job/<int:job_pk>/period/delete/<int:pk>/", views.PeriodDelete.as_view(), name="period_delete"),
    path("job/<int:job_pk>/period/update/<int:pk>/", views.PeriodUpdate.as_view(), name="period_update"),

    path("job/<int:job_pk>/period/<int:period_pk>/", views.ShiftList.as_view(), name="shift_list"),
    path("job/<int:job_pk>/period/<int:period_pk>/create/", views.ShiftCreate.as_view(), name="shift_create"),
    path("job/<int:job_pk>/period/<int:period_pk>/delete/<int:pk>/", views.ShiftDelete.as_view(), name="shift_delete"),
    path("job/<int:job_pk>/period/<int:period_pk>/update/<int:pk>/", views.ShiftUpdate.as_view(), name="shift_update"),
]
