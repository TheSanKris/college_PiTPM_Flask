from flask import Flask

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    print(i)
    return 'Привет, МИР!'

@app.route('/cases/')
@app.route('/career/')
def career():
    return 'Мой послужной список:'

@app.route('/feedback/')
def feedback():
    return 'Станичка отзывов'

@app.route('/user/<int:id>/')
def user_profile(id):
    return "Профиль пользователя: #{}".format(id)

if __name__ == "__main__":
    app.run()
    