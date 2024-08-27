from flask import Flask, render_template, request, redirect, url_for
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

def create_tables():
    db.create_all()

with app.app_context():
    create_tables()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        if user_input:
            new_user = User(input=user_input)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/entries')
def entries():
    users = User.query.all()
    return render_template('entries.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
