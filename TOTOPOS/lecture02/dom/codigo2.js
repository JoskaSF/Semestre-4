const body = document.querySelector('body')

const div = document.createElement('div')
div.style.height = '500px'
div.style.background = 'cyan'

const parrafo = document.createElement('p')
parrafo.textContent = 'Hola'
parrafo.style.textAlign = 'center'
parrafo.style.fontSize = '30px'

body.appendChild(div)
div.appendChild(parrafo)