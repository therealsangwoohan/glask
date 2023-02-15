from glask import Glask

from simple_custom_middleware import SimpleCustomMiddleware

app = Glask()

@app.route("/")
def home(request, response):
    response.body = "Hello from the HOME page"

@app.route("/about")
def about(request, response):
    response.body = "Hello from the ABOUT page"

@app.route("/hello/{name}")
def hello(request, response, name):
    response.body = f"Hello, {name}"

@app.route("/book")
def book(request, response):
    if request.method == "GET":
        response.body = "Books Page"
    elif request.method == "POST":
        response.body == "Endpoint to create a book"

app.add_middleware(SimpleCustomMiddleware)

from wsgiref.simple_server import make_server

server = make_server("localhost", 8000, app=app)
server.serve_forever()