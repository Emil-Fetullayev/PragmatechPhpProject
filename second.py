class User:
    def __init__(self,_name,_surname):
        self.Name=_name
        self.Surname=_surname
    def printFullName(self):
        return f'Adiniz :{self.Name}, Soyadiniz :{self.Surname}'