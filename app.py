import psycopg2
from flask import Flask
from psycopg2.extras import RealDictCursor

conn = psycopg2.connect(
    "host=movies dbname=movie user=movie password=movie",
    cursor_factory=RealDictCursor)
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello, World!"


   