from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Create an empty list to store the todo items
todo_list = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Add a new todo item
        todo_item = request.form['todo']
        todo_list.append(todo_item)
        return redirect('/')
    else:
        # Display all todo items
        return render_template('index.html', todo_list=todo_list)


@app.route('/check/<int:index>')
def check(index):
    # Check a todo item
    if index < len(todo_list):
        todo_list[index] = f'[X] {todo_list[index]}'
    return redirect('/')



app.run(port=8080, debug=True)


# from flask import Flask, request
# app = Flask(__name__, static_folder='.', static_url_path='')
# data = []

# @app.route('/')
# def index():
#     return app.send_static_file('index.html')

# @app.route('/append', methods=['GET', 'POST'])
# def append():
#     if request.method == 'POST':
#         data.append(request.form['message'])
#     return data
    
# app.run(port=8080, debug=True)

# from flask import Flask

# app = Flask(__name__, static_folder='.', static_url_path='')

# @app.route('/')
# def index():
#     return '<H1>Hello, Flask!</H1>'
    
# app.run(port=8080, debug=True)

