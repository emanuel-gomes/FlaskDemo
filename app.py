from flask import Flask, render_template, request
app = Flask(__name__)

wsgi_app = app.wsgi_app

@app.route('/', methods=["GET", "POST"])
def hello():
    if request.method=="POST":
        file = request.files["file"]
        file.save(os.path.join("uploads", file.filename))
        return render_template("index.html", message="Enviado com Sucesso!")
    return render_template("index.html", message="Esperando Upload!")

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except Exception as e:
        PORT = 5555
    app.run(HOST, PORT)
