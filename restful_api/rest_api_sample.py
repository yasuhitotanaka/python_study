# -*- coding: utf-8 -*-
import peewee
import json

from flask import Flask,jsonify,abort,make_response,request

db = peewee.PostgresqlDatabase("yasuhito")

class Products(peewee.Model):
    name = peewee.TextField()
    price = peewee.IntegerField()
    id = peewee.IntegerField()

    class Meta:
        database = db

api = Flask(__name__)


@api.route('/getproduct/<string:name>',methods=['GET'])
def get_product(name):
    try:
        product = Products.get(Products.name == name)
    except Products.DoesNotExist:
        abort(404)

    result = {
        "result":True,
        "data":{
            "name":product.name,
            "price":product.price,
        }
    }

    return make_response(jsonify(result))

@api.route('/product',methods=['GET'])
def get_products():
    try:
        products = Products.select()
    except Products.DoesNotExist:
        abort(404)

    product_list = list()
    for product in products:
        product_list.append({
            "name":product.name,
            "price":product.price,
        })

    result = {
        "result":True,
        "data":product_list
    }

    return make_response(jsonify(result))

@api.route('/product',methods=['POST'])
def post_product():
    dataDict = json.loads(request.data)
    try:
        data = Products.insert(name=dataDict["name"],price=dataDict["price"],id=dataDict['id'])
        data.execute()
        product = Products.get(Products.name == dataDict["name"])
    except Products.DoesNotExist:
        abort(404)

    result = {
        "result":True,
        "data":{
            "name":product.name,
            "price":product.price,
            "id": product.id
        }
    }

    return make_response(jsonify(result))

@api.route('/product/<string:name>',methods=['PUT'])
def put_product():
    dataDict = json.loads(request.data)
    try:
        data = Products.update(name=dataDict["name"],price=dataDict["price"],id=dataDict['id']).where(Products.name == dataDict["name"])
        data.execute()
        product = Products.get(Products.name == dataDict["name"])
    except Products.DoesNotExist:
        abort(404)

    result = {
        "result":True,
        "data":{
            "name":product.name,
            "price":product.price,
            "id": product.id
        }
    }

    return make_response(jsonify(result))

@api.route('/product/<string:name>',methods=['DELETE'])
def delete_product(name):
    try:
        data = Products.delete().where(Products.name == name)
        data.execute()
    except Products.DoesNotExist:
        abort(404)

    result = {
        "result":True,
    }

    return make_response(jsonify(result))


@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    api.run(host='0.0.0.0', port=3000)