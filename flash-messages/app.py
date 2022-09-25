from flask import Flask, render_template, flash

app = Flask(__name__)
app.secret_key = 'messi'
app.debug = True

@app.route('/')
def index():
    flash("flash msg 1: wubba lubba dub dub")
    return render_template('index.html')


if __name__ == "__main__":
    app.run()