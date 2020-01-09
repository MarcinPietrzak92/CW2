class Decyzja:

    def __inicjuj__(s, decyzja=0, listaIndex=0):
        s.decyzja = ""
        s.listaIndex = []

    def ustawDecyzje(s, a):
        s.decyzja = a

    def ustawListeIndex(s, a):
        s.indexList = a

    def wezDecyzje(s):
        return s.decyzja

    def wezListeIndex(s):
        return s.indexList
