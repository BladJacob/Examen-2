from flask import Flask, render_template, request

app = Flask(__name__)

# --- Rutas Informativas ---

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/empresa')
def empresa():
    return render_template('empresa.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')


# --- Rutas de Cálculo (POST) ---

@app.route('/compra', methods=['GET', 'POST'])
def compra():
    resultado = None
    if request.method == 'POST':
        try:
            cantidad = int(request.form.get('cantidad', 0))
            precio = float(request.form.get('precio', 0))
            
            subtotal = cantidad * precio
            descuento = 0
            
            # Regla: descuento 10% si subtotal > 1000
            if subtotal > 1000:
                descuento = subtotal * 0.10
            
            total = subtotal - descuento
            
            resultado = {
                'cantidad': cantidad,
                'precio': precio,
                'subtotal': f"{subtotal:.2f}",
                'descuento': f"{descuento:.2f}",
                'total': f"{total:.2f}"
            }
        except ValueError:
            resultado = {'error': 'Por favor, ingrese valores numéricos válidos.'}
            
    return render_template('compra.html', resultado=resultado)

@app.route('/salario', methods=['GET', 'POST'])
def salario():
    resultado = None
    if request.method == 'POST':
        try:
            horas = float(request.form.get('horas', 0))
            pago_hora = float(request.form.get('pago_hora', 0))
            
            horas_normales = min(horas, 40)
            horas_extra = max(0, horas - 40)
            
            pago_normal = horas_normales * pago_hora
            pago_extra = horas_extra * (pago_hora * 2) # Horas extra al doble
            
            total = pago_normal + pago_extra
            
            resultado = {
                'horas': horas,
                'pago_hora': pago_hora,
                'horas_extra': horas_extra,
                'total': f"{total:.2f}"
            }
        except ValueError:
            resultado = {'error': 'Por favor, ingrese valores numéricos válidos.'}
            
    return render_template('salario.html', resultado=resultado)

@app.route('/temperatura', methods=['GET', 'POST'])
def temperatura():
    resultado = None
    if request.method == 'POST':
        try:
            celsius = float(request.form.get('celsius', 0))
            
            fahrenheit = (celsius * 9/5) + 32
            kelvin = celsius + 273.15
            
            resultado = {
                'celsius': celsius,
                'fahrenheit': f"{fahrenheit:.2f}",
                'kelvin': f"{kelvin:.2f}"
            }
        except ValueError:
            resultado = {'error': 'Por favor, ingrese un valor numérico válido.'}
            
    return render_template('temperatura.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)