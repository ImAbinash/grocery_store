
from flask import jsonify, request, g, url_for, current_app
from .. import db
from ..models import Item
from . import api

@api.route('/item/<int:id>')
def get_item(id):
    item = Item.query.get_or_404(id)
    return jsonify(item.to_json())


@api.route('/item/', methods=['POST'])
def new_item():
    params = request.json
    item = Item(item_id = params['item_id'],item_name= params['item_name'],item_group=params['item_group'],item_price=params['item_price'])
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_json()), 201, {"Message":"Successfully created!"}
