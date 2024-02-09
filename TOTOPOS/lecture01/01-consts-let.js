let numeroAleatorio = Math.floor(Math.random() * 41)

if (numeroAleatorio < 21 && numeroAleatorio > 18){
    console.log("Salio ",numeroAleatorio," Ganaste")
} else {
    console.log("Salio ",numeroAleatorio," Perdiste")
}