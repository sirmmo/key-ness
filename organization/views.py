from django.http import HttpResponse
from organization.models import *
from django.shortcuts import render_to_response

try:
	import json
except:
	import simplejson as json

def view_year(request, year):
	y = Year.objects.get(name = year)
	res = [{
		"section":str(s),
		'url':str(s.url()),
		'description':s.description
	} for s in y.sections.all()]
	return render_to_response('year.html', {
                'sections':res,
                'breadcrumbs':[{
                        "name":y.name,
                        "url":str(y.url())
                }]
        })

def view_section(request, year, section):
	y = Year.objects.get(name = year)
	s = SchoolSection.objects.get(year = y, suffix = section)
	res = [{
		"course":str(c),
		'url':str(c.url()),
		'description':c.description
	} for c in s.courses.all()]
	return render_to_response('section.html', {
                'courses':res,
                'breadcrumbs':[{
                        "name":y.name,
                        "url":str(y.url())
                },{
                        "name":s.name,
                        "url":str(s.url())
                }]
        })

def view_course(request, year, section, course):
	y = Year.objects.get(name = year)
	s = SchoolSection.objects.get(year = y, suffix = section)
	c = Course.objects.get(section = s, name = course)
	res = [{ "klass":str(k), 'url':str(k.url()), 'students':k.students.all().count(), 'teachers':k.teachers.all().count(), } for k in c.klasses.all()]
        return render_to_response('course.html', {
                "klasses":res,
                'breadcrumbs':[{
                        "name":y.name,
                        "url":str(y.url())
                },{
                        "name":s.name,
                        "url":str(s.url())
                },{
                        "name":c.name,
                        "url":str(c.url())
                }]
        })

def view_klass(request, year,section, course, klass):
	y = Year.objects.get(name = year)
	s = SchoolSection.objects.get(year = y, suffix = section)
	c = Course.objects.get(section = s, name = course)
	k = Klass.objects.get(course = c, name = klass)
	res = []
	for q in k.students.all():
		res.append({
			'type':"student",
			"name":str(q),
			#'url':str(q.url()),
			} )
	for q in k.teachers.all():
		res.append({
			'type':"teacher",
			"name":str(q),
			#'url':str(q.url()),
			} )

	return render_to_response('class.html', {
                'breadcrumbs':[{
                        "name":y.name,
                        "url":str(y.url())
                },{
                        "name":s.name,
                        "url":str(s.url())
                },{
                        "name":c.name,
                        "url":str(c.url())
                },{
                        "name":k.name,
                        "url":str(k.url())
                }]})
