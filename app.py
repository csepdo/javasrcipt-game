from flask import Flask, render_template, request
import data_manager


app = Flask(__name__)


@app.route('/', methods=["GET"])
def hello_world():
    return render_template('index.html')


@app.route('/jatek')
def play_game():
    word_number = int(request.args.get('word-number', 10))
    selected_words = data_manager.get_random_words(word_number)
    return render_template('game.html', words=selected_words)


@app.route('/szavak')
def show_words():
    words_ly = data_manager.get_words_for_game("LY.txt")
    words_j = data_manager.get_words_for_game("J.txt")
    return render_template('words.html', words_ly=words_ly, words_j=words_j)


if __name__ == '__main__':
    app.run()
