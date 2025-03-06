from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models.book import Book, BookSchema
from app.models.user import User
from app.services.rate_limiter import rate_limit_book_routes
from app.utils.decorators import admin_required

book_bp = Blueprint('books', __name__)
book_schema = BookSchema()
books_schema = BookSchema(many=True)

@book_bp.route('', methods=['POST'])
@jwt_required()
@rate_limit_book_routes
def create_book():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    
    try:
        data = request.get_json()
        new_book = book_schema.load(data, session=db.session)
        new_book.user_id = current_user_id
        
        db.session.add(new_book)
        db.session.commit()
        
        return book_schema.jsonify(new_book), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@book_bp.route('', methods=['GET'])
@jwt_required()
@rate_limit_book_routes
def get_books():
    books = Book.query.all()
    return books_schema.jsonify(books)

@book_bp.route('/<int:book_id>', methods=['GET'])
@jwt_required()
@rate_limit_book_routes
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return book_schema.jsonify(book)

@book_bp.route('/<int:book_id>', methods=['PUT'])
@jwt_required()
@rate_limit_book_routes
def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    try:
        data = request.get_json()
        book_schema.load(data, instance=book, session=db.session)
        db.session.commit()
        return book_schema.jsonify(book)
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@book_bp.route('/<int:book_id>', methods=['DELETE'])
@jwt_required()
@rate_limit_book_routes
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    try:
        db.session.delete(book)
        db.session.commit()
        return '', 204
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400