class jatekos:
    def __init__(self, egysor):
        darabok=egysor.split(';')
        self.nev=darabok[0]
        self.gol=int(darabok[1])
        self.kapura=int(darabok[2])
        self.siker=int(darabok[3])
        self.proba=int(darabok[4])
        self.ket=int(darabok[5])
        self.poszt=darabok[6]
        self.magassag=int(darabok[8])
        self.csapat=darabok[9]
f=open('kezieb.txt','r',encoding="utf8")
beolvas=f.readlines()
f.close()
jatekosok=[]
for item in beolvas:
    jatekosok.append(Jatekos[i])
print(jatekosok[0].nev)