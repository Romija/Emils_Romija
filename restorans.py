class Produkts:
    def __init__(self,nosaukums,skaits,dienu_skaits,minimalais_skaits):
        self.nosaukums = nosaukums
        self.skaits = skaits
        self.dienu_skaits = dienu_skaits
        self.minimalais_skaits = minimalais_skaits

class Noliktava(Produkts):
    def __init__(self, nosaukums, skaits, dienu_skaits, minimalais_skaits):
        super().__init__(nosaukums, skaits, dienu_skaits, minimalais_skaits)

    def info(self):
        return f"{self.nosaukums}: {self.skaits} kg"

    def pietrukst(self):
        return self.skaits<self.minimalais_skaits

    def pievienot(self, daudzums):
        self.skaits += daudzums
    
    def dzest(self):
        self.skaits = 0
        self.dienu_skaits=0

class Pasutijums:
    saglabatie_pasutijumi = []

    def __init__(self, adresats, prece, apjoms):
        self.adresats = adresats
        self.prece = prece
        self.apjoms = apjoms
        Pasutijums.saglabatie_pasutijumi.append(self)

    def saglabat_faila(self, faila_nosaukums = 'saturs.txt'):
        with open(faila_nosaukums, "a", encoding = 'utf8') as fails:
            fails.write(f"{self.nosaukums}: {self.skaits} kg")

    @classmethod
    def nolasit_saturu(self, faila_nosaukums):
        try:
            with open(faila_nosaukums, "r", encoding = "utf8") as fails:
                saturs = fails.readlines()
                if not saturs:
                    return "Failā nav satura!"
                return "".join(saturs) 
        except FileNotFoundError:
            print("Fails nepastāv!")

class Tirgotajs:
    pass

tirgotaji = {
    "Maiznieks" : Tirgotajs("Maiznieks", "Maize", 5),
    "Miesnieks" : Tirgotajs("Miesnieks", "Gaļa", 15),
    "Piena kombināts" : Tirgotajs("Piena kombināts", "Piens", 20),
    "Šokolādes fabrika" : Tirgotajs("Šokolādes fabrika", "Šokolāde", 3),
    "Miltu fabrika" : Tirgotajs("Miltu fabrika", "Milti", 5),
    "Kartupeļu lauks" : Tirgotajs("Kartupeļu lauks", "Kartupeļi", 30),
    "Siernīca" : Tirgotajs("Siernīca", "Siers", 15)
}

maize = Produkts("Maize",7,2,5)
gala = Produkts("Gaļa",20,1,25)
piens = Produkts("Piens",5,2,7)
sokolade = Produkts("Šokolāde", 2, 3, 2)
milti = Produkts("Milti", 2, 13, 3)
kartupeli = Produkts("Kartupeļi", 35, 3, 30)
siers = Produkts("Siers",10,2,8)