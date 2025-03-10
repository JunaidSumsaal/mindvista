from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now, timedelta
from .models import WeeklyReport

@login_required
def weekly_report(request):
    """
    Displays the user's productivity report for the current week.
    """
    today = now().date()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    report, created = WeeklyReport.objects.get_or_create(
        user=request.user, start_date=start_of_week, end_date=end_of_week
    )
    
    if created:
        report.generate_report()

    return render(request, "reports/weekly_report.html", {"report": report})
