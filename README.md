
# **CRUD Django**

Este é um projeto de gerenciamento básico de entidades (CRUD) desenvolvido com Django. Ele permite gerenciar produtos, categorias, clientes, fornecedores e pedidos de forma simples e eficiente.

## **Funcionalidades**

- **Produtos**:
  - Adicionar, editar, visualizar e excluir produtos.
  - Campos: nome, descrição, preço, estoque, categoria e fornecedor.

- **Categorias**:
  - Adicionar, editar, visualizar e excluir categorias.
  - Campos: nome.

- **Clientes**:
  - Adicionar, editar, visualizar e excluir clientes.
  - Campos: nome, email, telefone.

- **Fornecedores**:
  - Adicionar, editar, visualizar e excluir fornecedores.
  - Campos: nome, contato.

- **Pedidos**:
  - Criar, editar e excluir pedidos.
  - Campos: cliente, data do pedido, total.

---

## **Requisitos**

- **Python 3.9+**
- **Django 5.1+**
- **Banco de dados**: MySQl
- **Navegador moderno** para interface web.

---

## **Configuração**

### **1. Clone o repositório**
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### **2. Crie e ative um ambiente virtual**
```bash
python -m venv venv
venv\Scripts\activate
```

### **3. Instale as dependências**
```bash
pip install -r requirements.txt
```

### **4. Configure o banco de dados**
1. Edite o arquivo `settings.py` para configurar o banco de dados (se necessário).
2. Aplique as migrações:
   ```bash
   python manage.py migrate
   ```

### **5. Popule os dados iniciais (opcional)**
Se existir um arquivo `fixtures.json`, você pode usá-lo para criar dados iniciais:
```bash
python manage.py loaddata fixtures.json
```

### **6. Inicie o servidor**
```bash
python manage.py runserver
```

Acesse o projeto em: [http://localhost:8000](http://localhost:8000)

## **Principais URLs**

- `/produtos/` - Lista de produtos
- `/categorias/` - Lista de categorias
- `/clientes/` - Lista de clientes
- `/fornecedores/` - Lista de fornecedores
- `/pedidos/` - Lista de pedidos

---

## **Validações do Formulário**

Os formulários incluem validações no frontend (JavaScript) e no backend (Django) para garantir:
- Preenchimento de todos os campos obrigatórios.
- Validação de formatos como email e números.
- Prevenção de erros no envio de dados.


