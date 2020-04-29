#!/usr/bin/python3
import datetime
import os

UPDATED_FILENAME = '/tmp/updated.txt'

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    html = '<html><head><title>Hello from Flask!</title></head>'
    html = '%s<body><h1>Hello from Flask!</h1>' % html

    if os.path.exists(UPDATED_FILENAME):
        with open(UPDATED_FILENAME, 'r') as f:
            timestamp = f.read()
    else:
        timestamp = 'Never updated'

    html = '%s<h2>%s</h2></body></html>' % (html, timestamp)
    return html

@app.route('/update', methods=['POST'])
def update():
    with open('/tmp/updated.txt', 'wt') as f:
        f.write('Updated on %s UTC' % str(datetime.datetime.utcnow()))
    return '', 204

if __name__ == '__main__':
    app.run()