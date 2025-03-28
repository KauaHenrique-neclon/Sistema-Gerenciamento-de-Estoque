var adicionarFornecedor = document.getElementById("cadastro")
var buttonAdicionarFonecedor = document.getElementById("buttonCadastar")

buttonAdicionarFonecedor.addEventListener("click", function(){
    var adicionarFornecedor = document.getElementById("cadastro")
    if (adicionarFornecedor.style.display === "block"){
         adicionarFornecedor.style.display = "block"
    }else{
        adicionarFornecedor.style.display = "block"
        adicionarEntrega.style.display = "none"
    }
})
var adicionarEntrega = document.getElementById("recebimento")
var buttonAdicionarEntrega = document.getElementById("buttonEntregas")

buttonAdicionarEntrega.addEventListener("click", function(){
    var adicionarEntrega = document.getElementById("recebimento")
    if (adicionarEntrega.style.display === "block"){
        adicionarEntrega.style.display = "block"
    }else{
        adicionarEntrega.style.display = "block"
        adicionarFornecedor.style.display = "none"
    }
})