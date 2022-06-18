// Seleccionamos todos los botones que tengan la clase btn-detele
const btnDelete = document.querySelectorAll('.btn-delete')
if (btnDelete){
    const btnArray = Array.from(btnDelete)
    btnArray.forEach((btn) => {
        btn.addEventListener('click',(e) => {
            if(!confirm('Are you sure you want to delete it?')){
                e.preventDefault();
            }
        });
    });
}

// Luego de guardados en una constante btnDelete, comprobamos si existen, si existen los transformamos en un arreglo (dado que queryselectorAll devuelve una lista de nodos html que tienen que transformarse en arreglos para ser recorridos)
// Para cada boton obtenido se hace un for each par recorrer cada uno y agregar un evento de escucha, este evento sera el clicl y tomara la informacion de lo que pase dentro
// Si aparece una ventana de confirm y tiene de texto "Are you sure to delete it" y se presiona en cancelAnimationFrame, se previene todo lo que se hizo o cancela el evento click, pero si se presiona en aceptar, el código sigue y se ejecuta la query