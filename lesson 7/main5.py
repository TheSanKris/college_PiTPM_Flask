from jinja2 import Template
from flask import Flask, render_template

print(Template("{{ 13 + 5 }}").render())
print(Template("{{ 13 ** 5 }}").render())

print(Template("{{ var }}").render(var="pitpm"))

print(Template("{{ var[2] }}").render(var=["qwe", 15, [1, 2, 3]]))
print(Template("{{ var['profession'] }}").render(var={'name': 'Pitirim', 'age': 18, 'profession': 'Programmer'}))


class Foo:
    def __str__(self):
        return "This is an instance of Foo class"


print(Template("{{ var }}").render(var=Foo()))


def foo():
    return "foo() called"


print(Template("{{ foo() }}").render(foo=foo))


class Foo:
    def __init__(self, i):
        self.i = i

    def do_something(self):
        return "do_something() called"


print(Template("{{ obj.i }}").render(obj=Foo(10)))
print(Template("{{ obj.do_something() }}").render(obj=Foo(10)))

app = Flask(__name__, template_folder="templates")


class User:
    def __init__(self, count):
        self.count = count


@app.route('/')
def index():
    context = dict(bookmarks=True, user=User(10), user_list=["user1", "user2", "user1232131231"])
    return render_template('index.html', **context)


@app.route('/home')
def home():
    return 'you are at home'


@app.route('/blog')
def blog():
    return 'you are in blog'


@app.route('/contact')
def contact():
    return 'it is your contacts'


if __name__ == "__main__":
    app.run(debug=True)
