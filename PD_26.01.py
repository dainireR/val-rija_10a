#augšpielāde

v1=input("Ivadi 1. virkni: ")
v2=input("Ivadi 2. virkni: ")
v3=input("Ivadi 3. virkni: ")
b=""

if len(v1)>len(v2) and len(v1)>len(v2):
    b=v1.count("e")+v1.count("a")+v1.count("u")+v1.count("i")+v1.count("o")
    print(v1[::-2])
    print(f'Virknē {v1} ir {b} patskaņu')
elif len(v2)>len(v1) and len(v2)>len(v3):
    b1=v2.count("e")+v2.count("a")+v2.count("u")+v2.count("i")+v2.count("o")
    print(v2[::-2])
    print(f'Virknē {v2} ir {b1} patskaņu')
elif len(v3)>len(v2) and len(v3)>len(v1):
    b2=v3.count("e")+v3.count("a")+v3.count("u")+v3.count("i")+v3.count("o")
    print(v3[::-2])
    print(f'Virknē {v3} ir {b2} patskaņu')
else:

    print("Kļūda!!!")
