
u: mickyMcK
p: mickypass

def index_view(request):
    return render(request, "directory/index.html")
    latest_cohort = Cohort.objects.filter(
        end_date__lte=timezone.now().date()).order_by('-end_date')[0]
    return render(request, "directory/index.html", {"cohort": latest_cohort})

    post_date = models.DateField(default=timezone.now)
    is_solved = models.BooleanField(default=False)