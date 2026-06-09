# Ava3_Pra2

Projeto desenvolvido com Django e React para criação de um formulário web.

## Tecnologias

* Python
* Django
* React
* Vite
* SQLite
* Git/GitHub

## Estrutura

```text
Ava3e4/
│
├── meu_projeto/   # Backend Django
└── frontend/      # Frontend React
```

## Funcionalidades

* Formulário para preenchimento de nome e e-mail.
* Interface desenvolvida em React.
* Backend desenvolvido em Django.
* Comunicação entre frontend e backend através de API.
* Respostas em formato JSON.

## Executando o backend

Na pasta `meu_projeto`:

```bash
python manage.py runserver
```

Servidor disponível em:

```text
http://127.0.0.1:8000
```

## Executando o frontend

Na pasta `frontend`:

```bash
npm install
npm run dev
```

Servidor disponível em:

```text
http://localhost:5173
```

## API

Endpoint utilizado pelo formulário:

```http
POST /api/formulario/
```

Exemplo:

```json
{
  "nome": "João",
  "email": "joao@email.com"
}
```

## Autor

Desenvolvido como atividade prática utilizando Django e React.
