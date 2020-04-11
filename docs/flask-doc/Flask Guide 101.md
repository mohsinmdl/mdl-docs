Flask Guide 101


Heroku setup
heroku toolbelt

## Creating Environment

### Conda Environment 
```commandline
conda create --name flask
activate flask
```


### Virtualenv Environment


#### Installing pip
`easy_install pip`

#### Installing Virtualenv
`pip install virtualenv`

#### Creating virtualenv
`virtualenv venv`

#### Activating virtualenv
`venv\Scripts\activate`


## Installing Flask

```commandline
pip install flask
```


## Sample App Flask

```python
# Basic flask application 
# hello.py

from flask import Flask
app=Flask(__name__)
 
 
 
 
@app.route('/')
def index():
        return '<h1>Learning Flask</h1>'
 
@app.route('/user/<name>')
def user(name):
        return 'Hello, %s' % format(name)
 


```


## Running Server

**For Windows**

```commandline
set Flask_App=hello.py
flask run
```

**For Linux**

```commandline
export Flask_App=hello.py
flask run
```

or for production
`flask run --host 0.0.0.0 --port 5200`


## Flask Commandline

```python
# filename: cli.py
import click

from flask import Flask
app = Flask(__name__)

@app.cli.command()
def sayhi():
    """Say Hello."""
    click.echo('Hello')

```


```commandline
set Flask_App=cli.py
run sayhi

```


##  Response Template

```python
# filename: food.py

from flask import Flask
from flask import request
app=Flask(__name__)

from flask import render_template

@app.route('/dinner/')
@app.route('/dinner/<food>')
def eat(food=None):
    return render_template('food.html', food=food)

```

```html
 <!–– filename: food.html -->
 <!–– Location: base_dir\templates\food.html -->


<!doctype html>
<title>What's for dinner?</title>
{% if food %}
  <h1>I want {{ food }}!</h1>
{% else %}
  <h1>Anything is fine!</h1>
{% endif %}

```

## Integrating Bootstrap

```python
# filename: food.py
# Location: base_dir\food.py
# Location: base_dir\templates\food.html

from flask import Flask
from flask import request
from flask_bootstrap import Bootstrap

app=Flask(__name__)

Bootstrap(app)
from flask import render_template

@app.route('/dinner/')
@app.route('/dinner/<food>')
def eat(food=None):
    return render_template('food.html', food=food, list=["pizza", "sushi", "quinoa"])
```




```html
<!-- filename: food.html -->
<!--  Location: base_dir\templates\food.html -->

{% extends "bootstrap/base.html" %}

{% block title %}What's for dinner?{% endblock %}

{% block content %}

<div class="container">

	{% if food %}
 	  <div class="alert alert-success">
  	  <h1>I want {{ food }}!</h1>
	{% else %}
	  <div class="alert alert-info">
	  <h1>Anything is fine!</h1>
	{% endif %}
	</div>
	{% if list %}
	<p>Now we'll loop through the list</p>
		<ul>
		{% for n in list %}
			<li><a href="/dinner/{{n}}">{{n}}</li>
		{% endfor %}
		</ul>
	{% endif %}
</div>

{% endblock %}

```

## Create Web Forms



```python
# filename: food.py
# Location: base_dir\hello.py
# Location: base_dir\templates\hello.html

from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, StringField, SubmitField
from flask_bootstrap import Bootstrap

# App config.
DEBUG = True
app = Flask(__name__)
Bootstrap(app)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'SuperSecretKey'
 
class NameForm(Form):
    name = TextField('Name:')
 
@app.route("/", methods=['GET', 'POST'])
def hello():
    form = NameForm(request.form)
 
    print (form.errors)
    if request.method == 'POST':
        name=request.form['name']
        print (name)
 
        flash('Hello ' + name)
         
    return render_template('hello.html', form=form)


```



```html
<!-- filename: food.html -->
<!--  Location: base_dir\templates\food.html -->

{% extends "bootstrap/base.html" %}
{% block title %} Form Demo {% endblock %}
{% block content %}
    <div class="container">
        <h1>Form Demo</h1>
    
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                <ul>
                    {% for message in messages %}
                        <li>{{ message[0] }}</li>
                    {% endfor %}
                </ul>
            {% endif %}
        {% endwith %}
        <form action="" method="post">
                <div class="form-group">
                    {{ form.name.label }} {{ form.name(class="form-control",placeholder="What's your name?") }}
                </div>
     
                <div class="input submit">
                    <button type="submit" class="btn btn-success">Submit</button>
                </div>
            </form>
    </div>
{% endblock %}

```

## CGPA Prediction System


``` python tab="cgpaPrediction.py"

# filename: cgpaPrediction.py
# Location: base_dir\cgpaPrediction.py
# Location: base_dir\templates\index.html

{!flask-doc/assets/python/cgpaPrediction.py!}

```

``` html tab="index.html"
<!-- filename: index.html -->
<!--  Location: base_dir\templates\index.html -->

{!flask-doc/assets/html/index.html!}

```



