from flask import Flask, render_template

from controllers.bookings_controller import bookings_blueprint
from controllers.courses_controller import courses_blueprint
from controllers.members_controlller import members_blueprint 

app = Flask(__name__)

app.register_blueprint(bookings_blueprint) 
app.register_blueprint(courses_blueprint)
app.register_blueprint(members_blueprint) 

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)