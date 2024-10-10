from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Artigo(Base):
    __tablename__ = 'artigos'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    link = Column(String(255))

# Função para criar o banco de dados
def criar_banco(url):
    engine = create_engine(url)
    Base.metadata.create_all(engine)

# Substitua 'usuario', 'senha', 'host', 'porta', 'nome_do_banco' pelos seus dados
DATABASE_URL = 'mysql+pymysql://usuario:senha@localhost:3306/nome_do_banco'
criar_banco(DATABASE_URL)
