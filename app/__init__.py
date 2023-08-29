from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://todo:553781@localhost:5432/postgres'



from app.routes import auth
app.register_blueprint(auth)