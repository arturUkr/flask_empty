import json

from src.infrastructure import DB

from flask import Flask, Response, render_template

from src.model import Restaurant


def setup_db():
    DB['restaurant'] = []


def create_app():
    setup_db()
    app = Flask(__name__, instance_relative_config=False)
    with app.app_context():
        return app


app = create_app()


@app.route('/restaurants', methods=['GET'])
def all_restaurants():
    data = json.dumps(DB['restaurant'])
    return Response(data, status=200)


@app.route('/restaurants', methods=['POST'])
def restaurants_create():
    DB['restaurant'].append(Restaurant("ABC", 5))
    return Response(status=200)


@app.route('/_health_check', methods=['GET'])
def check():
    resp = Response(status=200)
    return resp


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

