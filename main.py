class Werknemer:
    def __init__(self,id,voornaam,achternaam,startjaar):
        self.id = id
        self.voornaam = voornaam
        self.achternaam = achternaam
        self.startjaar = startjaar

    def toon_volledige_naam(self):
        return self.voornaam+" "+self.achternaam
    def toon_info_werknemer(self):
        return "ID: {} \n voornaam: {} \n achternaam: {} \n startjaar: {} ".format(
            self.id,self.voornaam,self.achternaam,self.startjaar
        )

class Bediende(Werknemer):

    def __init__(self,id,voornaam,achternaam,startjaar,basis_loon):
        super().__init__(id,voornaam,achternaam,startjaar)
        self.basis_loon = basis_loon

    def toon_info_bediende(self):
        return super().toon_info_werknemer()+" basisloon is € "+str(self.basis_loon)

    def bereken_loon(self):
        aantal_dienstjaar = 2022-self.startjaar
        procent = self.basis_loon*(aantal_dienstjaar*2)/100
        jaar_bonus = aantal_dienstjaar*10
        loon = self.basis_loon+procent+jaar_bonus
        return loon

class Arbeider(Werknemer):
    def __init__(self,id,voornaam,achternaam,startjaar,uurloon):
        super().__init__(id,voornaam,achternaam,startjaar)
        self.uurloon = uurloon
        self.uren_per_maand = 192

    def toon_arbeider_info(self):
        return super().toon_info_werknemer()+" uurloon is € "+str(self.uurloon)
    def bereken_loon(self):
        aantal_dienstjaar = 2022-self.startjaar
        basisloon = self.uurloon*self.uren_per_maand
        procent = basisloon*(aantal_dienstjaar*2)/100
        jaar_bonus = aantal_dienstjaar*10
        loon = basisloon+procent+jaar_bonus
        return loon


#functies
def toon_keuze():
    print("1: Toon alle mederwerkers")
    print("2: Toon alle arbeiders of bediende")
    print("3: Voeg medewerker toe")
    print("4: Wijzig looninfo")
    print("5: Sorteer bediende op loon")
    print("6: verwijder medeweker")
    print("7: loon_kost bedrijf")


def toon_alle_mederwerkers(lijst):
    for x in lijst:
        print(x.toon_info_werknemer())

def toon_alle_mederwerker_per_type(lijst):
    type = input("Arbeider of bediende : a/b")
    for x in lijst:
        if(type == "b"):
            if(isinstance(x,Bediende)):
                print(x.toon_info_bediende())
        else:
            if(isinstance(x,Arbeider)):
                print(x.toon_arbeider_info())

def voeg_mederwerker_toe(lijst):
    id = input("geef het id")
    voornaam = input("geef de voornaam")
    achternaam = input("geef de achternaam")
    bed_of_arb = input("arbeider of bediende : a/b")

    if(bed_of_arb == "a"):
        uurloon = float(input("geef het uurloon in"))
        w = Arbeider(id,voornaam,achternaam,2022,uurloon)
        lijst.append(w)
    elif(bed_of_arb == "b"):
        maandloon = float(input("geef het basis maandloon in"))
        w = Bediende(id,voornaam,achternaam,2020,maandloon)
        lijst.append(w)
    else:
        print("enkel arbeider of bediende")

def wijzig_loon_gegevens(lijst):
    wn = input("geef het id van de werknemer")
    for x in lijst:
        if(wn == x.id):
            if(isinstance(x,Arbeider)):
                x.uurloon = float(input("geef een nieuw uurloon"))
            else:
                x.basis_loon = float(input("geef een nieuw basisloon"))

def sorteer_bediende_loon(lijst):
    lijst_bed = []
    for x in lijst:
        if isinstance(x,Bediende):
            lijst_bed.append(x)
    lijst_bed.sort(key=lambda x:x.startjaar)
    for y in lijst_bed:
        print(y.toon_info_bediende())

def verwijder_mederwerker(lijst):
    wm = input("geef het id van de medewerker")
    for x,o in enumerate(lijst):
        if o.id == wm:
            lijst.pop(x)

def bereken_loonkost(lijst):
    lonen_som = 0
    for x in lijst:
        lonen_som += x.bereken_loon()
    print(lonen_som)






b1 = Bediende("w1","Mark","Jansen",2004,2700)
b2 = Bediende("w2","Petra","Mertens",2007,2200)
b3 = Bediende("w3","Paulien","Jansen",2018,1750)
b4 = Bediende("w4","Wouter","Verjans",2019,1850)
a1 = Arbeider("w5","Nico","Jansen",2004,16)
a2 = Arbeider("w6","Frank","Mertens",2008,13.5)
a3 = Arbeider("w7","Mario","Verjans",2010,12)
a4 = Arbeider("w8","Karel","Jansen",2014,12)
a5 = Arbeider("w9","Jannick","Peters",2018,11)


print(b1.toon_info_werknemer())

medewerkers = [b1,b2,b3,b4,a1,a2,a3,a4,a5]

toon_keuze()
keuze = input("geef je keuze in")

while(not keuze == "stop"):
    if(keuze == "1"):
        toon_alle_mederwerkers(medewerkers)
    elif(keuze == "2"):
        toon_alle_mederwerker_per_type(medewerkers)
    elif(keuze == "3"):
        voeg_mederwerker_toe(medewerkers)
    elif(keuze == "4"):
        wijzig_loon_gegevens(medewerkers)
    elif(keuze == "5"):
        sorteer_bediende_loon(medewerkers)
    elif(keuze == "6"):
        verwijder_mederwerker(medewerkers)
    elif(keuze == "7"):
        bereken_loonkost(medewerkers)



    toon_keuze()
    keuze = input("geef je keuze")



