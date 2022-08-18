from flask import Flask, render_template
from flask_session import Session


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = 'filesystem'
app.config['SECRET_KEY'] = ''
Session(app)


@app.route('/home')
def home():
    return render_template("home.html")



if __name__ == "__main__":
    app.run(debug=True)