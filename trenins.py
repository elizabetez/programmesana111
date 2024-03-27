def rezultats(sk1, sk2):
    if sk1<6 and sk2<6:
        rez = sk1*sk2
    else:
        rez = sk1+sk2

    return rez

for skaitlis in range(1, 11, 2): #range - funkcija, kas skaita skaitļus
    for otrs in range (2, 11, 2):
        print("pirmais skaitlis:", skaitlis,"otrais skaitlis:", otrs, "rezultāts:", rezultats (skaitlis, otrs))


def zvaigznites(skaits):
    for rindasNr in range(1, skaits+1):
         for zvaigzne in range(rindasNr):
             print("*",end="")
        print("")

    def zvaigznites2(skaits):
        for rindasNr in range(1, skaits+1):
            print("*"*rindasNr)
        
zvaigznites (7)




saraksts1 = [1, 7, 5, 9, 35, 2]
saraksts2 = [4, 2, 2, 39, 6, 4]
for skaititajs in range(len(saraksts1)):
    print("skaititajs:", skaititajs, "pirmais skaitlis:", saraksts1[skaititajs],"otrais skaitlis:", saraksts2[skaititajs], "rezultāts:", rezultats (saraksts1[skaititajs], saraksts2[skaititajs]))









skaitlis1 = 7
skaitlis2 = 3

print("pirmais skaitlis:", skaitlis1, "otrais skaitlis:", skaitlis2, "rezultāts:", rezultats(skaitlis1,skaitlis2))


pirmais = "6"

print(pirmais)

vards2 = "Nē"

print(pirmais + vards2)