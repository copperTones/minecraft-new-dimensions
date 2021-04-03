from flask import Flask, render_template, Response, request
from json import dumps
import os
from io import BytesIO
from zipfile import ZipFile


def create_app(test_config=None):
    app = Flask(__name__)

    @app.route('/test', methods=('GET', 'POST'))
    def test():
        if request.method == 'GET':
            return render_template('download.html')

        mem_io = BytesIO()
        with ZipFile(mem_io, 'w') as zf:
            zf.writestr(os.path.join('New Dimensions', 'pack.mcmeta'),
                    dumps({"pack": {"description": request.form['description'], "pack_format": 6}}))
        mem_io.seek(0)
        return Response(mem_io,
                headers={"Content-Disposition":
                "attachment;filename=new_dimensions.zip"})
    
    return app
