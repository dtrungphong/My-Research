from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import pandas as pd
import numpy as np
import json

app = Flask(__name__)
api = Api(app)



class First_Phase(Resource):
    def get(self):
        data = pd.read_csv('./data_season.csv')
        
        data_api = {
            'rows':data.shape[0],
            'url' : ['ip:port/data-%s' % (i) for i in range(1,500)]
        }
        bug = {
            'access':['try-hard-%s' % (i) for i in range(160)],
            'data':data_api
        }
        
        return jsonify({"Layer":[bug]})


# Link 21
class Second_Phase_1(Resource):
    def get(self):
        data = pd.read_csv('./data_season.csv')
        data = data[:200].to_json(orient='records')
        real = {
            'data':[[json.loads(data)],0],
            'Find something':"Not easy"
            }
        return jsonify({"data":str(real)})

# Link 1969   
class Second_Phase_2(Resource):
    def get(self):
        data = pd.read_csv('./data_season.csv')
        data = data[200:1000].to_json(orient='records')
        real = {
            'data':[json.loads(data)],
            'Find something':"Look up"
            }
        return jsonify({"data":real})



# Link 1999 
class Second_Phase_3(Resource):
    def get(self):
        data = pd.read_csv('./data_season.csv')
        data = data[1000:2000].to_json(orient='records')
        real = {
            'data':[json.loads(data)],
            'Find something':"Look up"
            }
        return jsonify({"data":[str(real)]})


class Second_Phase_4(Resource):
    def get(self):
        third_api = {
            'rows':data.shape[0],
            'url' : ['ip:port/final-%s' % (i) for i in range(1,100)]
        }
        return jsonify({"data":third_api})
    
    
class Third_Phase(Resource):
    def get(self):
        data = pd.read_csv('./data_season.csv')
        data = data[2000:].to_json(orient='records')
        real = {
            'Find something':"Around hia",
            'data':[1,[0,0,json.loads(data)]]
            }
        return jsonify({"data":[str(real)]})

class Second_Phase_Fake(Resource):
    def get(self):
        real = {
            'data':[{'subject':'Introduction to DS',
                     'code': 'CS321'}]
            }
        return jsonify({"data":[str(real)]})

class Third_Phase_Fake(Resource):
    def get(self):
        data = pd.read_csv('./data_season.csv')
        data = data[2000:].to_json(orient='records')
        real = {'message': 'Last time I can try' }
        return jsonify({"data":[str(real)]})

# Link 1110
@app.route('/data-250')
def link_250():
    return """
    Hello world!
    
    This is my first web app!

    I'm so excited!
    """
@app.route('/try-hard-50')
def link_50():
    return """
    Hello world!
    
    This is my first web app!

    I'm so excited!
    """
    
# Link 999
class Troll(Resource):
    def get(self):
        data_api = {
            '?????????????????????????? ' : '😀😀😀😀😀'
        }
        return jsonify({"Layer":[data_api]})
api.add_resource(First_Phase, '/start')
api.add_resource(Second_Phase_1, '/data-21')
api.add_resource(Second_Phase_2, '/data-169')
api.add_resource(Second_Phase_3, '/data-121')
api.add_resource(Second_Phase_Fake, '/data-221')
api.add_resource(Second_Phase_4, '/data-131')
api.add_resource(Third_Phase, '/final-41')
api.add_resource(Third_Phase_Fake, '/final-40')

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=6510,threaded = True)
