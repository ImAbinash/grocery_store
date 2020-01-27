from flask import current_app
from . import db

class ItemGroup:
    Fruits = 1
    Others = 2

class Item(db.Model):
    __tablename__='items'
    item_id = db.Column(db.Integer, primary_key=True)
    item_name =db.Column(db.String(60)) 
    item_group = db.Column(db.Integer)
    item_price = db.Column(db.Integer)
    # item_availabllity = db.Column(db.Boolean, default=False)


    def to_json(self):
        json_item = {
            item_name =db.Column(db.String(60)) 
            item_group = db.Column(db.Integer)
            item_price = db.Column(db.Integer)
        }
        return json_item