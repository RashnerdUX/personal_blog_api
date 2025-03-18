from flask import Flask
from flask_restful import Api, Resource, reqparse, fields, marshal_with, abort
from flask_sqlalchemy import SQLAlchemy
import datetime
import json

#This creates the Flask app and provides the root of the application as its required argument
app = Flask(__name__)
#This initializes the API using the flask app as its root
api = Api(app)
#This configures the app to store the location for the SQLite database as this root location
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
#This initialises the SQL Alchemy database and sets the above as its location. It can be anything. It's a temporary space
db = SQLAlchemy(app)

#The Reqparse object to ensure Post gets all data points
new_blog_post = reqparse.RequestParser(bundle_errors=True)
new_blog_post.add_argument(name="title", type=str, help="This blog has no title", required=True, location="json")
new_blog_post.add_argument(name="category", type=str, help="This blog has no category", required=True, location="json")
new_blog_post.add_argument(name="body", type=str, help="This blog has no body", required=True, location="json")
new_blog_post.add_argument(name="tags", type=list, help="This blog has no tags", required=True, location="json")

#This Reqparse object is to help with updating
update_blog_post = reqparse.RequestParser()
update_blog_post.add_argument(name="title", type=str, help="This blog has no title")
update_blog_post.add_argument(name="category", type=str, help="This blog has no category")
update_blog_post.add_argument(name="body", type=str, help="This blog has no body")
update_blog_post.add_argument(name="tags", type=list, help="This blog has no tags", location="json")

#This creates the Model class for the data to be stored in the Database
class BlogModel(db.Model):
    #This is how data is stored in the database. In rows and columns. Columns designate what each data should have
    id = db.Column(db.Integer, primary_key=True)
    #Primary key tells the database the unique identifier for queries
    date = db.Column(db.DateTime, nullable=True, default=datetime.datetime.now())
    title = db.Column(db.String, nullable=True)
    category = db.Column(db.String, nullable=True)
    body = db.Column(db.String, nullable=True)
    tags = db.Column(db.Text, nullable=True)

    @property
    def tags_list(self):
        return json.loads(self.tags) if self.tags else []

    @tags_list.setter
    def tags_list(self, value):
        self.tags = json.dumps(value)

    def __repr__(self):
        return f" The following blog post '{self.title}' was created by me on {self.date} in the {self.category} with the following tags - {self.tags}"

#This is where fields is used to define how to parse the resource object received from the database with Marshal module
blog_fields = {
    "id": fields.Integer,
    "date":fields.DateTime,
    "title":fields.String,
    "category":fields.String,
    "body":fields.String,
    "tags":fields.List(fields.String, attribute="tags_list")
}

class Blogpost_List(Resource):
    @marshal_with(blog_fields)
    def get(self):
        result = db.session.execute(db.select(BlogModel)).scalars().all()
        return result

    def post(self):
        args = new_blog_post.parse_args()
        print(args)

        tags = args.get("tags")
        if tags is not None:
            args["tags"] = json.dumps(tags)
        db.session.add(BlogModel(**args))
        db.session.commit()
        return {"message": "Blog post created successfully!"}, 201


class Blogpost(Resource):
    @marshal_with(blog_fields)
    def get(self, blog_id):
        result = db.session.get(BlogModel, blog_id)
        return result

    def put(self, blog_id):
        result = db.session.get(BlogModel, blog_id)
        args = update_blog_post.parse_args()

        if "tags" in args and isinstance(args["tags"], list):
            args["tags"] = json.dumps(args["tags"])

        #Check if the result exists and if it doesn't, a new entry is created
        if result is None:
            new_post = BlogModel(**args)
            new_post.id = blog_id
            db.session.add(new_post)
            db.session.commit()
            return {}, 201

        #This helps to update the database entry
        for key, value in args.items():
            if value is not None:
                #This is a built-in function that updates the attribute of the result object.
                setattr(result, key, value)
        db.session.commit()
        return {"message": "Blog post modified successfully!"}, 201

    def delete(self, blog_id):
        result = db.session.get(BlogModel, blog_id)
        db.session.delete(result)
        db.session.commit()
        return {"message": "Blog post deleted successfully!"}, 201

api.add_resource(Blogpost,'/blogpost/<blog_id>')
api.add_resource(Blogpost_List, '/')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
