from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# instantiate the app
app = Flask(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# SQLAlchemy配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://chenrui:Acr3711229,.@localhost/flaskvue'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 实例化SQLAlchemy对象
db = SQLAlchemy(app)

# 定义Book模型
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    read = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Book {self.title}>'

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/books', methods=['GET', 'POST'])
def all_books():
    if request.method == 'POST':
        post_data = request.get_json()
        title = post_data.get('title')
        author = post_data.get('author')
        read = post_data.get('read')

        # 创建新的Book对象并添加到数据库
        new_book = Book(title=title, author=author, read=read)
        db.session.add(new_book)
        db.session.commit()

        return jsonify({'message': 'Book added!'})

    else:
        # 获取所有书籍信息
        books = Book.query.all()

        # 将查询结果转换为字典列表
        books_dict_list = [{'id': book.id, 'title': book.title, 'author': book.author, 'read': book.read} for book in books]
        
        return jsonify({'books': books_dict_list})

@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    book = Book.query.get_or_404(book_id)

    if request.method == 'PUT':
        post_data = request.get_json()
        book.title = post_data.get('title')
        book.author = post_data.get('author')
        book.read = post_data.get('read')

        db.session.commit()

        return jsonify({'message': 'Book updated!'})

    if request.method == 'DELETE':
        db.session.delete(book)
        db.session.commit()

        return jsonify({'message': 'Book removed!'})

if __name__ == '__main__':
    app.run()
