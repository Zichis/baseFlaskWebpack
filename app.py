from flask import Flask, render_template
from flask_webpack.components.blog.blog import blog_bp
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)

app.register_blueprint(blog_bp, url_prefix="/blog")

@app.route('/')
def index():
    return render_template('index.html')