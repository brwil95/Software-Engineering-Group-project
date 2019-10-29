import flask
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import os, request, apiCalls


app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    response = apiCalls.api()
    images = []
    for i in range(1, 7):
        images.append(response['hits'][i]['recipe']['image'])
    return render_template('index.html', image1=images[0], image2=images[1], image3=images[2], image4=images[3],
                           image5=images[4], image6=images[5])


@app.route('/recipes')  # , methods=['POST'])    -- **Waiting for questionnaire response**
# The API_Calls are shooting me with an error. Please advise on the modules that need to be installed to make it work properly.
def recipes():
    response = apiCalls.api()
    return render_template("response.html", response=response['hits'][0]['recipe']['url'])


@app.route('/quiz')
def questions():
    q1 = "Are you on a diet? If so which one"
    q2 = "Would you like recipes that are Gluten-free?"
    q3 = "Are you allergic to any food?"
    q4 = "What is your maximum calorie intake?"
    return flask.render_template(
        "quiz.html",
        question1=q1,
        question2=q2,
        question3=q3,
        question4=q4
    )
@app.route('/answers', methods=['POST'])
def user_answers():
    value = request.questions['value']
    return value





app.run(
    port=int(os.getenv('PORT', 8086)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)

if __name__ == '__main__':
    app.run(debug=True)
