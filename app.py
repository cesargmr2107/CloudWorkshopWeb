import os
import pyodbc

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)


@app.route('/')
def index():

    # Connect to database
    db_connection_string = os.environ["SQLAZURECONNSTR_DB_CONNECTION_STRING"]
    db_connection = pyodbc.connect(db_connection_string)

    # Execute query
    cursor = db_connection.cursor()
    query = "SELECT [id], [description], [completed] FROM [dbo].[BUCKET_LIST_ITEMS]"
    cursor.execute(query)
    items = [row for row in cursor.fetchall()]

    # Render and return template
    return render_template('index.html', items=items)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/x-icon')


if __name__ == '__main__':
    app.run()
