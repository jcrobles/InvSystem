from util           import Base
from sqlalchemy     import Column, Integer, String, ForeignKey, Float

class Item(Base):
    __tablename__ = 'Item'
    id 					= Column(Integer, primary_key = True)
    name 				= Column(String(100))
    num					= Column(String(100))
    quantity_on_hand 	= Column(Integer)
    reorder_quantity	= Column(Integer)
    reorder_point		= Column(Integer)
#    vendor 				= relationship('Vendor', backref='item')
#    offer 				= relationship('Offer', backref='item')
    
    def __init__(self, name, num, quantity_on_hand, reorder_quantity, reorder_point):
        self.name 				= name
        self.num 				= num
        self.quantity_on_hand 	= quantity_on_hand
        self.reorder_quantity	= reorder_quantity
        self.reorder_point		= reorder_point

class Vendor(Base):
    __tablename__ = 'Primary Vendor'
    id          = Column(Integer, primary_key = True)
    item_id		= Column(Integer, ForeignKey('Item.id'))
    name 		= Column(String(100))
    
    def __init__(self):
        self.name 		= name

class Offer(Base):
	__tablename__ = 'Offer'
	id 			= Column(Integer, primary_key = True)
	item_id		= Column(Integer, ForeignKey('Item.id'))
	quantity 	= Column(Integer)
	price 		= Column(Float)
    
	def __int__(self):
		self.quantity 	= quantity
		self.price 		= price

class UOM(Base):
    __tablename__ = 'UOM'
    id          = Column(Integer, primary_key = True)
    name		= Column(String(100))
    
    def __init__(self):
        self.name 		= name
