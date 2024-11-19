function validarFormulario(event) {
    const nome = document.querySelector('input[name="nome"]').value.trim();
    const descricao = document.querySelector('textarea[name="descricao"]').value.trim();
    const preco = document.querySelector('input[name="preco"]').value.trim();
    const estoque = document.querySelector('input[name="estoque"]').value.trim();
    const categoria = document.querySelector('select[name="categoria"]').value.trim();
    const fornecedor = document.querySelector('select[name="fornecedor"]').value.trim();

    if (!nome || !descricao || !preco || !estoque || !categoria || !fornecedor) {
        alert("Por favor, preencha todos os campos antes de salvar.");
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

    return true;
}

document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    if (form) {
        form.addEventListener("submit", validarFormulario);
    }
});
