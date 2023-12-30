from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home(): 
    return render_template("home.html")

@app.route('/content')
def content(): 
    return render_template("content.html")

@app.route('/quiz')
def quiz(): 
    return render_template("quiz.html")

@app.route('/about')
def about(): 
    return render_template("about.html")

@app.route('/calculate_score', methods=['POST'])
def calculate_score():
    quiz_answers = {
        'quiz01': request.form['quiz01'],
        'quiz02': request.form['quiz02'],
        'quiz03': request.form['quiz03']
    }

    score = 0
    if quiz_answers['quiz01'] == 'aws01-04':
        score += 1
    if quiz_answers['quiz02'] == 'aws02-03':
        score += 1
    if quiz_answers['quiz03'] == 'aws03-02':
        score += 1

    return jsonify({'score': score})

if __name__ == '__main__': 
    app.run(host='0.0.0.0',port='5000',debug=True)
