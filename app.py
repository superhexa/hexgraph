from flask import Flask, render_template, request, redirect, url_for
from FlashSQL import Client
import uuid  
from datetime import datetime

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
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    db.set(post_id, {'title': title, 'content': content, 'timestamp': timestamp})

    return redirect(url_for('view_post', post_id=post_id))

@app.route('/post/<post_id>')
def view_post(post_id):
    post = db.get(post_id)
    post['views'] = post.get('views', 0) + 1; db.set(post_id, post)
    return render_template('post.html', title=post['title'], content=post['content'], timestamp=post['timestamp'], views=post['views']) if post else ("Post not found", 404)

if __name__ == '__main__':
    app.run(port=1020)
