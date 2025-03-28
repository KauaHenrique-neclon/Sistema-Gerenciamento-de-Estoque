var adicionarCPF = document.getElementById("adicionarCPF")
var buttonAdicionarCPF = document.getElementById("buttonAdicionarCPF")

buttonAdicionarCPF.addEventListener("click",function(){
    var adicionarCPF = document.getElementById("adicionarCPF")
    if(adicionarCPF.style.display === "block"){
        adicionarCPF.style.display = "block"
    }else{
        adicionarCPF.style.display = "block"
        adicionarCNPJ.style.display = "none"
    }
});
var adicionarCNPJ = document.getElementById("adicionarCNPJ")
var buttonAdicionarCNPJ = document.getElementById("buttonAdicionarCNPJ")

buttonAdicionarCNPJ.addEventListener("click",function(){
    var adicionarCNPJ = document.getElementById("adicionarCNPJ")
    if(adicionarCNPJ.style.display === "block"){
        adicionarCNPJ.style.display = "block"
    }else{
        adicionarCNPJ.style.display = "block"
        adicionarCPF.style.display = "none"
    }
});