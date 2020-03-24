class circle:
    def __init__(self, rayon):
        self.__rayon = rayon

    def getRayon(self):
        return self.__rayon

    def __add__(self, c):
       return circle(self.__rayon + c.__rayon)

    def __lt__(self, c):
        return self.__rayon < c.__rayon

    def __gt__(self, c):
       return self.__rayon > c.__rayon





if __name__=='__main__':
    c1 = circle(2)
    c2 = circle(3)
    c3 = c1 + c2
    c4 = c1 < c2
    c5 = c2 > c3

    print(c3.getRayon())
    print("Instance :", isinstance(c3,circle))
    print("**********")
    print(c4)
    print("Instance :", isinstance(c4,circle))
    print("**********")
    print(c5)
    print("Instance :", isinstance(c5,circle))
