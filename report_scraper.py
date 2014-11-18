#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import re
import csv
import requests
import os
#from pattern.web import URL
from bs4 import BeautifulSoup

from time import strptime, strftime
from string import split

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crimeDI.settings')
import django
django.setup()
import crimeDI.data.models as models

file_path = 'CPD5391.txt'
with open (file_path, "r") as livefile:
	data = livefile.read()

header_pattern = re.compile('\f.*\n.*')
strip_headers = re.sub(header_pattern,'', data)
#print strip_headers
#print strip_headers

pattern = re.compile('(?=(\d{5}\s+)((.|\n)*?)(LOCATION: )((.|\n)*?)(OCCURRED: )(.*?)(REPORTED: )((.|\n)*?)(OFFICER: )((.|\n)*?)(SUMMARY: )((.|\n)*?)((PROPERTY: )((.|\n)*?))?(PEOPLE: )((.|\n)*?)((ARRESTS: )((.|\n)*?))?(C13-\d{5}|\Z))')
#with properties.. (nonfunctional)
#(?=(\d{5}\s+)((.|\n)*?)(LOCATION: )((.|\n)*?)(OCCURRED: )(.*?)(REPORTED: )((.|\n)*?)(OFFICER: )((.|\n)*?)(SUMMARY: )((.|\n)*?)((PROPERTY: )((.|\n)*?))?(PEOPLE: )((.|\n)*?)((ARRESTS: )((.|\n)*?))?(C13-\d{5}|\Z))
#no property
#(?=(\d{5}\s+)((.|\n)*?)(LOCATION: )((.|\n)*?)(OCCURRED: )(.*?)(REPORTED: )((.|\n)*?)(OFFICER: )((.|\n)*?)(SUMMARY: )((.|\n)*?)(PEOPLE: )((.|\n)*?)((ARRESTS: )((.|\n)*?))?(C13-\d{5}|\Z))

incidents = pattern.findall(strip_headers)
#print incidents

j = 0


def create_incident(items):
	agency = models.Agency.objects.get(name="Champaign Police Department")
	code = items['code']
	datetime_occurred = items['datetime_occurred']
	datetime_reported = items['datetime_reported']
	summary = items['description']
	
	officer = models.Officer(name=items['reporting_officer'],agency=agency)
	officer.save()
	location = models.Location(address_name=items['location'], agency=agency, city="Champaign")
	location.save()

	properties = items['properties']
	arrests = items['arrests']

	newInc = models.Incident(agency=agency, code=code,
		summary=summary,  officer=officer, location_occurred=location)
	newInc.save()


for i in incidents:
	j += 1
	incidentItems = {}
	code = i[0].strip()
	incidentItems['code'] = code
	description = i[1].strip()
	incidentItems['description'] = description
	location = i[4].strip()
	incidentItems['location'] = location
	datetime_occurred = i[7].strip()
	incidentItems['datetime_occurred'] = datetime_occurred
	datetime_reported = i[9].strip()
	incidentItems['datetime_reported'] = datetime_reported
	reporting_officer = i[12].strip()
	incidentItems['reporting_officer'] = reporting_officer
	summary = i[15].strip()
	incidentItems['summary'] = summary
	properties = i[19].strip()
	incidentItems['properties'] = properties
	people = i[22].strip()
	incidentItems['people'] = people
	arrests = i[26].strip()
	arrests += i[27].strip()

	arrest_pattern = re.compile('(.*)(AGE: )(\d+)\s+(SEX: )(M|F)(\s+)(.*)\n(.*)(CHARGE: )(\w+)\s+(.*)\n(.*)(AT: )(.*)(BY: )(.*)')

	arrests_re = arrest_pattern.findall(arrests)
	incidentItems['arrests'] = arrests_re

	create_incident(incidentItems)
	
	x = 0
	for a in arrests_re:
		x = x+1


	# (C\d{2}-\d{5}\s+)(.*?)(\s{3,})(.*?)(LOCATION: )(.*?)(\n)

	#(C\d{2}-\d{5}\s+)(.*?)(\s{3,})(.*?)(LOCATION: )(.*?)(\n+)(\s+)(OCCURRED: )(.*?)(REPORTED: )(.*?)(\n+)(\s+)(OFFICER: )(.*?)(\n+)(\s+)(SUMMARY: )

	#

#Pe

#arrests
#(.*)(AGE: )(\d+)\s+(SEX: )(M|F)(\s+)(.*)\n(.*)(CHARGE: )(\w+)\s+(.*)\n(.*)(AT: )(.*)(BY: )(.*)

#how do we parse people?
#have Victim pattern. Repeat as necessary. Victim is mandatory at least once.


#((VICTIM)\s+AGE: (.*)SEX: (M|F)(.*))|(VICTIM|OFFENDER)(.*)

#Have offender hattern

#TODO:
#ARRESTS: (.*)(AGE: )(\d+)\s+(SEX: )(M|F)(\s+)(.*)\n(.*)(CHARGE: )(\w+)\s+(.*)\n(.*)(AT: )(.*)(BY: )(.*)
#PEOPLE: ((VICTIM)\s+AGE: (.*)SEX: (M|F)(.*))|(VICTIM|OFFENDER)(.*)
#PROPERTY: (DAMAGED|BURNED|STOLEN|LOST|NONE)(.*)(\d+)(.*)




'''

(?=
0	(\d{5}\s+)
1	(
2		(.|\n) *?)
3	(LOCATION: )
4	(
5		(.|\n) *?)
6	(OCCURRED: )
7	(.*?)
8	(REPORTED: )
9	(
10		(.|\n)*?)
11	(OFFICER: )
12	(
13		(.|\n)*?)
14	(SUMMARY: )
15	(
16		(.|\n)*?)
17	(
18		(PROPERTY: )
19		(
20			(.|\n)*?) )?
21	(PEOPLE: )
22	(
23		(.|\n)*?)
24	(
25		(ARRESTS: )
26		(
27			(.|\n)*?))?
28	(C13-\d{5}|\Z))?


'''