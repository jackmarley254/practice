from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('to-do-list.html', todos=todos)