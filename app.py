from flask import Flask, render_template

app = Flask(_name_)

@app.route('/')
def index():
    return render_template('listar.html')

app.run(host="0.0.0.0", port=5000)