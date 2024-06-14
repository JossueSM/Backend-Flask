from flask import Flask
from controllers.user_controller import user_blueprint
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)

app.register_blueprint(user_blueprint)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)