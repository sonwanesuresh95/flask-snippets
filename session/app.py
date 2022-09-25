from flask import Flask, request, session, render_template

app = Flask(__name__)
app.debug = True
app.secret_key = 'lionel messi'

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        # adding session variable
        session['username'] = request.form['username']
        return f"welcome {session['username']} !"+"<br><br><a href='/logout'>logout</a>"
    return render_template('t1.html')

@app.route('/logout')
def logout():
    # removing session variable
    session.pop('username', None)
    return "you are logged out, <a href='/login'>click here to login</a>"


if __name__ == "__main__":
    app.run()