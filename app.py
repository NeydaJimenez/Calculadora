from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/sumar/<int:num1>/<int:num2>')
def sumar(num1, num2):
    resultado = num1 + num2
    return render_template_string(
        titulo="Resultado de la Suma",
        mensaje=f"La suma de {num1} + {num2} = {resultado}",
        maximo=max(num1, num2),
        minimo=min(num1, num2)
    )

@app.route('/restar/<int:num1>/<int:num2>')
def restar(num1, num2):
    resultado = num1 - num2
    return render_template_string(
        titulo="Resultado de la Resta",
        mensaje=f"La resta de {num1} - {num2} = {resultado}",
        maximo=max(num1, num2),
        minimo=min(num1, num2)
    )

@app.route('/multi/<int:num1>/<int:num2>')
def multiplicar(num1, num2):
    resultado = num1 * num2
    return render_template_string(
        titulo="Resultado de la Multiplicación",
        mensaje=f"La multiplicación de {num1} x {num2} = {resultado}",
        maximo=max(num1, num2),
        minimo=min(num1, num2)
    )

@app.route('/div/<int:num1>/<int:num2>')
def dividir(num1, num2):
    if num2 == 0:
        return "<h2>Error: No se puede dividir por cero.</h2><hr><footer><strong>Neyda Nahomi Jiménez Martínez 5-D</strong></footer>"
    resultado = num1 / num2
    return render_template_string(
        titulo="Resultado de la División",
        mensaje=f"La división de {num1} ÷ {num2} = {resultado}",
        maximo=max(num1, num2),
        minimo=min(num1, num2)
    )

@app.route('/')
def index():
    return '''
        <h1>Bienvenidos a la Calculadora de Python</h1>
        <p>Para usar la calculadora, escribe <strong>127.0.0.1:5000</strong> en tu navegador.</p>
        <ul>
            <li><a href="/sumar/10/20">Sumar 10 + 20</a></li>
            <li><a href="/restar/10/20">Restar 10 - 20</a></li>
            <li><a href="/multi/10/20">Multiplicar 10 x 20</a></li>
            <li><a href="/div/10/20">Dividir 10 ÷ 20</a></li>
        </ul>
        <hr> 
        <footer>
           Neyda Nahomi Jiménez Martínez - 5°D 
        </footer>
    '''

if __name__ == '__main__':
    app.run(debug=True)
