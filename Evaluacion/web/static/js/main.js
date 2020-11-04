/*Funcion que validara el correo en el archivo index.html*/
function validarCorreo(correo){
    var expReg  = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/; /*expresion regular para validar caracteres*/
    var esValido= expReg.test(correo);
    if(esValido==true){
        alert('El correo ha sido ingresado.')

    }
    if(correo.length<1){
        alert('Debe ingresar un correo.')
    }
    else{
        alert('El correo es invalido, intente nuevamente.')
    }
}


