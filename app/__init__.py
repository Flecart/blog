from flask import Flask, render_template, request
from app.helper import * 
from time import time
# non ho capito perch'e  se cambio il nome qua
# gunicorn non mi capisce pi`u cosa sto provando a fare
# probabilmente sta nel comando gunicorn app:app
# che non ho cpaito il secondo app cosa sia.

# da fare per usare flask run: 
#  export FLASK_APP=__init__.py  
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["date_parser"] = date_parser

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

# creare parser per permettere a matteo di scrifere su?
# sarebbe bello provare a fare compatibilit`a con word o docs

# creare database

# creare pagina base e decidere formato della landing page (come displayare tutti articoli e cose simili)
