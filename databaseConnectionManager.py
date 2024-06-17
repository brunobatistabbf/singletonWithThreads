from singleton import Singleton

class DatabaseConnectionManager(metaclass=Singleton): #para gerenciar a conexão
    def __init__(self):
        self.connection = self._connect_to_database()

    def _connect_to_database(self):
        return "Conecção estabelecida!!!"

    def get_connection(self):
        return self.connection