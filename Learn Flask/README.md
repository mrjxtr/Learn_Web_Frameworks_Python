# Learning Flask Basics

## Summary

A basic summary of flask.

### 1. **Installation and Setup**

First, install Flask in your environment:

```bash
pip install Flask
```

Once Flask is installed, you can create your first Flask app.

### 2. **Basic Flask App**

Here's a basic "Hello World" app:

```python
from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route (URL endpoint) and its corresponding function
@app.route('/')
def hello():
    return "Hello, Flask!"

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

- **Flask instance**: `app = Flask(__name__)` creates a Flask app instance.
- **Route**: The `@app.route('/')` decorator maps the URL `/` to the function `hello()`, which returns a response when the user visits the URL.
- **Run**: `app.run(debug=True)` runs the app in debug mode, allowing for auto-reloads and better error messages during development.

### 3. **Routing and Dynamic URLs**

You can define routes that handle dynamic URLs. For example, creating a personalized greeting based on the URL:

```python
@app.route('/hello/<name>')
def hello_name(name):
    return f"Hello, {name}!"
```

- **Dynamic URL**: `<name>` captures part of the URL and passes it to the function as an argument.
- If you visit `/hello/Jester`, the app will return `"Hello, Jester!"`.

### 4. **HTTP Methods (GET and POST)**

Flask supports different HTTP methods (e.g., GET, POST). You can define which method a route accepts:

```python
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        return "Data submitted via POST!"
    return "Submit your data!"
```

- By default, routes only accept `GET` requests. To accept `POST` (and other methods), you need to specify it with the `methods` argument.

### 5. **Working with Forms**

To handle form data, you can use the `request` object:

```python
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return f"Logged in as: {username}"
    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit">
        </form>
    '''
```

- **GET and POST forms**: In this example, when the form is submitted via POST, Flask captures the `username` and `password` fields using `request.form`.

### 6. **Templates (Jinja2)**

Flask uses **Jinja2** as its templating engine. You can separate your HTML into a template file.

1. First, create a folder named `templates` in your project directory.
2. Create a `hello.html` file inside the `templates` folder:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Hello</title>
  </head>
  <body>
    <h1>Hello, {{ name }}!</h1>
  </body>
</html>
```

3. Now, render this template in your Flask app:

```python
from flask import render_template

@app.route('/greet/<name>')
def greet(name):
    return render_template('hello.html', name=name)
```

- **Rendering Templates**: `render_template` is used to load the HTML file and pass dynamic data into it using the `{{ }}` syntax from Jinja2.

### 7. **Static Files (CSS, JavaScript, Images)**

Flask serves static files from the `static` folder. Create a `static` folder in your project directory and place your CSS, JavaScript, or images there.

In your HTML, you can reference static files using `url_for`:

```html
<link
  rel="stylesheet"
  type="text/css"
  href="{{ url_for('static', filename='style.css') }}"
/>
```

- **CSS Example**: Place a file named `style.css` in the `static` folder. Then, use it in your HTML template.

### 8. **Flask Blueprints**

As your app grows, you might want to modularize your application using **Blueprints**. This helps you organize routes, static files, and templates into different sections.

1. Define a blueprint in a separate file, say `auth.py`:

```python
from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "Login page"
```

2. Register the blueprint in your main app file:

```python
from auth import auth

app = Flask(__name__)
app.register_blueprint(auth)
```

Now, you've organized your code into separate modules using blueprints.

### 9. **Handling JSON (for APIs)**

Flask makes it easy to work with JSON when building APIs:

```python
from flask import jsonify

@app.route('/api/data')
def api_data():
    data = {'name': 'Jester', 'age': 25}
    return jsonify(data)
```

- **JSON Response**: `jsonify` converts a Python dictionary into a JSON response, which is useful when building APIs.

### 10. **Database Integration (Flask-SQLAlchemy)**

For database integration, you can use **Flask-SQLAlchemy**, an extension that adds support for **SQLAlchemy**, a popular ORM (Object Relational Mapper).

1. Install Flask-SQLAlchemy:

```bash
pip install Flask-SQLAlchemy
```

2. Configure your database and model in your app:

```python
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

# Creating tables
with app.app_context():
    db.create_all()

# Inserting a new user
new_user = User(username='Jester')
db.session.add(new_user)
db.session.commit()
```

- **Database Setup**: SQLAlchemy helps you define models (tables) as Python classes and interact with the database using high-level Python code.

### 11. **Error Handling**

You can handle errors like 404 (Page Not Found) with custom error pages:

```python
@app.errorhandler(404)
def page_not_found(e):
    return "Page not found!", 404
```

### 12. **Testing Flask Applications**

Flask comes with a built-in test client, which makes testing easy:

```python
import unittest

class FlaskTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
```

This sets up basic unit tests for your Flask app.

---

### Summary of What We've Covered

1. **Setting up Flask**.
2. **Routing and dynamic URLs**.
3. **Handling forms and HTTP methods**.
4. **Rendering templates with Jinja2**.
5. **Serving static files**.
6. **Organizing with Blueprints**.
7. **Building APIs and handling JSON**.
8. **Integrating databases with Flask-SQLAlchemy**.
9. **Error handling and custom error pages**.
10. **Testing Flask apps**.

Flask is a powerful framework with a lot of flexibility. You can start simple and scale it as your app grows! Let me know if you'd like more detail on any specific part.
