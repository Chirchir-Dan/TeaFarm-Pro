from flask import Blueprint, jsonify
from app import db
from app.models import Farmer

bp = Blueprint('main', __name__)

@bp.route('/test_db')
def test_db():
    try:
        # Example query to check if the database is accessible
        farmer_count = Farmer.query.count()
        return jsonify({'Total farmers': farmer_count})
    except Exception as e:
        return str(e)

def register_routes(app):
    app.register_blueprint(bp)
