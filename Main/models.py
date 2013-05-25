from util import db

class Item(db.Model):
    __tablename__ = 'Item'
    id 					= db.Column(db.Integer, primary_key = True)
    name 				= db.Column(db.String(100))
    num					= db.Column(db.String(100))
    quantity_on_hand 	= db.Column(db.Integer)
    reorder_quantity	= db.Column(db.Integer)
    reorder_point		= db.Column(db.Integer)
    vendor 				= db.relationship('Vendor', backref='item')
    offer 				= db.relationship('Offer', backref='item')
    
    def __init__(self, name, num, quantity_on_hand, reorder_quantity, reorder_point):
        self.name 				= name
        self.num 				= num
        self.quantity_on_hand 	= quantity_on_hand
        self.reorder_quantity	= reorder_quantity
        self.reorder_point		= reorder_point

class Vendor(db.Model):
    __tablename__ = 'Primary Vendor'
    id          = db.Column(db.Integer, primary_key = True)
    item_id		= db.Column(db.Integer, db.ForeignKey('Item.id'))
    name 		= db.Column(db.String(100))
    
    def __init__(self):
        self.name 		= name

class Offer(db.Model):
	__tablename__ = 'Offer'
	id 			= db.Column(db.Integer, primary_key = True)
	item_id		= db.Column(db.Integer, db.ForeignKey('Item.id'))
	quantity 	= db.Column(db.Integer)
	price 		= db.Column(db.Float)
    
	def __int__(self):
		self.quantity 	= quantity
		self.price 		= price

class UOM(db.Model):
    __tablename__ = 'UOM'
    id          = db.Column(db.Integer, primary_key = True)
    name		= db.Column(db.String(100))
    
    def __init__(self):
        self.name 		= name
