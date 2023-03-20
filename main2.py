from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Привет, Flask!'

@app.route('/user/<int:user_id>/')
def user_profile(user_id):
    return "Провиль пользователя #{}".format(user_id)

@app.route('/books//<string:genre>/')
def books(genre):
    return "Все книги в{} категории".format(genre)

if __name__ == "__main__":
    app.run(debug=True)