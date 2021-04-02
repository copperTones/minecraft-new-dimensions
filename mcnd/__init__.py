from flask import Flask, render_template, Response
from json import dumps


def create_app(test_config=None):
    app = Flask(__name__)

    @app.route('/test')
    def test():
        return render_template('download.html')
    
    @app.route('/download.json')
    def download():
        return Response(dumps({'test':1}),
                headers={"Content-Disposition":
                "attachment;filename=test.json"})

    return app
