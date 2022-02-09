class Activiteit:
    def __init__(self,id,naam,kostprijs):
        self.id = id
        self.naam = naam
        self.kostprijs = kostprijs
        self.begeleider = "geen begeleider"
    def toon_info(self):
        return "ID:{} {} en kostprijs is € {}".format(self.id,self.naam,self.kostprijs)


class Persoon:
    def __init__(self,id,naam,leeftijd):
        self.id = id
        self.naam = naam
        self.leeftijd = leeftijd

    def toon_info(self):
        return "ID {}: {} is {} jaar ".format(self.id,self.naam,self.leeftijd)
    def toon_leeftijd(self):
        return self.leeftijd

class Begeleider(Persoon):
    def __init__(self,id,naam,leeftijd,kostprijs):
        super().__init__(id,naam,leeftijd)
        self.kostprijs = kostprijs

    def toon_info(self):
        return super().toon_info()+" dagprijs "+str(self.kostprijs)

class Deelnemer(Persoon):
     def __init__(self,id,naam,leeftijd,organisatie):
        super().__init__(id,naam,leeftijd)
        self.organisatie = organisatie
        self.aantalinschrijving = 0

     def toon_info(self):
        return super().toon_info()+" organisatie "+self.organisatie
     def toon_leeftijd(self):
        return self.leeftijd


class Inschrijving:
    def __init__(self,id,deelnemer,activiteit):
        self.id = id
        self.deelnemer = deelnemer
        self.activiteit = activiteit
        self.deelnemer.aantalinschrijving += 1

    def toon_info(self):
        return "ID {} : {} ingeschreven voor {}"\
            .format(self.id,self.deelnemer.naam,self.activiteit.naam)
    def toon_naam_deelnemer(self):
        return self.deelnemer.naam
    def toon_activiteit_naam(self):
        return self.activiteit.naam

def toon_menu():
    print("1: Toon inschrijvingen")
    print("2: Toon persoons Info")
    print("3: Toon begeleiders")
    print("4: voeg persoon toe")
    print("5: verwijder inschrijving")
    print("6: print activiteit van deelnemer")
    print("7: Sorteer deelnemers op leeftijd")
    print("8: Sorteer op activiteit")

def toon_alle_inschrijvingen(lijst):
    for x in lijst:
        print(x.toon_info())
def toon_alle_personen(lijst):
    for x in lijst:
        print(x.toon_info())
def toon_alle_begeleiders(lijst):
    for x in lijst:
        if isinstance(x,Begeleider):
            print(x.toon_info())
def persoon_toevoegen(lijst):
    id = input("geef het id in")
    naam = input("geef de naam in")
    leeftijd = input("geef de leeftijd in")
    type = input("begeleider of deelnemer b/d")
    if type == "b":
        vergoeding = int(input("geef de vergoeding in"))
        b = Begeleider(id,naam,leeftijd,vergoeding)
        lijst.append(b)
    else:
        org = input("geef de organisatie in")
        d = Deelnemer(id,naam,leeftijd,org)
        lijst.append(d)
def verwijder_inschrijving(lijst):
    id = input("geef het id van de inschrijving")
    for x,o in enumerate(lijst):
        if o.id == id:
            lijst.pop(x)
def toon_inschrijven_deelnemer(lijst):
    naam = input("geef de naam van de deelnemer")
    for x in lijst:
        if naam == x.toon_naam_deelnemer():
            print(x.toon_activiteit_naam())
def sorteer_deelnemer_leeftijd(lijst):
    deelnemer = []
    for x in lijst:
        if isinstance(x,Deelnemer):
            deelnemer.append(x)
    deelnemer.sort(key = lambda x:x.toon_leeftijd())
    for y in deelnemer:
        print(y.toon_info())
def sorteer_activiteit_kostprijs(lijst):
    lijst.sort(key= lambda x:x.kostprijs)
    for x in lijst:
        print( x.toon_info())
#data

a1 = Activiteit("a1","Bowlen",10)
a2 = Activiteit("a2","Paintballen",25)
a3 = Activiteit("a3","Karten",22)
a4 = Activiteit("a4","Snowboarden",32)
a5 = Activiteit("a5","Gin tasting",28)

activiteiten = [a1,a2,a3,a4,a5]

b1 = Begeleider("B1","Bart", 32, 85)
b2 = Begeleider("B2","Jan", 36, 87)
b3 = Begeleider("B1","Linda", 29, 78)

d1 = Deelnemer("D1","Kurt",40,"Syntra")
d2 = Deelnemer("D2","Mark",34,"Syntra")
d3 = Deelnemer("D3","Petra",35,"VDAB")
d4 = Deelnemer("D4","Nina",36,"VDAB")
d5 = Deelnemer("D5","Nancy",33,"Thor park")

personen = [b1,b2,b3,d1,d2,d3,d4,d5]

i1 = Inschrijving("I1",d1,a5)
i2 = Inschrijving("I2",d1,a2)
i3 = Inschrijving("I3",d2,a1)
i4 = Inschrijving("I4",d3,a5)
i5 = Inschrijving("I5",d5,a2)
i6 = Inschrijving("I6",d2,a3)
i7 = Inschrijving("I7",d4,a5)
i8 = Inschrijving("I8",d5,a4)
i9 = Inschrijving("I9",d1,a1)

inschrijving = [i1,i2,i3,i4,i5,i6,i7,i8,i9]


#hoofdprogramma
toon_menu()
keuze = input("geef je keuze in")
while(not keuze == "stop"):
    if keuze == "1":
        toon_alle_inschrijvingen(inschrijving)
    elif keuze == "2":
        toon_alle_personen(personen)
    elif keuze == "3":
        toon_alle_begeleiders(personen)
    elif keuze == "4":
        persoon_toevoegen(personen)
    elif keuze == "5":
        verwijder_inschrijving(inschrijving)
    elif keuze == "6":
        toon_inschrijven_deelnemer(inschrijving)
    elif keuze == "7":
        sorteer_deelnemer_leeftijd(personen)
    elif keuze == "8":
        sorteer_activiteit_kostprijs(activiteiten)

    toon_menu()
    keuze = input("geef je keuze in")
