from flask import Flask, render_template, Response
from json import dumps
from io import BytesIO
from zipfile import ZipFile


def create_app(test_config=None):
    app = Flask(__name__)

    @app.route('/test')
    def test():
        return render_template('download.html')
    
    @app.route('/download')
    def download():
        mem_io = BytesIO()
        with ZipFile(mem_io, 'w') as zf:
            zf.writestr('test.json', dumps({"test": 2}))
        mem_io.seek(0)
        return Response(mem_io,
                headers={"Content-Disposition":
                "attachment;filename=test.json"})

    return app
