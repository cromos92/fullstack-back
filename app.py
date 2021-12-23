"""importacion modulos iniciales"""
from flask import Flask, render_template, request,redirect
app = Flask(__name__)
@app.route("/",methods=["GET"])
def index():
    """ ruta index """
    return render_template('prepara_pedido.html')
@app.route("/pizza",methods=["GET","POST"])
def mostrar_ruta():
    """ obtiene campos y los muestra en otra pagina"""
    name = request.form.get("nombreCliente")
    surname = request.form.get("apellidosCliente")
    print(name,surname)
    return redirect ("http://localhost/templates/solicita_pedido")
if __name__ == '__main__':
    
