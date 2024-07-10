from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    # Simulate some to-do list items
    todos = ["Buy groceries", "Finish report"]
    return render_template('to-do-list.html', todos=todos)

if __name__ == '__main__':
    app.run(debug=True)
