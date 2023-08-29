from flask import Blueprint,render_template,request,redirect, url_for
from app.models import Todo,db


auth=Blueprint("auth",__name__)

@auth.route('/')
def index():
    todos = Todo.query.all()

    return render_template('index.html',todos=todos)



@auth.route('/add',methods = ["POST"])
def add_todo():
    title=request.form.get("title")
    content=request.form.get("content")

    newTodo = Todo(title=title,content=content,complete=False)
    db.session.add(newTodo)
    db.session.commit()
    return redirect(url_for("index"))
    

@auth.route('/complete/<string:id>')
def completeTodo(id):
    todo=Todo.query.filter_by(id=id).first()
    if(todo.complete==False):
      todo.complete=True
    else:
      todo.complete=False

    db.session.commit()
    return redirect(url_for("index"))


@auth.route('/delete/<string:id>')
def deleteTodo(id):
   todo = Todo.query.filter_by(id=id).first()
   db.session.delete(todo)
   db.session.commit()

   return redirect(url_for("index"))

@auth.route('/detail/<string:id>')
def detailTodo(id):
   todo = Todo.query.filter_by(id=id).first()

   return render_template( "detail.html",todo=todo)

@auth.route('/create_todo')  #methods=['POST', 'GET']
def create_todo():
    todo = Todo(title='baslik', content='content',complate='denememe')
    db.session.add(todo)
    db.session.commit()
    return 'Todo created successfully'