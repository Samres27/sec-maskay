from flask import Flask, render_template, request, url_for, redirect
import json
import re, base64, subprocess

app = Flask(__name__)

### TOOLS SERVER
def dominio_valido(dominio):
    return re.match(r'^(?!-)[A-Za-z0-9-]{1,63}(?<!-)(\.(?!-)[A-Za-z0-9-]{1,63}(?<!-))*\.?[A-Za-z]{2,}$', dominio) is not None

def leerArchivo(archivo):
    data =[];
    with open(f"archivos/{archivo}") as f:
        for x in f:
            data.append(json.loads(x))
        
        return data
    
def escaneo(dominio):
    dirrecion = base64.b64encode(dominio.encode()).decode("utf-8")
    subfinder=subprocess.Popen(["./binarios/subfinder","-d", dominio, "-silent"], stdout=subprocess.PIPE)
    httpx = subprocess.Popen(["./binarios/httpx", "-silent","-status-code", "-title", "-tech-detect", 
                              "-server", "-ip","-cname" ,"-location" ,"-content-length" ,
                              "-web-server" ,"-no-color" ,"-json"], stdin=subfinder.stdout, stdout=subprocess.PIPE)
    subfinder.stdout.close()
    output, _ = httpx.communicate()
    with open(f"archivos/{dirrecion}", 'w') as guardar:
        guardar.write(output.decode())
    httpx.stdout.close()
    return dirrecion

### APP WEB
@app.route('/')
def index():
    return redirect("/escaneo")

@app.route('/escaneo')
def escaneoView():
    return render_template('escaneo/view.html')

@app.route('/escaneo/dominio', methods =['GET','POST'])
def escaneoDominio():
    if request.method == 'POST' :
        dominio = request.form.get("buscar_dominio")
        if dominio_valido(dominio): 
            dir= escaneo(dominio)
            return redirect(url_for('escaneoDominio', escan=dir))
        return redirect("/escaneo")
    elif request.method == 'GET':
        data=leerArchivo(request.args.get('escan', default="fee", type=str))
        return render_template('escaneo/show.html',d=data,tam=len(data))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)