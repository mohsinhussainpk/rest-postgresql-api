from flask import request
from flask_restful import Resource
from Model import db, Tasks, TaskSchema

categories_schema = TaskSchema(many=True)
category_schema = TaskSchema()

 class TaskResource(Resource):
    def get(self):
        tasks = Tasks.query.all()
        tasks = tasks_schema.dump(tasks).data
        return {'status': 'success', 'data': categories}, 200


    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = category_schema.load(json_data)
        if errors:
            return errors, 422
        category = Tasks.query.filter_by(title=data['title']).first()
        if category:
            return {'message': 'Category already exists'}, 400
        category = Category(
            title=json_data['title']
            )

        db.session.add(category)
        db.session.commit()

        result = category_schema.dump(category).data

        return { "status": 'success', 'data': result }, 201
