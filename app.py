import flask, random, os, apiCalls

app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template("index.html")


@app.route('/recipes', methods=['POST'])
def recipes():
    response = apiCalls.api()
    return flask.render_template("response.html", response=response['hits'][0]['recipe']['url'])



app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)
