import re
import random
from Faworyzacja import Faworyzacja
from Decyzja import Decyzja
from Klasyfikacja import Klasyfikacja
from Parametr import Parametr


def wezIndexZDecyzji(array):
    decyzje = wezDecyzje(array)
    rezultat = []
    for x in decyzje:
        ObjektDecyzyjny = Decyzja()
        ObjektDecyzyjny.ustawDecyzje(x)
        lista = []
        for i in range(len(array)):
            if array[i][len(array[i]) - 1] == x:
                lista.append(i)
        ObjektDecyzyjny.ustawListeIndex(lista)
        rezultat.append(ObjektDecyzyjny)
    return rezultat

def odliczParametr(a, indeksDecyzji, tTab):
    i = 0
    listaDecyzyjna = []
    for sprawdzInnaDecyzje in indeksDecyzji:
        listaDecyzyjna.append(sprawdzInnaDecyzje.wezDecyzje())
    listaFaworyzacji = []
    listaP = []
    for xX in a:
        i += 1
        param = Parametr()
        for decyzja in indeksDecyzji:
            param = Parametr()
            param.ustawObjTest("x" + str(i))
            param.ustawCObjekt(decyzja.wezDecyzje())
            j = 0
            listaOdlParametr = []
            ktory = 0
            for elemOfX in xX:
                if ktory == len(xX) - 1:
                    continue
                licz = 0
                for k in decyzja.wezListeIndex():
                    if elemOfX == tTab[k][ktory]:
                        licz += 1
                if (licz == 0):
                    sprawdzZero = True
                    for k in range(len(tTab) - 1):
                        if elemOfX == tTab[k][ktory]:
                            sprawdzZero = False
                            break

                    if sprawdzZero == False:
                        faworyzacja = Faworyzacja()
                        faworyzacja.ustawDecyzje(decyzja.wezDecyzje())
                        faworyzacja.ustawElem(ktory)
                        faworyzacja.ustawObjektTest(param.wezObjTest())
                        listaFaworyzacji.append(faworyzacja)
                ktory += 1
                listaOdlParametr.append(licz / len(decyzja.wezListeIndex()))
            rezultatParametr = (1 / 2) * sum(listaOdlParametr)
            param.ustawParametr(rezultatParametr)
            listaP.append(param)

    for elem in listaP:
        for faworyzacja in listaFaworyzacji:
            if elem.wezObjTest() == faworyzacja.wezObjektTest() and elem.wezCObj() != faworyzacja.wezDecyzje():
                dlugosc = 0
                for elemDecyzyjny in indeksDecyzji:
                    if elemDecyzyjny.wezDecyzje() == elem.wezCObj():
                        dlugosc = len(elemDecyzyjny.wezListeIndex())
                elem.ustawParametr(elem.wezParam() + ((1 / 2) * (1 / dlugosc)))
    return listaP


def listaAtrybutowINumery(s):
    linie = splitWLiniach(s)
    mojA = []
    for linia in linie:
        mojA.append(linia.split(" "))
    return mojA

def drukujPlik(s):
    f = open(s)
    print(f.read())

def splitWLiniach(s):
    return re.split(r'\n', s)

def delOstatniCiR(s):
    for i in range(len(s)):
        del s[i][len(s[i]) - 1]
    del s[len(s) - 1]
    return s

def wezDecyzje(array):
    wynik = []
    for i in range(len(array)):
        if not array[i][len(array[i]) - 1] in wynik:
            wynik.append(array[i][len(array[i]) - 1])
    return wynik

def wezDecyzjeListTST(a):
    wynik = []
    for r in a:
        wynik.append(r[len(r) - 1])
    return wynik

def unikalne(l1):
    unikalnaL = []
    for x in l1:
        if x not in unikalnaL:
            unikalnaL.append(x)
    return unikalnaL

def papamWPetliEq(parametWL):
    x = []
    for elem in parametWL:
        x.append(elem.wezParam())
    if len(unikalne(x)) == 1:
        return True
    return False

def numerPoprawnegoKlasyfik(listaCP, ListaDecyzjiTST, textFile):
    listaKlasyfik = []
    i = 1
    listaParametrWP = []
    pKlasyfik = 0
    klasyfik = 0

    for decyzjaU in unikalne(ListaDecyzjiTST):
        klasyfikacja = Klasyfikacja()
        klasyfikacja.setCObject(decyzjaU)
        klasyfikacja.ustawListeKlasyfik(0)
        klasyfikacja.ustawListaKlasykPoprawnie(0)
        listaKlasyfik.append(klasyfikacja)

    enum = 0
    for liczParametr in listaCP:
        objektX = "x" + str(i)
        if objektX == liczParametr.wezObjTest():
            listaParametrWP.append(liczParametr)

        if objektX != listaCP[enum + 1].wezObjTest() or \
                len(ListaDecyzjiTST) == 1 and len(listaParametrWP) == 2:
            cObject = ""
            param = 0
            najX = ""
            listaParamIPiter = 0
            for elem in listaParametrWP:
                if param < elem.wezParam():
                    param = elem.wezParam()
                    najX = elem.wezObjTest()
                    cObject = elem.wezCObj()
                    listaParamIPiter += 1

            if listaParamIPiter > 1:
                textFile.write("P c==" + listaParametrWP[0].wezCObj() + "<" + "P C==" + listaParametrWP[
                    len(listaParametrWP)-1].wezCObj() + " dla Obj" + najX)
            if listaParamIPiter <= 1:
                textFile.write("P c==" + listaParametrWP[0].wezCObj() + ">" + "P C==" + listaParametrWP[
                    len(listaParametrWP)-1].wezCObj() + " dla Obj " + najX)

            if papamWPetliEq(listaParametrWP):
                randomParam = random.choice(listaParametrWP)
                if randomParam.getCObject() == ListaDecyzjiTST[i - 1]:
                    textFile.write(" decyzja zgodna (decyzja eksperta == " +
                                   ListaDecyzjiTST[i - 1] + ")\n")
                    for element in listaKlasyfik:
                        if element.wezObjekt() == randomParam.getCObject():
                            element.ustawListaKlasykPoprawnie(element.wezListaKlasykPoprawnie() + 1)
                            element.ustawListeKlasyfik(element.wezListeKlasyfik() + 1)

                else:
                    textFile.write(" decyzja nie zgodna (decyzja ekspert == " +
                                   ListaDecyzjiTST[i - 1] + ")\n")
                    for element in listaKlasyfik:
                        if element.wezObjekt() == randomParam.getCObject():
                            element.ustawListeKlasyfik(element.wezListeKlasyfik() + 1)
            else:
                if cObject == ListaDecyzjiTST[i - 1]:
                    textFile.write("decyzja zgodna (decyzja ekspert == " +
                                   ListaDecyzjiTST[i - 1] + ")\n")
                    for element in listaKlasyfik:
                        if element.wezObjekt() == cObject:
                            element.ustawListaKlasykPoprawnie(element.wezListaKlasykPoprawnie() + 1)
                            element.ustawListeKlasyfik(element.wezListeKlasyfik() + 1)
                else:
                    textFile.write(" decyzja nie zgodna (decyzja ekspert == " +
                                   ListaDecyzjiTST[i - 1] + ")\n")
                    for element in listaKlasyfik:
                        if element.wezObjekt() == cObject:
                            element.ustawListeKlasyfik(element.wezListeKlasyfik() + 1)
            i += 1
            listaParametrWP = []
        enum += 1
        if enum == len(listaCP) - 1:
            enum = 0

    return listaKlasyfik

class NaiwnyKlasyfikatorBayesa():
    def main(self):
        plikDecyz = open("wyniki/dec_bayes.txt", "w+")
        linijki = listaAtrybutowINumery(open("australian_TST.txt").read())
        australianTRN =listaAtrybutowINumery(open("australian_TRN.txt").read())
        linijki = delOstatniCiR(linijki)
        australianTRN = delOstatniCiR(australianTRN)
        wezDecyzjeTrn = wezIndexZDecyzji(australianTRN)
        zliczoneP = odliczParametr(linijki, wezDecyzjeTrn, australianTRN)
        sklasyfikowane = numerPoprawnegoKlasyfik(zliczoneP, wezDecyzjeListTST(linijki), plikDecyz)

if __name__ == "__main__":
    NaiwnyKlasyfikatorBayesa.main("args")
