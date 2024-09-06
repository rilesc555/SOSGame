from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Set initial player to 'X'
    return render_template('tictactoe.html', current_player='X')

if __name__ == '__main__':
    app.run(debug=True)