from flask import Flask
app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/greet/<name>')
def greet(name):
    return f"Hello {name}"

@app.route('/profile/<userId>')
def profile(userId):
    return {
        'userId': userId,
        'name': "A user",
        'description': "Pretend this is a user"
    }

@app.route('/bye/<name>')
def bye(name):
    return f"Goodbye {name}!"