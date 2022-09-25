from flask import Flask, request, session, jsonify

app = Flask(__name__)
app.debug = True
app.secret_key = 'lionel messi'

@app.route('/login')
def login():
    # adding session variable
    session['username'] = 'surie'
    return f"welcome {session['username']} !"+"<br><br><a href='/logout'>logout</a>"

@app.route('/logout')
def logout():
    session.pop('username', None)
    return "you are logged out, <a href='/login'>click here to login</a>"


if __name__ == "__main__":
    app.run()