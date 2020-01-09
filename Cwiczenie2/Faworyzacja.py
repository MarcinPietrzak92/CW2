class Faworyzacja:

    def __inicjuj__(s, decyzja=0, jakiElem=0, testowyObj=0):
        s.decyzja = ""
        s.jakiElem = 0
        s.testowyObj=""

    def ustawDecyzje(s, a):
        s.decyzja = a

    def ustawElem(self, a):
        self.jakiElem = a

    def ustawObjektTest(s, a):
        s.testowyObj = a

    def wezDecyzje(s):
        return s.decyzja

    def wezZElem(s):
        return s.jakiElem

    def wezObjektTest(s):
        return s.testowyObj
