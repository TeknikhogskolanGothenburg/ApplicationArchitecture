import json

from flask import Flask, render_template

from application.bll.records_controllers import get_all_records

app = Flask(__name__)


# WEB
@app.route('/')
def index():
    users = get_all_records()
    return render_template('index.html', users=users)


# API
@app.route('/api/v1_0/users')
def get_users():
    users = get_all_records()
    return json.dumps([user.to_dict() for user in users])


if __name__ == '__main__':
    app.run()
