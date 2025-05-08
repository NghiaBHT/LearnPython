from flask import Flask, jsonify, request

app = Flask(__name__)

# Dữ liệu mẫu giả lập
books = [
    {"id": 1, "title": "Clean Code", "author": "Robert C. Martin"},
    {"id": 2, "title": "Fluent Python", "author": "Luciano Ramalho"},
]

# GET /books
@app.route("/books", methods=["GET"])
def get_books():
    return jsonify(books), 200

# GET /books/<id>
@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if book:
        return jsonify(book), 200
    return jsonify({"error": "Book not found"}), 404

# POST /books
@app.route("/books", methods=["POST"])
def create_book():
    data = request.get_json()
    new_book = {
        "id": books[-1]["id"] + 1 if books else 1,
        "title": data["title"],
        "author": data["author"],
    }
    books.append(new_book)
    return jsonify(new_book), 201

# Khởi chạy server
if __name__ == "__main__":
    app.run(debug=True)
