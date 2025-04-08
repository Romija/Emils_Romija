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
        print(f"{self.nosaukums}: {self.skaits}")

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
            fails.write(self) #######################

    def nolasit_saturu(self, faila_nosaukums):
        try:
            with open(faila_nosaukums, "r", encoding = "utf8") as fails:
                fails.readlines(faila_nosaukums)

                '''
                if not in fails:
                    print("Failā nav satura!")
                    '''
                    
        except FileNotFoundError:
            print("Fails nepastāv!")