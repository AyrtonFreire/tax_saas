🛠 Comandos para iniciar o projeto

# Criar ambiente virtual
python -m venv venv
.\venv\Scripts\Activate

# Instalar dependências
pip install -r requirements.txt

# Rodar FastAPI localmente
uvicorn app.main:app --reload

🧱 Estrutura inicial do projeto
saas_irish_accounting/
├── app/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── endpoints/
│   │   │   │   ├── users.py
│   │   │   │   ├── invoices.py
│   │   │   │   ├── taxes.py
│   │   │   │   └── reports.py
│   │   │   └── __init__.py
│   │   └── __init__.py
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   ├── crud/
│   │   ├── crud_user.py
│   │   ├── crud_invoice.py
│   │   └── crud_tax.py
│   ├── db/
│   │   ├── base.py
│   │   ├── session.py
│   │   └── models/
│   │       ├── user.py
│   │       ├── invoice.py
│   │       └── tax.py
│   ├── schemas/
│   │   ├── user.py
│   │   ├── invoice.py
│   │   └── tax.py
│   └── main.py
├── alembic/
│   └── (migrations)
├── .env
├── requirements.txt
└── README.md