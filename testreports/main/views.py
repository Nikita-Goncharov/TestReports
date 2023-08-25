from django.shortcuts import render

from .report_function import create_report

def reports(request):
    return render(request, template_name='main/reports.html', context={'report': create_report()})