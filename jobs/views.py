from django.views import generic
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.contrib.auth import mixins
from django.db.models import ExpressionWrapper, F, Sum, Count, FloatField, DateTimeField
from . import models


class JobList(mixins.LoginRequiredMixin, generic.ListView):
    def get_queryset(self):
        return models.Job.objects.filter(user=self.request.user)


class JobDetail(mixins.LoginRequiredMixin, generic.DetailView):
    def get_queryset(self):
        return models.Job.objects.annotate(
            total_hours=Sum("shift__length"),
            shift_count=Count("shift"),
            total_income=ExpressionWrapper(
                Sum("shift__length") * F("hourly_rate"), output_field=FloatField()
            ),
        ).filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["shifts"] = models.Shift.objects.filter(job=self.get_object()).annotate(
            income=ExpressionWrapper(
                F("length") * F("job__hourly_rate"), output_field=FloatField()
            ),
        )
        return context


class JobCreate(mixins.LoginRequiredMixin, generic.CreateView):
    model = models.Job
    fields = ["title", "hourly_rate"]
    success_url = reverse_lazy("jobs")

    def form_valid(self, form):
        job = form.save(commit=False)
        job.user = self.request.user
        job.save()
        form.save_m2m()
        return redirect(self.success_url)


class ShiftCreate(mixins.LoginRequiredMixin, generic.CreateView):
    model = models.Shift
    fields = ["start", "length"]
    success_url = "/"

    def form_valid(self, form):
        shift = form.save(commit=False)
        shift.job = models.Job.objects.get(pk=self.kwargs["pk"])
        shift.save()
        return redirect(self.success_url)


class ShiftUpdate(mixins.LoginRequiredMixin, generic.UpdateView):
    model = models.Shift
    fields = ["start", "length"]
    success_url = "/"


class ShiftDelete(mixins.LoginRequiredMixin, generic.DeleteView):
    model = models.Shift
    success_url = "/"
