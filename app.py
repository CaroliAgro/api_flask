from flask import Flask,  render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/tasks.db"
db = SQLAlchemy(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200))
    done = db.Column(db.Boolean)
    def json(self):
        return {
            "id": self.id,
            "content": self.content,
            "done": self.done
        }

@app.route('/todos')
def home():
    tasks = [u.json() for u in db.session.query(Task).all()]
    return jsonify(tasks)

@cross_origin()
@app.route('/todos', methods=['POST'])
def create():
    req = request.get_json()
    task = Task(content=req['content'], done=False)
    db.session.add(task)
    db.session.commit()
    return jsonify(task.json()), 201




if __name__== '__main__':
    app.run(debug=True)