class Duree:
    def __init__(self,jour, heure, minute, seconde):
        self.__heure = heure
        self.__minute = minute
        self.__seconde = seconde
        self.__jour = jour

    def afficher(self):
        if self.__seconde>59:
            q = self.__seconde // 60
            self.__seconde = self.__seconde - q*60
            self.__minute = self.__minute + q
        if self.__minute>59:
            q = self.__minute // 60
            self.__minute = self.__minute - q*60
            self.__heure = self.__heure + q
        if self.__heure>23:
            q = self.__heure // 24
            self.__heure = self.__heure - q*24
            self.__jour = self.__jour + q

        print(str(self.__jour)+'j'+str(self.__heure)+"h"+str(self.__minute)+"min"+str(self.__seconde)+"s")

    def __add__(self, objet):
       return Duree(self.__jour + objet.__jour, self.__heure + objet.__heure, self.__minute + objet.__minute, self.__seconde + objet.__seconde)


if __name__=='__main__':
    d1 = Duree(1,14,45,39)
    d2 = Duree(2,11,22,30)
    d3 = d1 + d2
    d3.afficher()
