class Klasyfikacja:

    def __inicjuj__(s, decyzja=0, indexList=0):
        s.cObject = ""
        s.listaKlasykPoprawnie = 0
        s.listaKlasyfik = 0

    def setCObject(s, a):
        s.cObject = a

    def ustawListaKlasykPoprawnie(s, a):
        s.listaKlasykPoprawnie = a

    def ustawListeKlasyfik(s, a):
        s.listaKlasyfik = a

    def wezObjekt(s):
        return s.cObject

    def wezListaKlasykPoprawnie(s):
        return s.listaKlasykPoprawnie

    def wezListeKlasyfik(s):
        return s.listaKlasyfik
