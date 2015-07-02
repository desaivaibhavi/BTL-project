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

class specs_order(models.Model):
	#each item will have a provision to be selected

	specs_org_1 = models.ForeignKey(specs, related_name='specs_org_1',default='')
	specs_org_2 = models.ForeignKey(specs, related_name='specs_org_2',default='')
	specs_org_3 = models.ForeignKey(specs, related_name='specs_org_3',default='')
	specs_org_4 = models.ForeignKey(specs, related_name='specs_org_4',default='')
	specs_org_5 = models.ForeignKey(specs, related_name='specs_org_5',default='')
	specs_org_6 = models.ForeignKey(specs, related_name='specs_org_6',default='')
	specs_org_7 = models.ForeignKey(specs, related_name='specs_org_7',default='')
	specs_org_8 = models.ForeignKey(specs, related_name='specs_org_8',default='')
	specs_org_9 = models.ForeignKey(specs, related_name='specs_org_9',default='')
	specs_org_10 = models.ForeignKey(specs, related_name='specs_org_10',default='')
	specs_org_11 = models.ForeignKey(specs, related_name='specs_org_11',default='')
	specs_org_12 = models.ForeignKey(specs, related_name='specs_org_12',default='')
	specs_org_13 = models.ForeignKey(specs, related_name='specs_org_13',default='')
	specs_org_14 = models.ForeignKey(specs, related_name='specs_org_14',default='')
	specs_org_15 = models.ForeignKey(specs, related_name='specs_org_15',default='')
	specs_org_16 = models.ForeignKey(specs, related_name='specs_org_16',default='')
	specs_org_17 = models.ForeignKey(specs, related_name='specs_org_17',default='')
	specs_org_18 = models.ForeignKey(specs, related_name='specs_org_18',default='')

	specs_1 = models.BooleanField(default=False)
	specs_2 = models.BooleanField(default=False)
	specs_3 = models.BooleanField(default=False)
	specs_4 = models.BooleanField(default=False)
	specs_5 = models.BooleanField(default=False)
	specs_6 = models.BooleanField(default=False)
	specs_7 = models.BooleanField(default=False)
	specs_8 = models.BooleanField(default=False)
	specs_9 = models.BooleanField(default=False)
	specs_10 = models.BooleanField(default=False)
	specs_11 = models.BooleanField(default=False)
	specs_12 = models.BooleanField(default=False)
	specs_13 = models.BooleanField(default=False)
	specs_14 = models.BooleanField(default=False)
	specs_15 = models.BooleanField(default=False)
	specs_16 = models.BooleanField(default=False)
	specs_17 = models.BooleanField(default=False)
	specs_18 = models.BooleanField(default=False)

	specs_1_qty = models.IntegerField(default=0)
	specs_2_qty = models.IntegerField(default=0)
	specs_3_qty = models.IntegerField(default=0)
	specs_4_qty = models.IntegerField(default=0)
	specs_5_qty = models.IntegerField(default=0)
	specs_6_qty = models.IntegerField(default=0)
	specs_7_qty = models.IntegerField(default=0)
	specs_8_qty = models.IntegerField(default=0)
	specs_9_qty = models.IntegerField(default=0)
	specs_10_qty = models.IntegerField(default=0)
	specs_11_qty = models.IntegerField(default=0)
	specs_12_qty = models.IntegerField(default=0)
	specs_13_qty = models.IntegerField(default=0)
	specs_14_qty = models.IntegerField(default=0)
	specs_15_qty = models.IntegerField(default=0)
	specs_16_qty = models.IntegerField(default=0)
	specs_17_qty = models.IntegerField(default=0)
	specs_18_qty = models.IntegerField(default=0)




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
	# BTLtype_post = models.ForeignKey(BTL, related_name='BTLtype_post')
	#item
	# item_post = models.ForeignKey(item, related_name='item_post', default='')
	#specs ordered for the post
	specs_post = models.ForeignKey(specs_order, related_name='specs_post', default='')
	#rtype
	rtype_post = models.ForeignKey(Rtype, related_name='rtype_post')
	#requested quantity
	# qty_post = models.IntegerField(default=0)
	#email
	email_post = models.EmailField(max_length=254,default='')

class Upost(models.Model):
	#post asscociated
	post_upost = models.ForeignKey(Post, related_name='post_upost', default='')
	#comment
	comment_upost = models.CharField(max_length=2000, default='')
	#status of the post
	status_upost = models.IntegerField(default=0)

	def __unicode__(self):
		return self.post_upost.email_post






