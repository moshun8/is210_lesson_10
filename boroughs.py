#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 1 Reading a CSV"""


import csv
import json


GRADES = {'A': float(1.0),
          'B': float(0.9),
          'C': float(0.8),
          'D': float(0.7),
          'F': float(0.6)}


def get_score_summary(filename):
    '''Makes a dict with ID, Boro, and Grade from CSV file'''

    inspect = open(filename)
    report = csv.reader(inspect, delimiter=',')
    # report = inspect.readlines()
    summary = {}

    for line in report:
        # info = line.split(',')
        idnum = line[0]
        boro = line[1]
        grade = line[10]
        # idnum = info[0]
        # boro = info[1]
        # grade = info[10]
        # if grade == 'P' or grade == '' or idnum == 'CAMIS':
        if grade is 'A' or grade is 'B' or grade is 'C' or \
           grade is 'D' or grade is 'F':
            summary[idnum] = (boro, grade)
            # return summary
        else:
            continue
    inspect.close()

    # byboro = {}
    mhscore = 0.0
    mhcount = 0
    bxscore = 0.0
    bxcount = 0
    siscore = 0.0
    sicount = 0
    qnscore = 0.0
    qncount = 0
    bkscore = 0.0
    bkcount = 0

    for score in summary.itervalues():
        # mhcount = score[1].count('MANHATTAN')
        # bxcount = score[1].count('BRONX')
        # sicount = score[1].count('STATEN ISLAND')
        # qncount = score[1].count('QUEENS')
        # bkcount = score[1].count('BROOKLYN')

        if score[0] is 'MANHATTAN':
            mhscore += GRADES[score[1]]
            mhcount += 1
        elif score[0] is 'BRONX':
            bxscore += GRADES[score[1]]
            bxcount += 1
        elif score[0] is 'STATEN ISLAND':
            siscore += GRADES[score[1]]
            sicount += 1
        elif score[0] is 'QUEENS':
            qnscore += GRADES[score[1]]
            qncount += 1
        elif score[0] is 'BROOKLYN':
            bkscore += GRADES[score[1]]
            bkcount += 1
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


def get_market_density(filename):
    '''opens a JSON file type'''
    gmarketfile = open(filename, 'r')
    gmarketdata = json.load(gmarketfile)
    # gmarketdict = {}
    mhnum = 0
    bxnum = 0
    sinum = 0
    bknum = 0
    qnnum = 0

    for entry in gmarketdata['data']:
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

    gmarketdict = {u'STATEN ISLAND': sinum,
                   u'BRONX': bxnum,
                   u'BROOKLYN': bknum,
                   u'MANHATTAN': mhnum,
                   u'QUEENS': qnnum}
    return gmarketdict


def correlate_data(restaurants, greenmarket, combined):
    '''putting the 2 things together'''
    restscores = get_score_summary(restaurants)
    gmarkets = get_market_density(greenmarket)
    # market saturation --> number of markets / number restaurants
    bxsat = float(gmarkets['BRONX']/restscores['BRONX'][0])
    qnsat = float(gmarkets['QUEENS']/restscores['QUEENS'][0])
    mhsat = float(gmarkets['MANHATTAN']/restscores['MANHATTAN'][0])
    bksat = float(gmarkets['BROOKLYN']/restscores['BROOKLYN'][0])
    sisat = float(gmarkets['STATEN ISLAND']/restscores['STATEN ISLAND'][0])
    
    bothscores = {'BRONX': (restscores['BRONX'][1], bxsat),
                  'MANHATTAN': (restscores['MANHATTAN'][1], mhsat),
                  'BROOKLYN': (restscores['BROOKLYN'][1], bksat),
                  'QUEENS': (restscores['QUEENS'][1], qnsat),
                  'STATEN ISLAND': (restscores['STATEN ISLAND'][1], sisat)}
    opencombined = open(combined, 'w')
    json.dump(bothscores, opencombined)