from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    name = 'World'
    if request.method == 'POST':
        name = request.form['name']
    
    template = '''
    <!doctype html>
    <html>
    <head>
      <title>Hello App</title>
    </head>
    <body>
      <h1>Hello, {{ name }}!</h1>
      <form method="post">
        <input type="text" name="name" placeholder="Enter your name" />
        <input type="submit" value="Submit" />
      </form>
    </body>
    </html>
    '''
    return render_template_string(template, name=name)

if __name__ == '__main__':
    app.run(debug=True)