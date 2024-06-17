class Singleton(type):
    _instances = {}

    def get_instance(cls, *args, **kwargs):

        #Garante que apenas uma instancia seja criada
        if cls not in cls._instances:
            instance = cls(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]