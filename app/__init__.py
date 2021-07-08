from flask import Flask, render_template, request
from app.helper import * 
from time import time
# non ho capito perch'e  se cambio il nome qua
# gunicorn non mi capisce pi`u cosa sto provando a fare
# probabilmente sta nel comando gunicorn app:app
# che non ho cpaito il secondo app cosa sia.

app = Flask(__name__)

# Custom filter
# see here https://flask.palletsprojects.com/en/2.0.x/templating/#registering-filters
app.jinja_env.filters["date_parser"] = date_parser

# Ensure responses aren't cached, for debuggin purposes
if app.debug:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# set environment variables and catch errors meanwhile
try:
    DATABASE = os.getenv("NOTION_DATABASE_ID")
    API_KEY = os.getenv("NOTION_KEY")
    VERSION = os.getenv("NOTION_VERSION")
except Exception as e:
    print(e)
    exit(1)


@app.route("/")
def index():

    # getting the stuff to fetch
    data = {"page_size": 5}
    pages = query(DATABASE, data)

    # mi creo una lista di pagine, che saranno delle cards dopo
    scrapped_pages = []

    for page in pages['results']:
        # sono le proprieta del database che ho deciso io!
        # quindi sono abbastanza sicuro che ci siano
        # quindi le tengo cosi
        tmp_dict = page['properties']
        tmp_dict['id'] = page['id']
        scrapped_pages.append(tmp_dict)
    
    return render_template("index.jinja", pages=scrapped_pages)
    

@app.route("/errore_interno")
def tmp():
    return render_template("error.html")


@app.route('/articles/<id>')
def article(id):
    # getting the stuff to fetch
    response = get_page_content(id)

    # TODO validare che esista sul serio la pagina
    return render_template("article.jinja", page=response)


# BIG TO DOS
# decidere la grafica del sito
# in particolare come si fa a creare un css template?

# creare database

# creare pagina base e decidere formato della landing page (come displayare tutti articoli e cose simili)
