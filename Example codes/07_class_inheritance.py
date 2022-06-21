class Employee:
    def __init__(self):
        self.name = ''
        self.age = ''
        self.code_melli = ''
        self.estekhdam_date = ''
    
    def sayHello(self):
        print('Hello from', self.name)

class Saati(Employee):
    saat_kar = ''
    
    def saat_zadan(self):
        print('Saat zadam')

class TamamVaght(Employee):
    sh_bime = ''

person1 = Saati()
person1.name = "Ali"
person1.saat_kar = 10
person1.sayHello()

person2 = TamamVaght()
person2.name = "David"
person2.sh_bime = 2234235432
person2.sayHello()
    


