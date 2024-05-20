# Máte zadanou tuto classu
class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age





# Vytvořte 3 objekty (instance) podle classy
# dokážete vysvětlit, jaký je vztah mezi classou a objektem?

dog_1 = Dog("dogty", 20)
dog_2 = Dog("pes", 12)
dog_3 = Dog("havo", 7)

# Vytvořte funkci, která určí nejstaršího psa z vámi zadaných

##dlha forma zapisu
""" psi = [dog_1, dog_2, dog_3]

def najstarsi(vsetky_psi):
    vek_najstarsieho_psa = 0

    for jeden_pes in vsetky_psi:
        if jeden_pes.age > vek_najstarsieho_psa:
            vek_najstarsieho_psa = jeden_pes.age

    return vek_najstarsieho_psa


result = najstarsi(psi) """

# Vypište výslednou větu "Věk nejstaršího psa: X"

""" print(f"Vek najstarsieho psa je: {result} rokov") """

## kratka forma zapisu

def najstarsi (*args):
    return max(args)

result = najstarsi(dog_1.age, dog_2.age, dog_3.age)

print(f"Vek najstarsieho psa je: {result} rokov") 