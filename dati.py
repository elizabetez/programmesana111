def ierakstit(teksts):
    fails = open("teksts.txt", "w", encoding="utf-8")  # r - read; w - write; a - append
    fails.write(teksts+"\n")
    fails.close()

  #  ierakstit("Mani sauc Eli")

def pierakstit_klat(teksts):
    fails = open("teksts.txt", "a", encoding="utf-8")
    fails.write(teksts+"\n")
    fails.close()

# pierakstit_klat("Es esmu") 
    
def nolasit_visu():
    fails = open("teksts.txt", "r", encoding="utf-8")
    teksts = fails.read()
    return teksts

# print(nolasit_visu())
    

def dabut_rindinas():
    fails = open("teksts.txt", "r", encoding="utf-8")
    rindas = fails.redlines()

    for i in range (len(rindas)):
        rindas [i] = rindas [i].strip()

    return rindas
    

 #sraksts = dabut_rindinas()
# print(saraksts)

ierakstit("Anna", "https://artprojectsforkids.org/wp-content/uploads/2022/05/How-to-Draw-a-Girl.jpg")
pierakstit_klat("Katls", "https://dans.lv/imgs/1gb-nami%C5%86%C5%A1-mini-roku-mazg%C4%81%C5%A1anas-pot-miniat%C5%ABras_1-image/143144.jpg")
pierakstit_klat("Kartupelis", "https://stemgeneration.org/wp-content/uploads/2018/03/Potato_Battery_Main.jpg")