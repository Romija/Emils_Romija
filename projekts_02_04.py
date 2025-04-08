from abc import ABC
class Produkts(ABC):
    def __init__(self,nosaukums,skaits,dienu_skaits,minimalais_skaits):
        self.nosaukums = nosaukums
        self.skaits = skaits
        self.dienu_skaits = dienu_skaits
        self.minimalais_skaits = minimalais_skaits


siers = Produkts("Siers",10,2,8)
piens = Produkts("Piens",5,2,7)
maize = Produkts("Maize",7,2,5)


class SvaigsProdukts(Produkts):
    def __init__(self,nosaukums,skaits,dienu_skaits,minimalais_skaits):
        super().__init__(nosaukums,skaits,dienu_skaits,minimalais_skaits)
    


class Tirgotajs:       
    def __init__(self,tirgotajs,min_pasutijuma_daudzums):
        self.tirgotajs = tirgotajs
        self.min_pasutijuma_daudzums = min_pasutijuma_daudzums

        if self.adresats = adresats:
            pass
        else:
            print("Nepareizais adresāts!")

    def pienemt_pasutijumu(self):
        if pasutijuma_daudzums >= min_pasutijuma_daudzums:
           print("Pasūtījums ir pieņemts")
        elif minimalais_skaits > min_pasutijuma_daudzums:
            print("Pasūtījums netiek pieņemts, jo pasūtījuma daudzums ir mazāks par minimālo daudzumu")
        



maiznieks = Tirgotajs("Maiznieks")

