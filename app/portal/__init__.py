from flask import Flask, render_template, request
from portal.config import BaseConfig

app = Flask(__name__)
app.config.from_object(BaseConfig)


@app.route('/', methods=['GET'])
def index():
    return render_template(
        'index.html',
        ip_address=request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    )
