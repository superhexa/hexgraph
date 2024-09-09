from flask import Flask, render_template, request, redirect, url_for
from FlashSQL import Client
import uuid  

app = Flask(__name__)
db = Client('database.db')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_post', methods=['POST'])
def create_post():
    title = request.form.get('title')
    content = request.form.get('content')

    post_id = str(uuid.uuid4())
    db.set(post_id, {'title': title, 'content': content})

    return redirect(url_for('view_post', post_id=post_id))

@app.route('/post/<post_id>')
def view_post(post_id):
    post = db.get(post_id)
    if post:
        title = post['title']
        content = post['content']
        return render_template('post.html', title=title, content=content)
    else:
        return "Post not found", 404

if __name__ == '__main__':
    app.run(port=1030)
