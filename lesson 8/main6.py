from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('hello'))


@app.route('/hello')
def hello():
    return 'Hello Flask'


@app.route('/user/<user_id>/')
def user_profile(user_id):
    return "Profile page of user #{}".format(user_id)


@app.route('/books/<genre>/')
def books(genre):
    return "All Books in {} category".format(genre)


with app.test_request_context('/api'):
    print(url_for('index'))

with app.test_request_context('/api'):
    print(url_for('index', _external=True))

with app.test_request_context('/api'):
    print(url_for('books', genre='history', page=10, sort_by='date-published'))

if __name__ == "__main__":
    app.run(debug=True)
