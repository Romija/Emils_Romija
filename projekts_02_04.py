from abc import ABC
class Produkts(ABC):
    def __init__(self,nosaukums,skaits,dienu_skaits,minimalais_skaits):
        self.nosaukums = nosaukums
        self.skaits = skaits
        self.dienu_skaits = dienu_skaits
        self.minimalais_skaits = minimalais_skaits

siers = Produkts("Siers",10,5,8)

class SvaigsProdukts(Produkts):
    def __init__(self,nosaukums,skaits,dienu_skaits,minimalais_skaits):
        super().__init__(nosaukums,skaits,dienu_skaits,minimalais_skaits)
    
class Tirgotajs:       
    def __init__(self,tirgotajs):
        self.tirgotajs = tirgotajs

        if self.adresats = adresats:
            pass
        else:
            print("Nepareizais adresāts!")

    def pienemt_pasutijumu(self):
        if pasutijuma_daudzums =< 
        

maiznieks = Tirgotajs("Maiznieks")









    
