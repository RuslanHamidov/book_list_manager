from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

books = []
book_id_counter = 1


@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books', methods=['POST'])
def add_book():
    global book_id_counter
    book_title = request.json.get('title')
    if not book_title:
        return jsonify({'error': 'Title is required'}), 400
    new_book = {'id': book_id_counter, 'title': book_title}
    books.append(new_book)
    book_id_counter += 1
    return jsonify(new_book), 201

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return '', 204


if __name__ == '__main__':
    app.run(debug=True, port=5000)
