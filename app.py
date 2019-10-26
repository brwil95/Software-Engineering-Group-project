import flask, random, os, apiCalls, copy, render_templates

app = flask.Flask(__name__)

#hard coded questions
original_questions = {
    'is your diet':['Vegetarian','Vegan', 'Pescatarian', 'Keto', 'Paleo', 'Neither'],
    'do you prefer':['Dairy-free', 'Gluten-free', 'Soy-free', 'Wheat-free'],
    'are you health concerns':['Kidney friendly', 'Low potassium', 'Sugar-conscious', 'Kosher'],
    'kind of diet would you like':['Balanced', 'High-fiber', 'High-protein', 'Low-carb', 'Low-fat', 'Low-sodium'],
    'food product are you allergic too':['Tree-nut-free', 'Peanut-free', 'Mustard-free', 'Shellfish-free'],
    'is your maximum calorie intake':['1500', '1800', '2000', '2500'],
    'nutrients is most important for your diet': ['Carbs', 'Fiber', 'Sodium', 'Iron', 'Cholesterol', 'Protein']


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


@app.route('-')
def quiz():
    shuffled_questioins = shuffle(questions)
    for i in questions.keys():
        random.shuffle(questions[i])
    return render_template('index.html', q = shuffled_questioins, o = questions)



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

if __name__ == '__main__':
    app.run(debug=True)