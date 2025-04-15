from flask import Flask, render_template, request
import json

app = Flask(__name__)


def leerArchivo(archivo):
    data =[];
    with open(archivo) as f:
        for x in f:
            data.append(json.loads(x))
        a=open("salvada",'w')
        a.write(str(data))
        return data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/escaneo')
def escaneoView():
    return render_template('escaneo/view.html')

@app.route('/escaneo/dominio')#, methods =['POST'])
        
def escaneoDominio():
    data=leerArchivo('save.json')
    return render_template('escaneo/show.html',d=data,tam=len(data))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)