from flask import Response

from src import create_app

app = create_app()


@app.route('/_health_check', methods=['GET'])
def check():
    response = Response(status=200)
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
