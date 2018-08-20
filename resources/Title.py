from flask import jsonify, request
from flask_restful import Resource
from Model import db, Title, TitleSchema

titles_schema = TitleSchema(many=True)
title_schema = TitleSchema()

class TitleResource(Resource):
    def get(self):
        titles = Title.query.all() 
        titles = titles_schema.dump(titles).data
        return {"status":"success", "data":titles}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = title_schema.load(json_data)
        if errors:
            return {"status": "error", "data": errors}, 422
        title = Title.query.filter_by(title=data['title']).first()
        if title:
            return {'status': 'error', 'message': 'title id not found'}, 400
        title = Title(
            title=json_data['title'],
            title_id = json_data['title_id'],
            description = json_data['description']
           
            )
        db.session.add(title)
        #db.session.add(description)
        #db.session.add(done)
        db.session.commit()

        result = title_schema.dump(title).data

        return {'status': "success", 'data': result}, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = title_schema.load(json_data)
        if errors:
            return errors, 422
        title = Title.query.filter_by(title=data['title']).first()
        if title:
            return {'message': 'Category does not exist'}, 400
        
        title = json_data['title']
        db.session.commit()

        result = title_schema.dump(title).data

        return { "status": 'success', 'data': result }, 204
