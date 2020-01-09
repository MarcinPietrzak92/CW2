class Parametr:

    def __inicjuj__(s, objektTest=0, cObjet=0, param=0):
            s.objektTest = ""  
            s.cObjet = ""  
            s.param = 0 

    def ustawObjTest(s, a):
            s.objektTest = a

    def ustawCObjekt(s, a):
            s.cObjet = a

    def ustawParametr(s, a):
            s.param = a

    def wezObjTest(s):
            return s.objektTest

    def wezCObj(s):
            return s.cObjet

    def wezParam(s):
            return s.param
