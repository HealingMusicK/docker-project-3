# Product Service

# Import framework
from flask import Flask
from flask_restful import Resource, Api

# Instantiate the app
app = Flask(__name__)
api = Api(app)

class Product(Resource):
    def get(self):
        return {
            'products': ['[핫딜] 핫 스파이시 치킨 : 7950원 -> 4770원!!', '[삼원가든] 등심 불고기 : 19000원 -> 15200원', '제철 맞은 우럭회 : 13000원 -> 10400원' ,'백종원의 만능 양념장 : 3840원', '깐마늘 : 2000원' ]
        }

# Create routes
api.add_resource(Product, '/')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
