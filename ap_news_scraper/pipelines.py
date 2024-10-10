from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Artigo  # Importar o modelo de dados

class MySQLPipeline:
    def open_spider(self, spider):
        DATABASE_URL = 'mysql+pymysql://usuario:senha@localhost:3306/nome_do_banco'  # Substitua com seus dados
        self.engine = create_engine(DATABASE_URL)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def close_spider(self, spider):
        self.session.close()

    def process_item(self, item, spider):
        artigo = Artigo(title=item['title'], link=item['link'])
        self.session.add(artigo)
        self.session.commit()
        return item
