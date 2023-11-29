from flask import Flask, render_template

#framework

app = Flask(__name__, template_folder ="C:\\desarrollo\\proyectos\\lowMadeco\\frontend")

@app.route('/inicio')
def inicio():
    return render_template('index.html')

@app.route('/recuperarContrasenia')
def recuperarContrasenia():
    return render_template('recuperarContraseña.html')

@app.route('/cambioContrasenia')
def cambioContraseña():
    return render_template('cambioContraseña.html')


if __name__ == '__main__':
    app.run(debug=True)



