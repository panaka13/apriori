from core.database import Database

class Factory:
  database = None

  @classmethod
  def setup_db(cls, database: Database):
    cls.database = database
