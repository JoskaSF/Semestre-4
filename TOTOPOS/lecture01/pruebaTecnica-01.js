class Libro{
    constructor(titulo, autor, year, genero){
        this.titulo = titulo
        this.autor = autor
        this.genero = genero
        this.year = year
    }

    informacionTotalLibro (){
        // `` Templent stick. Cadenas o salidas de cadena en consola
        return `El libro se llama ${titulo} y lo escribio
        el autor ${autor} en ${year} y pertenece al genero ${genero}.` 
    }
}

const mostrarTodosLibros = () => {
    libros.map((libro) => {
        console.log("Libro: ",libro.titulo)
        console.log("   Autor: ",libro.autor)
        console.log("   Year: ",libro.year)
        console.log("   Genero: ",libro.genero)
    }) 
}

function mostrarAutores(){
    const autores = libros.map(libro => libro.autor)
    const autoresOrdenados = autores.sort()
    console.log("Los autores existentes son:")
    autoresOrdenados.map((autoresOrdenados) => {
        console.log(autoresOrdenados)
    })
    
}

function mostrarPorGenero(){
    const librorequerido = prompt("Cual genero buscas?")
    const libroencontrado = libros.filter((libro) => libro.genero == librorequerido)
    
    if(libroencontrado.length > 0){
        console.log("Libros de genero",librorequerido,":")
        libroencontrado.map((libro) => {
            console.log("Libro: ",libro.titulo)
            console.log("   Autor: ",libro.autor)
            console.log("   Year: ",libro.year)
            console.log("   Genero: ",libro.genero)
        })
    } else {
        console.log("Ningun libro es de ese genero.")
    }
}

const libros = []

while(libros.length < 3){
    let titulo = prompt(`Nombre del libro ${libros.length + 1}:`)
    let autor = prompt(`Autor del libro ${libros.length + 1}:`)
    let year = prompt(`Year del libro ${libros.length + 1}:`)
    let genero = prompt(`Genero del libro ${libros.length + 1}: (terror) (fantasia) (aventura)`)

    if(titulo != "" && autor != "" && year != "" && genero != ""){
        if(year > 999 && year < 10000 && !isNaN(year)){
            if(genero == "aventura" || genero == "terror" ||     genero == "fantasia"){
                libros.push(new Libro(titulo, autor, year, genero))
            } else {
                console.log("Solo se permiten libros del genero: aventura, terror o fantasia.")
            }
        } else {
            console.log("El year del libro debe ser de 4 digitos.")
        }          
    } else { 
        console.log("Se debe llenar todos los campos de informacion.")
    }
}
mostrarTodosLibros()
mostrarAutores()
mostrarPorGenero()
