from abc import ABC, abstractmethod
class Produkts(ABC): # abstrakta klase Produkts, kurai ir attiecīgie atribūti
    def __init__(self,nosaukums,skaits,dienu_skaits,minimalais_skaits):
        self.nosaukums = nosaukums
        self.skaits = skaits
        self.dienu_skaits = dienu_skaits
        self.minimalais_skaits = minimalais_skaits

    @abstractmethod # abstrakta metode info()
    def info(self):
        pass

class Noliktava(Produkts): # Noliktava manto klases Produkts atribūtus
    def __init__(self, nosaukums, skaits, dienu_skaits, minimalais_skaits):
        super().__init__(nosaukums, skaits, dienu_skaits, minimalais_skaits)

    def info(self): # funkcija info(), kas izdrukā informāciju par produktu
        return f"{self.nosaukums}: {self.skaits} kg"

    def pietrukst(self): # funkcija, kas pārbauda, vai produkts pietrūkst
        return self.skaits<self.minimalais_skaits

    def pievienot(self, daudzums): # funkcija, kas papildina daudzumu, ja lietotājs pasūta šo produktu vēl
        self.skaits += daudzums
    
    def dzest(self): # funkcija, kas "izdzēš" produktu, ja lietotājs ir ievadījis 6. izvēli
        self.skaits = 0
        self.dienu_skaits=0

class SvaigsProdukts(Produkts): #klase, kas manto Produkta atribūtus
    def __init__(self,nosaukums,skaits,dienu_skaits,minimalais_skaits):
        super().__init__(nosaukums,skaits,dienu_skaits,minimalais_skaits)

    def pietrukst(self): # funkcija, kas pārbauda, vai produkts pietrūkst
        return self.skaits<self.minimalais_skaits

class Tirgotajs:  # klase, kurai ir 3 atribūti, kuri apraksta tirgotāju, viņa preci un minimālo pasūtījuma daudzumu 
    def __init__(self,tirgotajs,produkts,min_pasutijuma_daudzums):
        self.tirgotajs = tirgotajs
        self.produkts = produkts
        self.min_pasutijuma_daudzums = min_pasutijuma_daudzums


    def pasutijums(self, produkts, daudzums):
        if daudzums < self.min_pasutijuma_daudzums: # funkcija pārbauda, vai pasūtīts pietiekams daudzums
           return f"Nevar pasūtīt zem minimālā skaita! ({self.min_pasutijuma_daudzums} kg)"
        if produkts!=self.produkts: # funkcija pārbauda, vai preces nosaukums ir pareizi ievadīts
            return "Nepareiza ievade!"
        return f"{prece} ir pasūtīts/a!!!" # izvada šo, ja prece ir veiksmīgi pasūtīta

class Pasutijums:
    saglabatie_pasutijumi = [] # saraksts, kas saturēs pasūtījumus

    def __init__(self, adresats, prece, apjoms): # klases konstruktors, kas satur lietotāja iavadītos datus par pasūtījumu
        self.adresats = adresats
        self.prece = prece
        self.apjoms = apjoms
        Pasutijums.saglabatie_pasutijumi.append(self) # sarakstu papildina ar pasūtījuma informāciju

    def saglabat_faila(self, faila_nosaukums = 'saturs.txt'): # funkcija, kas saglabā failā pasūtījuma informāciju
        with open(faila_nosaukums, "a", encoding = 'utf8') as fails:
            fails.write(f"{self.prece}: {self.apjoms} kg\n")

    @classmethod
    def nolasit_saturu(cls, faila_nosaukums="saturs.txt"):
        try:
            with open(faila_nosaukums, "r", encoding = "utf8") as fails: # funkcija, kas nolasa faila saturu
                saturs = fails.readlines()
                if not saturs: # brīdinājums, ja fails ir tukšs
                    return "Failā nav satura!"
                return "".join(saturs) # atgriež faila saturu
        except FileNotFoundError: # pārbaude, vai fails pastāv
            print("Fails nepastāv!")

# vārdnīca ar tirgotāju objektiem, kuri satur adresātu, preci un minimālo daudzumu
tirgotaji = {
    "Maiznieks" : Tirgotajs("Maiznieks", "Maize", 5),
    "Miesnieks" : Tirgotajs("Miesnieks", "Gaļa", 15),
    "Piena kombināts" : Tirgotajs("Piena kombināts", "Piens", 20),
    "Šokolādes fabrika" : Tirgotajs("Šokolādes fabrika", "Šokolāde", 3),
    "Miltu fabrika" : Tirgotajs("Miltu fabrika", "Milti", 5),
    "Kartupeļu lauks" : Tirgotajs("Kartupeļu lauks", "Kartupeļi", 30),
    "Siernīca" : Tirgotajs("Siernīca", "Siers", 15)
}

# produktu objekti
maize = Noliktava("Maize",7,2,5)
gala = Noliktava("Gaļa",20,1,25)
piens = Noliktava("Piens",5,2,7)
sokolade = Noliktava("Šokolāde", 2, 3, 2)
milti = Noliktava("Milti", 2, 13, 3)
kartupeli = Noliktava("Kartupeļi", 35, 3, 30)
siers = Noliktava("Siers",10,90,8)

# saraksts, kas satur produktu objektus
produkti = [maize,gala,piens,sokolade,milti,kartupeli,siers]

while True: # cikls, kas atkārtojas
    print("\n1 - pārbaudīt noliktavu\n2 - parādīt informāciju par produktiem, kuri pietrūkst\n3 - parādīt informāciju par produktiem, kuriem ir beidzies derīguma termiņš\n4 - pasūtīt produktus\n5 - apskatīt pasūtījumu vēsturi\n6 - atbrīvoties no produkta kuram beidzies derīguma termiņš\n7- iziet")
    izvele = input("\nIevadiet savu izvēli: ")

    if izvele == "1": # 1 - parāda informāciju par visiem produktiem (ar ciklu izejot cauri produktu sarakstam)
        for produkts in produkti:
            print(produkts.info())

    elif izvele =="2": # 2 - parāda informāciju par produktiem, kuri pietrūkst (ar ciklu izejot cauri produktu sarakstam)
        for produkts in produkti:
            if produkts.pietrukst():
                print(produkts.info(),f"(nepieciešami vismaz {produkts.minimalais_skaits})")
            
    elif izvele =="3": # 3 - parāda informāciju par produktiem, kuriem beidzies derīguma termiņš (ar ciklu izejot cauri produktu sarakstam)
        for produkts in produkti:
            if produkts.nosaukums=='Šokolāde' and produkts.dienu_skaits>14: # pārbaude šokolādei, jo to var uzglabāt ilgāk par pārējiem produktiem 
                print(produkts.info(),"(Beidzies derīguma termiņš)")
            elif produkts.nosaukums == "Milti" and produkts.dienu_skaits>10: # pārbaude miltiem, jo tos var uzglabāt ilgāk par pārējiem produktiem
                print(produkts.info(),"(Beidzies derīguma termiņš)")
            elif produkts.dienu_skaits>5: # pārejiem produktiem visiem vienāds derīguma termiņš
                print(produkts.info(),"(Beidzies derīguma termiņš)")

    elif izvele== "4":
        print("Adresāti un preces (iekavās minimālais pasūtījuma daudzums):\nMaiznieks-Maize (5), Miesnieks-Gaļa (15), Piena Kombināts-Piens (20), Šokolādes fabrika-Šokolāde (3), Miltu fabrika-milti (5), Kartupeļu lauks-Kartupeļi (30), Siernīca-Siers (15)")
        while True: # cikls, kas jautā lietotājam ievadīt adresātu
            adresats = input("Lūdzu ievadiet adresātu: ")
            if adresats not in tirgotaji: # pārbaude, vai adresāts ir eksistējošs
                print("Nepareizs adresāts. Mēģini vēlreiz.")
            else:
                break

        while True: # cikls, kas jautā lietotājam ievadīt preci
            prece = input("Lūdzu ievadiet preci: ")
            if prece not in [p.nosaukums for p in produkti]: # pārbaude, vai prece ir eksistējoša
                print("Nepareiza prece. Mēģini vēlreiz.")
            else:
                break

        while True: # cikls, kas jautā lietotājam ievadīt pasūtījuma daudzumu
            try:
                daudzums = int(input("Lūdzu ievadiet preces daudzumu: "))
                if daudzums <= 0: # pārbaude, vai ievadīts pozitīvs skaitlis
                    print("Daudzumam jābūt pozitīvam skaitlim.")
                else:
                    break
            except ValueError: # pārbaude, vai lietotājs ievadīja skaitli
                print("Lūdzu ievadiet skaitli!")

        if adresats in tirgotaji: # pārbaude, vai adresāts ir tirgotāju vārdnīcā
            tirgotajs = tirgotaji[adresats]
            rezultats = tirgotajs.pasutijums(prece, daudzums) # pieņem pasūtījumu
            print(rezultats)
            if f"{prece} ir pasūtīts/a!!!" in rezultats: # ja pasūtījums pieņemts, tiek izveidots pasūtījuma objekts un saglabāts failā
                pasutijums = Pasutijums(adresats, prece, daudzums)
                pasutijums.saglabat_faila()
                for p in produkti: # pārbaude, vai ievadītajai precei ir atbilstošs nosaukums (ar ciklu iziet cauri produktu sarakstam)
                    if p.nosaukums == prece:
                        p.pievienot(daudzums)
                        break

    elif izvele == "5": # funkcija, kas parāda pasūtījuma vēsturi jeb nolasa faila saturu
        print("\nPasūtījumu vēsture:")
        print(Pasutijums.nolasit_saturu())

    elif izvele =="6": # funkcija, kas izdzēšs vecos produktus
        print("Nederīgie produkti ir izmesti!")
        for produkts in produkti:
            if produkts.nosaukums=='Šokolāde' and produkts.dienu_skaits>14: # pārbaude šokolādei, jo to var uzglabāt ilgāk par pārējiem produktiem
                produkts.dzest()
            elif produkts.nosaukums == "Milti" and produkts.dienu_skaits>10: # pārbaude miltiem, jo tos var uzglabāt ilgāk par pārējiem produktiem
                produkts.dzest()
            elif produkts.dienu_skaits>5: # pārejiem produktiem visiem vienāds derīguma termiņš
                produkts.dzest()

    elif izvele =="7" or izvele == "iziet": # opcija iziet no programmas
        print("\nProgramma tika pārtraukta")
        exit()
        
    else: # pārbaude, vai ievadīts skaitlis no 1-7 vai "iziet"
        print("Nepareizi ievadīti dati! Ievadiet pareizus!")


