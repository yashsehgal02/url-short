from flask import *
import requests

app = Flask(__name__)

@app.route('/<string:id>')
def short(id):
    data = requests.get("https://docs.google.com/spreadsheets/d/1QAUlWAbMRemISJJe0Ujjk0vdtz5oq67ZOG-GWcRlcII/gviz/tq?tqx=out:csv&tq=SELECT *")
    data_format = data.text.split("\n")
    data_final = [i.split(",") for i in data_format]
    ids = []
    urls = []
    for i in data_final:
        ids.append(i[0].replace('"',''))

    for i in data_final:
        urls.append(i[1].replace('"',''))
    
    for i in ids:
        if i == id:
            return redirect(urls[ids.index(i)])

if __name__ == '__main__':
    app.run()

