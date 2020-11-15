from flask import Flask
from flask_restful import Api, Resource, reqparse
from mr_modeling.predictor.predictor import Predictor
import pickle

app = Flask(__name__)
api = Api(app)
#load model
predictor = pickle.load(open("/home/apuzyk/Projects/lb_model_api/predictor.p", 'rb'))


class PredictSentiment(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('query')
        super().__init__()
    
    def get(self):
        args = self.parser.parse_args()
        query = args['query']
        preds = predictor.get_prediction(query)

        return {'sentiment': preds}


api.add_resource(PredictSentiment, '/')


if __name__ == '__main__':
    app.run(debug=True)