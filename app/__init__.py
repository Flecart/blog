from flask import Flask, render_template, request

# non ho capito perch'e  se cambio il nome qua
# gunicorn non mi capisce pi`u cosa sto provando a fare
# probabilmente sta nel comando gunicorn app:app
# che non ho cpaito il secondo app cosa sia.

# da fare per usare flask run: 
#  export FLASK_APP=__init__.py  
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    

@app.route("/tipoquesto")
def tmp():
    return render_template("error.html")


@app.route('/profile/<username>')
def lihat_profile(username):
    return "welcome to profile page %s" % username


# BIG TO DOS
# decidere la grafica del sito
# in particolare come si fa a creare un css template?

# creare parser per permettere a matteo di scrifere su?
# sarebbe bello provare a fare compatibilit`a con word o docs

# creare database

# creare pagina base e decidere formato della landing page (come displayare tutti articoli e cose simili)
