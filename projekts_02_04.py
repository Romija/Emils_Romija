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

class SvaigsProdukts(Produkts): #Manto klasi "Produkts"
    def __init__(self,nosaukums,skaits,dienu_skaits,minimalais_skaits):
        super().__init__(nosaukums,skaits,dienu_skaits,minimalais_skaits)
    

class Tirgotajs: # klase Tirgotājs      
    def __init__(self,tirgotajs,produkts,min_pasutijuma_daudzums):
        self.tirgotajs = tirgotajs
        self.produkts = produkts
        self.min_pasutijuma_daudzums = min_pasutijuma_daudzums


    def pienemt_pasutijumu(self): # funkcija pārbauda vai lietotājs var pasūtīt produktus, vai nav mazāk par minimālo daudzumu
        if pasutijuma_daudzums >= min_pasutijuma_daudzums:
           print("Pasūtījums ir pieņemts")
        elif min_pasutijuma_daudzums > pasutijuma_daudzums:
            print(f"Pasūtījums netiek pieņemts, jo pasūtījuma daudzums ir mazāks ({self.pasutijuma_daudzums}) par minimālo daudzumu ({self.min_pasutijuma_daudzums})")
        else:
            print("Ievadiet pareizus datus!")
        
        
#objektu izveide
tirgotajs1 = Tirgotajs("Maiznieks","Maize",5)
tirgotajs2 = Tirgotajs("Miesnieks","Gaļa",3)
tirgotajs3 = Tirgotajs("Piena kombināts","piens",7)

maize = Produkts("Maize",7,2,5)
gala = Produkts("Gaļa",10,2,3)
piens = Produkts("Piens",5,2,7)