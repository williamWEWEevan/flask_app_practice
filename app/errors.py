from flask import render_template, jsonify
from werkzeug.exceptions import HTTPException
from app import app, db

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

# @app.errorhandler(Exception)
# def exeption_error(error):
#     code = 500
#     if isinstance(e, HTTPException):
#         code = e.code
#     return jsonify(error=str(e)), code
