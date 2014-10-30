#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 1 Reading a CSV"""


grades = {
    'A': float(100.0),
    'B': float(90.0),
    'C': float(80.0),
    'D': float(70.0),
    'F': float(60.0)
}

def get_summary_score(filename):
    '''Makes a dict with ID, Boro, and Grade from CSV file'''

    inspect = open(filename)
    reports = inspect.readline()
    summary = {}

    for eachline in reports:
        info = reports.split(',')
        idnum = info[0]
        boro = info[1]
        grade = info[10]

        for thegrade in eachline:
            if thegrade is 'P' or '' or 'GRADE':
                continue
            summary[idnum] = (boro, grade)
            return summary
        inspect.close()

            # for boro in summary
            #     boro.count('Manhattan')
            #     boro.count('Bronx')
            #     boro.count('Staten Island')
            #     boro.count('Queens')
            #     boro.count('Brooklyn')
print get_summary_score('inspection_results.csv')
'''x = set(x)
y = set(y)
y.difference(x) # will return whats different in the sets'''