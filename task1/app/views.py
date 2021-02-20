import csv
from django.shortcuts import render

def inflation_view(request):
    with open("inflation_russia.csv", encoding='utf-8') as r_file:
        file_reader = csv.DictReader(r_file, delimiter=";")
        data = list(file_reader)

        return render(request, 'inflation.html', context={'data': data,
                                                          'titles': data[0]})