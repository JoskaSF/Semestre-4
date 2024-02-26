class Persona{
    constructor(nombre, direccion, telefono, edad){
        this.nombre = nombre
        this.direccion = direccion
        this.telefono = telefono
        this.edad = edad
    }
}

function ningunCampoVacio(nombre, direccion, telefono, edad){
    if(nombre == "" || direccion == "" || telefono == "" || edad == ""){
        console.log("Se debe llenar todos los campos de informacion.")
        return false;
    }
    return true;
}

function verificarEdadNumero(edad){
    if(!isNaN(edad)){
        return true;
    } else {
        console.log("La edad debe ser un numero.")
        return false;
    }
}

function promedioEdad() {
    let promedioEdad = 0;
    personas.map((persona) => {
        promedioEdad += parseInt(persona.edad);
    });

    promedioEdad = promedioEdad / personas.length;
    console.log(`El promedio de edad de las personas es ${promedioEdad}`);
}

function mostrarNombres(){
    const nombres = personas.map(persona => persona.nombre)
    const nombresOrdenados = nombres.sort()
    console.log("Las personas registradas son:")
    const nombresMayusculas = nombresOrdenados.map((nombre) => nombre.toUpperCase())
    nombresMayusculas.map((nombresMayusculas) => {
        console.log(nombresMayusculas)
    })
}

const personas = []

while(personas.length < 5){
    let nombre = prompt(`Nombre (Sin apellidos) de la persona ${personas.length + 1}:`)
    let direccion = prompt(`Direccion de la persona ${personas.length + 1}:`)
    let telefono = prompt(`Telefono de la persona ${personas.length + 1}:`)
    let edad = prompt(`Edad de la persona ${personas.length + 1}:`)
    
    if(ningunCampoVacio(nombre, direccion, telefono, edad)){
        if(verificarEdadNumero(edad)){
            personas.push(new Persona(nombre, direccion, telefono, edad))
        }
    } 
}
promedioEdad()
mostrarNombres()