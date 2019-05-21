import random



#Definiramo konstante
STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = "+"
PONOVLJENA_CRKA = "o"
NAPACNA_CRKA = "-"
ZACETEK = "S"
ZMAGA = "w"
PORAZ = "x"


#Definiramo logični model igre

class Igra:

    def __init__(self, geslo, crke):
        self.geslo = geslo.upper()
        self.crke = crke
        return
    
    def napacne_crke(self):
        return [x for x in self.crke if x not in self.geslo]

    def pravilne_crke(self):
        return [x for x in self.crke if x in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        for iz_gesla in self.geslo:
            if iz_gesla not in self.crke:
                return False
        
        return self.stevilo_napak() <= STEVILO_DOVOLJENIH_NAPAK
    
    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        geslo = self.geslo
        znane = self.pravilne_crke()
        rez = ""
        for crka in geslo:
            if crka in znane:
                rez += crka
            else:
                rez += " _"
        rez = rez.strip()
        return rez

    def nepravilni_ugibi(self):
        niz = ""
        for crka in self.napacne_crke():
            niz += crka + " "
        return niz

    def ugibaj(self, ugib):
        crka = ugib.upper()

        if self.zmaga():
            return ZMAGA
        elif self.poraz():
            return PORAZ
        
        if crka in self.crke:
            return PONOVLJENA_CRKA
        else:
            self.crke.append(crka)
            if self.zmaga():
                return ZMAGA
            elif self.poraz():
                return PORAZ
            
            if crka in self.napacne_crke():
                return NAPACNA_CRKA
            else:
                return PRAVILNA_CRKA


#Ustvarimo bazen besed

with open("besede.txt", 'r', encoding='utf-8') as dat:
    bazen_besed = [r.strip() for r in dat.readlines()]



#Začnemo novo igro   
def nova_igra():
    beseda = random.choice(bazen_besed)
    return Igra(beseda, [])



#Razni testi
#spil = nova_igra()
#print(spil.ugibaj("e"))
#print(spil.pravilni_del_gesla())
#print(Igra("GESLO", ['G','S','L']).pravilni_del_gesla())
#print(Igra("GESLO", ['G','E','S','L']).ugibaj('o'))




class Vislice:

    def __init__(self):
        # V slovarju igre ima vsaka igra svoj ID
        # ID je celo število
        self.igre = {} 
        return 

    def prost_id_igre(self):
        if self.igre == {}:
            return 0
        else:
            # preverimo katero od prvih "n+1" števil
            # še ni uporabljeno za id "n" iger
            for i in range(len(self.igre) + 1):
                if i not in self.igre.keys():
                    return i
    
    def nova_igra(self):
        # naredi novo igro z naključnim geslom in jo shrani (ZACETEK, igra) v slovar z novim id
        nov_id = self.prost_id_igre()
        self.igre[nov_id] = (nova_igra(), ZACETEK)
        return nov_id

    def ugibaj(self, id_igre, crka):
        # Pridobi igro
        (igra, poskus) = self.igre[id_igre]
        # Ugibaj
        nov_poskus = igra.ugibaj(crka)
        # Shrani rezultat poskusa v slovar
        self.igre[id_igre] = (igra, nov_poskus)
        return
        

        