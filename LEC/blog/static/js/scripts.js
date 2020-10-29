function checkform()
{
    var f = document.forms["formulario_registro"].elements;
    var cansubmit = true;
    let boton = document.getElementById('boton_confirmar');


    for (var i = 0; i < f.length; i++) {
        if (f[i].value.length == 0) cansubmit = false;
    }

    if (cansubmit) {
        boton.disabled = false;
        boton.classList.remove("cursor-not-allowed");
    }
    else {
        boton.disabled = 'disabled';

    }
}

function postClick(){
    console.log("hola");
}