a = int(input("Nummer a?"))
b = int(input("Nummer b?"))
c = int(input("Nummer c?"))
def maximum(a,b,c):
    if (a<c>b):
        print("C ar det storsta talet")
    elif (a<b>c):
        print("B ar det storsta talet")
    elif (b<a>c):
        print("A ar det storsta talet")
    else:
        print("Talen ar lika stora")
maximum(a,b,c)
