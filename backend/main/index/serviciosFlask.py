from flask import Flask, render_template
from flask import Flask, jsonify, render_template, request
from logueo import validar_correo_electronico
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

@app.route('/inicio')
def inicio():
    mail = request.form.get('email')
    password = request.form.get('password')
    if validar_correo_electronico(mail):
     return "Datos del formulario recibidos: Email={}, Password={}".format(mail, password)
    else:
      return print("error")

    
     
if __name__ == '__main__':
    app.run(debug=True)



