function validarFormularioProduto(event) {
    const nome = document.querySelector('input[name="nome"]').value.trim();
    const descricao = document.querySelector('textarea[name="descricao"]').value.trim();
    const preco = document.querySelector('input[name="preco"]').value.trim();
    const estoque = document.querySelector('input[name="estoque"]').value.trim();
    const categoria = document.querySelector('select[name="categoria"]').value.trim();
    const fornecedor = document.querySelector('select[name="fornecedor"]').value.trim();

    if (!nome || !descricao || !preco || !estoque || !categoria || !fornecedor) {
        alert("Por favor, preencha todos os campos obrigatórios.");
        event.preventDefault();
        return false;
    }

    if (isNaN(preco) || Number(preco) <= 0) {
        alert("Por favor, insira um preço válido (número positivo).");
        event.preventDefault();
        return false;
    }

    if (isNaN(estoque) || Number(estoque) < 0) {
        alert("Por favor, insira um estoque válido (número inteiro positivo ou zero).");
        event.preventDefault();
        return false;
    }
}

function validarFormularioCategoria(event) {
    const nome = document.querySelector('input[name="nome"]').value.trim();
    if (!nome) {
        alert("O campo Nome não pode ficar em branco.");
        event.preventDefault();
    }
}

function validarFormularioCliente(event) {
    const nome = document.querySelector('input[name="nome"]').value.trim();
    const email = document.querySelector('input[name="email"]').value.trim();
    const telefone = document.querySelector('input[name="telefone"]').value.trim();

    if (!nome || !email || !telefone) {
        alert("Por favor, preencha todos os campos obrigatórios (Nome, Email e Telefone).");
        event.preventDefault();
        return false;
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        alert("Por favor, insira um email válido.");
        event.preventDefault();
    }
}

function validarFormularioFornecedor(event) {
    const nome = document.querySelector('input[name="nome"]').value.trim();
    const contato = document.querySelector('input[name="contato"]').value.trim();
    if (!nome || !contato) {
        alert("Os campos Nome e Contato não podem ficar em branco.");
        event.preventDefault();
    }
}

function validarFormularioPedido(event) {
    const cliente = document.querySelector('select[name="cliente"]').value.trim();
    const data = document.querySelector('input[name="data"]').value.trim();

    if (!cliente || !data) {
        alert("Por favor, selecione o cliente e insira a data do pedido.");
        event.preventDefault();
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    if (form) {
        const pageType = form.getAttribute("data-type");
        if (pageType === "produto") {
            form.addEventListener("submit", validarFormularioProduto);
        } else if (pageType === "categoria") {
            form.addEventListener("submit", validarFormularioCategoria);
        } else if (pageType === "cliente") {
            form.addEventListener("submit", validarFormularioCliente);
        } else if (pageType === "fornecedor") {
            form.addEventListener("submit", validarFormularioFornecedor);
        } else if (pageType === "pedido") {
            form.addEventListener("submit", validarFormularioPedido);
        }
    }
});
