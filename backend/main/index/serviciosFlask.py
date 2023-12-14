from flask import Flask, render_template
from flask import Flask, jsonify, render_template, request
from logueo import validar_correo_electronico, validar_contrasenia
from connectionSQL import consultarDominio
#framework

app = Flask(__name__, template_folder ="C:\\Desarrollo\\Mis Proyectos\\lowMadeco\\frontend\\HTML\\templateFiles", static_folder = "C:\\Desarrollo\\Mis Proyectos\\lowMadeco\\frontend\\HTML\\staticFiles")

@app.route('/inicio')
def inicio():
    return render_template('index.html')

@app.route('/recuperarContrasenia')
def recuperarContrasenia():
    return render_template('recuperarContraseña.html')

@app.route('/cambioContrasenia')
def cambioContraseña():
    return render_template('cambioContraseña.html')

@app.route('/bienvenida')
def bienvenida():
    return render_template('bienvenida.html')

@app.route('/iniciarUsuario', methods=['POST'])
def login():
    try:
        data = request.get_json()
        mail = data.get('email')
        password = data.get('contrasenia')
        mensaje = data.get('mensaje')

        if mail and password is not None:
            mensaje = "OK"

        if validar_correo_electronico(mail) and validar_contrasenia(password):
            if consultarDominio(mail, password) == True:
                mensaje == "OK"
            else:
                mensaje = "error"
        else:
            mensaje = "error"

        return jsonify({"mensaje": mensaje})
    
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"mensaje": "error"})

    
     
if __name__ == '__main__':
    app.run(debug=True)


