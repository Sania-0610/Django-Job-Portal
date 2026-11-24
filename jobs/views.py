from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import get_template
from .forms import ApplicationForm
from .models import Job


def home(request):
    print("TEMPLATE PATH:", get_template("index.html").origin.name)
    jobs = Job.objects.all()
    return render(request, "index.html", {"jobs": jobs})


def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    submitted = request.GET.get("applied") == "1"

    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()
            return redirect(f"/jobs/{job.id}/?applied=1")
    else:
        form = ApplicationForm()

    return render(
        request,
        "job_detail.html",
        {
            "job": job,
            "form": form,
            "submitted": submitted,
        },
    )