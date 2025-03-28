var adicionar = document.getElementById("adicionar")
var button_adicionar = document.getElementById("buttonAdicionar")

button_adicionar.addEventListener("click", function (){
    var adicionar = document.getElementById("adicionar")
    if(adicionar.style.display === "block"){
        adicionar.style.display = "block"
    }else{
        adicionar.style.display = "block"
        listasUsuario.style.display = "none"
    }
});
var listasUsuario = document.getElementById("listasUsuario")
var button_lista = document.getElementById("buttonListas")

button_lista.addEventListener("click", function (){
    var listasUsuario = document.getElementById("listasUsuario")
    if(listasUsuario.style.display === "block"){
        listasUsuario.style.display = "block"
    }else{
        listasUsuario.style.display = "block"
        adicionar.style.display = "none"
    }
});