from flask import Blueprint, render_template, request, flash, redirect, url_for
from db import db
from models.book import Book

books_bp = Blueprint('books', __name__)

@books_bp.route('/')
def index():
    books = Book.query.all() 
    return render_template('books/book_index.html', books=books)

@books_bp.route('/reserve/<int:book_id>', methods=['GET', 'POST'])
def reserve(book_id):
    book = Book.query.get(book_id)

    if request.method == 'POST':
        if book.available:
            flash('Este livro já está reservado!', 'warning')
        else:
            book.available = True
            db.session.commit()
            flash(f'Livro "{book.title}" reservado com sucesso!', 'success')
        return redirect(url_for('books.index'))

    return render_template('books/book_reserve.html', book=book)

@books_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']

        if not title or not author:
            flash('Todos os campos são obrigatórios!', 'danger')
            return redirect(url_for('books.create'))

        new_book = Book(title=title, author=author)
        db.session.add(new_book)
        db.session.commit()
        flash('Livro criado com sucesso!', 'success')
        return redirect(url_for('books.index'))

    return render_template('books/book_create.html')