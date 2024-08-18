from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Capturar lo que se escribió en el textbox
        user_input = request.form['input_text']
        # Respuesta predeterminada
        response = "chupame el pene"
        return redirect(url_for('response', message=response))
    return render_template('index.html')

@app.route('/response')
def response():
    message = request.args.get('message', 'chupame el pene')
    return f"""
    <html>
    <body>
        <h1>{message}</h1>
        <a href="/">Volver</a>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
