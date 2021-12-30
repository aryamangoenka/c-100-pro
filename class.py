class Car(object):
    def __init__(self,speed,colour,model,company) :
        self.speed=speed
        self.colour=colour
        self.model=model
        self.company=company
   
    def start(self) :
        print("started")

    def stop(self) :
        print("stoped")

    def accerlate(self) :
        print("acceralating")

    def changegear(self) :
        print("gear changed")

audi= Car(1,"red","x","audi")
bmw= Car(2,"YELOW","y","BMW")
toyota= Car(2,"green","y","toyota")
print(audi.colour)
print( audi.accerlate())