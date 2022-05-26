#Importar librerias framework de Python
from turtle import position
from flask import Flask, render_template, request, redirect
#Intanciar a la aplicacion 
app = Flask(__name__)
#Arreglo que permite almacenar la lista
lista_Tareas = []

#Controlador de la ruta especifica
@app.route("/")

#Funcion que permite llamar a la paquina layout
def principal():
	return render_template("index.html", tareas=lista_Tareas)

#Define la ruta para el envio
@app.route("/enviar", methods=["GET", "POST"])

#Funciuon para enviar datos
def enviar():
	if request.method == "POST":
		tarea = request.form.get("Ingresar_tarea")
        
		
		lista_Tareas.append(tarea)
		
		return redirect("/")

#Define la ruta el borrado
@app.route("/borrar", methods=["GET", "POST"])

#Funciuon para el borrar datos
def borrar():
    if request.method == "POST":
        tarea = request.form.get("palabra")
        lista_Tareas.remove(tarea)
        return redirect("/")

#main del programa
if __name__ == "__main__":
	app.run(debug=True)
