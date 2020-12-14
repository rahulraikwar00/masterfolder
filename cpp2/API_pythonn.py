from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

name = {"rahul": {"age":	 }}
class HelloWorld(Resource):
	def get(self,name):
		return {"name":name}
	
#	def post(self):
#		return {"data": "data posted"}

api.add_resource(HelloWorld, "/helloworld/<string:name>")


if __name__ == "__main__":
	app.run(debug=True)
 

