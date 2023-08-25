from django.shortcuts import render
from django.db.models import F, Count, FloatField, ExpressionWrapper, DecimalField
from django.db.models.functions import ExtractDay, ExtractMonth, ExtractYear

from datetime import date

from .models import Profile


def create_report():
    return_report = {}
    block_borders_by_age = {'block1': (18, 30), 'block2': (31, 45), 'block3': (46, 100)}
    today = date.today()
    users = Profile.objects.annotate(
        years=ExtractYear(F('date_of_birth')),
        months=ExtractMonth(F('date_of_birth')),
        days=ExtractDay(F('date_of_birth'))
    ).annotate(age=(today.year - F('years')))

    all_count_users = users.count()
    return_report.update({'count_users': all_count_users})

    for block_key, borders in block_borders_by_age.items():
        users_for_current_block = users.filter(age__range=borders).order_by('city')

        return_report.update({
            block_key: {
                'count_block_users': users_for_current_block.count(), 
                'string_borders': f'{borders[0]}/{borders[1]}',
                'users': users_for_current_block.values('city').annotate(c_count=Count('city')).annotate(percentage=ExpressionWrapper(F('c_count') / all_count_users, output_field=DecimalField(max_digits=6, decimal_places=2)))
            }
        })
    return return_report

def reports(request):
    return render(request, template_name='main/reports.html', context={'report': create_report()})