from abc import ABC, abstractmethod
class Produkts(ABC): #
    def __init__(self,nosaukums,skaits,dienu_skaits,minimalais_skaits):
        self.nosaukums = nosaukums
        self.skaits = skaits
        self.dienu_skaits = dienu_skaits
        self.minimalais_skaits = minimalais_skaits

    @abstractmethod
    def info(self):
        pass

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

class SvaigsProdukts(Produkts): #Manto klasi "Produkts"
    def __init__(self,nosaukums,skaits,dienu_skaits,minimalais_skaits):
        super().__init__(nosaukums,skaits,dienu_skaits,minimalais_skaits)

    def pietrukst(self):
        return self.skaits<self.minimalais_skaits

class Tirgotajs: # klase Tirgotājs      
    def __init__(self,tirgotajs,produkts,min_pasutijuma_daudzums):
        self.tirgotajs = tirgotajs
        self.produkts = produkts
        self.min_pasutijuma_daudzums = min_pasutijuma_daudzums


    def pienemt_pasutijumu(self, produkts, pasutijuma_daudzums): # funkcija pārbauda vai lietotājs var pasūtīt produktus, vai nav mazāk par minimālo daudzumu
        if pasutijuma_daudzums < self.min_pasutijuma_daudzums:
           return f"Pasūtījums netiek pieņemts, jo pasūtījuma daudzums ir mazāks ({self.pasutijuma_daudzums}) par minimālo daudzumu ({self.min_pasutijuma_daudzums})"
        if produkts==self.produkts:
            return "Šāds produkts nepastāv!"
        
        return "Pasūtījums ir pieņemts"

class Pasutijums:
    saglabatie_pasutijumi = []

    def __init__(self, adresats, prece, apjoms):
        self.adresats = adresats
        self.prece = prece
        self.apjoms = apjoms
        Pasutijums.saglabatie_pasutijumi.append(self)

    def saglabat_faila(self, faila_nosaukums = 'saturs.txt'):
        with open(faila_nosaukums, "a", encoding = 'utf8') as fails:
            fails.write(f"{self.prece}: {self.apjoms} kg")

    @classmethod
    def nolasit_saturu(cls, faila_nosaukums="saturs.txt"):
        try:
            with open(faila_nosaukums, "r", encoding = "utf8") as fails:
                saturs = fails.readlines()
                if not saturs:
                    return "Failā nav satura!"
                return "".join(saturs) 
        except FileNotFoundError:
            print("Fails nepastāv!")

tirgotaji = {
    "Maiznieks" : Tirgotajs("Maiznieks", "Maize", 5),
    "Miesnieks" : Tirgotajs("Miesnieks", "Gaļa", 15),
    "Piena kombināts" : Tirgotajs("Piena kombināts", "Piens", 20),
    "Šokolādes fabrika" : Tirgotajs("Šokolādes fabrika", "Šokolāde", 3),
    "Miltu fabrika" : Tirgotajs("Miltu fabrika", "Milti", 5),
    "Kartupeļu lauks" : Tirgotajs("Kartupeļu lauks", "Kartupeļi", 30),
    "Siernīca" : Tirgotajs("Siernīca", "Siers", 15)
}

maize = Noliktava("Maize",7,2,5)
gala = Noliktava("Gaļa",20,1,25)
piens = Noliktava("Piens",5,2,7)
sokolade = Noliktava("Šokolāde", 2, 3, 2)
milti = Noliktava("Milti", 2, 13, 3)
kartupeli = Noliktava("Kartupeļi", 35, 3, 30)
siers = Noliktava("Siers",10,90,8)

produkti = [maize,gala,piens,sokolade,milti,kartupeli,siers]

while True:
    print("\n1 - pārbaudīt noliktavu\n2 - parādīt informāciju par produktiem, kuri pietrūkst\n3 - parādīt informāciju par produktiem, kuriem ir beidzies derīguma termiņš\n4 - pasūtīt produktus\n5 - apskatīt pasūtījumu vēsturi\n6 - atbrīvoties no produkta kuram beidzies derīguma termiņš\n7- iziet")
    izvele = input("\nIevadiet savu izvēli: ")

    if izvele == "1":
        for produkts in produkti:
            print(produkts.info())

    elif izvele =="2":
        for produkts in produkti:
            if produkts.pietrukst():
                print(produkts.info())
            
    elif izvele =="3":
        for produkts in produkti:
            if produkts.nosaukums=='Šokolāde' and produkts.dienu_skaits>14:
                print(produkts.info())
            elif produkts.nosaukums == "Milti" and produkts.dienu_skaits>10:
                print(produkts.info())
            elif produkts.dienu_skaits>5:
                print(produkts.info())

    elif izvele== "4":
        adresats = input("Lūdzu ievadiet adresātu: ")
        prece = input("Lūdzu ievadiet preci: ")
        pasutijuma_daudzums = int(input("Lūdzu ievadiet preces daudzumu: "))

        if adresats in tirgotaji:
            tirgotajs = tirgotaji[adresats]
            rezultats = tirgotajs.pienemt_pasutijumu(Produkts, pasutijuma_daudzums)
            print(rezultats)
            if "Pasūtījums ir pieņemts" in rezultats:
                pasutijums = Pasutijums(adresats, prece, pasutijuma_daudzums)
                pasutijums.saglabat_faila()
                for p in produkti:
                    if p.nosaukums == prece:
                        p.pievienot(pasutijuma_daudzums)
                        break

    elif izvele == "5":
            print(Pasutijums.nolasit_saturu())

    elif izvele =="6":
     for produkts in produkti:
            if produkts.nosaukums=='Šokolāde' and produkts.dienu_skaits>14:
                produkts.dzest()
            elif produkts.nosaukums == "Milti" and produkts.dienu_skaits>10:
                produkts.dzest()
            elif produkts.dienu_skaits>5:
                produkts.dzest()

    elif izvele =="7" or izvele == "iziet":
        print("Programma beidzas")
        exit()
        
    else:
        print("Nepareiza ievade")


