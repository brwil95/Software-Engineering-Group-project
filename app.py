import flask
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import os, requests, apiCalls, json

app = Flask(__name__)
app.secret_key = "b'_5#y2LF4Q8znxec]/'"
Bootstrap(app)

stored = apiCalls.Queue()

@app.route('/')
def index():
    # todo figure out how to do one api call for these images
    response = apiCalls.api('breakfast', 'vegetarian', 'dairy-free', 'balanced', '2000')
    urls = []
    labels = []
    images = []
    for i in range(1, 7):
        labels.append(response['hits'][i]['recipe']['label'])
        urls.append(response['hits'][i]['recipe']['url'])
        images.append(response['hits'][i]['recipe']['image'])
    # Automatically set these images from the api, we cannot do too many api calls at once so I had to manually enter these images)
    return render_template('index.html',
                           image1=images[0],
                           image2=images[1],
                           image3=images[2],
                           image4=images[3],
                           image5=images[4],
                           image6=images[5],
                           url1=urls[0],
                           url2=urls[1],
                           url3=urls[2],
                           url4=urls[3],
                           url5=urls[4],
                           url6=urls[5],
                           label1=labels[0],
                           label2=labels[1],
                           label3=labels[2],
                           label4=labels[3],
                           label5=labels[4],
                           label6=labels[5],
                           )


@app.route('/recipes', methods=['POST'])
# The API_Calls are shooting me with an error. Please advise on the modules that need to be installed to make it work properly.
def recipes():
    if stored.not_empty():
        stored.remove_stored()

    user_response = flask.request.form
    print(user_response)
    stored.add_stored(user_response)
    response = apiCalls.api(user_response['food_type'], user_response['health_type'], user_response['healt'], user_response['diet'], user_response['calories'])#, user_response['calories'])
    dictionary_items = {}
    images = []
    if response['count'] == 0:
        flask.flash("No results to display, try different entry")
        return render_template("response.html", results=False)
    for i in range(1, 10):
        if response['hits'][i]['recipe']['url'] not in dictionary_items:
            dictionary_items[response['hits'][i]['recipe']['label']] = (response['hits'][i]['recipe']['url'], response['hits'][i]['recipe']['image'])
            images.append(response['hits'][i]['recipe']['image'])
    return render_template("response.html", results=True, response_list=dictionary_items, recipe_image=images, stored=user_response)

#todo make path for both login and blog

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/blog')
def blog():
    return render_template('blog-post.html')

# def stored_recipes(response):
#     print(response)
#     stored = response
#     return response

@app.route('/recipe/details', methods=['POST'])
def detail_view():
    user_choice = flask.request.form
    previous_data = stored.get_stored()
    response = apiCalls.specific_recipe(previous_data['food_type'], previous_data['health_type'], previous_data['healt'], previous_data['diet'], previous_data['calories'], user_choice['recipe'])
    for item in range(len(response['hits'])):
        if response['hits'][item]['recipe']['label'] == user_choice['recipe']:
            response_values = response['hits'][item]['recipe']
            break
    return render_template("recipe-details.html", name=response_values['label'], image=response_values['image'], url=response_values['url'], diet=response_values['dietLabels'], health=response_values['healthLabels'], ingredients=response_values['ingredientLines'])


# quiz questions
@app.route('/quiz')
def questions():
    q1 = "Are you on a diet? If so which one"#html health_type
    q2 = "Would you like recipes to be free of anything?"#html healt
    q3 = "How would you like your diet?"#html diet
    q4 = "What is your maximum calorie count?"#html calories
    q5 = "What type of food would you like?(chicken, chocolate chip cookies, bacon, etc.)" #html q


    return flask.render_template(
        "quiz.html",
        question1=q1,
        question2=q2,
        question3=q3,
        question4=q4,
        question5=q5
    )


# stores users answers
@app.route('/answers', methods=['POST'])
def user_answers():
    value = requests.questions['value']
    return value


app.run(
    port=int(os.getenv('PORT', 8086)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)

if __name__ == '__main__':
    app.run(debug=True)
