from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "<h1> Hello flask <h1> <p> Хрень </p> <table border='1 px solid black'> <tr><th> Фамилия </th> <th>Имя </th></tr></th> </tableborder>"


@app.route('/hello')
def hello():
    return "<h1> Доровеньку булы </h1> <p> Вторая строчка </p>"\
        "<h1> Hello flask <h1> <p> Хрень </p> <table border='1 px solid black'> <tr><th> Фамилия </th> <th>Имя </th></tr></th> </tableborder>"



if __name__ == '__main__':
    app.run(debug=True)
