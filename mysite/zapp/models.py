from django.db import models

# Create your models here.



#Post table stores details about posts
class City(models.Model):
	#name
	city_name = models.CharField(max_length=300)

	def __unicode__(self):
		return self.city_name

class BTL(models.Model):
	#BTL name
	BTL_name = models.CharField(max_length=300)
	

	def __unicode__(self):
		return self.BTL_name

class item(models.Model):
	#item name
	item_name = models.CharField(max_length=300)
	#BTL
	item_BTL = models.ForeignKey(BTL, related_name='iten_BTL')

	def __unicode__(self):
		return self.item_name

class specs(models.Model):	
	#specs name
	specs_name = models.CharField(max_length=300)	
	#item
	specs_item = models.ForeignKey(item, related_name='specs_item')
	#available quantity
	specs_qty = models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.specs_name

class Language(models.Model):
	#name
	lang_name = models.CharField(max_length=300)
	
	def __unicode__(self):
		return self.lang_name

class Rtype(models.Model):
	#Type name
	rtype_name = models.CharField(max_length=300)
	

	def __unicode__(self):
		return self.rtype_name

class Post(models.Model):
	#instruct
	instruct_post = models.CharField(max_length=2000)
	#many to many relationship with the city
	city_post = models.ManyToManyField(City)
	#many to many relationship with the language
	lang_post = models.ManyToManyField(Language)
	#field to note the timestamp when the post was created
	created = models.DateTimeField(auto_now_add=True)
	#field to note the timestamp when the post was last updated
	updated = models.DateTimeField(auto_now=True)
	#BTL
	BTLtype_post = models.ForeignKey(BTL, related_name='BTLtype_post')
	#item
	item_post = models.ForeignKey(item, related_name='item_post', default='')
	#specs
	specs_post = models.ForeignKey(specs, related_name='specs_post', default='')
	#rtype
	rtype_post = models.ForeignKey(Rtype, related_name='rtype_post')
	#requested quantity
	qty_post = models.IntegerField(default=0)
	#email
	email_post = models.EmailField(max_length=254,default='')
	
	def __unicode__(self):
		return self.id




