from flask import Flask, make_response, redirect, abort, render_template

app = Flask(__name__, template_folder="templates")
app.debug = True

#Перехватичики запросов
@app.before_first_request
def before_first_request():
    print("before_first_request() called")

@app.before_request
def before_request():
    print("before_request() called")

@app.after_request
def after_request(response):
    print("after_request() called")
    return response

@app.errorhandler(404)
def http_404_handler(error):
    return "HTTP 404 Error Encountered", 404

@app.errorhandler(500)
def http_500_handler(error):
    return "HTTP 500 Error Encountered", 500

#Роуты
@app.route("/template")
def request_template():
    name, age, profession = "Net", 24, "Developer"
    template_context = dict(name = name, age = age, profession = profession)
    return render_template("index.html", **template_context)

@app.route("/net")
def request_still():
    print("index() called")
    return 'Testings Request Hooks'

@app.route("/netnet")
def request_abort():
    abort(404)

@app.route("/")
def http_404_handler():
    return make_response("404 Error", 400)

@app.route("/da")
def render_markdown():
    return "## Заголовки", 200, {'Content-Type': 'text/markdown'}

@app.route("/dada")
def render_location():
    return "", 302, {'location': 'http://127.0.0.1:5000/da'}

@app.route("/books/<int:number>")
def books(number):
    return "Все книги в {} категории".format(number)

@app.route('/transfer')
def transfer():
    return redirect("https://localhost:5000/books/1")

@app.route("/jornals/<int:number>")
def jornals(number):
    res = make_response("А все журналы лежат в актегории {}".format(number))
    res.headers["Content-type"] = "text/plain"
    res.headers["Server"] = "Foobar"
    res.set_cookie("favorite-color", "skyblue", 60)
    res.set_cookie("favorite-font", "sans-serif", 60)
    return res

if __name__ == "__main__":
    app.run()