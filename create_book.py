from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://chenrui:Acr3711229,.@localhost/flaskvue'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# 定义Book模型类
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    read = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Book {self.title}>'

# 在应用上下文中创建所有尚未在数据库中存在的表
with app.app_context():
    db.create_all()

