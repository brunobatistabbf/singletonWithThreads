import threading
from databaseConnectionManager import  DatabaseConnectionManager
from singleton import Singleton

class DatabaseAccessThread(threading.Thread): #Representa as Threads acessando
    def run(self):
        manager = Singleton.get_instance(DatabaseConnectionManager)
        connection = manager.get_connection()
        print(f"{self.name} conectando: {connection}")