from flask import Flask

app = Flask(__name__)

@app.route('/sumar/<int:num1>/<int:num2>')
def sumar(num1, num2):
    resultado = num1 + num2
    return f'El resultado de la suma de {num1} y {num2} es: {resultado}'

@app.route('/restar/<int:num1>/<int:num2>')
def restar(num1, num2):
    resultado = num1 - num2
    return f'El resultado de la resta de {num1} y {num2} es: {resultado}'

@app.route('/multi/<int:num1>/<int:num2>')
def multiplicar(num1, num2):
    resultado = num1 * num2
    return f'El resultado de la multiplicación de {num1} y {num2} es: {resultado}'

@app.route('/div/<int:num1>/<int:num2>')
def dividir(num1, num2):
    if num2 == 0:
        return 'Error: No se puede dividir por cero.'
    resultado = num1 / num2
    return f'El resultado de la división de {num1} y {num2} es: {resultado}'

@app.route('/')
def index():
    return '''
        <h1>Bienvenidos a la Calculadora de Python</h1>
        <p>Para sumar dos números, ingresa: <a href="/sumar/10/20">Sumar 10 y 20</a></p>
        <p>Para restar dos números, ingresa: <a href="/restar/10/20">Restar 10 y 20</a></p>
        <p>Para multiplicar dos números, ingresa: <a href="/multi/10/20">Multiplicar 10 y 20</a></p>
        <p>Para dividir dos números, ingresa: <a href="/div/10/20">Dividir 10 entre 20</a></p>
    '''

if __name__ == '__main__':
    app.run(debug=True)
