from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app and configure the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'  # SQLite database
db = SQLAlchemy(app)

# Define the BlogPost model
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<Post {self.title}>'

# Home route to show all blog posts
# curl -v 127.0.0.1:5000
@app.route('/')
def home():
    posts = BlogPost.query.order_by(BlogPost.date_posted.desc()).all()  # Get all posts
    posts = [
        {'title': 'post1', 'date': '31-12-2024', 'content': 'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Libero eveniet ipsam eos unde, magnam minus consequatur ullam aliquam eaque vitae quo perspiciatis culpa impedit nisi distinctio deleniti laudantium vero provident.'},
        {'title': 'post2', 'date': '31-12-2024', 'content': 'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Libero eveniet ipsam eos unde, magnam minus consequatur ullam aliquam eaque vitae quo perspiciatis culpa impedit nisi distinctio deleniti laudantium vero provident.'},
        {'title': 'post3', 'date': '31-12-2024', 'content': 'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Libero eveniet ipsam eos unde, magnam minus consequatur ullam aliquam eaque vitae quo perspiciatis culpa impedit nisi distinctio deleniti laudantium vero provident.'},
    ]
    return render_template('index.html', posts=posts)

#@app.route('create')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create tables
    app.run(debug=True)