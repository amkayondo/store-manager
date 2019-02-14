from flask_restful import Resource
from flask import jsonify, request
from ...v1.models.appmodels import products
from .check import CheckId


# Products View
class Products(Resource):
    def get(self):
        """Method to get all produts available"""
        if len(products) == 0:
            return jsonify({
                "message": "No Products available"
            })
        else:
            return jsonify({
             "message": products
            })
 


# Get Product by ID
class GetProduct(Resource):
    def get(self, p_id):
       x = CheckId(p_id, products, 'p_id')
       response = x.check_id()
       
       if response:
           return response

       return jsonify({
           "message": "Product Not Found"
       }) 