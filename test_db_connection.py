from app.core.database import SessionLocal
from sqlalchemy import text  # <-- import necessário

def test_connection():
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))  # Encapsula a string SQL com text()
        print("✅ Conexão com o banco de dados estabelecida com sucesso!")
    except Exception as e:
        print("❌ Erro ao conectar ao banco de dados:", e)
    finally:
        db.close()

if __name__ == "__main__":
    test_connection()