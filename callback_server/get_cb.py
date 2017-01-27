#!/usr/bin/env python

from logging import getLogger, basicConfig, DEBUG

from flask import Flask, request
app = Flask(__name__)


@app.route("/cb", methods=['POST'])
def hello():
    logger = getLogger(__name__)
    logger.info("Got request with params %s", request.get_json())
    return "OK"

if __name__ == "__main__":
    basicConfig(level=DEBUG)
    app.run(host='0.0.0.0')
