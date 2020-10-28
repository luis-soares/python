class Usuario:
    def __init__(self,name,idade,pais,**kwargs):
        self.name = name
        self.idade = idade
        self.pais = pais
        self.prof = kwargs.get('prof')
        self.manager = kwargs.get('manager')
    def getname(self):
        print(self.name)
    def setname(self,name02):
        self.name = name02
    def getmanager(self):
        print(self.manager)

def luis(*args,**kwargs):
    #pass
    print("minhas args sao:{}".format(args)) 
    print("minhas kwargs sao:{}".format(kwargs))    
