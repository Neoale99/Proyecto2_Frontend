from flask import Flask, jsonify, request
from flask_cors import CORS 
from Persona import Persona
from Admin import Admin
from doctores import doctores
from Enfermeras import Enfermeras
from Medicamentos import Medicamentos
import json


Pacientes = []
Admon = []
app = Flask(__name__)
CORS(app)
@app.route("/", methods = ['GET'])
def paempezar():
    print("Omla")
  
    return("Persona.getNombre")

@app.route("/", methods = ['POST'])
def paprobar():
        print("Omla")
        objeto = {"Mensaje" : "Sise puede"}
        return(jsonify(objeto))

@app.route("/Personas", methods = ['GET'])
def prendpersona():
    global Pacientes
    Datitos = []
    for Persona in Pacientes:
            objeto = {
                'Nombre': Persona.getNombre,
                'Apellido': Persona.getApellido,
                'Edad': Persona.getEdad,
                'Fn': Persona.getfn,
                'Usuario': Persona.getusuario,
                'Sexo': Persona.getSexo,
                'Telefono': Persona.getTelefono,
                'Contra': Persona.getContra
                }
            Datitos.append(objeto)
    return(jsonify(Datitos))

@app.route('/Personas/<string:nombre>', methods=['GET'])

def ObtenerPersona(nombre): 
    global Pacientes
    for persona in Pacientes:
 
        if persona.getNombre() == nombre:
            
            objeto = {
            'Nombre': persona.getNombre(),
            'Apellido': persona.getApellido(),
            'Edad': persona.getEdad(),
            'fn': persona.getfn,
            'Usuario': persona.getusuario,
            'Sexo': persona.getSexo,
            'Telefono': persona.getTelefono,
            'Contra': persona.getContra        
            }
            return(jsonify(objeto))
      
    salida = { "Mensaje": "No existe el usuario con ese nombre"}

    return(jsonify(salida))

@app.route('/Admin/<string:usuario>/<string:contra>', methods=['GET'])
def Compararadmin(usuario,contra): 
    global Admon
    if "admin" == usuario and "1234" == contra:
        print("omla me quiemro mamtar")
            
        return ("Abner tengo amsiedad")
      
  

    return("Nombre: False")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 3000, debug = True)