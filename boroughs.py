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


def get_score_summary(filename):
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
        mhcount = score[1].count('MANHATTAN')
        bxcount = score[1].count('BRONX')
        sicount = score[1].count('STATEN ISLAND')
        qncount = score[1].count('QUEENS')
        bkcount = score[1].count('BROOKLYN')

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
    'MANHATTAN': (mhcount, float(mhscore)/float(mhcount)),
    'BRONX': (bxcount, float(bxscore)/float(bxcount)),
    'STATEN ISLAND': (sicount, float(siscore)/float(sicount)),
    'QUEENS': (qncount, float(qnscore)/float(qncount)),
    'BROOKLYN': (bkcount, float(bkscore)/float(bkcount))
    }
    return byboro
# print 


def get_market_density(filename):
    '''opens a JSON file type'''
    gmarketFile = open(filename, 'r')
    gmarketData = json.load(gmarketFile)
    gmarketDict = {}
    mhnum = 0
    bxnum = 0
    sinum = 0
    bknum = 0
    qnnum = 0

    for entry in gmarketData['data']:
        boro = entry[8]
        boros = boro[:4]
        if boros is 'Manh':
            mhnum += 1
        elif boros is 'Bron':
            bxnum += 1
        elif boros is 'Broo':
            bknum += 1
        elif boros is 'Stat':
            sinum += 1
        elif boros is 'Quee':
            qnnum += 1

    # gmarketFile.close()

    gmarketDict = {
    u'STATEN ISLAND': sinum,
    u'BRONX': bxnum,
    u'BROOKLYN': bknum,
    u'MANHATTAN': mhnum,
    u'QUEENS': qnnum
    }

def correlate_data(restaurants, greenMarket, combined):
    '''putting the 2 things together'''
    restscores = get_score_summary(restaurants)
    gmarkets = get_market_density(greenMarket)
    bothScores = {
    'BRONX': (restscores, gmarkets),
    'MANHATTAN': (restscores, gmarkets),
    'BROOKLYN': (restscores, gmarkets),
    'QUEENS': (restscores, gmarkets),
    'STATEN ISLAND': (restscores, gmarkets)
    }
    json.dump(bothScores, combined)