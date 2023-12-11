from flask import Flask, render_template
from flask import Flask, jsonify, render_template, request
from logueo import validar_correo_electronico, validar_contrasenia
from connectionSQL import consultarEmail, consultarContrasenia
#framework

app = Flask(__name__, template_folder ="C:\\desarrollo\\proyectos\\lowMadeco\\frontend", static_folder = "C:\\desarrollo\\proyectos\\lowMadeco\\frontend\\staticFolder")

@app.route('/inicio')
def inicio():
    return render_template('index.html')

@app.route('/recuperarContrasenia')
def recuperarContrasenia():
    return render_template('recuperarContraseña.html')

@app.route('/cambioContrasenia')
def cambioContraseña():
    return render_template('cambioContraseña.html')

@app.route('/iniciarUsuario', methods=['POST'])
def login():
    data = request.get_json
    mail = data.__get__('email')
    password = data.__get__('contrasenia')
    mensaje = "hola"
    
    if mail and password is not None:
        mensaje = "ok"

    if validar_correo_electronico(mail):
       if validar_contrasenia(password):
        if consultarEmail(mail) and consultarContrasenia():   
         return mensaje == "ok"
    else:
     return mensaje == "error"
    

    
     
if __name__ == '__main__':
    app.run(debug=True)


