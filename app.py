from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import os, copy, random

original_questions = {
    'is your diet':['Vegetarian','Vegan', 'Pescatarian', 'Keto', 'Paleo', 'Neither'],
    'do you prefer':['Dairy-free', 'Gluten-free', 'Soy-free', 'Wheat-free'],
    'are you health concerns':['Kidney friendly', 'Low potassium', 'Sugar-conscious', 'Kosher'],
    'kind of diet would you like':['Balanced', 'High-fiber', 'High-protein', 'Low-carb', 'Low-fat', 'Low-sodium'],
    'food product are you allergic too':['Tree-nut-free', 'Peanut-free', 'Mustard-free', 'Shellfish-free'],
    'is your maximum calorie intake':['1500', '1800', '2000', '2500'],
    'nutrients is most important for your diet': ['Carbs', 'Fiber', 'Sodium', 'Iron', 'Cholesterol', 'Protein']
}

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recipes', methods=['POST'])
# The API_Calls are shooting me with an error. Please advise on the modules that need to be installed to make it work properly.
def recipes():
    response = apiCalls.api()
    return render_template("response.html", response=response['hits'][0]['recipe']['url'])



}

#returns a deepcopy of original_questions
questions = copy.deepcopy(original_questions)

#shuffles the questions around
def shuffle(q):
    selected_keys = []
    i = 0
    while i < len(q):
        current_question = random.choice(q.key())
        if current_question not in selected_keys:
            selected_keys.append(current_question)
            i += 1
        return selected_keys

<<<<<<< HEAD

=======
>>>>>>> 2d963e2dbc602193dbeab71039b495b6b3933220
@app.route('/quiz')
def quiz():
    shuffled_questioins = shuffle(questions)
    for i in questions.keys():
        random.shuffle(questions[i])
    return flask.render_template('index.html', q = shuffled_questioins, o = questions)



@app.route('/')
def index():
    return flask.render_template("index.html")


@app.route('/recipes', methods=['POST'])
def recipes():
    response = apiCalls.api()
    return flask.render_template("response.html", response=response['hits'][0]['recipe']['url'])
        # This should be changed >>Index.html<< is our homepage?
        # should we update to >>quizQuestions.html<< ?
    return render_template('index.html', q = shuffled_questioins, o = questions)




app.run(
    port=int(os.getenv('PORT', 8080)),
    port=int(os.getenv('PORT', 8081)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)

if __name__ == '__main__':
    app.run(debug=True)