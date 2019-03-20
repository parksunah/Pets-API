from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


def checkPostedData(postedData, fuctionName):
    
    if fuctionName == "add" or fuctionName == "substract" or fuctionName == "multiply":
        if "x" not in postedData or "y" not in pstedData:
            return 301

        else:
            return 200

    elif fuctionName == 'division':

        if "x" not in postedData or "y" not in postedData:
            return 301

        elif int(postedData["y"]) == 0:
            return 302

        else:
            return 200

class Add(Resource):
    def post(self):
        #If I am here, then the resource Add was requested using the method POST

        #Step 1: Get posted data:

        #Step 1b : Verify validity of posted data
        status_code = checkPostedData(postedData, "add")
        
        if status_code != 200:

            retMap = {
                'Message' : "An error happened",
                "Status Code" : status_code
            }
            return jsonify(retMap)

        postedData = request.get_json()

        #If I am here, then status_code == 200:
        x = postedData["x"]
        y = postedData["y"]

        #Step 2: Add the posted data
        ret = x + y
        retMap = {
            'Message' : ret,
            'Status Code' : 200
        }
        return jsonify(retMap)

class Substract(Resource):
    def post(self):
        #If I am here, then the resource Substract was requested using the method POST

        #Step 1: Get posted data:

        #Step 1b : Verify validity of posted data
        status_code = checkPostedData(postedData, "substract")
        
        if status_code != 200:

            retMap = {
                'Message' : "An error happened",
                "Status Code" : status_code
            }
            return jsonify(retMap)

        postedData = request.get_json()
         
        #If I am here, then status_code == 200:
        x = postedData["x"]
        y = postedData["y"]

        #Step 2: Substract the posted data
        ret = x - y
        retMap = {
            'Message' : ret,
            'Status Code' : 200
        }
        return jsonify(retMap)

class Multifly(Resource):
    def post(self):
        #If I am here, then the resource Multply was requested using the method POST

        #Step 1: Get posted data:

        #Step 1b : Verify validity of posted data
        status_code = checkPostedData(postedData, "multiply")
        
        if status_code != 200:

            retMap = {
                'Message' : "An error happened",
                "Status Code" : status_code
            }
            return jsonify(retMap)

        postedData = request.get_json()
         
        #If I am here, then status_code == 200:
        x = postedData["x"]
        y = postedData["y"]

        #Step 2: Multiply the posted data
        ret = x * y
        retMap = {
            'Message' : ret,
            'Status Code' : 200
        }
        return jsonify(retMap)

class Divide(Resource):
    def post(self):
        #If I am here, then the resource Divide was requested using the method POST

        #Step 1: Get posted data:

        #Step 1b : Verify validity of posted data
        status_code = checkPostedData(postedData, "division")
        
        if status_code != 200:

            retMap = {
                'Message' : "An error happened",
                "Status Code" : status_code
            }
            return jsonify(retMap)

        postedData = request.get_json()
         
        #If I am here, then status_code == 200:
        x = postedData["x"]
        y = postedData["y"]

        #Step 2: Divide the posted data
        ret = (x * 1.0) / y
        retMap = {
            'Message' : ret,
            'Status Code' : 200
        }
        return jsonify(retMap)


api.add_resource(Add, "/add")
api.add_resource(Substract, "/substract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/division")


@app.route('/')
def hello_world():
    return "Hello World"


if __name__ == '__main__':
    app.run(debug=True)
        