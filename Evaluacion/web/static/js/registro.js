/*Se guardaran los datos ingresados en los input en cada variable segun corresponda*/
const nombre = document.getElementById("name")
const nombreU = document.getElementById("nameU")
const email = document.getElementById("email")
const pass = document.getElementById("password")
const form = document.getElementById("form")
const parrafo = document.getElementById("warnings")
const fecha = document.getElementById("datepicker")

form.addEventListener("submit", e=>{
    e.preventDefault()
    let warnings = ""
    let entrar = false
    let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/ /*expresion regunlar para validar caracteres*/
    parrafo.innerHTML = ""
    if(nombreU.value.length <6){
        warnings += "El nombre de usuario debe tener 6 caracteres minimo <br>"
        entrar = true
    }
    if(nombre.value.length <5){
        warnings += "El nombre debe tener 10 caracteres minimo<br>"
        entrar = true
    }
    if(!regexEmail.test(email.value)){
        warnings += "El email no es valido <br>"
        entrar = true
    }
    if(pass.value.length < 8){
        warnings += "La contraseña debe tener 8 caracteres minimo<br>"
        entrar = true
    }
    if(fecha.value.length<1){
        warnings += "Debes seleccionar una fecha para validar el registro<br>"
        entrar = true
    }
    if(entrar){
        parrafo.innerHTML = warnings
    }else{
        parrafo.innerHTML = "Enviado"
        
    }
})

$(function(){
    $("#datepicker").datepicker({
        dateFormat: "dd-mm-yy",
        changeMonth: true,
        changeYear: true,
        maxDate: "today",
       
    });
});
 
