from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.db import IntegrityError
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from zapp.models import *

import jinja2
from jinja2.ext import loopcontrols

jinja_environ = jinja2.Environment(loader=jinja2.FileSystemLoader(['ui']), extensions=[loopcontrols])

#Calls index page
def index(request):
	all_cities = City.objects.all()
	all_lang = Language.objects.all()
	all_rtype = Rtype.objects.all()
	all_BTL = BTL.objects.all()
	all_item = item.objects.all()
	all_specs = specs.objects.all()
	return HttpResponse(jinja_environ.get_template('index.html').render({"all_cities":all_cities,"all_lang":all_lang,"all_rtype":all_rtype,"all_BTL":all_BTL,"all_item":all_item,"all_specs":all_specs}))

#Called when a user clicks submit on new post form.    
@csrf_exempt                                                                      
def post_new(request):
	instruct_post = request.REQUEST['instruct']
	city_post = request.REQUEST['city']
	lang_post = request.REQUEST['lang']
	BTLtype_post = request.REQUEST['BTLtype']
	item_post = request.REQUEST['item']
	specs_post = request.REQUEST['specs']
	rtype_post = request.REQUEST['rtype']
	qty_post = request.REQUEST['qty']
	email_post = request.REQUEST['email']
	
   
	entry = Post(instruct_post = instruct_post,
		city_post = city_post,
		lang_post = lang_post,
		BTLtype_post = BTLtype_post,
		item_post = item_post,
		specs_post = specs_post,
		rtype_post = rtype_post,
		qty_post = qty_post,
		email_post = email_post,
				
				 )
	entry.save()
	return HttpResponse(jinja_environ.get_template('notice.html').render({"text":'Post created successfully.'}))

#Calls index page
def update(request):
	all_post = Post.objects.all()
	all_specs = specs.objects.all()
	
	return HttpResponse(jinja_environ.get_template('update.html').render({"all_post":all_post,"all_specs":all_specs}))


