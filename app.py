from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def render_start():
    return render_template('index.html')

@app.route('/game')
def render_game():
    return render_template('game.html')

if __name__=='__main__':
    app.run(debug=True)