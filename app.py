from boggle import Boggle
from flask import Flask, request, render_template, jsonify, session
from boggle import Boggle
import random

app = Flask(__name__)
app.config["SECRET_KEY"] = "secretkey"

boggle_game = Boggle()


def make_board(size=4):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    board = [[random.choice(letters) for _ in range(size)] for _ in range(size)]
    return board

if __name__ == '__main__':
    app.run(debug=True)

###################################################################################

@app.route("/")
def homepage():
    """Display the Boggle Board."""

    board = boggle_game.make_board()
    session['board'] = board
    highscore = session.get("highscore", 0)
    number_of_plays = session.get("number_of_plays", 0)

    return render_template("index.html", board=board, highscore=highscore, number_of_plays=number_of_plays)


@app.route("/check-word")
def check_word():
    """Check the words.txt dictionary."""

    word = request.args["word"]
    board = session["board"]
    response = boggle_game.check_valid_word(board, word)

    return jsonify({'result': response})


@app.route("/post-score", methods=["POST"])
def post_score():
    """Display the current score, number_of_plays, and high score."""

    score = request.json["score"]
    highscore = session.get("highscore", 0)
    number_of_plays = session.get("number_of_plays", 0)
    
    session['highscore'] = max(score, highscore)
    session['number_of_plays'] = number_of_plays + 1


    return jsonify(brokeRecord = score > highscore)




