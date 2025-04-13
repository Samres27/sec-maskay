from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/escaneo')
def escaneoView():
    return render_template('escaneo/view.html')

@app.route('/escaneo/dominio', methods =['POST'])
        
def escaneoDominio():
    return render_template('escaneo/show.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)