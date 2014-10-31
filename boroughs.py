#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 1 Reading a CSV"""


import csv
import json


GRADES = {
    'A': float(1.0),
    'B': float(0.9),
    'C': float(0.8),
    'D': float(0.7),
    'F': float(0.6)
}


def get_summary_score(filename):
    '''Makes a dict with ID, Boro, and Grade from CSV file'''

    inspect = open(filename)
    report = csv.reader(inspect)
    # inspect.readline()
    summary = {}

    for line in report:
        # info = line.split(',')
        idnum = line[0]
        boro = line[1]
        grade = line[10]
        if grade == 'A' or 'B' or 'C' or 'D' or 'F':
            summary[idnum] = (boro, grade)
            # return summary
        else:
            continue
    # return summary
    inspect.close()

    byboro = {}
    mhscore = 0
    bxscore = 0
    siscore = 0
    qnscore = 0
    bkscore = 0

    for score in summary.itervalues():
        mh = score[1].count('MANHATTAN')
        bx = score[1].count('BRONX')
        si = score[1].count('STATEN ISLAND')
        qn = score[1].count('QUEENS')
        bk = score[1].count('BROOKLYN')

        if score[1] is 'MANHATTAN':
            mhscore += score[1]
        elif score[1] is 'BRONX':
            bxscore += score[1]
        elif score[1] is 'STATEN ISLAND':
            siscore += score[1]
        elif score[1] is 'QUEENS':
            qnscore += score[1]
        elif score[1] is 'BROOKLYN':
            bkscore += score[1]
        else:
            pass

        byboro = {
        'MANHATTAN': (mh, float(mhscore)/float(mh)),
        'BRONX': (bx, float(bxscore)/float(bx)),
        'STATEN ISLAND': (si, float(siscore)/float(si)),
        'QUEENS': (qn, float(qnscore)/float(qn)),
        'BROOKLYN': (bk, float(bkscore)/float(bk))
        }
    return byboro

# def get_market_density(filename):
#     '''docstring'''