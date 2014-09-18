from app import db
from datetime import datetime

ROLE_USER = 0
ROLE_ADMIN = 1


class Group(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	create_at = db.Column(db.DateTime)
	update_at = db.Column(db.DateTime)
	name = db.Column(db.String(64), index = True, unique = True)
	description = db.Column(db.String(500))
	
	def __init__(self, name, description=None):
		self.name = name
		self.description = description
		self.create_at = datetime.utcnow()
		self.update_at = datetime.utcnow()

	def __repr__(self):
		return '<Group %r>' % (self.name)


class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	create_at = db.Column(db.DateTime)
	update_at = db.Column(db.DateTime)
	group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
	username = db.Column(db.String(64), index = True, unique = True)
	email = db.Column(db.String(120), index = True, unique = True)
	password = db.Column(db.String(64))
	is_active = db.Column(db.Boolean, default=False)
	group = db.relationship('Group', backref = db.backref('group', lazy = 'dynamic'))
	
	def __init__(self, group, username, email, password, is_active=False):
		self.username = username
		self.email = email
		self.password = password
		self.is_active = is_active
		self.group = group
		self.create_at = datetime.utcnow()
		self.update_at = datetime.utcnow()

	def __repr__(self):
		return '<User %r>' % (self.nickname)
		

class Article_class(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	parent_id = db.Column(db.Integer, db.ForeignKey('article_class.id'))
	name = db.Column(db.String(64), index = True, unique = True)
	keywords = db.Column(db.String(160))
	description = db.Column(db.String(500))
	posi = db.Column(db.Integer)
	create_at = db.Column(db.DateTime)
	update_at = db.Column(db.DateTime)
	parent = db.relationship('Article_class', backref = db.backref('parent_article_class'), remote_side=[id])

	def __init__(self, name, keywords=None, description=None, posi=0, parent_id=0):
		self.parent_id = parent_id 
		self.name = name
		self.keywords = keywords
		self.description = description
		self.posi = posi 
		self.create_at = datetime.utcnow()
		self.update_at = datetime.utcnow()

	def __repr__(self):
		return '<Article Class %r>' % (self.name)


class Article(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	keywords = db.Column(db.String(160))
	description = db.Column(db.String(500))
	posi = db.Column(db.Integer)
	create_at = db.Column(db.DateTime)
	title = db.Column(db.String(60))
	picture = db.Column(db.String(60))
	content = db.Column(db.Text)
	create_at = db.Column(db.DateTime)
	update_at = db.Column(db.DateTime)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	article_class_id = db.Column(db.Integer, db.ForeignKey('article_class.id'))
	article_class = db.relationship('Article_class', backref = db.backref('article_class', lazy = 'dynamic'))

	def __init__(self, article_class, title, content, picture=None, keywords=None, description=None, posi=0):
		self.title = title
		self.picture = picture
		self.content = content 
		self.article_class = article_class 
		self.keywords = keywords
		self.description = description
		self.posi = posi 
		self.create_at = datetime.utcnow()
		self.update_at = datetime.utcnow()

	def __repr__(self):
		return '<Article %r>' % (self.title)


class Product_class(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(64), index = True, unique = True)
	keywords = db.Column(db.String(160))
	description = db.Column(db.String(300))
	posi = db.Column(db.Integer)
	create_at = db.Column(db.DateTime)
	create_at = db.Column(db.DateTime)
	update_at = db.Column(db.DateTime)

	def __init__(self, name, keywords=None, description=None, posi=0):
		self.name = name
		self.keywords = keywords
		self.description = description
		self.posi = posi 
		self.create_at = datetime.utcnow()
		self.update_at = datetime.utcnow()

	def __repr__(self):
		return '<Product Class %r>' % (self.name)


class Product(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	keywords = db.Column(db.String(160))
	description = db.Column(db.String(500))
	posi = db.Column(db.Integer)
	create_at = db.Column(db.DateTime)
	name = db.Column(db.String(60))
	picture = db.Column(db.String(60))
	content = db.Column(db.Text)
	create_at = db.Column(db.DateTime)
	update_at = db.Column(db.DateTime)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	product_class_id = db.Column(db.Integer, db.ForeignKey('product_class.id'))
	product_class = db.relationship('Product_class', backref = db.backref('product_class', lazy = 'dynamic'))
	
	def __init__(self, product_class, name, title, content, picture=None, keywords=None, description=None, posi=0):
		self.name = name
		self.title = title
		self.picture = picture
		self.content = content 
		self.product_class = product_class 
		self.keywords = keywords
		self.description = description
		self.posi = posi 
		self.create_at = datetime.utcnow()
		self.update_at = datetime.utcnow()

	def __repr__(self):
		return '<Product %r>' % (self.title)


class Product_picture(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	keywords = db.Column(db.String(160))
	description = db.Column(db.String(500))
	posi = db.Column(db.Integer)
	create_at = db.Column(db.DateTime)
	title = db.Column(db.String(60))
	picture = db.Column(db.String(60))
	content = db.Column(db.Text)
	create_at = db.Column(db.DateTime)
	update_at = db.Column(db.DateTime)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
	product = db.relationship('Product', backref = db.backref('product', lazy = 'dynamic'))

	def __init__(self, product, title, content, picture=None, keywords=None, description=None, posi=0):
		self.title = title
		self.picture = picture
		self.content = content 
		self.product = product 
		self.keywords = keywords
		self.description = description
		self.posi = posi 
		self.create_at = datetime.utcnow()
		self.update_at = datetime.utcnow()

	def __repr__(self):
		return '<Product Pictures %r>' % (self.title)


class Picture_class(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(64), index = True, unique = True)
	keywords = db.Column(db.String(160))
	description = db.Column(db.String(500))
	posi = db.Column(db.Integer)
	create_at = db.Column(db.DateTime)
	create_at = db.Column(db.DateTime)
	update_at = db.Column(db.DateTime)

	def __init__(self, name, keywords=None, description=None, posi=0):
		self.name = name
		self.keywords = keywords
		self.description = description
		self.posi = posi 
		self.create_at = datetime.utcnow()
		self.update_at = datetime.utcnow()

	def __repr__(self):
		return '<Picture Class %r>' % (self.name)


class Picture(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	keywords = db.Column(db.String(160))
	description = db.Column(db.String(500))
	posi = db.Column(db.Integer)
	create_at = db.Column(db.DateTime)
	title = db.Column(db.String(60))
	picture = db.Column(db.String(60))
	content = db.Column(db.Text)
	create_at = db.Column(db.DateTime)
	update_at = db.Column(db.DateTime)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	picture_class_id = db.Column(db.Integer, db.ForeignKey('picture_class.id'))
	picture_class = db.relationship('Picture_class', backref = db.backref('picture_class', lazy = 'dynamic'))

	def __init__(self, picture_class, title, content, picture=None, keywords=None, description=None, posi=0):
		self.title = title
		self.picture = picture
		self.content = content 
		self.picture_class = picture_class 
		self.keywords = keywords
		self.description = description
		self.posi = posi 
		self.posi = posi 
		self.create_at = datetime.utcnow()
		self.update_at = datetime.utcnow()

	def __repr__(self):
		return '<Picture %r>' % (self.title)

class Config(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	create_at = db.Column(db.DateTime)
	update_at = db.Column(db.DateTime)
	sitename = db.Column(db.String(64), index = True, unique = True)
	keywords = db.Column(db.String(160))
	description = db.Column(db.String(500))
	domain = db.Column(db.String(100))
	company = db.Column(db.String(100))
	company_site = db.Column(db.String(100))
	linkman = db.Column(db.String(100))
	tel = db.Column(db.String(100))
	icp = db.Column(db.String(100))
	
	def __init__(self, sitename, keywords, description, domain, company, company_site, linkman, tel, icp):
		self.sitename = sitename
		self.keywords = keywords
		self.description = description
		self.domain = domain
		self.company = company
		self.company_site = company_site
		self.linkman = linkman
		self.tel = tel
		self.icp = icp
		self.description = description
		self.create_at = datetime.utcnow()
		self.update_at = datetime.utcnow()

	def __repr__(self):
		return '<Config %r>' % (self.sitename)

class Category(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	lft = db.Column(db.Integer)
	rgt = db.Column(db.Integer)
	layer = db.Column(db.Integer)
	title = db.Column(db.String(64), index = True, unique = True)
	keywords = db.Column(db.String(160))
	description = db.Column(db.String(500))
	picture = db.Column(db.String(60))
	content = db.Column(db.Text)
	create_at = db.Column(db.DateTime)
	update_at = db.Column(db.DateTime)

	def __init__(self, lft, rgt, layer, title, keywords=None, description=None, picture=None, content=None, status=1):
		self.lft = lft
		self.rgt = rgt
		self.layer = layer
		self.title = title
		self.keywords = keywords
		self.description = description
		self.picture = picture 
		self.content = content 
		self.create_at = datetime.utcnow()
		self.update_at = datetime.utcnow()

	def __repr__(self):
		return '<Class %r>' % (self.name)
		
class Member_group(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(64), index = True, unique = True)
	description = db.Column(db.String(500))
	create_at = db.Column(db.DateTime)
	update_at = db.Column(db.DateTime)
	
	def __init__(self, name, description=None):
		self.name = name
		self.description = description
		self.create_at = datetime.utcnow()
		self.update_at = datetime.utcnow()

	def __repr__(self):
		return '<Member Group %r>' % (self.name)


class Member(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	member_group_id = db.Column(db.Integer, db.ForeignKey('member_group.id'))
	username = db.Column(db.String(64), index = True, unique = True)
	email = db.Column(db.String(120), index = True, unique = True)
	password = db.Column(db.String(64))
	is_active = db.Column(db.Boolean, default=False)
	member_group = db.relationship('Member_group', backref = db.backref('member_group', lazy = 'dynamic'))
	create_at = db.Column(db.DateTime)
	update_at = db.Column(db.DateTime)
	
	def __init__(self, member_group, username, email, password, is_active=False):
		self.username = username
		self.email = email
		self.password = password
		self.is_active = is_active
		self.member_group = member_group
		self.create_at = datetime.utcnow()
		self.update_at = datetime.utcnow()

	def __repr__(self):
		return '<Member %r>' % (self.nickname)

class Data_model(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(64), index = True, unique = True)
	code = db.Column(db.String(64), index = True, unique = True)
	description = db.Column(db.String(500))
	is_active = db.Column(db.Boolean, default=False)
	create_at = db.Column(db.DateTime)
	update_at = db.Column(db.DateTime)
	
	def __init__(self, name, code, description, is_active=False):
		self.name = name
		self.code = code 
		self.description = description
		self.is_active = is_active
		self.create_at = datetime.utcnow()
		self.update_at = datetime.utcnow()

	def __repr__(self):
		return '<Model %r>' % (self.nickname)
