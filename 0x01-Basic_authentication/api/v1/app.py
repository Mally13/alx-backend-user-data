#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os
from api.v1.auth.basic_auth import Auth


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None
non_auth_list = [
    '/api/v1/status/',
    '/api/v1/unauthorized/',
    '/api/v1/forbidden/'
    ]


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def not_authorized(error) -> str:
    """ Not authorized handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """ Forbidden handler
    """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_request_handler():
    """Checks for authorization"""
    if not auth:
        return
    if not auth.require_auth(request.path, non_auth_list):
        return
    authorization_header = auth.authorization_header(request)
    if not authorization_header:
        abort(401)

    current_user = auth.current_user(request)
    if not current_user:
        abort(403)


if __name__ == "__main__":
    auth = getenv("AUTH_TYPE")
    if auth:
        auth = Auth()
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port, debug=True)
