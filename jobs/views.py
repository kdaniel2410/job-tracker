from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import mixins
from django.db.models import ExpressionWrapper, F, Sum, Count, FloatField, DateTimeField
from . import models


class JobList(mixins.LoginRequiredMixin, generic.ListView):
    def get_queryset(self):
        return models.Job.objects.filter(user=self.request.user)


class JobCreate(mixins.LoginRequiredMixin, generic.CreateView):
    model = models.Job
    fields = ["title", "hourly_rate"]
    success_url = reverse_lazy("job_list")

    def form_valid(self, form):
        job = form.save(commit=False)
        job.user = self.request.user
        job.save()
        form.save_m2m()
        return redirect(self.success_url)


class JobUpdate(mixins.LoginRequiredMixin, generic.UpdateView):
    model = models.Job
    fields = ["title", "hourly_rate"]
    success_url = reverse_lazy("job_list")


class JobDelete(mixins.LoginRequiredMixin, generic.DeleteView):
    model = models.Job
    success_url = reverse_lazy("job_list")


class PeriodList(mixins.LoginRequiredMixin, generic.ListView):
    def get_queryset(self):
        return models.Period.objects.filter(job__id=self.kwargs['job_pk']).annotate(
            income=ExpressionWrapper(
                Sum("shift__length") * F("job__hourly_rate"), output_field=FloatField()
            ),
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["job_pk"] = self.kwargs['job_pk']
        return context
    

class PeriodCreate(mixins.LoginRequiredMixin, generic.CreateView):
    model = models.Period
    fields = ["cutoff", "payday"]

    def get_success_url(self):
        return reverse_lazy("period_list", args=(self.kwargs["job_pk"],))

    def form_valid(self, form):
        period = form.save(commit=False)
        period.job = models.Job.objects.get(pk=self.kwargs["job_pk"])
        period.save()
        return redirect(self.get_success_url())


class PeriodUpdate(mixins.LoginRequiredMixin, generic.UpdateView):
    model = models.Period
    fields = ["start", "length"]

    def get_success_url(self):
        return reverse_lazy("period_list", args=(self.kwargs["job_pk"],))


class PeriodDelete(mixins.LoginRequiredMixin, generic.DeleteView):
    model = models.Period

    def get_success_url(self):
        return reverse_lazy("period_list", args=(self.kwargs["job_pk"],))

class ShiftList(mixins.LoginRequiredMixin, generic.ListView):
    def get_queryset(self):
        return models.Shift.objects.filter(
            period__id=self.kwargs['period_pk'],
        ).annotate(
            income=ExpressionWrapper(
                F("length") * F("period__job__hourly_rate"), output_field=FloatField()
            ),
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["job_pk"] = self.kwargs['job_pk']
        context["period_pk"] = self.kwargs['period_pk']
        return context


class ShiftCreate(mixins.LoginRequiredMixin, generic.CreateView):
    model = models.Shift
    fields = ["start", "length"]

    def get_success_url(self):
        return reverse_lazy("shift_list", args=(self.kwargs["job_pk"], self.kwargs["period_pk"]))

    def form_valid(self, form):
        shift = form.save(commit=False)
        shift.period = models.Period.objects.get(pk=self.kwargs["period_pk"])
        shift.save()
        return redirect(self.get_success_url())


class ShiftUpdate(mixins.LoginRequiredMixin, generic.UpdateView):
    model = models.Shift
    fields = ["start", "length"]

    def get_success_url(self):
        return reverse_lazy("shift_list", args=(self.kwargs["job_pk"], self.kwargs["period_pk"]))


class ShiftDelete(mixins.LoginRequiredMixin, generic.DeleteView):
    model = models.Shift

    def get_success_url(self):
        return reverse_lazy("shift_list", args=(self.kwargs["job_pk"], self.kwargs["period_pk"]))
