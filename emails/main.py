#!/usr/bin/env python

import sqlite3
import string
import csv
import random


def readAddresses(mailing):
    """Reads email addresses from a table.
    
    Updates the 'data' table from test.db with email addresses split into
    username, domain name, and the current day's date.
    
    Ignores duplicate email addresses.
    
    Args:
        none
    
    Returns:
        none
    """
    try:
        db = sqlite3.connect('test.db')
    except:
        print "Database path not found."
        
    cursor = db.cursor()

    with open(mailing, 'rb') as dataFile:
        mailingsTable = csv.reader(dataFile)
        for row in mailingsTable:
            mailingEntry = string.split(row[0], "@")
            cursor.execute("INSERT OR IGNORE INTO data VALUES(?, ?, date('now'))", mailingEntry)
            
    db.commit()
    db.close()
    
def updateCounts():
    """Updates a table containing counts of each domain.
    
    Updates the 'report' table in test.db with total counts of each domain name,
    new counts from within the last 30 days, and percent growth since the last 30 days.
       
    Args:
        none
    
    Returns:
        none
    """
    
    try:
        db = sqlite3.connect('test.db')
    except:
        print "Database path not found."

    cursor = db.cursor()
    totCounts = []
    newCounts = []
    
    for row in cursor.execute("SELECT domain, count(domain) FROM data GROUP by domain"):
        totCounts.append( row )
    
    for row in totCounts:
        cursor.execute("INSERT OR IGNORE INTO report (domain, totalCount) VALUES (?, ?)", row)
        cursor.execute("UPDATE report SET totalCount = ? WHERE domain LIKE ?", (row[1], row[0]))

    for row in cursor.execute("SELECT domain, count(domain) FROM data WHERE (date(dateVal)>= date('now', '-30 days')) GROUP by domain"):
        newCounts.append( row )
    
    for row in newCounts:
        cursor.execute("UPDATE report SET countPrev30 = ? WHERE domain LIKE ?", (row[1], row[0]))
    
    cursor.execute("UPDATE report SET growth = countPrev30/(totalCount - countPrev30)")

    db.commit()
    db.close()

def writeReport():
    """Writes report table from test.db to 'report.csv'.
    
    Writes domain name, total users, new users (in last 30 days), and percent growth
    for the top 50 largest growing domains, in descending order.
       
    Args:
        none
    
    Returns:
        none
    """

    try:
        db = sqlite3.connect('test.db')
    except:
        print "Database path not found."
    
    cursor = db.cursor()
    try:
        with open('report.csv', 'r+') as reportFile:
            reportFile.readline()
            newReport = csv.writer(reportFile)
            
            for row in cursor.execute("SELECT * FROM report ORDER BY growth DESC LIMIT 50"):
                newReport.writerow([row[0],row[1],row[2],row[3]*100])
        
        print "Report successfully written to file: report.csv"
    except:
        print "Report file not found."

    db.close()

#-----------------------
# Main program
#-----------------------
mailing = 'emails3.csv' # input mailing table, as comma-separated values

readAddresses(mailing)  # read mailings into database
updateCounts()          # count total and new usernames of each domain
writeReport()           # print report for top 50 domains, by percent growth