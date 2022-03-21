# Django-Rest-API

Rest API simples feita em Python utilizando o framework Django

Setup:
---------------------------  
1. Clone the repository:

   ```bash
   $ git clone https://github.com/Matezcp/Django-Rest-API.git
   ```

   or download as zip and extract.

Requirements:
--------------------------- 
Construir pelo menos dois endpoints utilizando Django:
  - Cadastrar usuário, fornecendo o login, senha e data de nascimento
  - Senha deixar como opcional, se não fornecido gerar uma senha aleatória.
  - Consultar usuários cadastrados.
  - Deve ser possível consultar em XLSX, CSV ou JSON.

Endpoints paths:
---------------------------  
-     path: ''   -- Exibe todos usuários cadastrados com um GET
-     path: 'add/'  -- Adiciona um novo usuário com um POST

add/ instruction:
---------------------------
POST passando login, senha (opcional) e data de nascimento do usuário no body do request:  
#### Template com senha
```json
{
"login": "login-do-usuario",
"password":"senha-do-usuario",
"birthday":"yyyy-mm-dd"
}
```
#### Template sem senha
```json
{
"login": "login-do-usuario",
"birthday":"yyyy-mm-dd"
}
```
