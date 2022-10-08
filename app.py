from flask import Flask, render_template, request
from stories import story, stories

app = Flask(__name__)

@app.route('/')
def pick_a_story():
    return render_template('homepage.html', stories = stories)

@app.route('/form')
def enter_words():
    picked_story = int(request.args['new_story']) 
    return render_template('form.html', story = stories[picked_story], story_id = picked_story)

@app.route('/story')
def create_story():
    answers = request.args
    story_id = int(request.args['story_id'])
    story = stories[story_id]
    text = story.generate(answers)
    return render_template('story.html', created_story = text)
    