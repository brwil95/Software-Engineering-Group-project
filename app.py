import flask, random, os

app = flask.Flask(__name__)


@app.route('/')
def index():
    r = random.randint(1, 100)
    return flask.render_template("index.html", random_num=r)


app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)
