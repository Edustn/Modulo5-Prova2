from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)
banco1 = []
banco2 = []

@app.route('/ping')
def pong():
    banco1.append({
    "endereco":request.environ['REMOTE_ADDR'],
    "metodo": request.method,
    "hora":datetime.now()
    })
    return render_template('pong.html')

@app.route('/echo', methods=['GET','POST'])
def echo():
    banco1.append({
    "endereco":request.environ['REMOTE_ADDR'],
    "metodo": request.method,
    "hora":datetime.now()
    })

    campo1 = request.args.get('dados')
    banco2.append(f'resposta:{campo1}')     
    return banco2



     
@app.route('/dash')
def dash():
    return render_template('dash.html', logs=banco1)

@app.route('/info')
def info():
    return render_template('info.html')




if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)
